from flask import Flask, jsonify, request

app = Flask(__name__)

playlist = [
    {    
        "id":1,
        "titulo": "Rumo a Goiania",
        "artista": "Leonardo"
    },
    {
        "id":2,
        "titulo": "e o amor",
        "artista": "Zeze di Camargo e Luciano"
    }
]

@app.route('/musicas', methods=['GET'])
def get_musicas():
    return jsonify({"playlist":playlist, "total": len(playlist)})

@app.route('/musicas/<int:id>', methods=['GET'])
def get_musica_id(id):
    for musica in playlist:
        if musica["id"] == id:
            return jsonify(musica)

    return "Música não encontrada"

@app.route('/musicas', methods=['POST'])
def add_musica():
    nova_musica = request.json

    nova_musica['id'] = len(playlist) + 1

    playlist.append(nova_musica)
    return jsonify({"mensagem": "Musica adicionada","musica": "MALANDRAMENTE"}), 201

if __name__ == '__main__':
    app.run(debug=True)