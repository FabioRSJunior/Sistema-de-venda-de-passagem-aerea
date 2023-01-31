#import database_utils
from flask import Blueprint, request, json, jsonify
from sqlalchemy import create_engine, select, update, func, null, insert
from sqlalchemy.orm.session import sessionmaker
import database

urls_blueprint = Blueprint('urls', __name__,)

@urls_blueprint.route('/')
def index():
    return 'Bem vindo ao Uber de Avião!! Essa aplicação NÃO é de resposabilidade de Fabio Romero'

@urls_blueprint.route('/create_tables', methods = ['GET'])
def create_database():
    try:
        database.init_db()
        ret = {"status": "Tables are created!!"}

    except Exception as e:
        print(e)
        ret = {"status": "Tables are not created!!"}    
    return ret    


## ---- Usuarios 

@urls_blueprint.route('/usuarios', methods = ['GET'])
def get_all_users():
    retorno = database.get_all_users()
    print(type(retorno))
    ret = ("Lista de todos os usuarios: "+str(retorno))
    return ret


@urls_blueprint.route('/usuarios', methods = ['POST'])
def add_usuarios():
    req_data = request.get_json()
    usuario_json = {"nome": req_data['nome'], "email": req_data['email'],
     "senha_usuario" : req_data["senha_usuario"], "senha_token":req_data["senha_token"] }
    #database.add_usuario() --> sem o JSON
    ret = database.add_usuario_json(usuario_json)
    print(usuario_json)
    ret = ("Usuario add"+ json.dumps(usuario_json))
    return ret

# fim dos usuarios


## ---- Aeroportos 

@urls_blueprint.route('/aeroportos', methods = ['POST'])
def add_aeroporto():
    req_data = request.get_json()
    aeroporto_json = {"nome_aeroporto": req_data['nome_aeroporto'], "cidade_aeroporto": req_data['cidade_aeroporto']}
    #database.add_usuario() --> sem o JSON
    ret = database.add_aeroporto_json(aeroporto_json)
    print(aeroporto_json)
    ret = ("Aeroporto add"+ json.dumps(aeroporto_json))
    return ret

@urls_blueprint.route('/aeroportos', methods = ['GET'])
def get_all_aeroportos():
    retorno = database.get_all_aeroportos()
    ret = ("Lista de todos os aeroportos: "+str(retorno))
    return ret


## ---- VOOS 

@urls_blueprint.route('/voos', methods = ['GET'])
def get_all_voos():
    retorno = database.get_all_voos()
    ret = ("Lista de todos os voos: "+str(retorno))
    return ret

@urls_blueprint.route('/voos', methods = ['POST'])
def add_voos():
    req_data = request.get_json()

    voos_json = {"nome_aeroporto_saida": req_data['nome_aeroporto_saida'],
                "nome_aeroporto_chegada": req_data['nome_aeroporto_chegada'], 
                 "data_voo": req_data['data_voo'],
                 "valor_voo": req_data['valor_voo']}

    #database.add_usuario() --> sem o JSON
    ret = database.add_voos_json(voos_json)
    print(voos_json)
    ret = ("Voo add"+ json.dumps(voos_json))
    return ret
 

## ---- COMPRAS
 
@urls_blueprint.route('/compras', methods = ['POST'])
def add_compras():
    req_data = request.get_json()

    compras_json = {"id_usuario":   req_data['id_usuario'], 
                    "id_vooo":       req_data['id_vooo'],
                    "id_valor_voo": req_data['id_valor_voo']}

    #database.add_usuario() --> sem o JSON
    ret = database.add_compras_json(compras_json)
    print(compras_json)
    ret = ("Compras add"+ json.dumps(compras_json))
    return ret

@urls_blueprint.route('/compras', methods = ['GET'])
def get_all_compras():
    retorno = database.get_all_compras()
    ret = ("Lista de todos os voos: "+str(retorno))
    return ret

#fim do compras 





#ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
#>>> session.add(ed_user)
        # Session = sessionmaker(self.db)
        # self.session = Session()     

            # query = (
            #         insert(Envios_Lembretes).
            #         values(
            #             id_lembrete = envio_lembrete.id_lembrete,
            #             id_usuario = envio_lembrete.id_usuario,
            #             lembrete = envio_lembrete.lembrete,
            #             data_para_envio = envio_lembrete.data_para_envio,
            #             data_enviado = None,
            #             meio_envio = envio_lembrete.meio_envio,
            #             criado_em = datetime.now()
            #             )
            # )
            # conn = self.db.connect()
            # result = conn.execute(query)

            # self.session.commit()
            # logging.debug("ATUALIZANDO ADCIONANDO UM NOVO ENVIOS_LEMBRETES")
    
