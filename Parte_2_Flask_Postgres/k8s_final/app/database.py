from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, update, func, null, insert
from models import Aeroporto, Compras, Usuario, Base, Voos
from sqlalchemy import Column, Integer, String, MetaData
from settings import DATABASE_URL

print(DATABASE_URL)

# Pro burrinho do fabio fazer a parte dele 
# engine = create_engine('postgresql+psycopg2://postgres:12345@localhost:5432/ufu_asa', convert_unicode=True)

# quando docker deixa esse 
engine = create_engine('postgresql+psycopg2://postgres:12345@postgres:5432/ufu_asa', convert_unicode=True)

#engine = create_engine('postgres://mudasir:12345@postgres:5432/ufu_asa')
#postgres://mudasir:12345@postgres:5432/demo_db

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
                                         
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()    
    import models
    Base.metadata.create_all(bind=engine)
    

    '''
def add_usuario():
    Session = sessionmaker(engine)
    session = Session()     

    query = (
            insert(Usuario).
            values(
                nome = 'Joao',
                email = 'joao@teste.com',
                senha_usuario = '123456',
                senha_token = "192"
                )
    )
    conn = engine.connect()
    result = conn.execute(query)

    session.commit()
'''



## ADD USUARIOS

def add_usuario_json(usuario_json):
    Session = sessionmaker(engine)
    session = Session()     

    query = (
            insert(Usuario).
            values(
                nome =          usuario_json["nome"],
                email =         usuario_json["email"],
                senha_usuario = usuario_json["senha_usuario"],
                senha_token =   usuario_json["senha_token"]
                )
    )
    conn = engine.connect()
    try:
        result = conn.execute(query)
        session.commit()
        ret = {"status": "Usuario foi adicionado"}
    

    except Exception as e:
        print(e)
        ret = {"status": str(e)}
    return ret



def get_all_users():

    lista = []
    lista.clear()

    Session = sessionmaker(engine)
    session = Session()     
    
    s = select(Usuario).where(Usuario.id != 999)
    conn = engine.connect()
    res = conn.execute(s)

    for row in res:
        tudim = ( "Nome:"+row['nome']+ " Email: " + row['email'])
        lista.append(tudim)
        print(tudim)

    return lista    

# fim dos usuarios 

# ---     AEROPORTOS
 
def add_aeroporto_json(json_aeroporto):
    Session = sessionmaker(engine)
    session = Session()     

    query = (
            insert(Aeroporto).
            values(
                nome_aeroporto = json_aeroporto['nome_aeroporto'],
                cidade_aeroporto = json_aeroporto['cidade_aeroporto'],
                )
    )
    conn = engine.connect()
    try:
        result = conn.execute(query)
        session.commit()
        ret = {"status": "User has been added"}
    

    except Exception as e:
        print(e)
        ret = {"status": str(e)}
    return ret


def get_all_aeroportos():

    lista = []
    lista.clear()

    Session = sessionmaker(engine)
    session = Session()     
    
    s = select(Aeroporto).where(Aeroporto.id_aeroporto != 999)
    conn = engine.connect()
    res = conn.execute(s)

    for row in res:
        tudim = ( str(row['id_aeroporto']), "Nome_aeroporto:" +row['nome_aeroporto']+ " Ciidade_aeroporto: " + row['cidade_aeroporto'])
        lista.append(tudim)
        print(tudim)

    return lista    

# fim aeroporto 

## ----- voos 

def get_all_voos():

    lista = []
    lista.clear()

    Session = sessionmaker(engine)
    session = Session()     
    
    s = select(Voos).where(Voos.id_voo != 999)
    conn = engine.connect()
    res = conn.execute(s)

    for row in res:

        tudim = ( str(row['id_voo']) + " Air_saida: " + row['nome_aeroporto_saida'] + " Air_chegada: " + row['nome_aeroporto_chegada'] )
        lista.append(tudim)
        print(tudim)

    return lista    


def add_voos_json(json_voos):
    Session = sessionmaker(engine)
    session = Session()     

    query = (
            insert(Voos).
            values(
                nome_aeroporto_saida =   json_voos["nome_aeroporto_saida"],
                nome_aeroporto_chegada = json_voos["nome_aeroporto_chegada"],
                data_voo =               json_voos["data_voo"],
                valor_voo =              json_voos["valor_voo"]
                )
    )
    conn = engine.connect()
    try:
        result = conn.execute(query)
        session.commit()
        ret = {"status": "VOOS foram adicionados"}
    

    except Exception as e:
        print(e)
        ret = {"status": str(e)}
    return ret

## fim do voo 

## ---------------- Compras

def get_all_compras():

    lista = []
    lista.clear()

    Session = sessionmaker(engine)
    session = Session()     
    
    s = select(Compras).where(Compras.id_compra != 999)
    conn = engine.connect()
    res = conn.execute(s)

    for row in res:

        tudim = ( str(row['id_compra']) + " id_usuario: " + row['id_usuario'] + " preco: " + row['id_valor_voo'] )
        lista.append(tudim)
        print(tudim)

    return lista    


def add_compras_json(json_compras):
    Session = sessionmaker(engine)
    session = Session()     

    query = (
            insert(Compras).
            values(
                id_usuario =   json_compras["id_usuario"],
                id_vooo =       json_compras["id_vooo"],
                id_valor_voo = json_compras["id_valor_voo"]
                )
    )
    conn = engine.connect()
    try:
        result = conn.execute(query)
        session.commit()
        ret = {"status": "Compras foram adicionados"}
    

    except Exception as e:
        print(e)
        ret = {"status": str(e)}
    return ret

# fim das compras 

# -- USUARIOS  


'''     
##ORIGINAL N MEXE 
def get_all_users():
    Session = sessionmaker(engine)
    session = Session()     
    
    s = select(Usuario).where(Usuario.id == 1)
    conn = engine.connect()
    res = conn.execute(s)
    for row in res:
        print(row['nome'])
'''
