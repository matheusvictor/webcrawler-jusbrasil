from constants import constants
from mocks.mocks import create_bs4_object_from_tjce
from models.CrawlerEsaj import CrawlerEsaj


class TjceFirstInstance(CrawlerEsaj):
    def __init__(self, base_url: str, cnj: str):
        super().__init__(base_url, cnj)
        self._body = create_bs4_object_from_tjce().body
        self._headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp, \
                                image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Host": "esaj.tjce.jus.br",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
                      AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Connection": "keep-alive",
        }

    @property
    def court_code(self) -> str:
        return constants.TJCE_CODE

    @property
    def url(self) -> str:
        return f"https://esaj.tjce.jus.br/cpopg/open.do?processo.numero={self.cnj}"
