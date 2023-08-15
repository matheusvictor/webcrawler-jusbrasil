import logging
from abc import abstractmethod
from http import HTTPStatus
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


class CrawlerSecondInstanceEsaj(CrawlerEsaj):
    @abstractmethod
    def court_code(self) -> str:
        pass

    def get_page(self) -> object or None:
        try:
            session = requests.Session()
            request = session.get(self.url, headers=self._headers)

            if request:
                return BeautifulSoup(request.text, "html.parser")

        except requests.RequestException:
            logging.error("Obtenção da página mal sucedida!")
            logging.info("Tentando novamente com auxílio do Selenium...")
            return self.get_page_by_selenium()

    def get_page_by_selenium(self) -> object or None:
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

        driver.get(self.url)
        sleep(3)

        form = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "formularioConsulta"))
        )

        if form:
            print(driver.title)
            driver.find_element(By.ID, "numeroDigitoAnoUnificado").send_keys(
                f"{self.cnj.split(self.court_code())[0][:-1]}"
            )
            driver.find_element(By.ID, "foroNumeroUnificado").send_keys(
                f"{self.cnj.split(self.court_code())[1][1:]}"
            )
            sleep(3)
            driver.find_element(By.ID, "pbConsultar").click()

            modal = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "modalIncidentes"))
            )

            if modal:
                if not driver.find_element(
                    By.CSS_SELECTOR, "#processoSelecionado"
                ).is_selected():
                    driver.find_element(By.CSS_SELECTOR, "#processoSelecionado").click()
                driver.find_element(By.ID, "botaoEnviarIncidente").click()
                sleep(3)

            page = driver.page_source
            driver.close()
            return BeautifulSoup(page, "html.parser")

    def get_search_form(self, soup: object) -> object or None:
        if soup:
            return self.body.find("form", {"name": "consultarProcessoForm"})
        return None

    def fill_form(self, form: object):
        if form:
            form_action = form.attrs["action"].split(";")[0][1:]
            form_url = self.url.replace("cposg5/open.do", form_action)

            form_data = {
                "cbPesquisa": "NUMPROC",
                "tipoNuProcesso": "UNIFICADO",
                "dePesquisaNuUnificado": f"{self.cnj}",
            }

            try:
                response = requests.post(form_url, params=form_data)
            except requests.exceptions.RequestException:
                logging.info("Erro ao fazer a solicitação")
                exit(1)

            if response.status_code == HTTPStatus.OK:
                logging.info(f"URL após redirecionamento: {response.url}")

                self._body = BeautifulSoup(response.content, "html.parser")
                modal = self.body.find("div", {"id": "modalIncidentes"})

                if modal:
                    select_value_for_search = modal.find(
                        "input", {"class": "custom-radio", "id": "processoSelecionado"}
                    ).attrs["value"]
                    new_request = requests.get(
                        f"{self.url.replace('open.do', 'show.do')}?processo.codigo={select_value_for_search}"
                    )

                    self._body = BeautifulSoup(new_request.content, "html.parser")
            else:
                logging.error("Status code:", response.status_code)

    def extract(self) -> dict:
        logging.info("Iniciando crawler para busca de 2ª instância...")

        try:
            search_form = self.get_search_form(self.body)
            self.fill_form(search_form)
        except Exception as ex:
            logging.info("Não foi possível localizar formulário: ", ex)

        self._result.get("detalhes").update(self.__get_process_header__())
        self._result.get("partesProcesso").update(self.__get_process_parts__())
        self._result["movimentacoes"] = self.__get_process_movement__()

        return self.result

    def __get_process_header__(self) -> dict:
        details_from_header = dict(
            classe=None,
            assunto=None,
            area=None,
            juiz=None,
            dataDistribuicao=None,
            valorAcao=None,
        )

        main_section = self.body.find("div", {"class": "unj-entity-header__summary"})

        if main_section:
            details_from_header["classe"] = main_section.find(
                "div", {"id": "classeProcesso"}
            ).span.get_text()
            details_from_header["area"] = main_section.find(
                "div", {"id": "areaProcesso"}
            ).span.get_text()
            details_from_header["assunto"] = main_section.find(
                "div", {"id": "assuntoProcesso"}
            ).span.get_text()

        details_section = self.body.find("div", {"id": "maisDetalhes"})
        if details_section:
            details_from_header["valorAcao"] = details_section.find(
                "div", {"id": "valorAcaoProcesso"}
            ).span.get_text()

        judge_tag = self.body.find("div", {"class": "div-conteudo container unj-mb-40"})

        if judge_tag:
            details_from_header["juiz"] = (
                judge_tag.find("tr", {"class": "fundoClaro"})
                .find_all("td")[3]
                .get_text(strip=True)
            )
        return details_from_header

    def __get_process_parts__(self) -> dict:
        all_parts = dict()
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
                    block.find(class_="nomeParteEAdvogado").text.strip().split("\t \t ")
                )

                for element in list_parts_process:
                    part = remove_special_symbols_from_string(element).strip()
                    if not part:
                        continue
                    person_data = part.split("\xa0")

                    if part_type not in all_parts.keys():
                        all_parts.update({part_type: list()})
                    all_parts.get(f"{part_type}").append(
                        dict(
                            nomes=[
                                name.strip() for name in person_data if ":" not in name
                            ],
                            categoria=person_data[0].replace(":", "")
                            if len(person_data) > 1
                            else "N/A",
                        )
                    )
        return all_parts

    def __get_process_movement__(self) -> list:
        all_movements = list()
        movements_section = self.body.find("tbody", {"id": "tabelaTodasMovimentacoes"})

        if movements_section:
            movement_section_rows = movements_section.find_all("tr")

            for index, block in enumerate(movement_section_rows):
                date = block.find("td", {"class": "dataMovimentacaoProcesso"}).get_text(
                    strip=True
                )

                title = block.find(
                    "td", {"class": "descricaoMovimentacaoProcesso"}
                ).find("a")
                if title is None:
                    title = remove_special_symbols_from_string(
                        block.find("td", {"class": "descricaoMovimentacaoProcesso"})
                        .contents[0]
                        .get_text(strip=True)
                    )
                else:
                    title = title.get_text(strip=True)

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
