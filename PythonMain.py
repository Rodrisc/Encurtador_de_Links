import json
from flask import Flask, request
from flask_cors import CORS
import time

app = Flask(__name__)
app.debug = True
CORS(app)


@app.route('/redirect',methods=['GET'])
def requisitar():
    #time.sleep(1)
    with open('arquivo.json', 'r') as myfile:
        data=myfile.read()

    obj = json.loads(data)
    print(obj)
    return obj
    
@app.route('/savelink', methods=['POST'] )
def guardar():
    
    with open('arquivo.json', 'w') as myfile:
        json.dump(request.get_json(), myfile, indent=4)

    # print(request.get_json())

    return "deucerto"

if __name__ == '__main__':
    app.run()