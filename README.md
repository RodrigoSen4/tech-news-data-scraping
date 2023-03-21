# Tech News

  <strong>👨‍💻 Foi desenvolvidor um crawler </strong><br/>

  O projeto tem como principal objetivo fazer consultas em notícias sobre tecnologia no [_blog da Trybe_](https://blog.betrybe.com).


  <strong>🚵 Habilidades:</strong>
  <ul>
    <li>Utilizar o terminal interativo do Python</li>
    <li>Aplicar técnicas de raspagem de dados</li>
    <li>Extrair dados de conteúdo HTML</li>
    <li>Armazenar os dados obtidos em um banco de dados (MongoDB)</li>
  </ul>

# Orientações

<details>

  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.

</details>

<details>
  <summary><strong>🏃🏾 Executando o Projeto</strong></summary><br />

  As notícias a serem raspadas estarão disponíveis no _Blog da Trybe_: https://blog.betrybe.com.
  Essas notícias devem são salvas no banco de dados.


  <strong>MongoDB</strong>

  Para a realização deste projeto, utilizaremos um banco de dados chamado `tech_news`.
  As notícias serão armazenadas em uma coleção chamada `news`.

  Rodar MongoDB via Docker:

  <code>docker-compose up -d mongodb</code> no terminal.
  Para mais detalhes acerca do mongo com o docker, olhe o arquivo `docker-compose.yml`

  Caso queira instalar e rodar o servidor MongoDB nativo na máquina, siga as instruções no tutorial oficial:

  Ubuntu: <https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/>
  MacOS:  <https://docs.mongodb.com/guides/server/install/>
  
  Lembre-se de que o mongoDB utilizará por padrão a porta 27017. Se já houver outro serviço utilizando esta porta, considere desativá-lo.

  <strong>Executando o crawler</strong>

1. Executar o aquivo scraper dentro do ambiente do python 

  ```bash
 python3 -i tech_news/scraper.py
  ```

2. Executar a função get_tech_news(n) onde "n" é a quantidade de noticas a serem raspadas e salvas no banco de dados

  ```bash
get_tech_news(n)
  ```


</details>
