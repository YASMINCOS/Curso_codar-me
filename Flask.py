from flask import Flask, jsonify
from evento import Evento
import json
#pip package installer for Python
app= Flask(__name__)


ev_online = self.cria_evento_online ("Live de Python")
ev2_online= self.cria_evento_online("Live de JavaScript")
ev_online.imprime_informacoes()
ev2_online.imprime_informacoes()

@app.route("/")
def index():
    return"<h1>Flask configurando com sucesso </h1>"

@app.route("/api/eventos/")
def listar_eventos():
    eventos_dict=[]
    for ev in eventos:
        eventos_dict.append({
            "id":ev.id,
            "nome":ev.nome,
            "local": ev.local
        })
    return jsonify(eventos_dict)