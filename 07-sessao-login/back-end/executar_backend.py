from geral.config import *
from rotas.login import *

@app.route("/")
def inicio():
    return 'backend operante, operação de editar'

app.run(debug=True)