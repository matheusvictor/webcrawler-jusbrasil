# Jusbrasil Crawler Challenge

---

## 🚀 Executando o projeto localmente

### 💻 Instalando dependências do projeto

A aplicação foi desenvolvida usando o framework **Flask** na versão `2.3.2`, e linguagem **Python** na versão
``3.13.3``. As dependências do projeto estão listadas no arquivo `requirements.txt`.

Além disso, será necessário ter instalado na máquina algum dos browsers a seguir: Firefox ou Chrome.
Para realizar as requisições, você pode optar por usar o Postman ou Insomnia.

### 🤖 Executando o projeto

Para executar o projeto, siga estas etapas:

1. Após baixar o projeto, abra um terminal dentro da pasta raiz (``webcrawler-jusbrasil``), execute o comando
   abaixo para instalar as dependências utilizando o `pip`:

````bash
pip install -r requirements.txt
````

2. Depois que as dependências forem instaladas, ainda no terminal, execute o comando a seguir:

````bash
python app.py
````

3. Aguarde até que o servidor local esteja pronto. Você verá a seguinte mensagem no terminal:

````commandline
* Running on http://127.0.0.1:5000 
````

4. Para ver mais informações sobre os endpoints disponíveis, exemplos de requisições e retornos, acesse a seguinte 
documentação: [Webcrawler Challenge Jusbrasil - Postman](https://documenter.getpostman.com/view/19098148/2s9Xy6qprs). Você pode realizar as requisições usando o Postman ou 
o Insomnia. Caso opte pelo Postman, dentro da pasta raiz do projeto, navegue até o diretório ``docs``, e lá você 
encontrará um arquivo ``Webcrawler Challenge Jusbrasil.postman_collection.json`` que poderá ser utilizado como coleções
de requisição que podem ser executadas. 

---

### 🔨 Requisitos básicos, ajustes e melhorias

**Requisitos básicos:**

- [x] Criar API
- [x] Criar crawlers
- [x] Extrair dados
- [x] Retornar JSON com dados extraídos 

**Ajustes e melhorias:**

- [ ] Criar front-end
- [x] Melhorar tratamento dos dados
- [x] Aplicação em paradgima POO
- [x] Tratamento de exceções
  - [ ] Melhorar tratamento de exeções
- [x] Testes unitários
- [x] Escrever ``README.md``
- [x] Escrever ``COMMENTS.md`` com sugestões de melhorias para o desafio
- [ ] Requisições assíncronas ou processamento em threads (investigar como)
- [x] Adicionar linter (Black)

[⬆ Voltar ao topo](#jusbrasil-crawler-challenge)<br>

