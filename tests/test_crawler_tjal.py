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
                "valorAcao": "R$ 281.178,42"
            },
            "movimentacoes": [
                {
                    "_numeroMovimentacao": 0,
                    "data": "21/07/2023",
                    "descricao": "Relação: 0450/2023\rData da Publicação: 24/07/2023\rNúmero do Diário: 3349",
                    "titulo": "Ato Publicado"
                },
                {
                    "_numeroMovimentacao": 1,
                    "data": "20/07/2023",
                    "descricao": "Relação: 0450/2023\rTeor do ato: Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Comum Cível Autor: José Carlos Cerqueira Souza Filho e outro Réu: Cony Engenharia Ltda. e outro ATO ORDINATÓRIO Em cumprimento ao disposto no Provimento nº 15/2019, da Corregedoria Geral da Justiça do Estado de Alagoas, fica(m) a(s) parte(s) ré intimada(s), na pessoa do seu advogado, para, no prazo de 15 (quinze) dias, providenciar(em) o recolhimento das custas processuais, sob pena de expedição de certidão ao FUNJURIS (Resolução TJ/AL nº 19/2007) para inscrição na divida ativa estadual, após o que será arquivado o processo. Ocorrendo o pagamento, devidamente atualizado, após a emissão da supracitada certidão de débito, deverá o interessado entregar a ficha de compensação bancária quitada na sede do FUNJURIS, que se responsabilizará pela devida baixa, além de oficiar à secretaria de onde se originou o débito acerca do referido pagamento (Resolução nº 19/2007, art. 33, § 6º). Maceió, 20 de julho de 2023 Marcelo Rodrigo Falcão Vieira Analista(escrivão substituto)\rAdvogados(s): Nelson Wilians Fratoni Rodrigues (OAB 9395AAL/), Carlos Henrique de Mendonça Brandão (OAB 6770AL /), Vinicius Faria de Cerqueira (OAB 9008/AL), Maria Eugênia Barreiros de Mello (OAB 14717AL/), Guilherme Freire Furtado (OAB 14781/AL), Vítor Reis de Araujo Carvalho (OAB 14928/AL)",
                    "titulo": "Disponibilização no Diário da Justiça Eletrônico"
                },
                {
                    "_numeroMovimentacao": 2,
                    "data": "20/07/2023",
                    "descricao": "Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Comum Cível Autor: José Carlos Cerqueira Souza Filho e outro Réu: Cony Engenharia Ltda. e outro ATO ORDINATÓRIO Em cumprimento ao disposto no Provimento nº 15/2019, da Corregedoria Geral da Justiça do Estado de Alagoas, fica(m) a(s) parte(s) ré intimada(s), na pessoa do seu advogado, para, no prazo de 15 (quinze) dias, providenciar(em) o recolhimento das custas processuais, sob pena de expedição de certidão ao FUNJURIS (Resolução TJ/AL nº 19/2007) para inscrição na divida ativa estadual, após o que será arquivado o processo. Ocorrendo o pagamento, devidamente atualizado, após a emissão da supracitada certidão de débito, deverá o interessado entregar a ficha de compensação bancária quitada na sede do FUNJURIS, que se responsabilizará pela devida baixa, além de oficiar à secretaria de onde se originou o débito acerca do referido pagamento (Resolução nº 19/2007, art. 33, § 6º). Maceió, 20 de julho de 2023 Marcelo Rodrigo Falcão Vieira Analista(escrivão substituto)Vencimento: 10/08/2023",
                    "titulo": " Ato ordinatório praticado"
                },
                {
                    "_numeroMovimentacao": 3,
                    "data": "20/07/2023",
                    "descricao": "Devolvido CJU - Cálculo de Custas Finais Realizado",
                    "titulo": " Devolvido CJU - Cálculo de Custas Finais Realizado"
                },
                {
                    "_numeroMovimentacao": 4,
                    "data": "20/07/2023",
                    "descricao": "",
                    "titulo": "Realizado cálculo de custas"
                },
                {
                    "_numeroMovimentacao": 5,
                    "data": "20/07/2023",
                    "descricao": "",
                    "titulo": "Juntada de Documento"
                },
                {
                    "_numeroMovimentacao": 6,
                    "data": "05/05/2023",
                    "descricao": "Seq.: 01 - Cumprimento de sentença",
                    "titulo": "Execução de Sentença Iniciada"
                },
                {
                    "_numeroMovimentacao": 7,
                    "data": "05/05/2023",
                    "descricao": "Relação: 0282/2023\rData da Publicação: 08/05/2023\rNúmero do Diário: 3296",
                    "titulo": "Ato Publicado"
                },
                {
                    "_numeroMovimentacao": 8,
                    "data": "04/05/2023",
                    "descricao": "Relação: 0282/2023\rTeor do ato: Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Comum Cível Autor: José Carlos Cerqueira Souza Filho e outro Réu: Cony Engenharia Ltda. e outro ATO ORDINATÓRIO Em cumprimento ao Provimento nº 15/2019, da Corregedoria-Geral da Justiça do Estado de Alagoas, em virtude do retorno dos autos da instância superior, manifestem-se as partes, em 15 (quinze) dias, requerendo o que de direito. Maceió, 04 de maio de 2023 Marcelo Rodrigo Falcão Vieira Analista(escrivão substituto)\rAdvogados(s): Nelson Wilians Fratoni Rodrigues (OAB 9395A/AL), Carlos Henrique de Mendonça Brandão (OAB 6770/AL), Vinicius Faria de Cerqueira (OAB 9008/AL), Maria Eugênia Barreiros de Mello (OAB 14717/AL), Guilherme Freire Furtado (OAB 14781/AL), Vítor Reis de Araujo Carvalho (OAB 14928/AL)",
                    "titulo": "Disponibilização no Diário da Justiça Eletrônico"
                },
                {
                    "_numeroMovimentacao": 9,
                    "data": "04/05/2023",
                    "descricao": "",
                    "titulo": "Recebido pela Contadoria UNIFICADA"
                },
                {
                    "_numeroMovimentacao": 10,
                    "data": "04/05/2023",
                    "descricao": "Ato Ordinatório- Remessa à contadoria",
                    "titulo": " Ato Ordinatório - Artigo 162, §4º, CPC"
                },
                {
                    "_numeroMovimentacao": 11,
                    "data": "04/05/2023",
                    "descricao": "Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Comum Cível Autor: José Carlos Cerqueira Souza Filho e outro Réu: Cony Engenharia Ltda. e outro ATO ORDINATÓRIO Em cumprimento ao Provimento nº 15/2019, da Corregedoria-Geral da Justiça do Estado de Alagoas, em virtude do retorno dos autos da instância superior, manifestem-se as partes, em 15 (quinze) dias, requerendo o que de direito. Maceió, 04 de maio de 2023 Marcelo Rodrigo Falcão Vieira Analista(escrivão substituto)Vencimento: 25/05/2023",
                    "titulo": " Ato ordinatório praticado"
                },
                {
                    "_numeroMovimentacao": 12,
                    "data": "03/05/2023",
                    "descricao": "",
                    "titulo": "Transitado em Julgado"
                },
                {
                    "_numeroMovimentacao": 13,
                    "data": "03/05/2023",
                    "descricao": "",
                    "titulo": "Recebimento da Instância Superior -  Altera situação para \"Julgado\""
                },
                {
                    "_numeroMovimentacao": 14,
                    "data": "26/04/2023",
                    "descricao": "Data do julgamento: 07/10/2021\rTrânsito em julgado: \rTipo de julgamento: Acórdão\rDecisão: à unanimidade de votos, em CONHECER de ambos os recursos de Apelação Cível; e, no mérito, por idêntica votação, NEGAR-LHES PROVIMENTO, mantendo incólume a Sentença proferida pelo Juízo de Direito de Primeiro Grau. Acordam, ainda, em majorar os honorários advocatícios sucumbenciais para 17% sobre o valor da condenação, nos termos do voto do Relator. \rSituação do provimento: \rRelator: Des. Otávio Leão Praxedes",
                    "titulo": "Recebido recurso eletrônico"
                },
                {
                    "_numeroMovimentacao": 15,
                    "data": "22/02/2021",
                    "descricao": "",
                    "titulo": "Remetido recurso eletrônico ao Tribunal de Justiça/Turma de recurso"
                },
                {
                    "_numeroMovimentacao": 16,
                    "data": "10/02/2021",
                    "descricao": "Nº Protocolo: WMAC.21.70031538-2\rTipo da Petição: Contrarrazões\rData: 10/02/2021 19:27\r",
                    "titulo": "Juntada de Documento"
                },
                {
                    "_numeroMovimentacao": 17,
                    "data": "06/01/2021",
                    "descricao": "Relação :0003/2021\rData da Publicação: 21/01/2021\rNúmero do Diário: 2738",
                    "titulo": "Ato Publicado"
                },
                {
                    "_numeroMovimentacao": 18,
                    "data": "06/01/2021",
                    "descricao": "Relação :0003/2021\rData da Publicação: 21/01/2021\rNúmero do Diário: 2738",
                    "titulo": "Ato Publicado"
                },
                {
                    "_numeroMovimentacao": 19,
                    "data": "06/01/2021",
                    "descricao": "Relação :0003/2021\rData da Publicação: 21/01/2021\rNúmero do Diário: 2738",
                    "titulo": "Ato Publicado"
                },
                {
                    "_numeroMovimentacao": 20,
                    "data": "06/01/2021",
                    "descricao": "Relação :0003/2021\rData da Publicação: 21/01/2021\rNúmero do Diário: 2738",
                    "titulo": "Ato Publicado"
                },
                {
                    "_numeroMovimentacao": 21,
                    "data": "06/01/2021",
                    "descricao": "Relação :0003/2021\rData da Publicação: 21/01/2021\rNúmero do Diário: 2738",
                    "titulo": "Ato Publicado"
                },
                {
                    "_numeroMovimentacao": 22,
                    "data": "06/01/2021",
                    "descricao": "Relação :0003/2021\rData da Publicação: 21/01/2021\rNúmero do Diário: 2738",
                    "titulo": "Ato Publicado"
                },
                {
                    "_numeroMovimentacao": 23,
                    "data": "05/01/2021",
                    "descricao": "Relação: 0003/2021\rTeor do ato: Ato Ordinatório: Interposto recurso de apelação pelos réus (Banco do Brasil e Cony Engenharia), intime-se a parte recorrida para apresentar contrarrazões, no prazo de 15 (quinze) dias, conforme o art. 1010,§ 1º do CPC. Se apresentada Apelação Adesiva pela parte recorrida (art.997, §2º do CPC), intime-se a parte contrária para contrarrazões, no prazo de 15 (quinze) dias, nos termos do Art. 1010, §2º do CPC. Caso as contrarrazões do recurso principal ou do adesivo ventilem matérias elencadas no art.1009, §1º do CPC, intime-se o recorrente para se manifestar sobre elas no prazo de 15(quinze) dias, conforme o art. 1009, § 2º, do CPC. Após as providências acima, remetam-se os autos ao Egrégio Tribunal de Justiça. Maceió, 04 de janeiro de 2021. Fernanda Patrícia Belo Marques Técnico Judiciário\rAdvogados(s): Carlos Henrique de Mendonça Brandão (OAB 6770/AL), Vinicius Faria de Cerqueira (OAB 9008/AL), Nelson Wilians Fratoni Rodrigues (OAB 9395A/AL), Maria Eugênia Barreiros de Mello (OAB 14717/AL), Guilherme Freire Furtado (OAB 14781/AL), Vítor Reis de Araujo Carvalho (OAB 14928/AL)",
                    "titulo": "Disponibilização no Diário da Justiça Eletrônico"
                },
                {
                    "_numeroMovimentacao": 24,
                    "data": "04/01/2021",
                    "descricao": "Ato Ordinatório: Interposto recurso de apelação pelos réus (Banco do Brasil e Cony Engenharia), intime-se a parte recorrida para apresentar contrarrazões, no prazo de 15 (quinze) dias, conforme o art. 1010,§ 1º do CPC. Se apresentada Apelação Adesiva pela parte recorrida (art.997, §2º do CPC), intime-se a parte contrária para contrarrazões, no prazo de 15 (quinze) dias, nos termos do Art. 1010, §2º do CPC. Caso as contrarrazões do recurso principal ou do adesivo ventilem matérias elencadas no art.1009, §1º do CPC, intime-se o recorrente para se manifestar sobre elas no prazo de 15(quinze) dias, conforme o art. 1009, § 2º, do CPC. Após as providências acima, remetam-se os autos ao Egrégio Tribunal de Justiça. Maceió, 04 de janeiro de 2021. Fernanda Patrícia Belo Marques Técnico Judiciário",
                    "titulo": " Ato Ordinatório - Artigo 162, §4º, CPC"
                },
                {
                    "_numeroMovimentacao": 25,
                    "data": "18/12/2020",
                    "descricao": "Nº Protocolo: WMAC.20.70269584-0\rTipo da Petição: Juntada de Instrumento de Procuração\rData: 18/12/2020 17:23\r",
                    "titulo": "Juntada de Documento"
                },
                {
                    "_numeroMovimentacao": 26,
                    "data": "18/12/2020",
                    "descricao": "Nº Protocolo: WMAC.20.70269581-5\rTipo da Petição: Recurso de Apelação\rData: 18/12/2020 17:18\r",
                    "titulo": "Juntada de Documento"
                },
                {
                    "_numeroMovimentacao": 27,
                    "data": "15/12/2020",
                    "descricao": "Nº Protocolo: WMAC.20.70265228-8\rTipo da Petição: Recurso de Apelação\rData: 15/12/2020 13:26\r",
                    "titulo": "Juntada de Documento"
                },
                {
                    "_numeroMovimentacao": 28,
                    "data": "24/11/2020",
                    "descricao": "Relação :0912/2020\rData da Publicação: 25/11/2020\rNúmero do Diário: 2711",
                    "titulo": "Ato Publicado"
                },
                {
                    "_numeroMovimentacao": 29,
                    "data": "24/11/2020",
                    "descricao": "Relação :0912/2020\rData da Publicação: 25/11/2020\rNúmero do Diário: 2711",
                    "titulo": "Ato Publicado"
                },
                {
                    "_numeroMovimentacao": 30,
                    "data": "24/11/2020",
                    "descricao": "Relação :0912/2020\rData da Publicação: 25/11/2020\rNúmero do Diário: 2711",
                    "titulo": "Ato Publicado"
                },
                {
                    "_numeroMovimentacao": 31,
                    "data": "24/11/2020",
                    "descricao": "Relação :0912/2020\rData da Publicação: 25/11/2020\rNúmero do Diário: 2711",
                    "titulo": "Ato Publicado"
                },
                {
                    "_numeroMovimentacao": 32,
                    "data": "23/11/2020",
                    "descricao": "Relação: 0912/2020\rTeor do ato: Forte nessas razões, JULGO PARCIALMENTE PROCEDENTES os pedidos da proemial, julgando extinto o processo com resolução de mérito, nos termos do art. 487, inciso I, do Estatuto Processual emergente, para o fim de CONDENAR AS DEMANDADAS, solidariamente: a) a ressarcir os danos materiais promovidos (lucros cessantes), cujo valor fixo em R$ 1.500,00 (três mil e quinhentos reais), por cada mês de atraso na entrega do imóvel , a incidir desde o dia 1 de agosto de 2017 até a data da efetiva entrega do imóvel, a ser apurada na fase de liquidação da sentença. Ressalto que esses valores deverão ser atualizados monetariamente pelo INPC desde a data em que cada aluguel seria devido, e acrescidos de juros de mora de 1% (um por cento) ao mês, contados da citação (art. 405 do Código Substantivo Civil). Para aqueles que venceram após a data da propositura da demanda, o juros de mora deverá incidir a partir da data de cada inadimplemento, para obstar o enriquecimento sem causa; b) em donos morais de R$ 5.000,00 (cinco mil reais), com juros de mora de 1% (um por cento) ao mês, a partir do dia 1 de agosto de 2017 (art. 397). Correção monetária, pelo INPC, desde a data do arbitramento; c) determino a substituição do índice INCC pelo IGP-M, a partir de 01 de agosto de 2017, e, como colorário, a devolução dos valores pagos a maior, com suas respectivas atualizações, nas mesmas condições do item a, deste dispositivo. Rejeito o pedido de restituição em dobro, por não vislumbrar má-fé dos beneficiários dos pagamentos indevidos. Oportunamente, condeno as demandada ao pagamento das custas e despesas processuais e dos honorários do advogado da parte adversa, que fixo, nos termos do art. 85, §2º, do Código de Processo Civil, e considerada a complexidade da demanda e as intervenções que exigiu, em 15% (quinze por cento) sobre o valor atualizado da condenação. Por fim, de modo a evitar o ajuizamento de embargos de declaração meramente protelatórios, registre-se que, ficam preteridas as demais alegações, por incompatíveis com a linha de raciocínio adotada, observando que os pedidos de ambas as partes foram apreciados nos limites em que foram formulados. Com efeito, ficam as partes advertidas, desde logo, que a oposição de embargos de declaração fora das hipóteses legais e/ou com postulação meramente infringente lhes sujeitará a imposição da multa prevista pelo artigo 1026, §2º, do Código de Processo Civil. Publique-se. Registre-se. Intimem-se.\rAdvogados(s): Orlando de Moura Cavalcante Neto (OAB 7313/AL), Thiago Maia Nobre Rocha (OAB 6213/AL), Vinicius Faria de Cerqueira (OAB 9008/AL), Marcus Vinicius Cavalcante Lins Filho (OAB 10871/AL)",
                    "titulo": "Disponibilização no Diário da Justiça Eletrônico"
                },
                {
                    "_numeroMovimentacao": 33,
                    "data": "23/11/2020",
                    "descricao": "Forte nessas razões, JULGO PARCIALMENTE PROCEDENTES os pedidos da proemial, julgando extinto o processo com resolução de mérito, nos termos do art. 487, inciso I, do Estatuto Processual emergente, para o fim de CONDENAR AS DEMANDADAS, solidariamente: a) a ressarcir os danos materiais promovidos (lucros cessantes), cujo valor fixo em R$ 1.500,00 (três mil e quinhentos reais), por cada mês de atraso na entrega do imóvel , a incidir desde o dia 1 de agosto de 2017 até a data da efetiva entrega do imóvel, a ser apurada na fase de liquidação da sentença. Ressalto que esses valores deverão ser atualizados monetariamente pelo INPC desde a data em que cada aluguel seria devido, e acrescidos de juros de mora de 1% (um por cento) ao mês, contados da citação (art. 405 do Código Substantivo Civil). Para aqueles que venceram após a data da propositura da demanda, o juros de mora deverá incidir a partir da data de cada inadimplemento, para obstar o enriquecimento sem causa; b) em donos morais de R$ 5.000,00 (cinco mil reais), com juros de mora de 1% (um por cento) ao mês, a partir do dia 1 de agosto de 2017 (art. 397). Correção monetária, pelo INPC, desde a data do arbitramento; c) determino a substituição do índice INCC pelo IGP-M, a partir de 01 de agosto de 2017, e, como colorário, a devolução dos valores pagos a maior, com suas respectivas atualizações, nas mesmas condições do item a, deste dispositivo. Rejeito o pedido de restituição em dobro, por não vislumbrar má-fé dos beneficiários dos pagamentos indevidos. Oportunamente, condeno as demandada ao pagamento das custas e despesas processuais e dos honorários do advogado da parte adversa, que fixo, nos termos do art. 85, §2º, do Código de Processo Civil, e considerada a complexidade da demanda e as intervenções que exigiu, em 15% (quinze por cento) sobre o valor atualizado da condenação. Por fim, de modo a evitar o ajuizamento de embargos de declaração meramente protelatórios, registre-se que, ficam preteridas as demais alegações, por incompatíveis com a linha de raciocínio adotada, observando que os pedidos de ambas as partes foram apreciados nos limites em que foram formulados. Com efeito, ficam as partes advertidas, desde logo, que a oposição de embargos de declaração fora das hipóteses legais e/ou com postulação meramente infringente lhes sujeitará a imposição da multa prevista pelo artigo 1026, §2º, do Código de Processo Civil. Publique-se. Registre-se. Intimem-se.Vencimento: 16/12/2020",
                    "titulo": " Julgado procedente em parte do pedido"
                },
                {
                    "_numeroMovimentacao": 34,
                    "data": "23/09/2020",
                    "descricao": "",
                    "titulo": "Conclusos"
                },
                {
                    "_numeroMovimentacao": 35,
                    "data": "16/08/2020",
                    "descricao": "Despacho Visto em Autoinspeção",
                    "titulo": " Visto em Autoinspeção"
                },
                {
                    "_numeroMovimentacao": 36,
                    "data": "11/05/2020",
                    "descricao": "Nº Protocolo: WMAC.20.70092549-0\rTipo da Petição: Pedido de Andamento do proc./sent./decisões/desp.\rData: 11/05/2020 13:28\r",
                    "titulo": "Juntada de Documento"
                },
                {
                    "_numeroMovimentacao": 37,
                    "data": "10/12/2019",
                    "descricao": "",
                    "titulo": "Conclusos"
                },
                {
                    "_numeroMovimentacao": 38,
                    "data": "11/11/2019",
                    "descricao": "DESPACHO Compulsando detidamente o feito, verifico que este inclui-se nos processos com prioridade de impulsionamento, consoante recomendação exarada pelo Conselho Nacional de Justiça, a qual determina a priorização de andamento das demandas paralisadas há mais de 100 (dias). Destarte, considerando que cada uma desses processos exige análise acurada por este magistrado a fim de que lhe seja dado efetivo provimento, determino a conclusão de todos os autos que se amoldem à hipótese alhures delineada - de competência do gabinete - para análise e devido impulsionamento, este especificamente, na fila concluso - impulso ao feito. Cumpra-se. Maceió(AL), 11 de novembro de 2019. José Cícero Alves da Silva Juiz de Direito",
                    "titulo": " Despacho de Mero Expediente"
                },
                {
                    "_numeroMovimentacao": 39,
                    "data": "12/07/2019",
                    "descricao": "Nº Protocolo: WMAC.19.70150828-9\rTipo da Petição: Petição\rData: 11/07/2019 23:50\r",
                    "titulo": "Juntada de Petição"
                },
                {
                    "_numeroMovimentacao": 40,
                    "data": "12/02/2019",
                    "descricao": "Nº Protocolo: WMAC.19.70034823-7\rTipo da Petição: Petição\rData: 12/02/2019 14:58\r",
                    "titulo": "Juntada de Petição"
                },
                {
                    "_numeroMovimentacao": 41,
                    "data": "11/02/2019",
                    "descricao": "Nº Protocolo: WMAC.19.70032532-6\rTipo da Petição: Petição\rData: 11/02/2019 09:13\r",
                    "titulo": "Juntada de Petição"
                },
                {
                    "_numeroMovimentacao": 42,
                    "data": "06/12/2018",
                    "descricao": "",
                    "titulo": "Conclusos"
                },
                {
                    "_numeroMovimentacao": 43,
                    "data": "05/12/2018",
                    "descricao": "Nº Protocolo: WMAC.18.70259903-1\rTipo da Petição: Petição\rData: 05/12/2018 16:46\r",
                    "titulo": "Juntada de Petição"
                },
                {
                    "_numeroMovimentacao": 44,
                    "data": "29/11/2018",
                    "descricao": "Nº Protocolo: WMAC.18.70255192-6\rTipo da Petição: Petição\rData: 29/11/2018 15:07\r",
                    "titulo": "Juntada de Petição"
                },
                {
                    "_numeroMovimentacao": 45,
                    "data": "28/11/2018",
                    "descricao": "Relação :0499/2018\rData da Publicação: 29/11/2018\rNúmero do Diário: 2233",
                    "titulo": "Ato Publicado"
                },
                {
                    "_numeroMovimentacao": 46,
                    "data": "27/11/2018",
                    "descricao": "Relação: 0499/2018\rTeor do ato: ATO ORDINATÓRIO Em cumprimento ao disposto no art. 152,VI do CPC, procedo à intimação das partes para especificarem e justificarem as provas que ainda pretendem produzir, fundamentamente, pelo prazo comum de 5(cinco) dias. Maceió, 27 de novembro de 2018\rAdvogados(s): Orlando de Moura Cavalcante Neto (OAB 7313/AL), Thiago Maia Nobre Rocha (OAB 6213/AL), Vinicius Faria de Cerqueira (OAB 9008/AL), Rafael Sganzerla Durand (OAB 10132A/AL), Marcus Vinicius Cavalcante Lins Filho (OAB 10871/AL)",
                    "titulo": "Disponibilização no Diário da Justiça Eletrônico"
                },
                {
                    "_numeroMovimentacao": 47,
                    "data": "27/11/2018",
                    "descricao": "ATO ORDINATÓRIO Em cumprimento ao disposto no art. 152,VI do CPC, procedo à intimação das partes para especificarem e justificarem as provas que ainda pretendem produzir, fundamentamente, pelo prazo comum de 5(cinco) dias. Maceió, 27 de novembro de 2018",
                    "titulo": " Ato ordinatório praticado"
                },
                {
                    "_numeroMovimentacao": 48,
                    "data": "26/11/2018",
                    "descricao": "Nº Protocolo: WMAC.18.70251514-8\rTipo da Petição: Impugnação à Contestação\rData: 26/11/2018 15:37\r",
                    "titulo": "Juntada de Documento"
                },
                {
                    "_numeroMovimentacao": 49,
                    "data": "26/11/2018",
                    "descricao": "Nº Protocolo: WMAC.18.70251511-3\rTipo da Petição: Impugnação à Contestação\rData: 26/11/2018 15:35\r",
                    "titulo": "Juntada de Documento"
                },
                {
                    "_numeroMovimentacao": 50,
                    "data": "09/11/2018",
                    "descricao": "Relação :0456/2018\rData da Publicação: 12/11/2018\rNúmero do Diário: 2222",
                    "titulo": "Ato Publicado"
                },
                {
                    "_numeroMovimentacao": 51,
                    "data": "08/11/2018",
                    "descricao": "Relação: 0456/2018\rTeor do ato: Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Ordinário Autor: José Carlos Cerqueira Souza Filho e outro Réu: Conaço Engenharia Ltda. e outro ATO ORDINATÓRIO Intimo a parte autora a apresentar, querendo, no prazo de 15 (quinze) dias, impugnação às contestações. Maceió, 06 de novembro de 2018 Hallph Sá de Araújo Analista Judiciário\rAdvogados(s): Vinicius Faria de Cerqueira (OAB 9008/AL)",
                    "titulo": "Disponibilização no Diário da Justiça Eletrônico"
                },
                {
                    "_numeroMovimentacao": 52,
                    "data": "06/11/2018",
                    "descricao": "Autos n°: 0710802-55.2018.8.02.0001 Ação: Procedimento Ordinário Autor: José Carlos Cerqueira Souza Filho e outro Réu: Conaço Engenharia Ltda. e outro ATO ORDINATÓRIO Intimo a parte autora a apresentar, querendo, no prazo de 15 (quinze) dias, impugnação às contestações. Maceió, 06 de novembro de 2018 Hallph Sá de Araújo Analista JudiciárioVencimento: 29/11/2018",
                    "titulo": " Ato ordinatório praticado"
                },
                {
                    "_numeroMovimentacao": 53,
                    "data": "16/10/2018",
                    "descricao": "Nº Protocolo: WMAC.18.70221617-5\rTipo da Petição: Contestação\rData: 16/10/2018 14:43\r",
                    "titulo": "Juntada de Documentos"
                },
                {
                    "_numeroMovimentacao": 54,
                    "data": "10/10/2018",
                    "descricao": "Nº Protocolo: WMAC.18.70218154-1\rTipo da Petição: Contestação\rData: 10/10/2018 14:04\r",
                    "titulo": "Juntada de Documentos"
                },
                {
                    "_numeroMovimentacao": 55,
                    "data": "24/09/2018",
                    "descricao": "",
                    "titulo": "Juntada de Documento"
                },
                {
                    "_numeroMovimentacao": 56,
                    "data": "24/09/2018",
                    "descricao": "",
                    "titulo": "Juntada de Documento"
                },
                {
                    "_numeroMovimentacao": 57,
                    "data": "24/09/2018",
                    "descricao": "Assentada - Genérico",
                    "titulo": " Audiência Realizada"
                },
                {
                    "_numeroMovimentacao": 58,
                    "data": "24/09/2018",
                    "descricao": "Nº Protocolo: WMAC.18.70203989-3\rTipo da Petição: Petição\rData: 24/09/2018 10:09\r",
                    "titulo": "Juntada de Petição"
                },
                {
                    "_numeroMovimentacao": 59,
                    "data": "21/09/2018",
                    "descricao": "Nº Protocolo: WMAC.18.70203544-8\rTipo da Petição: Petição\rData: 21/09/2018 18:07\r",
                    "titulo": "Juntada de Petição"
                },
                {
                    "_numeroMovimentacao": 60,
                    "data": "21/09/2018",
                    "descricao": "Nº Protocolo: WMAC.18.70203528-6\rTipo da Petição: Petição\rData: 21/09/2018 17:42\r",
                    "titulo": "Juntada de Petição"
                },
                {
                    "_numeroMovimentacao": 61,
                    "data": "21/09/2018",
                    "descricao": "Nº Protocolo: WMAC.18.70203260-0\rTipo da Petição: Petição\rData: 21/09/2018 13:58\r",
                    "titulo": "Juntada de Petição"
                },
                {
                    "_numeroMovimentacao": 62,
                    "data": "20/09/2018",
                    "descricao": "DESPACHO VISTO EM CORREIÇÃO",
                    "titulo": " Visto em correição"
                },
                {
                    "_numeroMovimentacao": 63,
                    "data": "06/06/2018",
                    "descricao": "Em 06  de  junho  de  2018 é juntado a estes autos o aviso de recebimento (AR803969759TJ - Cumprido), referente  ao  ofício  n. 0710802-55.2018.8.02.0001-0002, emitido para Conaço Engenharia Ltda.. Usuário: ",
                    "titulo": "Juntada de AR - Cumprido"
                },
                {
                    "_numeroMovimentacao": 64,
                    "data": "06/06/2018",
                    "descricao": "Em 06  de  junho  de  2018 é juntado a estes autos o aviso de recebimento (AR803969745TJ - Cumprido), referente  ao  ofício  n. 0710802-55.2018.8.02.0001-0001, emitido para Banco do Brasil S A. Usuário: ",
                    "titulo": "Juntada de AR - Cumprido"
                },
                {
                    "_numeroMovimentacao": 65,
                    "data": "15/05/2018",
                    "descricao": "Relação :0220/2018\rData da Publicação: 16/05/2018\rNúmero do Diário: 2105",
                    "titulo": "Ato Publicado"
                },
                {
                    "_numeroMovimentacao": 66,
                    "data": "15/05/2018",
                    "descricao": "Relação :0220/2018\rData da Publicação: 16/05/2018\rNúmero do Diário: 2105",
                    "titulo": "Ato Publicado"
                },
                {
                    "_numeroMovimentacao": 67,
                    "data": "11/05/2018",
                    "descricao": "Relação: 0220/2018\rTeor do ato: DECISÃOTrata-se de ação ordinária de indenização por danos morais e materias c/c obrigação de fazer c/c declaração de nulidade de contrato de financiamento bancário c/c pedido de tutela antecipada proposta por JOSÉ CARLOS CERQUEIRA SOUZA FILHO e LIVIA NASCIMENTO DA ROCHA, qualificados na inicial, em face de a CONY ENGENHARIA LTDA. e BANCO DO BRASIL, igualmente qualificados.Narra a exordial que os autores adquiriram o apartamento residencial de nº 502, da Torre I, do Empreendimento Residencial Dellavia Park Club, situado na Ladeira Murilo Monteiro Valente, n.º 375, no bairro do Barro Duro, Maceió/AL, cuja vendedora foi a ré CONY ENGENHARIA LTDA., pelo valor de R$ 232.000,00 (duzentos e trinta e dois mil reais).Segue narrando que o instrumento celebrado em 02/12/2013 previa a entrega do imóvel no prazo de 36 (trinta e seis) meses contados do início da obra, sendo admitida uma tolerância de no máximo 18 (dezoito) meses. Dentro dessa perspectiva, foi prometido que a obra seria iniciada em no máximo 60 (sessenta) dias da assinatura do contrato, ou seja seria iniciada em 02/02/2014 com previsão de entrega para 02/02/2017, porém, até a presente data a obra não foi concluída.Aduz que os demandantes ainda sendo cobrados ilegalmente pelo BANCO DO BRASIL, também réu da ação, numa suposta \"taxa de obra\", que decorre de financiamento bancário.Requer, em sede de tutela de urgência, que seja determinado ao BANCO DO BRASIL a SUSPENSÃO da cobrança de taxa de Obra.É o relatório. Decido.Ab initio, concedo aos Demandantes as benesses da assistência judiciária gratuita, em respeito as determinações contidas no art. 98 e art. 99 da Lei nº. 13.105/2015 (Código de Processo Civil - CPC/2015).O Código de Defesa do Consumidor, em seu art. 6.º, VIII, assegura como direito básico do consumidor a facilitação da defesa de seus direitos, inclusive com a inversão do ônus da prova, a seu favor, quando, a critério do juiz, for verossímil a alegação ou quando for ele hipossuficiente, segundo as regras ordinárias de experiência. Busca-se, assim assegurar a igualdade material.Em que pese bastar apenas um dos requisitos para a inversão, o caso em tela preenche as duas condições. Assim com fulcro no art. 6.º, VIII, do CDC DECIDO POR INVERTER O ÔNUS DA PROVA.Passo a apreciar o pedido de tutela provisória de urgência.Segundo o art. 300 do CPC/15, a tutela de urgência será concedida quando houver elementos que evidenciem a probabilidade do direito e o perigo de dano ou o risco ao resultado útil do processo. O dispositivo deixa evidentes os requisitos da tutela antecipada de urgência, quais sejam, a probabilidade do direito, doutrinariamente conhecida como fumus boni iuris, e o perigo de dano ou risco ao resultado útil do processo, chamado periculum in mora.Nesse trilhar, importa esclarecer que a tutela de urgência antecipada se funda em um Juízo de cognição sumária, de modo que a medida, quando concedida, será precária, haja vista ser fundamental a necessidade de ser reversível (300, §3º, do CPC/2015).Portanto, a antecipação provisória dos efeitos finais da tutela definitiva, permite o gozo antecipado e imediato dos efeitos próprios da tutela definitiva pretendida, mas não se funda em um juízo de valor exauriente, de modo que pode ser desconstituída a qualquer tempo.Nessa esteira de pensamento, passa-se a analisar o caso concreto e o preenchimento dos requisitos necessários à concessão da tutela provisória pretendida.No caso em tela, pretende a parte autora a suspensão da cobrança da \"taxa de obra\", em razão do suposto descumprimento contratual por parte da demandada no tocante ao prazo estabelecido para a entrega do imóvel.Conforme se extrai dos autos, as partes firmaram um contrato de compra e venda de um apartamento, tendo sido estipulada o prazo para sua entrega em 36 (trinta e seis) meses, com um prazo de tolerância de 18 (dezoito) meses, consoante cláusula quarta do contrato (fls.39). Logo o prazo final para entrega do imóvel se encerra em 02/08/2018, levando em consideração o prazo de tolerância estabelecido no contrato.É cediço que a taxa de evolução de obra é devida desde a aprovação do financiamento até o término da obra. Portanto, se a obra atrasar, é devido o pagamento da referida taxa ao banco que financiou o imóvel, no caso, o Banco do Brasil, até a sua conclusão. Sendo certo que ocorrendo a mora da construtora requerida em relação à entrega do imóvel, a parte autora não pode ser penalizada com o pagamento de tal encargo. No entanto, no caso em deslinde, ainda não houve mora da construtora, haja vista que ainda não fora encerrado o prazo estimado para entrega do imóvel. Nesse ponto impende destacar que é legal a cláusula contratual que prevê a prorrogação do prazo razoável para entrega do imóvel, considerando o princípio pacta sunt servanda. Desta feita, verifica-se a ausência de probabilidade do direito da parte autora, haja vista que, consoante dito alhures, a taxa de evolução de obra é devida até a conclusão da obra, bem como que não houve mora por parte da construtora demandada, haja vista que não houve, ainda, atraso na entrega do imóvel, tendo em vista a cláusula que prevê prazo de tolerância para entrega do imóvel.Ante o exposto, por considerar ausente a probabilidade do direito (art. 300 do CPC/15), INDEFIRO o pedido de tutela de urgência requestado.Inclua-se o feito em pauta de audiência de conciliação. Cite-se a parte ré eintime-a desta decisão, bem como para que compareça à audiência na data designada pelo Cartório, o que deve ser feito com antecedência mínima de 20 dias.Intime-se os autores por advogado constituído (art. 334, §3º, CPC/15).Deverá a parte ré ser advertida da possibilidade do art. 334, §5º, bem como do termo inicial do prazo de contestação (art. 335).Fiquem as partes advertidas, ainda, de que o não comparecimento injustificado à audiência de conciliação é considerado ato atentatório à dignidade da justiça e será sancionado com multa de até dois por cento da vantagem econômica pretendida ou do valor da causa (art. 334, §8º).Publique-se. Intime-seMaceió, 10 de maio de 2018.Henrique Gomes de Barros TeixeiraJuiz de Direito\rAdvogados(s): Vinicius Faria de Cerqueira (OAB 9008/AL)",
                    "titulo": "Disponibilização no Diário da Justiça Eletrônico"
                },
                {
                    "_numeroMovimentacao": 68,
                    "data": "11/05/2018",
                    "descricao": "Relação: 0220/2018\rTeor do ato: Conciliação\rData: 24/09/2018 Hora 14:00\rLocal: Sala de Audiência\rSituacão: Pendente\rAdvogados(s): Vinicius Faria de Cerqueira (OAB 9008/AL)",
                    "titulo": "Disponibilização no Diário da Justiça Eletrônico"
                },
                {
                    "_numeroMovimentacao": 69,
                    "data": "11/05/2018",
                    "descricao": "AR DIGITAL - Citação e Intimação - Audiência de Instrução e Julgamento - Juizado",
                    "titulo": " Carta Expedida"
                },
                {
                    "_numeroMovimentacao": 70,
                    "data": "11/05/2018",
                    "descricao": "AR DIGITAL - Citação e Intimação - Audiência de Instrução e Julgamento - Juizado",
                    "titulo": " Carta Expedida"
                },
                {
                    "_numeroMovimentacao": 71,
                    "data": "11/05/2018",
                    "descricao": "Conciliação\rData: 24/09/2018 Hora 14:00\rLocal: Sala de Audiência\rSituacão: Realizada",
                    "titulo": "Audiência Designada"
                },
                {
                    "_numeroMovimentacao": 72,
                    "data": "10/05/2018",
                    "descricao": "DECISÃOTrata-se de ação ordinária de indenização por danos morais e materias c/c obrigação de fazer c/c declaração de nulidade de contrato de financiamento bancário c/c pedido de tutela antecipada proposta por JOSÉ CARLOS CERQUEIRA SOUZA FILHO e LIVIA NASCIMENTO DA ROCHA, qualificados na inicial, em face de a CONY ENGENHARIA LTDA. e BANCO DO BRASIL, igualmente qualificados.Narra a exordial que os autores adquiriram o apartamento residencial de nº 502, da Torre I, do Empreendimento Residencial Dellavia Park Club, situado na Ladeira Murilo Monteiro Valente, n.º 375, no bairro do Barro Duro, Maceió/AL, cuja vendedora foi a ré CONY ENGENHARIA LTDA., pelo valor de R$ 232.000,00 (duzentos e trinta e dois mil reais).Segue narrando que o instrumento celebrado em 02/12/2013 previa a entrega do imóvel no prazo de 36 (trinta e seis) meses contados do início da obra, sendo admitida uma tolerância de no máximo 18 (dezoito) meses. Dentro dessa perspectiva, foi prometido que a obra seria iniciada em no máximo 60 (sessenta) dias da assinatura do contrato, ou seja seria iniciada em 02/02/2014 com previsão de entrega para 02/02/2017, porém, até a presente data a obra não foi concluída.Aduz que os demandantes ainda sendo cobrados ilegalmente pelo BANCO DO BRASIL, também réu da ação, numa suposta \"taxa de obra\", que decorre de financiamento bancário.Requer, em sede de tutela de urgência, que seja determinado ao BANCO DO BRASIL a SUSPENSÃO da cobrança de taxa de Obra.É o relatório. Decido.Ab initio, concedo aos Demandantes as benesses da assistência judiciária gratuita, em respeito as determinações contidas no art. 98 e art. 99 da Lei nº. 13.105/2015 (Código de Processo Civil - CPC/2015).O Código de Defesa do Consumidor, em seu art. 6.º, VIII, assegura como direito básico do consumidor a facilitação da defesa de seus direitos, inclusive com a inversão do ônus da prova, a seu favor, quando, a critério do juiz, for verossímil a alegação ou quando for ele hipossuficiente, segundo as regras ordinárias de experiência. Busca-se, assim assegurar a igualdade material.Em que pese bastar apenas um dos requisitos para a inversão, o caso em tela preenche as duas condições. Assim com fulcro no art. 6.º, VIII, do CDC DECIDO POR INVERTER O ÔNUS DA PROVA.Passo a apreciar o pedido de tutela provisória de urgência.Segundo o art. 300 do CPC/15, a tutela de urgência será concedida quando houver elementos que evidenciem a probabilidade do direito e o perigo de dano ou o risco ao resultado útil do processo. O dispositivo deixa evidentes os requisitos da tutela antecipada de urgência, quais sejam, a probabilidade do direito, doutrinariamente conhecida como fumus boni iuris, e o perigo de dano ou risco ao resultado útil do processo, chamado periculum in mora.Nesse trilhar, importa esclarecer que a tutela de urgência antecipada se funda em um Juízo de cognição sumária, de modo que a medida, quando concedida, será precária, haja vista ser fundamental a necessidade de ser reversível (300, §3º, do CPC/2015).Portanto, a antecipação provisória dos efeitos finais da tutela definitiva, permite o gozo antecipado e imediato dos efeitos próprios da tutela definitiva pretendida, mas não se funda em um juízo de valor exauriente, de modo que pode ser desconstituída a qualquer tempo.Nessa esteira de pensamento, passa-se a analisar o caso concreto e o preenchimento dos requisitos necessários à concessão da tutela provisória pretendida.No caso em tela, pretende a parte autora a suspensão da cobrança da \"taxa de obra\", em razão do suposto descumprimento contratual por parte da demandada no tocante ao prazo estabelecido para a entrega do imóvel.Conforme se extrai dos autos, as partes firmaram um contrato de compra e venda de um apartamento, tendo sido estipulada o prazo para sua entrega em 36 (trinta e seis) meses, com um prazo de tolerância de 18 (dezoito) meses, consoante cláusula quarta do contrato (fls.39). Logo o prazo final para entrega do imóvel se encerra em 02/08/2018, levando em consideração o prazo de tolerância estabelecido no contrato.É cediço que a taxa de evolução de obra é devida desde a aprovação do financiamento até o término da obra. Portanto, se a obra atrasar, é devido o pagamento da referida taxa ao banco que financiou o imóvel, no caso, o Banco do Brasil, até a sua conclusão. Sendo certo que ocorrendo a mora da construtora requerida em relação à entrega do imóvel, a parte autora não pode ser penalizada com o pagamento de tal encargo. No entanto, no caso em deslinde, ainda não houve mora da construtora, haja vista que ainda não fora encerrado o prazo estimado para entrega do imóvel. Nesse ponto impende destacar que é legal a cláusula contratual que prevê a prorrogação do prazo razoável para entrega do imóvel, considerando o princípio pacta sunt servanda. Desta feita, verifica-se a ausência de probabilidade do direito da parte autora, haja vista que, consoante dito alhures, a taxa de evolução de obra é devida até a conclusão da obra, bem como que não houve mora por parte da construtora demandada, haja vista que não houve, ainda, atraso na entrega do imóvel, tendo em vista a cláusula que prevê prazo de tolerância para entrega do imóvel.Ante o exposto, por considerar ausente a probabilidade do direito (art. 300 do CPC/15), INDEFIRO o pedido de tutela de urgência requestado.Inclua-se o feito em pauta de audiência de conciliação. Cite-se a parte ré eintime-a desta decisão, bem como para que compareça à audiência na data designada pelo Cartório, o que deve ser feito com antecedência mínima de 20 dias.Intime-se os autores por advogado constituído (art. 334, §3º, CPC/15).Deverá a parte ré ser advertida da possibilidade do art. 334, §5º, bem como do termo inicial do prazo de contestação (art. 335).Fiquem as partes advertidas, ainda, de que o não comparecimento injustificado à audiência de conciliação é considerado ato atentatório à dignidade da justiça e será sancionado com multa de até dois por cento da vantagem econômica pretendida ou do valor da causa (art. 334, §8º).Publique-se. Intime-seMaceió, 10 de maio de 2018.Henrique Gomes de Barros TeixeiraJuiz de DireitoVencimento: 01/06/2018",
                    "titulo": " Não Concedida a Antecipação de tutela"
                },
                {
                    "_numeroMovimentacao": 73,
                    "data": "03/05/2018",
                    "descricao": "",
                    "titulo": "Conclusos"
                },
                {
                    "_numeroMovimentacao": 74,
                    "data": "02/05/2018",
                    "descricao": "",
                    "titulo": "Conclusos"
                },
                {
                    "_numeroMovimentacao": 75,
                    "data": "02/05/2018",
                    "descricao": "",
                    "titulo": "Distribuído por Sorteio"
                }
            ],
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
                "autora": [
                    {
                        "categoria": "N/A",
                        "nomes": [
                            "Livia Nascimento da Rocha"
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
                ],
                "réu": [
                    {
                        "categoria": "N/A",
                        "nomes": [
                            "Banco do Brasil S A"
                        ]
                    },
                    {
                        "categoria": "Advogado",
                        "nomes": [
                            "Nelson Wilians Fratoni Rodrigues"
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
