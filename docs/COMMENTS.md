# Comentários sobre o desafio e o processo de desenvolvimento:

Inicialmente, pensei em desenvolver uma aplicação de ponta a ponta, isto é, incluindo também um front-end.
Cogitei utilizar o **Angular** para tal, pois possuo algum conhecimento na criação de componentes. Mas, por outro lado,
não tinha muita ideia de como construir um crawler usando TypeScript. 

Por isso, mesmo sendo um  framework que não possuo grande familiaridade, optei pelo uso do Flask. Essa escolha me 
pareceu uma alternativa bastante viável por dois principais motivos:

1. O **Flask** é um framework relativamente leve e poderia usar as rotas para a criação dos endpoints responsáveis
pela requisição. Além disso, teria a possibilidade de criar também um front-end; 
2. Possuo familiaridade com o Python e isso seria um ponto forte. Inclusive, por ter desenvolvido a solução de um outro
desafio de crawler (Software Engineer Intern, também para Jusbrasil), poderia aproveitar os conhecimentos que adquiri 
com ele, especialmente sobre o **BeautifulSoup**. 

Apesar disso, desenvolver a solução acabou demandando um pouco mais de tempo do imaginei, pois além de estar aprendendo
a utilizar algumas das tecnologias escolhidas (incluindo o Flask e o Selenium) durante o processo, encontrei problemas 
realizar requisições para o TJCE. Mais detalhes serão abordados na seção _**Principais dificuldades**_.

---

## 🥴 Principais dificuldades:

- Antes de começar o desenvolvimento, precisei entender melhor o que o desafio pedia e por outro eu poderia começar. 
Algumas coisas não estavam muito clara para mim e investi uma parte considerável do tempo pensando;
- Precisei estudar o básico do Flask para que conseguisse utilizar o framework. Iniciei tentando construir um front-end,
até perceber que não seria o "ideal", uma vez que o desafio focava em outro requisito e isso poderia ficar para um outro
momento;
- **Minhas requisições para o TJCE foram um grande empecilho para finalizar a solução**. Antes mesmo de crawlear
os portais de 2ª instância, passei dias buscando soluções para corrigir o problema, pois acreditava que isso poderia
ocorrer quando passasse para os portais de 2º grau e, além disso, também poderia acontecer em outras máquinas e 
comprometer a pessoa que fosse vir a utilizar a API que desenvolvi. Tentei utilizar bibliotecas alternativas à 
[Requests](https://requests.readthedocs.io/en/latest/), mas sem sucesso.
- Para além do [retorno 421](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/421) 
(como esse não é um dos códigos de retornos mais comuns e achei bastante específico, precisei dar uma rápida pesquisada
sobre), um dos erros mais comuns que encontrei:

```commandline
{SSLError}HTTPSConnectionPool(host='esaj.tjce.jus.br', port=443): Max retries exceeded with 
url: /cpopg/show.do?processo.numero=0070337-91.2008.8.06.0001
(Caused by SSLError(SSLZeroReturnError(6, 'TLS/SSL connection has been closed (EOF) 
(_ssl.c:1002)')))
```

**É importante pontuar que, embora o erro diga que o número máximo de tentativas foi feita para uma determinada URL,
isso  aconteceu logo na primeira vez que tentei acessar o portal de 1º grau do TJCE.**

- A nível de organização de código, senti que manter todas minhas classes em um único ``models.py`` dificultava leitura
e manutenção; então preferi separar cada classe em arquivos diferentes e agrupá-las no diretório ``models``.
- Aprender a fazer testes unitários foi um pouco estranho no início, mas logo 
- Desenvolver um front-end e ligar aos endpois

---

## 🤓 Soluções

- Para validar se de fato os crawlers que desenvolvi eram capazes de obter os dados nos portais indicados, precisei 
procurar outros números de processos como exemplo e testá-los.
- A fim de não ficar muito mais tempo tentando solucionar ..., precisei mockar uma página de exemplo para um número de 
processo específico a fim de validar o crawler desenvolvido. Como enfrentei o mesmo problema ao acessar o portal de 2º 
grau do TJCE, adotei o mesmo processo alternativo.
- Simular as extrações dos portais do TJCE (1º e 2º grau) por meio de mocks deixaria a API limitada, pois só seria
possível extrair as informações para um número bastante limitado de exemplos. Então, precisei pensar em alguma 
alternativa para simular o acesso aos portais (especialmente os do TJCE). Por fim, busquei automatizar o acesso aos
portais com uso do Selenium. Apesar desse processo fazer com que as requisições levem mais tempo, especialmente quando 
realizadas para o TJCE, entendi que seria um trade-off necessário e valeria a pena para tornar a API mais próxima de um 
cenário real.

---

## 💬 Sugestões

- Incluir exemplos de modelo de requisição e também de retorno.
- Incluir algumas orientações de troubleshooting de acordo com feedbacks de outras pessoas candidatas.
