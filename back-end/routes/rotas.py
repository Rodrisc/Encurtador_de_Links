from flask import redirect, request
from routes import app, conex, cursor
from db import busca_url, salvar

@app.route('/<redirecionar_url>')
#Se receber um paramentro e o mesmo estiver no BD, vai fazer o redirecionamento para url encontrada.
def redirecionar_url(redirecionar_url):

    try:
        retorno_da_url = busca_url(redirecionar_url, cursor)
        return redirect(retorno_da_url[0], code=301)
    except: return 'URL não encontrada'
    
@app.route('/savelink', methods=['POST'] )
def guardar():
    
    dict = request.get_json()
    url = dict['link']
    
    if not url:
        return {'link': 'Você precisa adicionar uma URL'}

    if url.startswith('http'):
        save = salvar(url, cursor, conex)
        
    else:
        save = salvar(f'http://{url}', cursor, conex)

    return {'link': f'http://127.0.0.1:5000/{save}'}