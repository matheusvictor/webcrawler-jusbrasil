import unittest

from models.tjal_first_instance import TjalFirstInstance


class TestCrawlerTjalFirstIntance(unittest.TestCase):
    def test_extract_general_details_when_cnj_is_07108025520188020001(self):
        # given
        cnj = "0710802-55.2018.8.02.0001"
        expected = {
            "area": "Cível",
            "assunto": "Dano Material",
            "classe": "Procedimento Comum Cível",
            "dataHoraDistribuicao": "02/05/2018 às 19:01 - Sorteio",
            "juiz": "José Cícero Alves da Silva",
            "valorAcao": "R$ 281.178,42",
        }

        crawler = TjalFirstInstance(
            base_url="https://www2.tjal.jus.br/cpopg/show.do",
            cnj=cnj,
        )

        result = crawler.__get_process_header__()
        self.assertEqual(result, expected)

    def test_extract_process_parts_when_cnj_is_07108025520188020001(self):
        # given
        cnj = "0710802-55.2018.8.02.0001"
        expected = {
            "autor": [
                {"categoria": "N/A", "nomes": ["José Carlos Cerqueira Souza Filho"]},
                {"categoria": "Advogado", "nomes": ["Vinicius Faria de Cerqueira"]},
            ],
            "autora": [
                {"categoria": "N/A", "nomes": ["Livia Nascimento da Rocha"]},
                {"categoria": "Advogado", "nomes": ["Vinicius Faria de Cerqueira"]},
            ],
            "ré": [
                {"categoria": "N/A", "nomes": ["Cony Engenharia Ltda."]},
                {
                    "categoria": "Advogado",
                    "nomes": [
                        "Carlos Henrique de Mendonça Brandão",
                        "Guilherme Freire Furtado",
                        "Maria Eugênia Barreiros de Mello",
                        "Vítor Reis de Araujo Carvalho",
                    ],
                },
            ],
            "réu": [
                {"categoria": "N/A", "nomes": ["Banco do Brasil S A"]},
                {"categoria": "Advogado", "nomes": ["Louise Rainer Pereira Gionédis"]},
            ],
        }

        crawler = TjalFirstInstance(
            base_url="https://www2.tjal.jus.br/cpopg/show.do",
            cnj=cnj,
        )

        result = crawler.__get_process_parts__()
        self.assertEqual(result, expected)

    def test_extract_process_movements_when_cnj_is_07108025520188020001(self):
        cnj = "0710802-55.2018.8.02.0001"
        expected = [
            {
                "_numeroMovimentacao": 0,
                "data": "09/08/2023",
                "titulo": "Juntada de Documento",
            },
            {"_numeroMovimentacao": 1, "data": "21/07/2023", "titulo": "Ato Publicado"},
            {
                "_numeroMovimentacao": 2,
                "data": "20/07/2023",
                "titulo": "Disponibilização no Diário da Justiça Eletrônico",
            },
            {
                "_numeroMovimentacao": 3,
                "data": "20/07/2023",
                "titulo": " Ato ordinatório praticado",
            },
            {
                "_numeroMovimentacao": 4,
                "data": "20/07/2023",
                "titulo": " Devolvido CJU - Cálculo de Custas Finais Realizado",
            },
            {
                "_numeroMovimentacao": 5,
                "data": "20/07/2023",
                "titulo": "Realizado cálculo de custas",
            },
            {
                "_numeroMovimentacao": 6,
                "data": "20/07/2023",
                "titulo": "Juntada de Documento",
            },
            {
                "_numeroMovimentacao": 7,
                "data": "05/05/2023",
                "titulo": "Execução de Sentença Iniciada",
            },
            {"_numeroMovimentacao": 8, "data": "05/05/2023", "titulo": "Ato Publicado"},
            {
                "_numeroMovimentacao": 9,
                "data": "04/05/2023",
                "titulo": "Disponibilização no Diário da Justiça Eletrônico",
            },
            {
                "_numeroMovimentacao": 10,
                "data": "04/05/2023",
                "titulo": "Recebido pela Contadoria UNIFICADA",
            },
            {
                "_numeroMovimentacao": 11,
                "data": "04/05/2023",
                "titulo": " Ato Ordinatório - Artigo 162, §4º, CPC",
            },
            {
                "_numeroMovimentacao": 12,
                "data": "04/05/2023",
                "titulo": " Ato ordinatório praticado",
            },
            {
                "_numeroMovimentacao": 13,
                "data": "03/05/2023",
                "titulo": "Transitado em Julgado",
            },
            {
                "_numeroMovimentacao": 14,
                "data": "03/05/2023",
                "titulo": 'Recebimento da Instância Superior -  Altera situação para "Julgado"',
            },
            {
                "_numeroMovimentacao": 15,
                "data": "26/04/2023",
                "titulo": "Recebido recurso eletrônico",
            },
            {
                "_numeroMovimentacao": 16,
                "data": "22/02/2021",
                "titulo": "Remetido recurso eletrônico ao Tribunal de Justiça/Turma de recurso",
            },
            {
                "_numeroMovimentacao": 17,
                "data": "10/02/2021",
                "titulo": "Juntada de Documento",
            },
            {
                "_numeroMovimentacao": 18,
                "data": "06/01/2021",
                "titulo": "Ato Publicado",
            },
            {
                "_numeroMovimentacao": 19,
                "data": "06/01/2021",
                "titulo": "Ato Publicado",
            },
            {
                "_numeroMovimentacao": 20,
                "data": "06/01/2021",
                "titulo": "Ato Publicado",
            },
            {
                "_numeroMovimentacao": 21,
                "data": "06/01/2021",
                "titulo": "Ato Publicado",
            },
            {
                "_numeroMovimentacao": 22,
                "data": "06/01/2021",
                "titulo": "Ato Publicado",
            },
            {
                "_numeroMovimentacao": 23,
                "data": "06/01/2021",
                "titulo": "Ato Publicado",
            },
            {
                "_numeroMovimentacao": 24,
                "data": "05/01/2021",
                "titulo": "Disponibilização no Diário da Justiça Eletrônico",
            },
            {
                "_numeroMovimentacao": 25,
                "data": "04/01/2021",
                "titulo": " Ato Ordinatório - Artigo 162, §4º, CPC",
            },
            {
                "_numeroMovimentacao": 26,
                "data": "18/12/2020",
                "titulo": "Juntada de Documento",
            },
            {
                "_numeroMovimentacao": 27,
                "data": "18/12/2020",
                "titulo": "Juntada de Documento",
            },
            {
                "_numeroMovimentacao": 28,
                "data": "15/12/2020",
                "titulo": "Juntada de Documento",
            },
            {
                "_numeroMovimentacao": 29,
                "data": "24/11/2020",
                "titulo": "Ato Publicado",
            },
            {
                "_numeroMovimentacao": 30,
                "data": "24/11/2020",
                "titulo": "Ato Publicado",
            },
            {
                "_numeroMovimentacao": 31,
                "data": "24/11/2020",
                "titulo": "Ato Publicado",
            },
            {
                "_numeroMovimentacao": 32,
                "data": "24/11/2020",
                "titulo": "Ato Publicado",
            },
            {
                "_numeroMovimentacao": 33,
                "data": "23/11/2020",
                "titulo": "Disponibilização no Diário da Justiça Eletrônico",
            },
            {
                "_numeroMovimentacao": 34,
                "data": "23/11/2020",
                "titulo": " Julgado procedente em parte do pedido",
            },
            {"_numeroMovimentacao": 35, "data": "23/09/2020", "titulo": "Conclusos"},
            {
                "_numeroMovimentacao": 36,
                "data": "16/08/2020",
                "titulo": " Visto em Autoinspeção",
            },
            {
                "_numeroMovimentacao": 37,
                "data": "11/05/2020",
                "titulo": "Juntada de Documento",
            },
            {"_numeroMovimentacao": 38, "data": "10/12/2019", "titulo": "Conclusos"},
            {
                "_numeroMovimentacao": 39,
                "data": "11/11/2019",
                "titulo": " Despacho de Mero Expediente",
            },
            {
                "_numeroMovimentacao": 40,
                "data": "12/07/2019",
                "titulo": "Juntada de Petição",
            },
            {
                "_numeroMovimentacao": 41,
                "data": "12/02/2019",
                "titulo": "Juntada de Petição",
            },
            {
                "_numeroMovimentacao": 42,
                "data": "11/02/2019",
                "titulo": "Juntada de Petição",
            },
            {"_numeroMovimentacao": 43, "data": "06/12/2018", "titulo": "Conclusos"},
            {
                "_numeroMovimentacao": 44,
                "data": "05/12/2018",
                "titulo": "Juntada de Petição",
            },
            {
                "_numeroMovimentacao": 45,
                "data": "29/11/2018",
                "titulo": "Juntada de Petição",
            },
            {
                "_numeroMovimentacao": 46,
                "data": "28/11/2018",
                "titulo": "Ato Publicado",
            },
            {
                "_numeroMovimentacao": 47,
                "data": "27/11/2018",
                "titulo": "Disponibilização no Diário da Justiça Eletrônico",
            },
            {
                "_numeroMovimentacao": 48,
                "data": "27/11/2018",
                "titulo": " Ato ordinatório praticado",
            },
            {
                "_numeroMovimentacao": 49,
                "data": "26/11/2018",
                "titulo": "Juntada de Documento",
            },
            {
                "_numeroMovimentacao": 50,
                "data": "26/11/2018",
                "titulo": "Juntada de Documento",
            },
            {
                "_numeroMovimentacao": 51,
                "data": "09/11/2018",
                "titulo": "Ato Publicado",
            },
            {
                "_numeroMovimentacao": 52,
                "data": "08/11/2018",
                "titulo": "Disponibilização no Diário da Justiça Eletrônico",
            },
            {
                "_numeroMovimentacao": 53,
                "data": "06/11/2018",
                "titulo": " Ato ordinatório praticado",
            },
            {
                "_numeroMovimentacao": 54,
                "data": "16/10/2018",
                "titulo": "Juntada de Documentos",
            },
            {
                "_numeroMovimentacao": 55,
                "data": "10/10/2018",
                "titulo": "Juntada de Documentos",
            },
            {
                "_numeroMovimentacao": 56,
                "data": "24/09/2018",
                "titulo": "Juntada de Documento",
            },
            {
                "_numeroMovimentacao": 57,
                "data": "24/09/2018",
                "titulo": "Juntada de Documento",
            },
            {
                "_numeroMovimentacao": 58,
                "data": "24/09/2018",
                "titulo": " Audiência Realizada",
            },
            {
                "_numeroMovimentacao": 59,
                "data": "24/09/2018",
                "titulo": "Juntada de Petição",
            },
            {
                "_numeroMovimentacao": 60,
                "data": "21/09/2018",
                "titulo": "Juntada de Petição",
            },
            {
                "_numeroMovimentacao": 61,
                "data": "21/09/2018",
                "titulo": "Juntada de Petição",
            },
            {
                "_numeroMovimentacao": 62,
                "data": "21/09/2018",
                "titulo": "Juntada de Petição",
            },
            {
                "_numeroMovimentacao": 63,
                "data": "20/09/2018",
                "titulo": " Visto em correição",
            },
            {
                "_numeroMovimentacao": 64,
                "data": "06/06/2018",
                "titulo": "Juntada de AR - Cumprido",
            },
            {
                "_numeroMovimentacao": 65,
                "data": "06/06/2018",
                "titulo": "Juntada de AR - Cumprido",
            },
            {
                "_numeroMovimentacao": 66,
                "data": "15/05/2018",
                "titulo": "Ato Publicado",
            },
            {
                "_numeroMovimentacao": 67,
                "data": "15/05/2018",
                "titulo": "Ato Publicado",
            },
            {
                "_numeroMovimentacao": 68,
                "data": "11/05/2018",
                "titulo": "Disponibilização no Diário da Justiça Eletrônico",
            },
            {
                "_numeroMovimentacao": 69,
                "data": "11/05/2018",
                "titulo": "Disponibilização no Diário da Justiça Eletrônico",
            },
            {
                "_numeroMovimentacao": 70,
                "data": "11/05/2018",
                "titulo": " Carta Expedida",
            },
            {
                "_numeroMovimentacao": 71,
                "data": "11/05/2018",
                "titulo": " Carta Expedida",
            },
            {
                "_numeroMovimentacao": 72,
                "data": "11/05/2018",
                "titulo": "Audiência Designada",
            },
            {
                "_numeroMovimentacao": 73,
                "data": "10/05/2018",
                "titulo": " Não Concedida a Antecipação de tutela",
            },
            {"_numeroMovimentacao": 74, "data": "03/05/2018", "titulo": "Conclusos"},
            {"_numeroMovimentacao": 75, "data": "02/05/2018", "titulo": "Conclusos"},
            {
                "_numeroMovimentacao": 76,
                "data": "02/05/2018",
                "titulo": "Distribuído por Sorteio",
            },
        ]

        crawler = TjalFirstInstance(
            base_url="https://www2.tjal.jus.br/cpopg/show.do",
            cnj=cnj,
        )

        result = crawler.__get_process_movement__()
        self.assertEqual(result, expected)

    def test_extract_data_when_cnj_is_07108025520188020001(self):
        cnj = "0710802-55.2018.8.02.0001"
        expected = {
            "detalhes": {
                "area": "Cível",
                "assunto": "Dano Material",
                "classe": "Procedimento Comum Cível",
                "dataHoraDistribuicao": "02/05/2018 às 19:01 - Sorteio",
                "juiz": "José Cícero Alves da Silva",
                "valorAcao": "R$ 281.178,42",
            },
            "movimentacoes": [
                {
                    "_numeroMovimentacao": 0,
                    "data": "09/08/2023",
                    "titulo": "Juntada de Documento",
                },
                {
                    "_numeroMovimentacao": 1,
                    "data": "21/07/2023",
                    "titulo": "Ato Publicado",
                },
                {
                    "_numeroMovimentacao": 2,
                    "data": "20/07/2023",
                    "titulo": "Disponibilização no Diário da Justiça Eletrônico",
                },
                {
                    "_numeroMovimentacao": 3,
                    "data": "20/07/2023",
                    "titulo": " Ato ordinatório praticado",
                },
                {
                    "_numeroMovimentacao": 4,
                    "data": "20/07/2023",
                    "titulo": " Devolvido CJU - Cálculo de Custas Finais Realizado",
                },
                {
                    "_numeroMovimentacao": 5,
                    "data": "20/07/2023",
                    "titulo": "Realizado cálculo de custas",
                },
                {
                    "_numeroMovimentacao": 6,
                    "data": "20/07/2023",
                    "titulo": "Juntada de Documento",
                },
                {
                    "_numeroMovimentacao": 7,
                    "data": "05/05/2023",
                    "titulo": "Execução de Sentença Iniciada",
                },
                {
                    "_numeroMovimentacao": 8,
                    "data": "05/05/2023",
                    "titulo": "Ato Publicado",
                },
                {
                    "_numeroMovimentacao": 9,
                    "data": "04/05/2023",
                    "titulo": "Disponibilização no Diário da Justiça Eletrônico",
                },
                {
                    "_numeroMovimentacao": 10,
                    "data": "04/05/2023",
                    "titulo": "Recebido pela Contadoria UNIFICADA",
                },
                {
                    "_numeroMovimentacao": 11,
                    "data": "04/05/2023",
                    "titulo": " Ato Ordinatório - Artigo 162, §4º, CPC",
                },
                {
                    "_numeroMovimentacao": 12,
                    "data": "04/05/2023",
                    "titulo": " Ato ordinatório praticado",
                },
                {
                    "_numeroMovimentacao": 13,
                    "data": "03/05/2023",
                    "titulo": "Transitado em Julgado",
                },
                {
                    "_numeroMovimentacao": 14,
                    "data": "03/05/2023",
                    "titulo": 'Recebimento da Instância Superior -  Altera situação para "Julgado"',
                },
                {
                    "_numeroMovimentacao": 15,
                    "data": "26/04/2023",
                    "titulo": "Recebido recurso eletrônico",
                },
                {
                    "_numeroMovimentacao": 16,
                    "data": "22/02/2021",
                    "titulo": "Remetido recurso eletrônico ao Tribunal de Justiça/Turma de recurso",
                },
                {
                    "_numeroMovimentacao": 17,
                    "data": "10/02/2021",
                    "titulo": "Juntada de Documento",
                },
                {
                    "_numeroMovimentacao": 18,
                    "data": "06/01/2021",
                    "titulo": "Ato Publicado",
                },
                {
                    "_numeroMovimentacao": 19,
                    "data": "06/01/2021",
                    "titulo": "Ato Publicado",
                },
                {
                    "_numeroMovimentacao": 20,
                    "data": "06/01/2021",
                    "titulo": "Ato Publicado",
                },
                {
                    "_numeroMovimentacao": 21,
                    "data": "06/01/2021",
                    "titulo": "Ato Publicado",
                },
                {
                    "_numeroMovimentacao": 22,
                    "data": "06/01/2021",
                    "titulo": "Ato Publicado",
                },
                {
                    "_numeroMovimentacao": 23,
                    "data": "06/01/2021",
                    "titulo": "Ato Publicado",
                },
                {
                    "_numeroMovimentacao": 24,
                    "data": "05/01/2021",
                    "titulo": "Disponibilização no Diário da Justiça Eletrônico",
                },
                {
                    "_numeroMovimentacao": 25,
                    "data": "04/01/2021",
                    "titulo": " Ato Ordinatório - Artigo 162, §4º, CPC",
                },
                {
                    "_numeroMovimentacao": 26,
                    "data": "18/12/2020",
                    "titulo": "Juntada de Documento",
                },
                {
                    "_numeroMovimentacao": 27,
                    "data": "18/12/2020",
                    "titulo": "Juntada de Documento",
                },
                {
                    "_numeroMovimentacao": 28,
                    "data": "15/12/2020",
                    "titulo": "Juntada de Documento",
                },
                {
                    "_numeroMovimentacao": 29,
                    "data": "24/11/2020",
                    "titulo": "Ato Publicado",
                },
                {
                    "_numeroMovimentacao": 30,
                    "data": "24/11/2020",
                    "titulo": "Ato Publicado",
                },
                {
                    "_numeroMovimentacao": 31,
                    "data": "24/11/2020",
                    "titulo": "Ato Publicado",
                },
                {
                    "_numeroMovimentacao": 32,
                    "data": "24/11/2020",
                    "titulo": "Ato Publicado",
                },
                {
                    "_numeroMovimentacao": 33,
                    "data": "23/11/2020",
                    "titulo": "Disponibilização no Diário da Justiça Eletrônico",
                },
                {
                    "_numeroMovimentacao": 34,
                    "data": "23/11/2020",
                    "titulo": " Julgado procedente em parte do pedido",
                },
                {
                    "_numeroMovimentacao": 35,
                    "data": "23/09/2020",
                    "titulo": "Conclusos",
                },
                {
                    "_numeroMovimentacao": 36,
                    "data": "16/08/2020",
                    "titulo": " Visto em Autoinspeção",
                },
                {
                    "_numeroMovimentacao": 37,
                    "data": "11/05/2020",
                    "titulo": "Juntada de Documento",
                },
                {
                    "_numeroMovimentacao": 38,
                    "data": "10/12/2019",
                    "titulo": "Conclusos",
                },
                {
                    "_numeroMovimentacao": 39,
                    "data": "11/11/2019",
                    "titulo": " Despacho de Mero Expediente",
                },
                {
                    "_numeroMovimentacao": 40,
                    "data": "12/07/2019",
                    "titulo": "Juntada de Petição",
                },
                {
                    "_numeroMovimentacao": 41,
                    "data": "12/02/2019",
                    "titulo": "Juntada de Petição",
                },
                {
                    "_numeroMovimentacao": 42,
                    "data": "11/02/2019",
                    "titulo": "Juntada de Petição",
                },
                {
                    "_numeroMovimentacao": 43,
                    "data": "06/12/2018",
                    "titulo": "Conclusos",
                },
                {
                    "_numeroMovimentacao": 44,
                    "data": "05/12/2018",
                    "titulo": "Juntada de Petição",
                },
                {
                    "_numeroMovimentacao": 45,
                    "data": "29/11/2018",
                    "titulo": "Juntada de Petição",
                },
                {
                    "_numeroMovimentacao": 46,
                    "data": "28/11/2018",
                    "titulo": "Ato Publicado",
                },
                {
                    "_numeroMovimentacao": 47,
                    "data": "27/11/2018",
                    "titulo": "Disponibilização no Diário da Justiça Eletrônico",
                },
                {
                    "_numeroMovimentacao": 48,
                    "data": "27/11/2018",
                    "titulo": " Ato ordinatório praticado",
                },
                {
                    "_numeroMovimentacao": 49,
                    "data": "26/11/2018",
                    "titulo": "Juntada de Documento",
                },
                {
                    "_numeroMovimentacao": 50,
                    "data": "26/11/2018",
                    "titulo": "Juntada de Documento",
                },
                {
                    "_numeroMovimentacao": 51,
                    "data": "09/11/2018",
                    "titulo": "Ato Publicado",
                },
                {
                    "_numeroMovimentacao": 52,
                    "data": "08/11/2018",
                    "titulo": "Disponibilização no Diário da Justiça Eletrônico",
                },
                {
                    "_numeroMovimentacao": 53,
                    "data": "06/11/2018",
                    "titulo": " Ato ordinatório praticado",
                },
                {
                    "_numeroMovimentacao": 54,
                    "data": "16/10/2018",
                    "titulo": "Juntada de Documentos",
                },
                {
                    "_numeroMovimentacao": 55,
                    "data": "10/10/2018",
                    "titulo": "Juntada de Documentos",
                },
                {
                    "_numeroMovimentacao": 56,
                    "data": "24/09/2018",
                    "titulo": "Juntada de Documento",
                },
                {
                    "_numeroMovimentacao": 57,
                    "data": "24/09/2018",
                    "titulo": "Juntada de Documento",
                },
                {
                    "_numeroMovimentacao": 58,
                    "data": "24/09/2018",
                    "titulo": " Audiência Realizada",
                },
                {
                    "_numeroMovimentacao": 59,
                    "data": "24/09/2018",
                    "titulo": "Juntada de Petição",
                },
                {
                    "_numeroMovimentacao": 60,
                    "data": "21/09/2018",
                    "titulo": "Juntada de Petição",
                },
                {
                    "_numeroMovimentacao": 61,
                    "data": "21/09/2018",
                    "titulo": "Juntada de Petição",
                },
                {
                    "_numeroMovimentacao": 62,
                    "data": "21/09/2018",
                    "titulo": "Juntada de Petição",
                },
                {
                    "_numeroMovimentacao": 63,
                    "data": "20/09/2018",
                    "titulo": " Visto em correição",
                },
                {
                    "_numeroMovimentacao": 64,
                    "data": "06/06/2018",
                    "titulo": "Juntada de AR - Cumprido",
                },
                {
                    "_numeroMovimentacao": 65,
                    "data": "06/06/2018",
                    "titulo": "Juntada de AR - Cumprido",
                },
                {
                    "_numeroMovimentacao": 66,
                    "data": "15/05/2018",
                    "titulo": "Ato Publicado",
                },
                {
                    "_numeroMovimentacao": 67,
                    "data": "15/05/2018",
                    "titulo": "Ato Publicado",
                },
                {
                    "_numeroMovimentacao": 68,
                    "data": "11/05/2018",
                    "titulo": "Disponibilização no Diário da Justiça Eletrônico",
                },
                {
                    "_numeroMovimentacao": 69,
                    "data": "11/05/2018",
                    "titulo": "Disponibilização no Diário da Justiça Eletrônico",
                },
                {
                    "_numeroMovimentacao": 70,
                    "data": "11/05/2018",
                    "titulo": " Carta Expedida",
                },
                {
                    "_numeroMovimentacao": 71,
                    "data": "11/05/2018",
                    "titulo": " Carta Expedida",
                },
                {
                    "_numeroMovimentacao": 72,
                    "data": "11/05/2018",
                    "titulo": "Audiência Designada",
                },
                {
                    "_numeroMovimentacao": 73,
                    "data": "10/05/2018",
                    "titulo": " Não Concedida a Antecipação de tutela",
                },
                {
                    "_numeroMovimentacao": 74,
                    "data": "03/05/2018",
                    "titulo": "Conclusos",
                },
                {
                    "_numeroMovimentacao": 75,
                    "data": "02/05/2018",
                    "titulo": "Conclusos",
                },
                {
                    "_numeroMovimentacao": 76,
                    "data": "02/05/2018",
                    "titulo": "Distribuído por Sorteio",
                },
            ],
            "partesProcesso": {
                "autor": [
                    {
                        "categoria": "N/A",
                        "nomes": ["José Carlos Cerqueira Souza Filho"],
                    },
                    {
                        "categoria": "Advogado",
                        "nomes": ["Vinicius Faria de Cerqueira"],
                    },
                ],
                "autora": [
                    {"categoria": "N/A", "nomes": ["Livia Nascimento da Rocha"]},
                    {
                        "categoria": "Advogado",
                        "nomes": ["Vinicius Faria de Cerqueira"],
                    },
                ],
                "ré": [
                    {"categoria": "N/A", "nomes": ["Cony Engenharia Ltda."]},
                    {
                        "categoria": "Advogado",
                        "nomes": [
                            "Carlos Henrique de Mendonça Brandão",
                            "Guilherme Freire Furtado",
                            "Maria Eugênia Barreiros de Mello",
                            "Vítor Reis de Araujo Carvalho",
                        ],
                    },
                ],
                "réu": [
                    {"categoria": "N/A", "nomes": ["Banco do Brasil S A"]},
                    {
                        "categoria": "Advogado",
                        "nomes": ["Louise Rainer Pereira Gionédis"],
                    },
                ],
            },
        }

        crawler = TjalFirstInstance(
            base_url="https://www2.tjal.jus.br/cpopg/show.do",
            cnj=cnj,
        )

        result = crawler.extract()
        self.assertEqual(result, expected)
