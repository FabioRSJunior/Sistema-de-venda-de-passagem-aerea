from sqlalchemy.sql.expression import false
from sqlalchemy.sql.functions import user
from utils import insere_aeroporto
from flask.wrappers import Response
from models import Usuario, Aeroporto, Voos, Compras
from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth

app = Flask(__name__)
api = Api(app)

# Home page

class Homerpage(Resource):
    def get(self):
        response = ("Bem vindo ao air Uber essa aplicação talvez seja de responsabilidade do Fabio Romero")
        return response    

api.add_resource(Homerpage,'/')


auth = HTTPBasicAuth() # Responsavel pela Autenticação
@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuario.query.filter_by(email_usuario=login, senha_usuario=senha).first()


def verifica_token(token):
    if  Usuario.query.filter_by(token_usuario=token).first() == None:
        print ("token invalido")
        return False
    else:
        print("token autenticado!")
        return True    


# so um usuario logado pode consultar usuarios 
class Usuarioo(Resource):
    @auth.login_required
    def get(self):
        usuario = Usuario.query.all()
        response = [{'id_usuario': i.id_usuario,   
            'nome_usuario': i.nome_usuario, 
            'email_usuario': i.email_usuario, 
            'senha_usuario': i.senha_usuario, 
            'token_usuario': i.token_usuario,} for i in usuario]
        return response    

    def put(self):
        dados = request.json
        userio = Usuario(nome_usuario =dados['nome_usuario'], email_usuario =dados['email_usuario'],senha_usuario =dados['senha_usuario'],token_usuario=dados['token_usuario'] )
        userio.save()

        response = {
            'id_usuario'   : userio.id_usuario,
            'nome_usuario' : userio.nome_usuario,
            'email_usuario': userio.email_usuario,
            'senha_usuario': userio.senha_usuario,
            'token_usuario': userio.token_usuario }
        return response


class Vooos(Resource):

    def get(self):
        voo = Voos.query.all()
        response = [{'id_voo':i.id_voo, 'Aeroporto saida': i.aeroporto_saida, 
                                        'Aeroporto chegada':i.aeroporto_chegada,
                                        'data':i.data_voo, 
                                        'Valor':i.valor_voo }  for i in voo]
        return response

    def put(self):
        dados = request.json
        voo = Voos(aeroporto_saida=dados['Aeroporto saida'],aeroporto_chegada=dados['Aeroporto chegada'],
        data_voo = dados['Data'], valor_voo=dados['Valor'])
        voo.save()

        response = {
            'id_aeroporto'      :voo.id_voo,    
            'Aeroporto saida'   :voo.aeroporto_saida,
            'Aeroporto chegada' :voo.aeroporto_chegada,
            'data'              :voo.data_voo,
            'valor voo'         :voo.valor_voo
        }
        return response

class Aeroportos(Resource):
    def get(self):
        aeroporto = Aeroporto.query.all()
        response = [{'id':i.id_aeroporto, 'nome': i.nome_aeroporto, 'Cidade':i.cidade_aeroporto}  for i in aeroporto]
        return response

    def put(self):
        dados = request.json
        aeroporto = Aeroporto(nome_aeroporto=dados['nome'],cidade_aeroporto=dados['Cidade'] )
        aeroporto.save() 

        response = {
            'id_aeroporto'     :aeroporto.id_aeroporto,    
            'nome_aeroporto'   :aeroporto.nome_aeroporto,  
            'cidade_aeroporto' :aeroporto.cidade_aeroporto
        }
        return response

    # Utilize de um id de aeroporto para modificar um aeroporto 
    def post(self):

        dados = request.json
        aeroporto = Aeroporto.query.filter_by(id_aeroporto=dados['id']).first()
        aeroporto.id_aeroporto = dados['id']
        aeroporto.nome_aeroporto = dados['nome'] 
        aeroporto.cidade_aeroporto = dados['Cidade']
        mensagem = 'Aeroporto {} Modificado com sucesso'.format(aeroporto.nome_aeroporto)
        aeroporto.save()

        return mensagem 

    def delete(self):
        dados = request.json
        aeroporto = Aeroporto.query.filter_by(id_aeroporto=dados['id']).first()
        mensagem = 'Aeroporto {} excluido com sucesso'.format(aeroporto.nome_aeroporto)
        aeroporto.delete()
        return {'status':'sucesso', 'mensagem':mensagem}    


# retorna uma lista de aeroportos que contem o aeroporto de origem e o aeroporto de destino 
class Get_voo(Resource):
    def get(self,id_aeroporto):
        voos = Voos.query.filter_by(aeroporto_saida=id_aeroporto)
        response = [{'id_voo':i.id_voo, 'Aeroporto saida': i.aeroporto_saida, 
                                        'Aeroporto chegada':i.aeroporto_chegada }  for i in voos]
        return response

class Get_voo_data(Resource):
    def get(self,data):
        voo = Voos.query.filter_by(data_voo=data)
        response = [{   'id_voo':i.id_voo, 
                        'Aeroporto saida': i.aeroporto_saida, 
                        'Aeroporto chegada':i.aeroporto_chegada,
                        'data':i.data_voo, 
                        'Valor':i.valor_voo }  for i in voo]
        
        return response

#Retorna a lista de voos organizado por preço, menor -> maior
class Get_voo_preco(Resource):
    def get(self):
        voo = Voos.query.all()
        response = [{'id_voo':i.id_voo, 'Aeroporto saida': i.aeroporto_saida, 
                                        'Aeroporto chegada':i.aeroporto_chegada,
                                        'data':i.data_voo, 
                                        'Valor':i.valor_voo }  for i in voo]        
        response.sort(key=lambda x: x['Valor'])
        return response

class Compra_voo(Resource):
    
    def get(self,token): #lista todas as compras
        compras = Compras.query.all()

        response = [{'id_compras': i.id_compras,   
                     'id_usuario': i.id_usuario, 
                     'id_voo': i.id_voo, 
                     'id_valor': i.id_valor } for i in compras]

        return response


    def put(self,token):

        dados = request.json

        user = Usuario.query.filter_by(id_usuario = dados['id_usuario']).first()
        voo  = Voos.query.filter_by(id_voo=dados['id_voo']).first()

        compras = Compras(id_usuario = user.id_usuario, id_voo = voo.id_voo, id_valor = voo.valor_voo )
        
        veri = verifica_token(token)

        if veri == True:
                            
            compras.save()
            response = [{ 'compras_id':    compras.id_compras,
                        'id_usuario':    compras.id_usuario,
                        'id_voo':       compras.id_voo,
                        'valor_voo':    compras.id_valor  }]
            
            return response
        else:
            return "token invalido"                   
    

class Exitt(Resource):
        def get(self):
            return ("Logout, volte sempre!!", 401 )

api.add_resource(Aeroportos,'/Aeroportos/')

api.add_resource(Vooos,'/vooos/')
api.add_resource(Get_voo,'/vooos/todos/<int:id_aeroporto>')
api.add_resource(Get_voo_data,'/vooos/data/<int:data>')
api.add_resource(Get_voo_preco,'/vooos/preco')


api.add_resource(Usuarioo,'/usuarios/')


# só pode ser feita em login 
api.add_resource(Compra_voo,'/usuarios/compar/<int:token>')
api.add_resource(Exitt,'/logout')


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="0.0.0.0")
