# O desafio

O Jusbrasil coleta uma variedade de dados públicos que não são facilmente acessíveis e melhora seu acesso para todos. Um dos tipos de dados coletados são os dados sobre processos.

O desafio é fazer uma API que busque dados de um processo em todos os graus dos Tribunais de Justiça de Alagoas (TJAL) e do Ceará (TJCE). Geralmente o processo começa no primeiro grau e pode subir para o segundo. Você deve buscar o processo em todos os graus e retornar suas informações.

Será necessário desenvolver crawlers para coletar esses dados no tribunal e uma API para fazer input e buscar o resultado depois.

## Input
Você deve criar uma api para receber um json contendo o número do processo. Para descobrir o tribunal você pode pedir no input ou usar o padrão cnj de numeração de processos jurídicos.

## Output
O cliente tem que ser capaz de pegar o dado quando o processamento termina, então você deve criar um mecanismo que permita isso, retornando sempre um JSON para os processos encontrados em todas as esferas.

Crawlers / Tribunais onde os dados serão coletados
Tanto o TJAL como o TJCE tem uma interface web para a consulta de processos. O endereço para essas consultas são:

**TJAL**

- 1º grau - https://www2.tjal.jus.br/cpopg/open.do
- 2º grau - https://www2.tjal.jus.br/cposg5/open.do

**TJCE**

- 1º grau - https://esaj.tjce.jus.br/cpopg/open.do
- 2º grau - https://esaj.tjce.jus.br/cposg5/open.do

### **Dados a serem coletados:**

- classe 
- área
- assunto
- data de distribuição
- juiz
- valor da ação
- partes do processo
- lista das movimentações (data e movimento)

### Exemplos de processos:

- 0710802-55.2018.8.02.0001 - TJAL
- 0017486-52.2009.8.02.0001 - TJAL
para mais números de processo, busque no diário oficial de Alagoas: https://www.jusbrasil.com.br/diarios/DJAL/

- 0070337-91.2008.8.06.0001 - TJCE
- 0200599-25.2022.8.06.0071 - TJCE
para mais números de processo, busque no diário de justiça do estado do Ceará: https://www.jusbrasil.com.br/diarios/DJCE/

### Alguns pontos que serão analisados:

- Organização do código
- Testes
- Facilidade ao rodar o projeto
- Escalabilidade: o quão fácil é escalar os crawlers.
- Performance: aqui avaliamos o tempo para crawlear todo o processo jurídico.

**Happy coding! :-)**

Instruções de envio
Após finalizar o desafio, nos envie um link para repositório do projeto (preferencialmente) ou um zip com o código, aqui por e-mail.

O tempo de término é livre, porém o ideal é que não demore muito mais do que uma semana, já que as circunstâncias para a vaga podem mudar. Mas não se preocupe quanto ao prazo, tente fazer o teste com bastante diligência, focando na qualidade do seu código!

Sendo assim, poderia nos confirmar o recebimento, por gentileza? 

Caso tenha alguma dúvida, não hesite em nos escrever! 

Um grande abraço e boa sorte 