import requests

url = "http://127.0.0.1:5000/musicas"

data = {
    "artista": "PIOPIO",
    "titulo": "malandramente"
}

response = requests.post(url,json=data)

print(response.text)
print(response.status_code)