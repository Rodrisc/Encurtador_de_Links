from flask import Flask, request
from flask_cors import CORS
from database import *
from werkzeug.utils import redirect

app = Flask(__name__)
app.debug = True
CORS(app)

#Vai para página principal onde se pede a url para encurtar
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

if __name__ == '__main__':
    conex, cursor = conetar_banco()
    app.run()