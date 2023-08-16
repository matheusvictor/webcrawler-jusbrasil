import logging
from abc import abstractmethod
from time import sleep

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from helpers.utils import remove_special_symbols_from_string
from models.crawler_esaj import CrawlerEsaj


class CrawlerFirstInstanceEsaj(CrawlerEsaj):
    @abstractmethod
    def court_code(self) -> str:
        pass

    def get_page(self) -> object or None:
        try:
            session = requests.Session()
            params = {"processo.numero": self.cnj}
            request = session.get(self.url, headers=self._headers, params=params)

            if request:
                return BeautifulSoup(request.text, "html.parser")

        except requests.RequestException:
            logging.error("Obtenção da página mal sucedida!")
            logging.info("Tentando novamente com auxílio do Selenium...")
            return self.get_page_by_selenium()

    def __get_process_header__(self) -> dict:
        logging.info("Coletando dados do cabeçalho...")

        details_from_header = dict(
            classe=None,
            assunto=None,
            area=None,
            juiz=None,
            dataHoraDistribuicao=None,
            valorAcao=None,
        )

        if self.body:
            main_section = self.body.find_all(
                "div", {"id": "containerDadosPrincipaisProcesso"}
            )

            if main_section:
                for div_id in main_section:
                    details_from_header["classe"] = div_id.find(
                        "span", {"id": "classeProcesso"}
                    ).text.strip()
                    details_from_header["assunto"] = div_id.find(
                        "span", {"id": "assuntoProcesso"}
                    ).text.strip()

                    judge = div_id.find("span", {"id": "juizProcesso"})
                    if judge:
                        details_from_header["juiz"] = judge.text.strip()

            more_details_section = self.body.find_all("div", {"id": "maisDetalhes"})

            if more_details_section:
                for label in more_details_section:
                    details_from_header["area"] = label.find(
                        "div", {"id": "areaProcesso"}
                    ).text.strip()
                    details_from_header["dataHoraDistribuicao"] = label.find(
                        "div", {"id": "dataHoraDistribuicaoProcesso"}
                    ).text.strip()

                    value = label.find("div", {"id": "valorAcaoProcesso"})
                    details_from_header["valorAcao"] = " ".join(
                        value.text.split() if value else list()
                    )

        return details_from_header

    def __get_process_parts__(self) -> dict:
        logging.info("Coletando informações das partes envolvidas...")

        all_parts = dict()
        if self.body:
            parts_section = self.body.find("table", {"id": "tableTodasPartes"})

            if parts_section:
                parts_section_rows = (
                    parts_section.find_all("tr") if parts_section else list()
                )

                for block in parts_section_rows:
                    part_type = (
                        remove_special_symbols_from_string(
                            block.find(class_="tipoDeParticipacao").text
                        )
                        .lower()
                        .strip()
                    )
                    list_parts_process = (
                        block.find(class_="nomeParteEAdvogado")
                        .text.strip()
                        .split("\t \n")
                    )

                    for element in list_parts_process:
                        part = remove_special_symbols_from_string(element)
                        if not part:
                            continue
                        person_data = part.split("\xa0")

                        if part_type not in all_parts.keys():
                            all_parts.update({part_type: list()})
                        all_parts.get(f"{part_type}").append(
                            dict(
                                nomes=[name for name in person_data if ":" not in name],
                                categoria=person_data[0].replace(":", "")
                                if len(person_data) > 1
                                else "N/A",
                            )
                        )

        return all_parts

    def __get_process_movement__(self) -> list:
        logging.info("Coletando movimentações do processo...")

        all_movements = list()
        if self.body:
            movements_section = self.body.find(
                "tbody", {"id": "tabelaTodasMovimentacoes"}
            )

            if movements_section:
                movement_section_rows = movements_section.find_all("tr")

                for index, block in enumerate(movement_section_rows):
                    date = block.find("td", {"class": "dataMovimentacao"}).text

                    title = block.find("td", {"class": "descricaoMovimentacao"}).find(
                        "a"
                    )
                    if title is None:
                        title = (
                            block.find("td", {"class": "descricaoMovimentacao"})
                            .contents[0]
                            .text
                        )
                    else:
                        title = title.text

                    all_movements.append(
                        {
                            "_numeroMovimentacao": index,
                            "data": remove_special_symbols_from_string(date),
                            "titulo": remove_special_symbols_from_string(title)
                            if title is not None
                            else "",
                        }
                    )

            return all_movements

    def get_page_by_selenium(self):
        try:
            driver = webdriver.Firefox()
        except:
            try:
                driver = webdriver.Chrome()
            except NoSuchDriverException:
                logging.error(
                    "Não foi possível abrir um navegador para realizar a busca!"
                )
                exit(1)

        driver.get("https://esaj.tjce.jus.br/cpopg/open.do")
        sleep(3)

        search_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "botaoConsultarProcessos"))
        )

        if search_button:
            driver.find_element(By.ID, "numeroDigitoAnoUnificado").send_keys(
                f"{self.cnj.split(self.court_code)[0][:-1]}"
            )
            driver.find_element(By.ID, "foroNumeroUnificado").send_keys(
                f"{self.cnj.split(self.court_code)[1][1:]}"
            )
            driver.find_element(By.ID, "botaoConsultarProcessos").click()

            page = driver.page_source
            driver.close()
            return BeautifulSoup(page, "html.parser")
