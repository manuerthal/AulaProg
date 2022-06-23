from geral.config import *

@app.route("/login", methods=['get'])
def login():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    # receber as informações do novo objeto
    dados = request.get_json()  
    try:  
        if dados['nome'] == 'mylogin' and dados['senha'] == '123':
            resposta = jsonify({"resultado": "ok", 
                                "detalhes": "login com sucesso"})
        else:
            resposta = jsonify({"resultado": "erro", "detalhes": "---"})        
        
    except Exception as e:  # em caso de erro...
        # informar mensagem de erro
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta  # responder!