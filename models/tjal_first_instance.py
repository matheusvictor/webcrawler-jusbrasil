from constants import constants
from models.crawler_esaj import CrawlerEsaj


class TjalFirstInstance(CrawlerEsaj):
    @property
    def court_code(self) -> str:
        return constants.TJAL_CODE

    @property
    def url(self) -> str:
        return f"https://www2.tjal.jus.br/cpopg/show.do?processo.numero={self.cnj}"
