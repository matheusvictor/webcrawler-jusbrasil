from constants import constants
from models.CrawlerEsaj import CrawlerEsaj


class TjalFirstInstance(CrawlerEsaj):
    def __init__(self, base_url: str, cnj: str):
        super().__init__(base_url, cnj)
        self._headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp, \
                             image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Host": "www2.tjal.jus.br",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
                   AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
            "Connection": "keep-alive",
        }

    @property
    def court_code(self) -> str:
        return constants.TJAL_CODE

    @property
    def url(self) -> str:
        return f"https://www2.tjal.jus.br/cpopg/show.do?processo.numero={self.cnj}"
