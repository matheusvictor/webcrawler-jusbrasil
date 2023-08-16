import logging
from abc import abstractmethod
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from models.crawler import Crawler

logging.basicConfig(level=logging.DEBUG, format="[%(levelname)s] %(message)s")


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
            try:
                soup: object = self.get_page()
                if soup:
                    self._body = soup.body
            except:
                logging.error("Não foi possível obter o corpo da página informada!")
                exit(1)

        return self._body

    @property
    def unmask_cnj(self) -> str:
        return self.cnj.replace("-", "").replace(".", "")

    @property
    def result(self) -> dict:
        return self._result

    @property
    def url(self) -> str:
        return self._base_url

    @abstractmethod
    def court_code(self) -> str:
        pass

    @abstractmethod
    def get_page_by_selenium(self):
        pass

    @abstractmethod
    def __get_process_header__(self) -> dict:
        pass

    @abstractmethod
    def __get_process_parts__(self) -> dict:
        pass

    @abstractmethod
    def __get_process_movement__(self) -> list:
        pass

    def extract(self) -> dict:
        logging.info("Iniciando crawler para busca de 1ª instância...")

        self._result.get("detalhes").update(self.__get_process_header__())
        self._result.get("partesProcesso").update(self.__get_process_parts__())
        self._result["movimentacoes"] = self.__get_process_movement__()

        return self.result

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
