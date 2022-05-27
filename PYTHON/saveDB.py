import random
#import psycopg2 as sql
import sqlite3


# iniciando a conexão com a table
try:
    conex = sqlite3.connect('teste.sqlite', check_same_thread=False)
    #conex = sql.connect(host='localhost', database='python', user='postgres', password='8850')
    cursor = conex.cursor()
except sqlite3.OperationalError: 
    print('Não foi possivel conectar ao banco de dados, verifique se o mesmo está ativo')
  
sql_comando = ('create table if not exists urls(codigourl integer primary key, urloriginal text not null, urlcurta text not null)')
cursor.execute(sql_comando)
conex.commit()

  
def busca_url(url=None):

    # Irá retornar todas as urls e hash criados

    if url == None:
        cursor.execute(f"select urloriginal, urlcurta from urls")
        lista = cursor.fetchall()
        print(type(lista))
        return lista
    
    # Irá fazer a busca usando o HASH e retornar a URL, caso encontrada

    else:
        cursor.execute(f"select urloriginal from urls where urlcurta = '{url}'")
        lista = cursor.fetchall()
        print(lista)
        return lista
    
    


def Salvar(url):

    verificador = verificar_urls_salvas(url)
    
    if len(verificador) == 1:
        
        return verificador[0][0]

    else:
        
        caracter_list = 'abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ'
        chars = random.choices(caracter_list, k=int(8))
        new_url = ''.join(chars)


        sql_comando = (f"insert into urls(urloriginal, urlcurta) values('{url}', '{new_url}')")
        cursor.execute(sql_comando)
        conex.commit()

        return new_url

def verificar_urls_salvas(url):
    sql_comando = (f"select urlcurta from urls where urloriginal='{url}'")
    cursor.execute(sql_comando)
    lista = cursor.fetchall()
    return lista