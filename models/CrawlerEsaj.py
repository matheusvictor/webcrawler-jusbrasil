import logging
from abc import abstractmethod
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from helpers.utils import (
    remove_special_symbols_from_string,
    is_cnj_format_valid,
)
from models.Crawler import Crawler


class CrawlerEsaj(Crawler):
    def __init__(self, base_url: str, cnj: str):
        super().__init__(base_url, cnj)
        self._body = None
        self._result = dict(
            detalhes=dict(), partesProcesso=dict(), movimentacoes=list()
        )
        self._headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp, \
                                     image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Host": f"{urlparse(self.url).hostname}",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
                           AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Connection": "keep-alive",
        }

    def __str__(self) -> str:
        return f"{self.__class__.__name__}__{self.unmask_cnj}"

    @property
    def body(self) -> object or None:
        if not self._body:
            soup: object = self.get_page()
            if soup:
                self._body = soup.body

        return self._body

    @property
    def unmask_cnj(self) -> str:
        return self.cnj.replace("-", "").replace(".", "")

    @property
    def url(self) -> str:
        return f"{self._base_url}{self.cnj}"

    @property
    def result(self) -> dict:
        return self._result

    @abstractmethod
    def court_code(self) -> str:
        pass

    def extract(self) -> dict:
        if not is_cnj_format_valid(self.cnj):
            logging.error("Formato de CNJ inválido!")
            exit(1)

        logging.info("Formato de CNJ válido!")

        logging.info("Iniciando crawler para busca de 1ª instância...")

        self._result.get("detalhes").update(self.__get_process_header__())
        self._result.get("partesProcesso").update(self.__get_process_parts__())
        self.__get_process_movement__()

        return self.result

    def get_page(self) -> object or None:
        session = requests.Session()

        try:
            request = session.post(self.url, headers=self._headers)
        except requests.RequestException:
            return None
        return BeautifulSoup(request.text, "html.parser")

    def __get_process_header__(self) -> dict:
        details_from_header = dict(
            classe=None,
            assunto=None,
            area=None,
            juiz=None,
            dataHoraDistribuicao=None,
            valorAcao=None,
        )

        logging.info("Coletando dados do cabeçalho...")
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

        all_parts = dict(list())
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
                    block.find(class_="nomeParteEAdvogado").text.strip().split("\t \n")
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

    def __get_process_movement__(self):
        logging.info("Coletando movimentações do processo...")

        movements_section = self.body.find("tbody", {"id": "tabelaTodasMovimentacoes"})

        if movements_section:
            movement_section_rows = movements_section.find_all("tr")

            for index, block in enumerate(movement_section_rows):
                date = block.find("td", {"class": "dataMovimentacao"}).text

                title = block.find("td", {"class": "descricaoMovimentacao"}).find("a")
                if title is None:
                    title = (
                        block.find("td", {"class": "descricaoMovimentacao"})
                        .contents[0]
                        .text
                    )
                else:
                    title = title.text
                desc = (
                    block.find("td", {"class": "descricaoMovimentacao"})
                    .find("span")
                    .text
                )

                self.result.get("movimentacoes").append(
                    {
                        "_numeroMovimentacao": index,
                        "data": remove_special_symbols_from_string(date),
                        "titulo": remove_special_symbols_from_string(title)
                        if title is not None
                        else "",
                        "descricao": remove_special_symbols_from_string(desc)
                        if desc is not None
                        else "",
                    }
                )
