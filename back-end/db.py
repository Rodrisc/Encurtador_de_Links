import random
import sqlite3
# iniciando a conexão com o banco
def conetar_banco():
    try:
        conex = sqlite3.connect('teste.sqlite', check_same_thread=False)
        cursor = conex.cursor()
    except sqlite3.OperationalError: 
        print('Não foi possivel conectar ao banco de dados, verifique se o mesmo está ativo')
    
    sql_comando = ('create table if not exists urls(codigourl integer primary key, urloriginal text not null, urlcurta text not null)')
    cursor.execute(sql_comando)
    conex.commit()

    return conex, cursor
# 
def busca_url(url, cursor):

    cursor.execute(f"select urloriginal from urls where urlcurta = '{url}'") 
    return cursor.fetchone()
    
def salvar(url, cursor, conex):
    
    verificar_hash = verificar_urls_salvas(url, cursor)
    
    if verificar_hash:
        return verificar_hash[0]
        
    caracter_list = 'abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ'
    chars = random.choices(caracter_list, k=int(8))
    hash = ''.join(chars)
    sql_comando = (f"insert into urls(urloriginal, urlcurta) values('{url}', '{hash}')")
    cursor.execute(sql_comando)
    conex.commit()
    return hash

def verificar_urls_salvas(url, cursor):

    sql_comando = (f"select urlcurta from urls where urloriginal='{url}'")
    cursor.execute(sql_comando)
    return cursor.fetchone()