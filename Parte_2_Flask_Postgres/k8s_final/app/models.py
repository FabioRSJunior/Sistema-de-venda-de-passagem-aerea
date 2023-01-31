from sqlalchemy import Column, Integer, String, MetaData
#from database import Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):

    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    email = Column(String(120))
    senha_usuario = Column(String(50))
    senha_token = Column(String(50))

    def __init__(self, nome=None, email=None, senha_usuario=None, senha_token = None):
        self.nome = nome
        self.email = email
        senha_usuario = senha_usuario
        senha_token = senha_token


    def __repr__(self):
        return '<Usuario:{}, Email:{} , senha_token;{} >'.format(self.nome,self.email, self.senha_token)


class Aeroporto(Base):
    __tablename__ = 'aeroporto'
    id_aeroporto = Column(Integer, primary_key=True)
    nome_aeroporto = Column(String(50))
    cidade_aeroporto = Column(String(120))

    def __init__(self, nome_aeroporto=None, cidade_aeroporto=None):
        self.nome_aeroporto = nome_aeroporto
        self.cidade_aeroporto = cidade_aeroporto

    def __repr__(self):
        return '< Id_Aeroporto{}, nome_Aeroporto{}, cidade_aeroporto: {}  >'.format(self.id_aeroporto,
                                                                                    self.nome_aeroporto, 
                                                                                    self.cidade_aeroporto)

class Voos(Base):
    __tablename__ = 'voos'
    id_voo = Column(Integer, primary_key=True)
    nome_aeroporto_saida =   Column(String(50))
    nome_aeroporto_chegada = Column(String(50))
    data_voo  =              Column(String(50))
    valor_voo =              Column(String(50))


    def __init__(self, nome_aeroporto_saida=None, nome_aeroporto_chegada = None, data_voo = None, valor_voo = None ):
        self.nome_aeroporto_chegada = nome_aeroporto_chegada
        self.nome_aeroporto_saida = nome_aeroporto_saida
        self.data_voo = data_voo
        self.valor_voo = valor_voo

    def __repr__(self):
        return '< Id_voo :{}, Aeroporto_saida : {}, Aeroporto_chegada : {}, data_voo: {}, valor_voo: {} >'.format(self.id_voo,
                                                                                                            self.nome_aeroporto_saida, 
                                                                                                            self.nome_aeroporto_chegada,
                                                                                                            self.data_voo,
                                                                                                            self.valor_voo)

class Compras(Base):
    __tablename__ = 'compras'
    id_compra       = Column(Integer, primary_key=True)
    id_usuario   = Column(String(50))
    id_vooo       = Column(String(50))
    id_valor_voo = Column(String(50))


    def __init__(self, id_usuario = None, id_vooo = None, id_valor_voo = None ):      
        self.id_usuario   = id_usuario   
        self.id_vooo      = id_vooo       
        self.id_valor_voo = id_valor_voo 

    def __repr__(self):
        return '< Id_compra :{}, id_usuario : {}, id_vooo : {}, id_valos_voo: {}>'.format(self.id_compra, 
                                                                                          self.id_usuario,
                                                                                          self.id_vooo,
                                                                                          self.id_valor_voo)
