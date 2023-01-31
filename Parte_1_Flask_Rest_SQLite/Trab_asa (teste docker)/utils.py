from models import Usuario, Aeroporto, Voos, Compras


def insere_voo(aeroporto_saida,aeroporto_chegada,data_voo,valor_voo):
    voos = Voos(aeroporto_saida = aeroporto_saida , aeroporto_chegada = aeroporto_chegada ,data_voo = data_voo, valor_voo = valor_voo)
    voos.save()
    print(voos)

# --------------------------------------------------------------------------------------------- Aeroportos ---
# insere dados na tabela aeroporto
def insere_aeroporto(nome_aeroporto ,cidade_aeroporto):
    aeroporto = Aeroporto(nome_aeroporto = nome_aeroporto, cidade_aeroporto = cidade_aeroporto)
    print(aeroporto)
    aeroporto.save()

def retorna_aeroporto():
    aeroporto = Aeroporto.query.all()
    print(aeroporto)
    return aeroporto

def deleta_aeroporto():
    aeroporto = Aeroporto.query.all()
    print(aeroporto)
    return aeroporto

# deleta um aeroporto, se receber o id do aeroporto
def deleta_aeroporto(nome):
    aeroporto = Aeroporto.query.filter_by(id_aeroporto=nome).first()
    aeroporto.delete()

def deleta_todos_aeroporto():
    #aeroporto = Aeroporto.query.all()
    #aeroporto.delete() 
    print("melhor não!") 

def cadastra_usuario(nome_usuario,email_usuario,senha_usuario,token_usuario):
    useer = Usuario(nome_usuario = nome_usuario , email_usuario = email_usuario ,senha_usuario = senha_usuario, token_usuario = token_usuario)
    useer.save()
    print(useer)



if __name__ == '__main__':
    insere_aeroporto('Santos','Sao Paulo')
    insere_aeroporto('Zema','Araxa')
    retorna_aeroporto()
    insere_voo(1,2,29,20) 
    cadastra_usuario("fabio","fabioufu","1111","1212")
    cadastra_usuario("fabia","fabiaufu","2222","1313")
