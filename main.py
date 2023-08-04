import logging
import re

from constants import constants
from helpers.utils import (find_court_from_cnj_by_regex,
                           is_cnj_format_valid, extrair_advogados_autores, remover_simbolos_especiais)
from models.models import Crawler

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(message)s')


def main():
    cnj = '0710802-55.2018.8.02.0001'

    if not is_cnj_format_valid(cnj):
        logging.error('Formato de CNJ inválido!')
        # TODO: Na chamada da API, essa condicional deve retornar uma response de erro
        # TODO: Caso inválido, mostrar mensagem de erro ainda no campo do form do front-end

    logging.info('Formato de CNJ válido!')
    if find_court_from_cnj_by_regex(cnj, constants.TJAL_CODE):
        logging.info('Iniciando crawler para busca de 1ª instância no TJAL...')

        crawler_tjal = Crawler()

        body = crawler_tjal.get_body(
            url=f'https://www2.tjal.jus.br/cpopg/show.do?processo.numero={cnj}',
        )

        main_section = crawler_tjal.get_all_tags_from_body_by_property(
            body, 'div', {'id': 'containerDadosPrincipaisProcesso'}
        )

        data_from_main_section = dict(
            principal=dict(
                classe=None,
                assunto=None,
                juiz=None
            ),
            detalhes=dict(
                area=None,
                dataHoraDistribuicao=None,
                valorAcao=None
            ),
            partesProcesso=dict(
                autoresProcesso=dict(
                    pessoas=list(),
                    profissionais=set()
                ),
                reusProcesso=dict(
                    reus=list(),
                    advogados=list()
                )
            )
        )

        for div_id in main_section:
            data_from_main_section.get('principal')['classe'] = div_id.find(
                'span', {'id': 'classeProcesso'}
            ).text.strip()
            data_from_main_section.get('principal')['assunto'] = div_id.find(
                'span', {'id': 'assuntoProcesso'}
            ).text.strip()
            data_from_main_section.get('principal')['juiz'] = div_id.find(
                'span', {'id': 'juizProcesso'}
            ).text.strip()

        more_details_section = crawler_tjal.get_all_tags_from_body_by_property(
            body, 'div', {'id': 'maisDetalhes'}
        )

        for label in more_details_section:
            data_from_main_section.get('detalhes')['area'] = label.find(
                'div', {'id': 'areaProcesso'}
            ).text.strip()
            data_from_main_section.get('detalhes')['dataHoraDistribuicao'] = label.find(
                'div', {'id': 'dataHoraDistribuicaoProcesso'}
            ).text.strip()
            data_from_main_section.get('detalhes')['valorAcao'] = label.find(
                'div',
                {'id': 'valorAcaoProcesso'}
            ).text.strip()

        logging.info('Coletando informações das partes envolvidas no processo...')
        parts_section = crawler_tjal.get_tag_from_page_by_property(
            body, 'table',
            {'id': 'tableTodasPartes'}
        )

        parts_section_rows = parts_section.find_all('tr')

        for block in parts_section_rows:
            # FIXME: Corrigir extração das partes
            part_type = remover_simbolos_especiais(block.find(class_='tipoDeParticipacao').text)
            part_content = block.text
            r = extrair_advogados_autores(part_content)
            # content = remover_simbolos_especiais(block.text)
            # part_content = re.split(r'Advogad\w\W', block.text)
            # if 'Autor' in part_type:
            #     pass
            # else:
            #     parts_section_result.get('autor').get('autores').append(part_content)
    #
    # # list_attrs = list()
    # #
    # # for div in main_section:
    # #     list_attrs.append(div.find('span', {'id': 'numeroProcesso'}).text.strip())
    # #
    # # print(list_attrs)
    # #
    # # div_ids_from_main_section = find_section_keys(main_section)
    # #
    # # print(div_ids_from_main_section)
    # #
    # # class_process = crawler_tjal.get_tags_from_page_by_properties(body, 'span', {'id': 'assuntoProcesso'})[0].text
    # # field = crawler_tjal.get_tags_from_page_by_properties(body, 'div', {'id': 'areaProcesso'})[0].text
    # #
    # # data_from_main_section = {
    # #     'classe': class_process,
    # #     'area': field,
    # #     'assunto': '',
    # #     'dataDistribuicao': '',
    # #     'juiz': '',
    # #     'valorAcao': 0,
    # #     'partes': [{}],
    # #     'movimentacoes': [{}]
    # # }
    # #
    # # print(data_from_main_section)


if __name__ == '__main__':
    main()
