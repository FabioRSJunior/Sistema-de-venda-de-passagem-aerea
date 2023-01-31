# Criação da Base de dados

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

#mude o engine quando for colocar no doker 
#engine = create_engine('sqlite:///atividades.db', convert_unicode=True)

#primeiro projeto, não sei como faz pra criar o k8s disso 
engine = create_engine('sqlite:///atividades.db')

#engine = create_engine('postgresql+psycopg2://postgres:12345@localhost:5432/ufu_asa', convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False,bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

#cada classe é uma tabela 
class Usuario(Base):

    __tablename__='usuarios'
    id_usuario    = Column(Integer,    primary_key=True)      # Id_usurio para relacinar com as passagens 
    nome_usuario  = Column(String(40), index=True)         # Nome normal 
    email_usuario = Column(String(40))        # Unique pois será usado na autenticacao
    senha_usuario = Column(String(20))                     # Senha para login 
    token_usuario = Column(String(20))                     # Aqui vai ficar o IP                            

    def __repr__(self):
        return '<Usuario:{}, Email: {}>'.format(self.id_usuario,self.nome_usuario,self.email_usuario,self.token_usuario)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Aeroporto(Base):

        __tablename__='aeroporto'
        id_aeroporto      = Column(Integer, primary_key=True) # Id de aeroporto, para as passagens 
        nome_aeroporto    = Column(String(40),unique=True)    # nome do aeroporto, não queremos 2 aeroportos com mesmo nome 
        cidade_aeroporto  = Column(String(40))                # cidade onde está o aeroporto 

        def __repr__(self):

                return '<Aeroporto ID: {}, Nome aeroporto: {}, Cidade Aeroporto {}>'.format(self.id_aeroporto ,self.nome_aeroporto,self.cidade_aeroporto )

        def save(self):
                db_session.add(self)
                db_session.commit()

        def delete(self):
                db_session.delete(self)
                db_session.commit()


class Voos(Base):
        __tablename__= 'voos'
        id_voo                 = Column(Integer, primary_key=True)                       # Registro do voo
        aeroporto_saida        = Column(Integer, ForeignKey('aeroporto.id_aeroporto') )  # De qual aeroporto ele está partindo
        aeroporto_chegada      = Column(Integer, ForeignKey('aeroporto.id_aeroporto') )  # Para qual aeroporto ele está indo
        data_voo               = Column(Integer)                             # Pode rir, foi uma solucão rapida  
        valor_voo              = Column(Integer)                                         # Qual o valor da passagem  

        def __repr__(self):
                return '<Id voo: {}, Aeroporto_saida: {}, Aeroporto_chegada: {}, data_voo: {},valor_voo {}>'.format(self.id_voo,self.aeroporto_saida, self.aeroporto_chegada, self.data_voo ,self.valor_voo)

        def save(self):
                db_session.add(self)
                db_session.commit()

        def delete(self):
                db_session.delete(self)
                db_session.commit()


class Compras(Base):
__tablename__='compras'  
id_compras = Integer, primary_key=True)                      # ID para recuperar a conta
id_usuario = String(40), ForeignKey('usuarios.id_usuario') ) # O usuario que faz a compra 
id_voo     = String(40), ForeignKey('voos.id_voo'))          # Qual voo está sendo comprado 
id_valor   = String(40), ForeignKey('voos.valor_voo'))       # valor que saiu a passagem 

        def __repr__(self):
                return '<Compras: {} ; ID usuario: {} ; ID voo: {} ; Valor: {}>'.format(self.id_compras,
                self.id_usuario, self.id_voo, self.id_valor)

        def save(self):
                db_session.add(self)
                db_session.commit()

        def delete(self):
                db_session.delete(self)
                db_session.commit()


def init_db():        
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()        