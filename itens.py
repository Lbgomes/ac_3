from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('sqlite:///rpg.db')

class ItemNaoExisteException(Exception):
    pass

def consultar_item(id_item):
    with engine.connect() as con: 
        sql= "SELECT * FROM Item WHERE id = :item"
        rs = con.execute(sql, [id_item])
        item = rs.fetchone()
        if item== None:
            raise ItemNaoExisteException
        return {'id':item[0], 'nome':item[1], 'tipo':item[2], 'fisico':item[3], 'magia':item[4], 'agilidade':item[4], 'emUso':[5]}


       