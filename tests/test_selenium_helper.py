import logging
import time
import unittest

from selenium import webdriver
from selenium.common import NoSuchDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from models.tjce_second_instance import TjceSecondInstance


class SeleniumHelper(unittest.TestCase):
    def test_navigation_process_from_second_instance(self):
        try:
            driver = webdriver.Firefox()
        except:
            try:
                driver = webdriver.Chrome()
            except NoSuchDriverException:
                logging.error(
                    "Não foi possível abrir um navegador para realizar a busca!"
                )
                exit(1)

        driver.get("https://esaj.tjce.jus.br/cposg5/open.do")
        time.sleep(3)

        form = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "formularioConsulta"))
        )

        if form:
            print(driver.title)
            driver.find_element(By.ID, "numeroDigitoAnoUnificado").send_keys(
                "0070337-91.2008"
            )
            driver.find_element(By.ID, "foroNumeroUnificado").send_keys("0001")
            time.sleep(3)
            driver.find_element(By.ID, "pbConsultar").click()

            modal = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "modalIncidentes"))
            )

            if modal:
                if not driver.find_element(
                    By.CSS_SELECTOR, "#processoSelecionado"
                ).is_selected():
                    driver.find_element(By.CSS_SELECTOR, "#processoSelecionado").click()
                driver.find_element(By.ID, "botaoEnviarIncidente").click()
                time.sleep(3)

                page = driver.page_source
                print(page)

        driver.close()

        self.assertIsNotNone(form)

    def test_get_process_from_tcje_second_instance_when_cnj_00703379120088060001(
        self,
    ):
        cnj = "0070337-91.2008.8.06.0001"
        expected = {
            "detalhes": {
                "area": "Criminal",
                "assunto": "Crimes de Trânsito",
                "classe": "Apelação Criminal",
                "dataDistribuicao": None,
                "juiz": "-",
                "valorAcao": "",
            },
            "movimentacoes": [
                {"_numeroMovimentacao": 0, "data": "14/05/2020", "titulo": "Remessa"},
                {
                    "_numeroMovimentacao": 1,
                    "data": "14/05/2020",
                    "titulo": "Baixa Definitiva",
                },
                {
                    "_numeroMovimentacao": 2,
                    "data": "13/05/2020",
                    "titulo": "Baixa Definitiva",
                },
                {
                    "_numeroMovimentacao": 3,
                    "data": "13/05/2020",
                    "titulo": "Transitado em Julgado pelo STJ",
                },
                {
                    "_numeroMovimentacao": 4,
                    "data": "13/05/2020",
                    "titulo": "Expedição de Certidão",
                },
                {
                    "_numeroMovimentacao": 5,
                    "data": "13/05/2020",
                    "titulo": "Recebidos os autos do STJ",
                },
                {
                    "_numeroMovimentacao": 6,
                    "data": "13/05/2020",
                    "titulo": "Juntada de Documento",
                },
                {
                    "_numeroMovimentacao": 7,
                    "data": "27/02/2020",
                    "titulo": "Enviados Autos Digitais ao STJ",
                },
                {
                    "_numeroMovimentacao": 8,
                    "data": "27/02/2020",
                    "titulo": "Expedida Certidão de Envio ao STJ",
                },
                {
                    "_numeroMovimentacao": 9,
                    "data": "17/07/2018",
                    "titulo": "Expedido Termo de Transferência",
                },
                {
                    "_numeroMovimentacao": 10,
                    "data": "17/07/2018",
                    "titulo": "Transferência",
                },
                {
                    "_numeroMovimentacao": 11,
                    "data": "12/07/2018",
                    "titulo": "Juntada de Petição",
                },
                {
                    "_numeroMovimentacao": 12,
                    "data": "10/07/2018",
                    "titulo": "Expedição de Certidão",
                },
                {
                    "_numeroMovimentacao": 13,
                    "data": "28/06/2018",
                    "titulo": "Expedida Certidão de Informação - Petição Portal",
                },
                {
                    "_numeroMovimentacao": 14,
                    "data": "28/06/2018",
                    "titulo": "Ato Ordinatório - Intimação Ministério Público - CIÊNCIA",
                },
                {
                    "_numeroMovimentacao": 15,
                    "data": "28/06/2018",
                    "titulo": "Decorrido prazo",
                },
                {
                    "_numeroMovimentacao": 16,
                    "data": "28/06/2018",
                    "titulo": "Certidão de Decurso de Prazo Emitida",
                },
                {
                    "_numeroMovimentacao": 17,
                    "data": "07/06/2018",
                    "titulo": "Expedida Certidão de Publicação de Decisão Monocrática",
                },
                {
                    "_numeroMovimentacao": 18,
                    "data": "06/06/2018",
                    "titulo": "Publicado no Diário da Justiça Eletrônico",
                },
                {
                    "_numeroMovimentacao": 19,
                    "data": "06/06/2018",
                    "titulo": "Publicado no Diário da Justiça Eletrônico",
                },
                {
                    "_numeroMovimentacao": 20,
                    "data": "06/06/2018",
                    "titulo": "Publicado no Diário da Justiça Eletrônico",
                },
                {
                    "_numeroMovimentacao": 21,
                    "data": "21/05/2018",
                    "titulo": "Enviados Autos Digitais da Vice-Presidência para Divisão de Recursos Privativos",
                },
                {
                    "_numeroMovimentacao": 22,
                    "data": "21/05/2018",
                    "titulo": "Enviados Autos Digitais da Vice-Presidência para Divisão de Recursos Privativos",
                },
                {
                    "_numeroMovimentacao": 23,
                    "data": "21/05/2018",
                    "titulo": "Prejudicado o recurso",
                },
                {
                    "_numeroMovimentacao": 24,
                    "data": "21/05/2018",
                    "titulo": "Recurso especial admitido",
                },
                {
                    "_numeroMovimentacao": 25,
                    "data": "09/05/2018",
                    "titulo": "Expedido Termo de Transferência",
                },
                {
                    "_numeroMovimentacao": 26,
                    "data": "09/05/2018",
                    "titulo": "Transferência",
                },
                {
                    "_numeroMovimentacao": 27,
                    "data": "27/04/2018",
                    "titulo": "Expedido Termo de Conclusão ao Vice-Presidente (Admissibilidade/Geral)",
                },
                {
                    "_numeroMovimentacao": 28,
                    "data": "27/04/2018",
                    "titulo": "Juntada de Petição",
                },
                {
                    "_numeroMovimentacao": 29,
                    "data": "01/03/2018",
                    "titulo": "Expedido Termo de Ciência ao MP",
                },
                {
                    "_numeroMovimentacao": 30,
                    "data": "15/02/2018",
                    "titulo": "Expedido Termo de Intimação",
                },
                {
                    "_numeroMovimentacao": 31,
                    "data": "15/02/2018",
                    "titulo": "Remetidos Autos à Coord. de Recur. aos Tribunais Superiores",
                },
                {
                    "_numeroMovimentacao": 32,
                    "data": "15/02/2018",
                    "titulo": "Juntada de Petição",
                },
                {
                    "_numeroMovimentacao": 33,
                    "data": "15/02/2018",
                    "titulo": "Juntada de Petição",
                },
                {
                    "_numeroMovimentacao": 34,
                    "data": "15/02/2018",
                    "titulo": "Juntada de Documento",
                },
                {
                    "_numeroMovimentacao": 35,
                    "data": "15/02/2018",
                    "titulo": "Juntada de Documento",
                },
                {
                    "_numeroMovimentacao": 36,
                    "data": "15/02/2018",
                    "titulo": "Juntada de Petição",
                },
                {
                    "_numeroMovimentacao": 37,
                    "data": "15/02/2018",
                    "titulo": "Juntada de Petição",
                },
                {
                    "_numeroMovimentacao": 38,
                    "data": "15/02/2018",
                    "titulo": "Juntada de Petição",
                },
                {
                    "_numeroMovimentacao": 39,
                    "data": "15/02/2018",
                    "titulo": "Juntada de Documento",
                },
                {
                    "_numeroMovimentacao": 40,
                    "data": "15/02/2018",
                    "titulo": "Juntada de Documento",
                },
                {
                    "_numeroMovimentacao": 41,
                    "data": "15/02/2018",
                    "titulo": "Juntada de Petição",
                },
                {
                    "_numeroMovimentacao": 42,
                    "data": "15/02/2018",
                    "titulo": "Juntada de Recurso Interno",
                },
                {
                    "_numeroMovimentacao": 43,
                    "data": "25/01/2018",
                    "titulo": "Expedida Certidão",
                },
                {
                    "_numeroMovimentacao": 44,
                    "data": "18/01/2018",
                    "titulo": "Juntada de Petição",
                },
                {
                    "_numeroMovimentacao": 45,
                    "data": "17/01/2018",
                    "titulo": "Concluso ao Relator",
                },
                {
                    "_numeroMovimentacao": 46,
                    "data": "11/01/2018",
                    "titulo": "Juntada de Documento",
                },
                {
                    "_numeroMovimentacao": 47,
                    "data": "18/12/2017",
                    "titulo": "Expedida Certidão de Publicação de Acórdão",
                },
                {
                    "_numeroMovimentacao": 48,
                    "data": "15/12/2017",
                    "titulo": "Expedido Termo de Ciência ao MP",
                },
                {
                    "_numeroMovimentacao": 49,
                    "data": "12/12/2017",
                    "titulo": "Expedida Certidão de Julgamento",
                },
                {
                    "_numeroMovimentacao": 50,
                    "data": "12/12/2017",
                    "titulo": "Acórdão - Assinado",
                },
                {
                    "_numeroMovimentacao": 51,
                    "data": "29/11/2017",
                    "titulo": "Decorrido prazo",
                },
                {
                    "_numeroMovimentacao": 52,
                    "data": "29/11/2017",
                    "titulo": "Certidão de Decurso de Prazo Emitida",
                },
                {
                    "_numeroMovimentacao": 53,
                    "data": "13/11/2017",
                    "titulo": "Juntada de Documento",
                },
                {
                    "_numeroMovimentacao": 54,
                    "data": "10/11/2017",
                    "titulo": "Expedido Termo de Autuação/Distribuição/Conclusão",
                },
                {
                    "_numeroMovimentacao": 55,
                    "data": "09/11/2017",
                    "titulo": "Juntada de Petição",
                },
                {
                    "_numeroMovimentacao": 56,
                    "data": "08/11/2017",
                    "titulo": "Juntada de Petição",
                },
                {
                    "_numeroMovimentacao": 57,
                    "data": "31/10/2017",
                    "titulo": "Expedida Certidão de Publicação de Acórdão",
                },
                {
                    "_numeroMovimentacao": 58,
                    "data": "30/10/2017",
                    "titulo": "Publicado no Diário da Justiça Eletrônico",
                },
                {
                    "_numeroMovimentacao": 59,
                    "data": "27/10/2017",
                    "titulo": "Expedido Termo de Ciência ao MP",
                },
                {
                    "_numeroMovimentacao": 60,
                    "data": "25/10/2017",
                    "titulo": "Enviado acórdão para publicação",
                },
                {
                    "_numeroMovimentacao": 61,
                    "data": "25/10/2017",
                    "titulo": "Enviados Autos Digitais para TJCENEXE - Apelação Crime",
                },
                {
                    "_numeroMovimentacao": 62,
                    "data": "25/10/2017",
                    "titulo": "Expedida Certidão de Julgamento",
                },
                {
                    "_numeroMovimentacao": 63,
                    "data": "24/10/2017",
                    "titulo": "Acórdão - Assinado",
                },
                {
                    "_numeroMovimentacao": 64,
                    "data": "24/10/2017",
                    "titulo": "Conhecido o recurso e provido em parte",
                },
                {"_numeroMovimentacao": 65, "data": "24/10/2017", "titulo": "Julgado"},
                {
                    "_numeroMovimentacao": 66,
                    "data": "17/10/2017",
                    "titulo": "Publicado no Diário da Justiça Eletrônico",
                },
                {
                    "_numeroMovimentacao": 67,
                    "data": "17/10/2017",
                    "titulo": "Publicado no Diário da Justiça Eletrônico",
                },
                {
                    "_numeroMovimentacao": 68,
                    "data": "16/10/2017",
                    "titulo": "Concluso ao Relator",
                },
                {
                    "_numeroMovimentacao": 69,
                    "data": "16/10/2017",
                    "titulo": "Expedida Certidão de Publicação de Pauta",
                },
                {
                    "_numeroMovimentacao": 70,
                    "data": "13/10/2017",
                    "titulo": "Pauta de Julgamento enviada para disponibilização no Diário da Justiça Eletrônica",
                },
                {
                    "_numeroMovimentacao": 71,
                    "data": "11/10/2017",
                    "titulo": "Inclusão em pauta",
                },
                {
                    "_numeroMovimentacao": 72,
                    "data": "10/10/2017",
                    "titulo": "Enviados Autos Digitais do Gabinete para Secretaria de Câmara",
                },
                {
                    "_numeroMovimentacao": 73,
                    "data": "10/10/2017",
                    "titulo": "Proferido despacho de mero expediente",
                },
                {
                    "_numeroMovimentacao": 74,
                    "data": "10/10/2017",
                    "titulo": "Proferido despacho de mero expediente",
                },
                {
                    "_numeroMovimentacao": 75,
                    "data": "09/10/2017",
                    "titulo": "Concluso ao Revisor",
                },
                {
                    "_numeroMovimentacao": 76,
                    "data": "06/10/2017",
                    "titulo": "Enviados Autos Digitais do Gabinete para Secretaria de Câmara",
                },
                {
                    "_numeroMovimentacao": 77,
                    "data": "06/10/2017",
                    "titulo": "Relatório - Assinado",
                },
                {
                    "_numeroMovimentacao": 78,
                    "data": "06/10/2017",
                    "titulo": "Concluso ao Relator",
                },
                {
                    "_numeroMovimentacao": 79,
                    "data": "05/10/2017",
                    "titulo": "Concluso ao Revisor",
                },
                {
                    "_numeroMovimentacao": 80,
                    "data": "05/10/2017",
                    "titulo": "Enviados Autos Digitais do Gabinete para Secretaria de Câmara",
                },
                {
                    "_numeroMovimentacao": 81,
                    "data": "05/10/2017",
                    "titulo": "Relatório - Assinado",
                },
                {
                    "_numeroMovimentacao": 82,
                    "data": "04/10/2016",
                    "titulo": "Concluso ao Relator",
                },
                {
                    "_numeroMovimentacao": 83,
                    "data": "04/10/2016",
                    "titulo": "Juntada de Petição",
                },
                {
                    "_numeroMovimentacao": 84,
                    "data": "16/09/2016",
                    "titulo": "Expedido Termo de Vista ao Ministério Público(PGJ)",
                },
                {
                    "_numeroMovimentacao": 85,
                    "data": "15/09/2016",
                    "titulo": "Expedido Termo de Autuação/Distribuição/Remessa  Coord. Apelação Crime",
                },
                {
                    "_numeroMovimentacao": 86,
                    "data": "13/09/2016",
                    "titulo": "Processo Distribuído por Sorteio",
                },
                {
                    "_numeroMovimentacao": 87,
                    "data": "08/09/2016",
                    "titulo": "Processo Autuado",
                },
                {
                    "_numeroMovimentacao": 88,
                    "data": "01/09/2016",
                    "titulo": "Recebidos os autos com Recurso",
                },
            ],
            "partesProcesso": {
                "apelado:": [
                    {
                        "categoria": "N/A",
                        "nomes": ["Ministério Público do Estado do Ceará"],
                    }
                ],
                "apelante:": [
                    {"categoria": "N/A", "nomes": ["William Azevedo dos Santos"]},
                    {"categoria": "Advogado", "nomes": ["Duquesne Monteiro de Castro"]},
                ],
                "custos legis:": [
                    {"categoria": "N/A", "nomes": ["Ministério Público Estadual"]}
                ],
            },
        }
        crawler = TjceSecondInstance(
            base_url="https://esaj.tjce.jus.br/cposg5/open.do",
            cnj=cnj,
        )

        result = crawler.extract()
        self.assertEqual(expected, result)
