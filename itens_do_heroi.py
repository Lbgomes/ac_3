from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('sqlite:///rpg.db')


class ItemNaoExisteException(Exception):
    pass


def heroi_tem_item(id_item):
    with engine.connect() as con: 
        sql = "SELECT * FROM ItemDoHeroi WHERE idHeroi = :item"
        rs = con.execute(sql, [id_item])
        item = rs.fetchone()
        if item != None:
            return True
        else:
            return False


def heroi_quantos_itens(id_heroi):
    with engine.connect() as con:
        query = text (""" 
                      SELECT * from Heroi h 
                      join ItemDoHeroi itdh on itdh.idHeroi = h.id
                      join Item it on it.id = itdh.idItem
                      WHERE h.id = :heroi""")
        resp = con.execute(query, heroi = id_heroi)
        itens_heroi = resp.fetchall()
        return len(itens_heroi)

def itens_do_heroi(id_heroi):
    with engine.connect() as con:
        query = text (""" 
                      SELECT * from Heroi h 
                      join ItemDoHeroi itdh on itdh.idHeroi = h.id
                      join Item it on it.id = itdh.idItem
                      WHERE h.id = :heroi""")
        resp = con.execute(query, heroi = id_heroi)
        itens_heroi = resp.fetchall()
        return itens_heroi
        