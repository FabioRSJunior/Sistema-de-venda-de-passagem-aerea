# Sistema para venda de passagens aéreas

# Explicação:

Esse repositório é dividido em 2 projetos que resolvem o problema de venda de passagens de avião. A primeira parte, contem uma aplicação usando Flask, Restful e SQL lite. Foi a que ficou melhor e mais elegante, ela possuí todas as partes requeridas no trabalho “container”. Utilizei bibliotecas e paradigmas diferentes do que vimos em aula para exercitar os conceitos. Mas tive dificuldades para desacoplar o SQLite do meu container e colocar ele em um diferente, portando nesse projeto a parte de banco de dados está junto a aplicação flask.

A segunda parte contem uma aplicação usando Flask e Postgresql, aqui não tem todas as funcionalidades requisitada no “trabalho container”, possui somente os get() e post() para cada classe. Fiz essa parte assim pois queria exercitar a orquestração de contêineres que trabalham juntos.

Docker + kubernetes + Flask + Sqlite:

[Sistema-de-venda-de-passagem-aerea/Parte_1_Flask_Rest_SQLite/Trab_asa (teste docker) at main · FabioRSJunior/Sistema-de-venda-de-passagem-aerea](https://github.com/FabioRSJunior/Sistema-de-venda-de-passagem-aerea/tree/main/Parte_1_Flask_Rest_SQLite/Trab_asa%20(teste%20docker))

Docker + kubernetes + Flask + MySQL:

[Sistema-de-venda-de-passagem-aerea/Parte_2_Flask_Postgres/k8s_final at main · FabioRSJunior/Sistema-de-venda-de-passagem-aerea](https://github.com/FabioRSJunior/Sistema-de-venda-de-passagem-aerea/tree/main/Parte_2_Flask_Postgres/k8s_final)

# Introdução:

![https://www.notion.so../Digital%20inovation/Carrefour_Data_Engineer_2021/M9_arquitetura_sistemas_avan%C3%A7ados/image-20211109001251797.png](https://www.notion.so../Digital%20inovation/Carrefour_Data_Engineer_2021/M9_arquitetura_sistemas_avan%C3%A7ados/image-20211109001251797.png)

image-20211109001251797

# Parte 1

Foi desenvolvido um sistema que vende e exibe passagens aéreas em REST com o banco de dados SQLite.

### Banco de Dados:

```
NOME DA TABELA: 'usuarios'     # Armazena os dados dos usuarios
    id_usuario    = Inteiro PK # Id_usurio para relacinar com as passagens
    nome_usuario  = String(40) # Nome normal
    email_usuario = String(40) # Unique pois será usado na autenticacao
    senha_usuario = String(20) # Senha para login
    token_usuario = String(20) # Aqui vai ficar o IP

NOME DA TABELA: 'aeroporto'
    id_aeroporto    = Inteiro PK # Id de aeroporto, para as passagens
    nome_aeroporto  = String(40) # Nome do aeroporto, n existe nomes repetidos
    cidade_aeroporto= String(40) # cidade onde está o aeroporto

NOME DA TABELA: 'voos'
    id_voo            = Integer PK   # Registro do voo
    aeroporto_saida   = Integer FK('aeroporto.id_aeroporto') ) # De qual aeroporto ele está partindo
    aeroporto_chegada = Integer FK('aeroporto.id_aeroporto') )  # Para qual aeroporto ele está indo
    data_voo          = Integer    # data do voo em inteiros
    valor_voo         = Integer    # Qual o valor da passagem

__tablename__='compras'
    id_compras = Integer, primary_key=True)# ID para recuperar a conta
    id_usuario = String(40), ForeignKey('usuarios.id_usuario') ) # O usuario que faz a compra
    id_voo = String(40), ForeignKey('voos.id_voo')) # Qual voo está sendo comprado
    id_valor= String(40), ForeignKey('voos.valor_voo'))# valor que saiu a passagem

```

## REST vs RESTful

REST é um estilo arquitetônico, um modelo para seguir ao desenvolver uma APIs, o RESTFUL é um serviço que utiliza desse paradigma. é utilizado para definir aplicações que implementam webservices que utilizam a arquitetura REST. Uma aplicação que segue a arquitetura REST é uma aplicação RESTful.

Flask-Restful é uma extensão do Flask que adiciona suporte para a construção rápida de REST APIs, incentiva a arquitetura rest.

As vantegens:

- As operações estão em json, que fica mais fácil para manipular.
- Fica bonito e limpo
- As classes ficam organizadas

### Projeto:

Uma vez que as rotas das APIS já estão configuradas, o banco de dados foi criado e alguns dados já vem por default. podemos realizar as operações abaixo:

```
# Voce pode rodar cada um de forma independente
python3 models
python3 utils

# Executa a aplicação:
flask run
```

Aqui temos todas as urls de acesso para cada função, temos também os json’s para ficar mais fácil de fazer os put’s e post’s.

Existe um usuário já cadastrado no banco, se quiser utilizar a função de requisição de usuários você pode utilizar login: **fabioufu** senha: **1111**. Quando se cria um usuário com o método post ele vira um usuário, e seu e-mail e sua senha são seus login e senha, respectivamente.

|  | Faz: | Endereço: | função: | json: POST |
| --- | --- | --- | --- | --- |
| 1 | * efetuar login(email,senha) | http://127.0.0.1:5000/usuarios/ | Retorna usuários se login | {“nome_usuario” : “fabricio”,“email_usuario”: “fabricio@karma”,“senha_usuario”: “2222”,“token_usuario”: “9999”} |
| 2 | * Efetuar logout(chave da sessão) | http://127.0.0.1:5000/usuarios/logout | Efetua login | só get(), logout() |
| 3 | *validar sessão (chave da sessão) | http://127.0.0.1:5000/usuarios/compar/9999 cuidado: é um put | Um usuário só faz uma compra se colocar seu token | urls : inteiro + put : { “id_usuario” : 1,“id_voo”: 3} |
| 4 | * (Retorna todos Aeroportos ) | http://127.0.0.1:5000/Aeroportos/ | Get,Set,Put,post | {“Aeroporto saida”:2, “Aeroporto chegada”:3,“Data”: 99 ,“Valor”:888} |
| 5 | Retornar aeroportos por origem | http://127.0.0.1:5000/vooos/todos/data/3 | o ultimo parâmetro é o id do aeroporto de origem | inteiro |
| 6 | Retornar todos os voos | http://127.0.0.1:5000/vooos/99 | para da data informada | inteiro |
| 7 | * Pesquisar voos | http://127.0.0.1:5000/vooos/preco | pesquisa voo menor tarifa | somente get() |
| 8 | * Realizar uma compra | http://127.0.0.1:5000/usuarios/compar | um usuário compra uma passagem | - exercício 3 - |

### 1 - Efetuar Login (Email,Senha)

![https://www.notion.so../Digital%20inovation/Carrefour_Data_Engineer_2021/M9_arquitetura_sistemas_avan%C3%A7ados/Screenshot%20from%202021-11-04%2021-59-17.png](https://www.notion.so../Digital%20inovation/Carrefour_Data_Engineer_2021/M9_arquitetura_sistemas_avan%C3%A7ados/Screenshot%20from%202021-11-04%2021-59-17.png)

Screenshot from 2021-11-04 21-59-17

### 2 - Efetuar Logout (Chave da sessão)

![https://www.notion.so../Digital%20inovation/Carrefour_Data_Engineer_2021/M9_arquitetura_sistemas_avan%C3%A7ados/Screenshot%20from%202021-11-08%2012-14-44.png](https://www.notion.so../Digital%20inovation/Carrefour_Data_Engineer_2021/M9_arquitetura_sistemas_avan%C3%A7ados/Screenshot%20from%202021-11-08%2012-14-44.png)

Screenshot from 2021-11-08 12-14-44

### 3,8 - Validar uma sessão com o Token e Efetuar uma compra

### 

![https://www.notion.so../Digital%20inovation/Carrefour_Data_Engineer_2021/M9_arquitetura_sistemas_avan%C3%A7ados/Screenshot%20from%202021-11-08%2012-33-46.png](https://www.notion.so../Digital%20inovation/Carrefour_Data_Engineer_2021/M9_arquitetura_sistemas_avan%C3%A7ados/Screenshot%20from%202021-11-08%2012-33-46.png)

### 4 - Retornar Aeroportos

![https://www.notion.so../Digital%20inovation/Carrefour_Data_Engineer_2021/M9_arquitetura_sistemas_avan%C3%A7ados/Screenshot%20from%202021-11-08%2012-15-51.png](https://www.notion.so../Digital%20inovation/Carrefour_Data_Engineer_2021/M9_arquitetura_sistemas_avan%C3%A7ados/Screenshot%20from%202021-11-08%2012-15-51.png)

Screenshot from 2021-11-08 12-15-51

### 5 - Retornar Aeroportos por origem

Infelizmente ele retorna as voos que tem o ID do aeroporto, minha modelagem de dados não foi muito interessante nessa parte. A função retorna uma lista com dos os voos que possuem como origem o aeroporto de id que se passa na URL.

### 

![https://www.notion.so../Digital%20inovation/Carrefour_Data_Engineer_2021/M9_arquitetura_sistemas_avan%C3%A7ados/Screenshot%20from%202021-11-08%2012-03-37.png](https://www.notion.so../Digital%20inovation/Carrefour_Data_Engineer_2021/M9_arquitetura_sistemas_avan%C3%A7ados/Screenshot%20from%202021-11-08%2012-03-37.png)

### 6 - Retorna todos os Voos para a data informada

![https://www.notion.so../Digital%20inovation/Carrefour_Data_Engineer_2021/M9_arquitetura_sistemas_avan%C3%A7ados/image-20211109023928415.png](https://www.notion.so../Digital%20inovation/Carrefour_Data_Engineer_2021/M9_arquitetura_sistemas_avan%C3%A7ados/image-20211109023928415.png)

image-20211109023928415

### 7 - Pesquisar VOOS

Ele organiza a tabela pelo índice preço antes de exibir, a tabela infelizmente estava com poucos dados

![https://www.notion.so../Digital%20inovation/Carrefour_Data_Engineer_2021/M9_arquitetura_sistemas_avan%C3%A7ados/Screenshot%20from%202021-11-08%2012-02-47.png](https://www.notion.so../Digital%20inovation/Carrefour_Data_Engineer_2021/M9_arquitetura_sistemas_avan%C3%A7ados/Screenshot%20from%202021-11-08%2012-02-47.png)

Screenshot from 2021-11-08 12-02-47

### Docker

Agora vamos criar um container do nosso projeto, precisamos de um dockerfile.yaml

```yaml
FROM ubuntuRUN apt-get update && apt-get install python3-pip -y && apt-get install python-dev -yWORKDIR /Trab_asaCOPY app.py models.py utils.py requirements.txt atividades.db /Trab_asa/WORKDIR /Trab_asaRUN pip install -r requirements.txtRUN pip install flaskCMD ["python3" ,"app.py"]
```

```
# Na pasta (Diretorio) que tem o dockerfile [É preciso ter um Docker file]
sudo docker build -t flask-lite-10 .#(não esquece o ponto)

# verificando se ele criou a imagem mesmo
docker images | grep flask-lite10

# Executando o docker pra saber se está tudo certo
# Coisas acontecendo da porta 5000 do container serão rebatidas na 5000 do seu pc
# Use a prosta 5000 para acessar seu container
docker run -p 5000:5000 flask-lite-10

# Voce pode visualizar seus containers em operação usado:
docker ps -a

# pegue no nome do container que voce quer parar na ultima coluna
# Parando O container
docker stop peacefull_driscoll
```

Podemos utilizar um navegador para verificar se o Container Docker está funcionando:

![https://www.notion.soImagens%20do%20relatorio/Screenshot%20from%202021-11-08%2020-44-47.png](https://www.notion.soImagens%20do%20relatorio/Screenshot%20from%202021-11-08%2020-44-47.png)

Subindo seu container para o Docker Hub. Para a orquestração de containers com o kubernets é recomendável que sua imagem Docker (Container) esteja no Docker hub:

```python
#TAGEANDO um container#vai la no docker e cria um repositorio, agora:#docker tag flask-fina1(nome_do_container) #fabioromerojunior99(meu_user)/farom99(quando_eu_fui_la_criar_o_repositorio:falsk_final1(#nome_que_eu_quero_la_no_repositorio)docker tag flask-fina1 fabioromerojunior99/farom99:flask_final1# colocando o docker no meu docker_hub# Dá um docker images# verifica se tem um com o repositorio(o seu) e a tag(que voce acabou de criar certo)# docker push#fabioromerojunior99(meu_user)/farom99(quando_eu_fui_la_criar_o_repositorio:falsk_final1(#nome_que_eu_quero_la_no_repositorio)docker push fabioromerojunior99/farom99:falsk_final1
```

você pode acessar esse link se quiser utilizar o container que foi criado:

```
https://hub.docker.com/repository/docker/fabioromerojunior99/flask-lite
docker push fabioromerojunior99/flask-lite:tagname
```

### K8s - Minikube

```
apiVersion: "apps/v1"
kind: "Deployment"
metadata:
  name: "flask"
  namespace: "default"
  labels:
    app: "flask"
spec:
  replicas: 1
  selector:
    matchLabels:
      app: "flask"
  template:
    metadata:
      labels:
        app: "flask"
    spec:
      containers:
      - name: "flask-final1"
        image: "fabioromerojunior99/flask-lite:flask-lite-10"

---
apiVersion: "v1"
kind: "Service"
metadata:
  name: "flask-service"
  namespace: "default"
  labels:
    app: "flask"
spec:
  ports:
  - protocol: "TCP"
    port: 80
    targetPort: 5000
  selector:
    app: "flask"
  type: "LoadBalancer"
  loadBalancerIP: ""
```

```
minikube start

# criando os containers, os que serão administrado pelo k8s
kubectl apply -f nome_da_coisa.yml

# visualizando seus pods. Voce definiu quantos seriam lá no deployments.yml
minikube dashboard

# Excluindo todos os pods (todos os pods m execução serão excluidos)
minikube delete

# Recriando seus pods
minikube start

# Faz o kubectl de novo para criar seus containers orquestrados
# Pode ser que não funcione de primeira, fantasmas da vida. as vezes dá certo...
# As vezes paciencia... Se estiver tudo bem os pods no minikube dashboard vão ficar verdes.
```

**Muito cuidado**, as vezes demora um pouco para o Kubernets deixar os pods verdes, vemos aqui um exemplo onde o tempo foi uma variável importante para o sucesso da execução.

**Uma orquestração que NÃO deu errado**

![https://www.notion.soImagens%20do%20relatorio/Screenshot%20from%202021-11-08%2022-29-12.png](https://www.notion.soImagens%20do%20relatorio/Screenshot%20from%202021-11-08%2022-29-12.png)

Screenshot from 2021-11-08 22-29-12

**Agora sim !! 3 minutos depois**

![https://www.notion.soImagens%20do%20relatorio/Screenshot%20from%202021-11-08%2022-33-16.png](https://www.notion.soImagens%20do%20relatorio/Screenshot%20from%202021-11-08%2022-33-16.png)

Screenshot from 2021-11-08 22-33-16

Por estarem todos verdes podemos dizer que estão funcionando mas para ter certeza é preciso acessa-lós podemos fazer isso pelo próprio minikube dashboard ou podemos utilizar o postman.

```
# Para pegar o link para acesso do pod no kubernets basta:
kubectl gel all

# Pegue o nome do serviço que está executando, nesse caso: flask-service
minikube service --url flask-service
```

![https://www.notion.so../Digital%20inovation/Carrefour_Data_Engineer_2021/M9_arquitetura_sistemas_avan%C3%A7ados/Screenshot%20from%202021-11-09%2010-00-00.png](https://www.notion.so../Digital%20inovation/Carrefour_Data_Engineer_2021/M9_arquitetura_sistemas_avan%C3%A7ados/Screenshot%20from%202021-11-09%2010-00-00.png)

Screenshot from 2021-11-09 10-00-00

# Parte 2

### Projeto:

Uma vez que as rotas das APIS já estão configuradas, podemos realizar as operações abaixo:

```
# Executa a aplicação:
flask run
```

Aqui temos todas as urls de acesso para cada função, temos também os json’s para ficar mais fácil de fazer os put’s e post’s.

Aqui, temos um projeto parecido com que vimos em aula, foi realizado somente as funções de get e post na api como o objetivo de treinar o uso do Docker e do Kubernets.

|  | Faz: | Endereço | função | json post() |
| --- | --- | --- | --- | --- |
| 1 | Retorna a mensagem de tudo bem | http://127.0.0.1:5000/ | retorna a mensagem |  |
| 2 | Retorna uma lista com todos os usuarios | http://127.0.0.1:5000/usuarios/ | Retorna usuários | {“nome”:“fabio3”,“email”:“fabio3@triste”, “senha_usuario”:“31234”,“senha_token”:“3192”} |
| 3 | Retorna uma lista com todos os aeroportos | http://127.0.0.1:5000/aeroportos | Retorna aertoportos | {“nome_aeroporto”: “Romeu Zema”, “cidade_aeroporto”: “Araxa” } |
| 4 | Retorna uma lista com todos os voos | http://127.0.0.1:5000/voos | retorna voos | {“nome_aeroporto_saida”: “romeu zema”,“nome_aeroporto_chegada”: “Uberlandiaairport”, “data_voo”: “agora”,“valor_voo”: “umreal”} |
| 5 | Retorna compras | http://127.0.0.1:5000/compras | Retorna compras | {“id_usuario”: “1”,“id_vooo”: “1”,“id_valor_voo”: “umreal”} |

### Docker

É preciso criar um container com essa aplicação:

```python
# Na pasta (Diretorio) que tem o dockerfile [É preciso ter um Docker file]sudo docker build -t flask-final-10 .# verificando se ele criou a imagem mesmodocker images | grep flask-final-10# Matar todos os dockers (dar stop em todos)docker kill $(docker ps -q)# NÃO USE, só se quiser# Remove todos os dockers# docker $(docker ps -a -q)# Executando o docker pra saber se está tudo certo# Coisas acontecendo da porta 5000 do container serão rebatidas na 5000 do seu pc# Use a prosta 5000 para acessar seu containerdocker run -p 5000:5000 flask-final1# Voce pode visualizar seus containers em operação usado:docker ps -a# pegue no nome do container que voce quer parar na ultima coluna# Parando O containerdocker stop peacefull_driscoll
```

Agora, com a ajuda de um navegador vamos ver o docker aceitando as requisições , vamos observar se o container está funcionando:

![https://www.notion.soImagens%20do%20relatorio/Screenshot%20from%202021-11-08%2010-17-30.png](https://www.notion.soImagens%20do%20relatorio/Screenshot%20from%202021-11-08%2010-17-30.png)

Screenshot from 2021-11-08 10-17-30

Subindo seu container para o Docker Hub. Para a orquestração de containers com o kubernets é recomendável que sua imagem Docker (Container) esteja no Docker hub:

```python
#TAGEANDO um container#vai la no docker e cria um repositorio, agora:#docker tag flask-fina1(nome_do_container) #fabioromerojunior99(meu_user)/farom99(quando_eu_fui_la_criar_o_repositorio:falsk_final1(#nome_que_eu_quero_la_no_repositorio)docker tag flask-fina1 fabioromerojunior99/farom99:flask_final1# colocando o docker no meu docker_hub# docker push#fabioromerojunior99(meu_user)/farom99(quando_eu_fui_la_criar_o_repositorio:falsk_final1(#nome_que_eu_quero_la_no_repositorio)fabioromerojunior99/farom99:falsk_final1
```

você pode acessar esse link se quiser utilizar o container que foi criado:

```
https://hub.docker.com/repository/docker/fabioromerojunior99/farom99
docker push fabioromerojunior99/farom99:tagname
```

### K8s - Minikube

```python
minikube start# criando os containers# kubectl apply -f nome_da_coisa.yml# visualizando seus pods. Voce definiu quantos seriam lá no deployments.ymlminikube dashboard# Excluindo todos os pods (todos os pods m execução serão excluidos)minikube delete# Recriando seus podsminikube start# Faz o kubectl de novo para criar seus containers orquestrados# Pode ser que não funcione de primeira, fantasmas da vida. as vezes dá certo...# As vezes paciencia... Se estiver tudo bem os pods no minikube dashboard vão ficar verdes.
```

Agora podemos observar os pods:

![https://www.notion.soImagens%20do%20relatorio/Screenshot%20from%202021-11-08%2023-06-10.png](https://www.notion.soImagens%20do%20relatorio/Screenshot%20from%202021-11-08%2023-06-10.png)

Screenshot from 2021-11-08 23-06-10

Por estarem todos verdes podemos dizer que estão funcionando mas para ter certeza é preciso acessa-lós podemos fazer isso pelo próprio minikube dashboard ou podemos utilizar o postman.

```
# Para pegar o link para acesso do pod no kubernets basta:
kubectl gel all

# Pegue o nome do serviço que está executando, nesse caso: flask-service
minikube service --url flask-service
```

![https://www.notion.so../Digital%20inovation/Carrefour_Data_Engineer_2021/M9_arquitetura_sistemas_avan%C3%A7ados/Screenshot%20from%202021-11-09%2009-39-21.png](https://www.notion.so../Digital%20inovation/Carrefour_Data_Engineer_2021/M9_arquitetura_sistemas_avan%C3%A7ados/Screenshot%20from%202021-11-09%2009-39-21.png)

Screenshot from 2021-11-09 09-39-21
