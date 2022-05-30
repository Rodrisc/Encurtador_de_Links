import random
#import psycopg2 as sql
import sqlite3
# iniciando a conexão com com o banco
try:
    conex = sqlite3.connect('teste.sqlite', check_same_thread=False)
    #conex = sql.connect(host='localhost', database='python', user='postgres', password='8850')
    cursor = conex.cursor()
except sqlite3.OperationalError: 
    print('Não foi possivel conectar ao banco de dados, verifique se o mesmo está ativo')
  
sql_comando = ('create table if not exists urls(codigourl integer primary key, urloriginal text not null, urlcurta text not null)')
cursor.execute(sql_comando)
conex.commit()

def busca_url(url):

    cursor.execute(f"select urloriginal from urls where urlcurta = '{url}'")
    lista = cursor.fetchone()
    print(lista)
    return lista
    
def salvar(url):
    
    verificar_hash = verificar_urls_salvas(url)
    
    if verificar_hash:
        print(verificar_hash)
        return verificar_hash[0]
        
    caracter_list = 'abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ'
    chars = random.choices(caracter_list, k=int(8))
    hash = ''.join(chars)
    sql_comando = (f"insert into urls(urloriginal, urlcurta) values('{url}', '{hash}')")
    cursor.execute(sql_comando)
    conex.commit()
    return hash

def verificar_urls_salvas(url):

    sql_comando = (f"select urlcurta from urls where urloriginal='{url}'")
    cursor.execute(sql_comando)
    return cursor.fetchone()