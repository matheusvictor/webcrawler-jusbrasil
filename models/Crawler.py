from abc import abstractmethod


class Crawler:
    def __init__(self, base_url: str, cnj: str):
        self.cnj = cnj
        self._base_url = base_url
        self._body = None

    @abstractmethod
    def body(self) -> object or None:
        pass

    @abstractmethod
    def extract(self) -> dict:
        pass

    @abstractmethod
    def url(self) -> str:
        pass

    @abstractmethod
    def get_page(self) -> object or None:
        pass
