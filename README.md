# Projeto-C115

## Como rodar a API sem docker

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

## Como rodar a API com docker
Para executar a aplicação em um container, é possível utilizar os comandos do Makefile, que tornam os comandos mais abstratos e mais simples de utilizar. Os comandos feitos por trás podem ser vistos no arquivo Makefile. O comando ```make up``` que fará a build do container, juntamente com a sua execução.

Para encerrar o container em execução, é possível utilizar o comando ```make stop```.

### Observação
A string de conexão com o banco de dados fornecida está alocada no MongoDB Atlas em sua versão gratuita. Por isso, é possível que o cluster esteja offline e não seja possível acessá-lo. Caso tenha algum problema ao acessar, manda uma mensagem pra mim :D

## Iniciar a conversa
A API pode ser acessado por meio de requisições HTTP, conforme os exemplos abaixo:

- GET   <http://0.0.0.0:7999chatbot/chatbot/>

- POST  <http://0.0.0.0:7999chatbot/1?matricula=:str_numerica>

- POST  <http://0.0.0.0:7999chatbot/2?matricula=:str_numerica&materia=:indice_int>

- POST  <http://0.0.0.0:7999chatbot/2?matricula=:str_numerica&materia=:indice_int&nota=:indice_int>

Existem endpoints destinados ao acesso ao banco de dados, porém não estão relacionados com o uso do chatbot.