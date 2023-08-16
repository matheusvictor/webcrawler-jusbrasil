# Comentários sobre o desafio e o processo de desenvolvimento:

---

## 🥴 Principais dificuldades:

- Antes de começar o desenvolvimento, precisei entender melhor o que o desafio pedia e por onde eu poderia começar. 
Como algumas coisas não estavam muito clara para mim, precisei de um tempo para entender melhor o problema, estudar e
planejar. 

- Precisei estudar o básico do Flask para que conseguisse utilizar o framework para criar uma API RESTful. Iniciei 
tentando construir um front-end, mas percebi que iria levar um tempo considerável para isso e não iria entregar os
requisitos que foram solicitados de fato; então decidi que isso poderia ficar para um outro momento.

- **Minhas requisições para o TJCE foram um grande empecilho para finalizar a solução**. Antes mesmo de crawlear
os portais de 2ª instância, passei dias buscando soluções para corrigir o problema, pois acreditava que isso poderia
ocorrer quando passasse para os portais de 2º grau e, além disso, também poderia acontecer em outras máquinas e 
comprometer a pessoa que fosse vir a utilizar a API que desenvolvi.

    Tentei utilizar bibliotecas alternativas à [Requests](https://requests.readthedocs.io/en/latest/), como a urllib3, mas sem sucesso. Busquei enriquecer um 
pouco mais a requisição, criando uma sessão com o Session e passando headers que pudessem ajudar a evitar a suspeita de
que as requisições estavam sendo feitas por um robô. Também cheguei a cogitar que pudesse ser algo relacionado ao meu
sistema operacional; então rodei o código em ambos os sistemas que tenho à minha disposição: Windows 10 e Linux 
(Ubuntu 22 LTS). Apesar disso, o problema ainda persistia.

  A fim de investigar um pouco mais as possibilidades, pedi para um amigo testar a mesma request que eu  estava tentando
fazer e, curiosamente, ele conseguiu realizar sem maiores problemas. Então, pensei na possibilidade de ser algo 
relacionado à minha rede e testei uma conexão através de uma rede 4G; mas sem sucesso. 

- Para além do [retorno 421](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/421) (como esse não é um dos códigos de retornos mais comuns e achei bastante específico, 
precisei dar uma rápida pesquisada sobre), logo abaixo está um dos erros mais frequentes que encontrei:

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

- Pretendia desenvolver um front-end interligado aos endpoints da API. Mas, como já havia passado um tempo desde que 
iniciei o desafio e precisei investir uma quantidade de tempo investigando os problemas descritos acima, optei por não
fazê-lo e focar apenas na construção da API. A construção de um font-end ficou para trabalhos futuros.
  
---

## 🤓 Comentários gerais e soluções adotadas

Inicialmente, pensei em desenvolver uma aplicação de ponta a ponta, isto é, incluindo também um front-end.
Cogitei utilizar o Angular para tal, pois possuo algum conhecimento na criação de componentes. Mas, por outro lado,
não tinha muita ideia de como construir um crawler usando TypeScript. 

Por isso, mesmo sendo um  framework que não possuo grande familiaridade, optei pelo uso do Flask. Essa escolha me 
pareceu uma alternativa bastante viável por dois principais motivos:

1. O **Flask** é um framework relativamente leve e poderia usar as rotas para a criação dos endpoints que lidaria com as
requisições. Além disso, teria a possibilidade de criar também um front-end; 

2. Possuo familiaridade com o Python e isso seria um ponto forte. Inclusive, por ter desenvolvido a solução de um outro
desafio de crawler (_Software Engineer Intern_, também para Jusbrasil), poderia aproveitar os conhecimentos que adquiri 
com ele, especialmente sobre o **BeautifulSoup**. 

Apesar disso, desenvolver a solução acabou demandando um pouco mais de tempo do imaginei, pois além de estar aprendendo
a utilizar algumas das tecnologias escolhidas (incluindo o Flask e o Selenium) durante o processo, encontrei problemas 
realizar requisições para o TJCE (esse talvez tenha sido meu maior desafio). Mais detalhes foram abordados na seção 
_**Principais dificuldades**_.

- Para validar se os crawlers que desenvolvi eram capazes de obter os dados nos portais indicados, precisei procurar
outros números de processos como exemplo e testá-los.

- A fim de não ficar mais tempo preso nos erros encontrados ao realizar requisições em busca de um processo de 1ª grau
no TJCE, precisei mockar uma página de exemplo para um número de processo específico a fim de validar o funcionamento do
crawler desenvolvido também neste portal, pois para o TJAL o comportamento estava como esperado.

- Como enfrentei o mesmo problema ao acessar o portal de 2º grau do TJCE e, considerando ainda a presença de pop-ups que
tornariam o mock desses comportamentos um pouco mais complicado para mim, precisei adotar outro processo alternativo
para obter a página do processo buscado. Mais detalhes sobre isso serão abordados nos tópicos abaixo.

- Simular as extrações por meio de mocks deixaria a API limitada, pois só seria possível extrair as informações para um
número bastante limitado de exemplos. Além disso, a presença de outros elementos interaivos (como os descritos acima) 
poderiam tornar o mock um pouco mais complexo. Então, precisei pensar em alguma alternativa para simular o acesso aos
portais (especialmente os do TJCE). Dessa forma, busquei automatizar o acesso aos portais com uso do Selenium. Apesar
de fazer com que as requisições levem mais tempo, especialmente quando realizadas para o TJCE (já que nesses cenários 
o Selenium é invocado para que possa ser obtida a página do processo), entendi que seria um trade-off necessário e
valeria a pena para tornar a API mais próxima de um cenário real. 

---

## 💬 Sugestões

- Incluir exemplos de modelo de requisição e também de retorno na descrição do desafio poderia ser um bom norte de como
os dados poderiam ser tratados.

- Incluir algumas orientações de troubleshooting de acordo com feedbacks de outras pessoas candidatas. Por exemplo: mais
alguém teve problemas realizados a bloqueio de IP, SSL, etc.? Se sim, alguns exemplos de maneiras mais comuns ou 
indicadas de se contarnar essas situações seriam de grande ajuda.
