# Desafio B2W

- [Introdução](#introdução)<br>
- [Sistema de desenvolvimento](#sistema-de-desenvolvimento)
- [Funcionamento](#funcionamento)
  - [Consultas](#consultas)
  - [Cache](#cache)
  - [Exclusão](#exclusão)
- [Testes](#testes)

## Introdução

O desafio consiste na criação de uma API que contenha os dados dos planetas do universo Star Wars. O sistema armazena apenas três dados do planeta, sendo: nome, clima e terreno. Ao carregar o recurso planeta, a API deve apresentar os dados dos planetas cadastrados e os filmes em que cada planeta aparece. Para tanto, será feito uso da API [swapi](https://swapi.dev/api/).

## Sistema de desenvolvimento

Para a resolução do desafio, utilizei a linguagem de programação Python, em conjunto com os frameworks Django e Django Rest Framework

## Funcionamento

A URL base da API para teste local é http://localhost:8000/api/ contendo apenas um endpoint: http://localhost:8000/api/planetas/

### Consultas

Ao acessar a URL http://localhost:8000/api/planetas/, o sistema apresentará todos os planetas cadastrados. Os atributos apresentados serão: id, nome, clima, terreno e filmes.

- **Id**: Número inteiro sequencial gerado automaticamente pelo sistema
- **Nome**: Nome do planeta informado pelo usuário
- **Clima** Clima do planeta informado pelo usuário
- **Terreno**: Terreno do planeta informado pelo usuário
- **Filmes**: Lista com os nomes dos filmes onde o referido planeta aparece

**OBS.: A listagem de filmes é provida pela API [swapi](https://swapi.dev/api/). Para que a listagem de filmes do planeta seja carregada corretamente, o nome do planeta, cadastrado pelo usuário, deve constar na base de dados da API swapi.**

Para carregar os dados de um único planeta, basta acessar, por exemplo, http://localhost:8000/api/planetas/1/ onde o número 1 representa o ID do planeta cadastrado. Também é possível realizar a busca pelo nome do planeta. Para isso, basta acessar, por exemplo, http://localhost:8000/api/planetas/?nome=Tatooine onde o termo Tatooine representa o nome do planeta cadastrado

### Cache

Para que o carregamento da listagem de filmes ocorra, é necessário realizar ao menos duas requisições a API [swapi](https://swapi.dev/api/) por planeta cadastrado, onde a primeira localiza o planeta em sua base de dados, afim de obter a relação de filmes onde o planeta aparece, e a segunda obtém o nome do filme. Tamanha necessidade de consultas a API externa gera lentidão no carregamento dos dados. Sendo assim, foi implementado o uso de cache das consultas, reduzindo assim o tempo de espera do resultado e a carga de dados na rede.

### Exclusão

Para excluir um planeta, basta realizar uma requisição utilizando o método HTTP DELETE para http://localhost:8000/api/planetas/1/ onde o número 1 representa o ID do planeta que se deseja excluir.

## Testes

Os testes da API foram elaborados para verificar a capacidade do sistema em realizar algumas operações, como:

- Obter a relação de filmes do planeta cadastrado
- Apresentar um aviso caso não seja possível obter a relação de filmes do planeta cadastrado
- Apresentar a relação de planetas cadastrados
- Apresentar o planeta cadastrado com base em busca por ID 
- Apresentar o planeta cadastrado com base em busca por NOME

Todos os testes utilizam mock para simular a consulta a API [swapi](https://swapi.dev/api/).
