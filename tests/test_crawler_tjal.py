import unittest

from models.crawlers import TjalFirstInstance


class TestCrawlerTjalFirstIntance(unittest.TestCase):

    def test_extracted_data_with_expected_format_when_cnj_is_07108025520188020001(self):
        # given
        cnj = '0710802-55.2018.8.02.0001'
        expected = {
            "detalhes": {
                "area": "Cível",
                "assunto": "Dano Material",
                "classe": "Procedimento Comum Cível",
                "dataHoraDistribuicao": "02/05/2018 às 19:01 - Sorteio",
                "juiz": "José Cícero Alves da Silva",
                "valorAcao": "R$         281.178,42"
            },
            "movimentacoes": {},
            "partesProcesso": {
                "autor": [
                    {
                        "categoria": "N/A",
                        "nomes": [
                            "José Carlos Cerqueira Souza Filho"
                        ]
                    },
                    {
                        "categoria": "Advogado",
                        "nomes": [
                            "Vinicius Faria de Cerqueira"
                        ]
                    }
                ],
                "ré": [
                    {
                        "categoria": "N/A",
                        "nomes": [
                            "Cony Engenharia Ltda."
                        ]
                    },
                    {
                        "categoria": "Advogado",
                        "nomes": [
                            "Carlos Henrique de Mendonça Brandão",
                            "Guilherme Freire Furtado",
                            "Maria Eugênia Barreiros de Mello",
                            "Vítor Reis de Araujo Carvalho"
                        ]
                    }
                ]
            }
        }
        crawler = TjalFirstInstance(cnj)

        # when
        result = crawler.extract()

        # then
        self.assertEqual(result, expected)  # add assertion here


if __name__ == '__main__':
    unittest.main()
