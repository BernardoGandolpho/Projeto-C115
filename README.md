# Projeto-C115

## Como rodar a API

Após clonar o repositório é necessário criar um arquivo com o nome ".env" (sem as aspas) seguindo o padrão do arquivo ".env.sample". Esse arquivo contém a string de conexão com o banco de dados mongo, que pode ser hospedado localmente ou em um serviço online como o MongoDB Atlas.
Criado o arquivo ".env" execute os comandos abaixo para executar a aplicação.
#### Criar ambiente virtual
```
virtualenv venv -p python3
source venv/bin/activate
```

#### Instalar requisitos
```
pip install -r requirements.txt
```

#### Executar o programa
```
python main.py
```

### Docker
Para executar o programa em um docker, é necessário ter docker e docker-compose instalados.
Os comandos para executar são:  
```
docker-compose build
docker-compose up
```

O conteúdo do banco de dados ficará armazenado em uma pasta com nome db, evitando que o conteúdo seja perdido quando o docker for criado.

## Iniciar a conversa
O bot pode ser acessado por meio de requisições HTTP, conforme os exemplos abaixo:

- GET   <http://0.0.0.0:7999chatbot/chatbot/>

- POST  <http://0.0.0.0:7999chatbot/1?matricula=:str_numerica>

- POST  <http://0.0.0.0:7999chatbot/2?matricula=:str_numerica&materia=:indice_int>

- POST  <http://0.0.0.0:7999chatbot/2?matricula=:str_numerica&materia=:indice_int&nota=:indice_int>