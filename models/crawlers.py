import logging
from abc import abstractmethod

import requests
from bs4 import BeautifulSoup

from constants import constants
from helpers.utils import remove_special_symbols_from_string, is_cnj_format_valid, find_court_from_cnj_by_regex


class Crawler:

    def __init__(self, cnj: str):
        self.cnj = cnj

    def __str__(self):
        return f'{self.__class__.__name__}__{self.unmask_cnj}'

    @property
    def unmask_cnj(self):
        return self.cnj.replace('-', '').replace('.', '')

    @abstractmethod
    def url(self) -> str:
        pass

    @abstractmethod
    def court_code(self) -> str:
        pass

    @abstractmethod
    def extract(self) -> dict:
        pass

    def __get_page__(self, url: str) -> object or None:
        # TODO: buscar entender como tornar essa parte assíncrona
        try:
            request = requests.get(url)
        except requests.RequestException:
            return None
        return BeautifulSoup(request.text, 'html.parser')

    def get_body(self, url: str) -> object or None:
        soup: object = self.__get_page__(url)
        if soup:
            return soup.body
        return None


class TjalFirstInstance(Crawler):

    def url(self) -> str:
        return f'https://www2.tjal.jus.br/cpopg/show.do?processo.numero={self.cnj}'

    def court_code(self) -> str:
        return constants.TJAL_CODE

    def extract(self):
        if not is_cnj_format_valid(self.cnj):
            logging.error('Formato de CNJ inválido!')
            exit(1)

        logging.info('Formato de CNJ válido!')
        if find_court_from_cnj_by_regex(self.cnj, self.court_code()):
            logging.info('Iniciando crawler para busca de 1ª instância no TJAL...')

            body = self.get_body(self.url())

            main_section = body.find_all('div', {'id': 'containerDadosPrincipaisProcesso'})

            result = dict(
                detalhes=dict(
                    classe=None,
                    assunto=None,
                    area=None,
                    juiz=None,
                    dataHoraDistribuicao=None,
                    valorAcao=None
                ),
                partesProcesso=dict(),
                movimentacoes=list()
            )

            for div_id in main_section:
                result.get('detalhes')['classe'] = div_id.find(
                    'span', {'id': 'classeProcesso'}
                ).text.strip()
                result.get('detalhes')['assunto'] = div_id.find(
                    'span', {'id': 'assuntoProcesso'}
                ).text.strip()
                result.get('detalhes')['juiz'] = div_id.find(
                    'span', {'id': 'juizProcesso'}
                ).text.strip()

            more_details_section = body.find_all('div', {'id': 'maisDetalhes'})

            for label in more_details_section:
                result.get('detalhes')['area'] = label.find(
                    'div', {'id': 'areaProcesso'}
                ).text.strip()
                result.get('detalhes')['dataHoraDistribuicao'] = label.find(
                    'div', {'id': 'dataHoraDistribuicaoProcesso'}
                ).text.strip()

                value = label.find(
                    'div',
                    {'id': 'valorAcaoProcesso'}
                )

                result.get('detalhes')['valorAcao'] = ' '.join(
                    value.text.split() if value else list()
                )

            logging.info('Coletando informações das partes envolvidas no processo...')
            parts_section = body.find('table', {'id': 'tableTodasPartes'})

            parts_section_rows = parts_section.find_all('tr') if parts_section else list()

            for block in parts_section_rows:
                part_type = remove_special_symbols_from_string(
                    block.find(class_='tipoDeParticipacao').text).lower().strip()
                list_parts_process = block.find(class_='nomeParteEAdvogado').text.strip().split('\t \n')

                for element in list_parts_process:
                    part = remove_special_symbols_from_string(element)
                    if not part:
                        continue
                    person_data = part.split('\xa0')

                    if part_type not in result.get('partesProcesso').keys():
                        result.get('partesProcesso').update(
                            {
                                part_type: list()
                            }
                        )
                    result.get('partesProcesso').get(f'{part_type}').append(
                        dict(
                            nomes=[name for name in person_data if ':' not in name],
                            categoria=person_data[0].replace(':', '') if len(person_data) > 1 else 'N/A'
                        )
                    )

            movements_section = body.find('tbody', {'id': 'tabelaTodasMovimentacoes'})
            movement_section_rows = movements_section.find_all('tr')

            for index, block in enumerate(movement_section_rows):
                date = block.find('td', {'class': 'dataMovimentacao'}).text

                title = block.find('td', {'class': 'descricaoMovimentacao'}).find('a')
                if title is None:
                    title = block.find('td', {'class': 'descricaoMovimentacao'}).contents[0].text
                else:
                    title = title.text
                desc = block.find('td', {'class': 'descricaoMovimentacao'}).find('span').text

                result.get('movimentacoes').append(
                    {
                        "_numeroMovimentacao": index,
                        "data": remove_special_symbols_from_string(date),
                        "titulo": remove_special_symbols_from_string(title) if title is not None else '',
                        "descricao": remove_special_symbols_from_string(desc) if desc is not None else '',
                    }
                )

            return result
