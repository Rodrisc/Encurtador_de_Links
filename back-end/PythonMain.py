import json
from traceback import print_tb
from flask import Flask, request
from flask_cors import CORS
from saveDB import *
from werkzeug.utils import redirect

app = Flask(__name__)
app.debug = True
CORS(app)

#Vai para página principal onde se pede a url para encurtar
@app.route('/<redirecionar_url>')
#Se receber um paramentro e o mesmo estiver no BD, vai fazer o redirecionamento para url encontrada.
def redirecionar_url(redirecionar_url):
    try:
        retorno_da_url = busca_url(redirecionar_url)
        return redirect(retorno_da_url[0][0], code=301)
    except: return 'URL não encontrada'

# @app.route('/requisitar',methods=['GET'])
# def requisitar():
    
#     listar = busca_url()
#     print(listar)
    # dict = {'link': f'{listar[0][1]}'}
#     return dict
    
@app.route('/savelink', methods=['POST'] )
def guardar():
    
    # with open('arquivo.json', 'w') as myfile:
    #     json.dump(request.get_json(), myfile, indent=4)

    # print(request.get_json())

    dict = request.get_json()
    url = dict['link']
    print(url)
    if not url:
        return {'link': 'Você precisa adicionar uma URL'}

    else:
        if url.startswith('http'):
            save = Salvar(url)

        else:
            save = Salvar(f'http://{url}')

    return {'link': f'http://127.0.0.1:5000/{save}'}

if __name__ == '__main__':
    app.run()