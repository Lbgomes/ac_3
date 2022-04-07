from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('sqlite:///rpg.db')

# Essa classe só representa uma exception com
#novo nome. Não mexa dentro dela.
# Escreva os imports (acima dela)
# E suas funcoes (depois dela)
class HeroiNaoExisteException(Exception):
    pass

#escreva suas funcoes aqui

# Ex1
# O arquivo herois deve conter uma função heroi_existe
# Ela recebe uma id de herói e consulta no banco para ver
# se o herói em questão existe. Ela retorna True
# se ele existe, False caso contrário

def heroi_existe(id_h):
   with engine.connect() as con: 
                                
       statement = text ("""SELECT * FROM Heroi WHERE id = :heroi""")
       rs = con.execute(statement, heroi=id_h)
       heroi = rs.fetchone()
       if heroi == None:                  
           return False
       return True


def consultar_heroi(id_heroi):
    with engine.connect() as con: 
        sql= "SELECT * FROM Heroi WHERE id = :heroi"
        rs = con.execute(sql, [id_heroi])
        heroi= rs.fetchone()
        if heroi== None:
            raise HeroiNaoExisteException
        return {'id':heroi[0], 'nome':heroi[1], 'fisico':heroi[2], 'magia':heroi[3], 'agilidade':heroi[4]}

def consultar_heroi_por_nome(nome_heroi):
    with engine.connect() as con: 
        sql= "SELECT * FROM Heroi WHERE nome = :heroi"
        rs = con.execute(sql, [nome_heroi])
        heroi= rs.fetchone()
        if heroi== None:
            raise HeroiNaoExisteException
        return {'id':heroi[0], 'nome':heroi[1], 'fisico':heroi[2], 'magia':heroi[3], 'agilidade':heroi[4]}

