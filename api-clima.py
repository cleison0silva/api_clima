import requests
import json

def requisicao(cidade):
    try:
        req = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+ cidade + "&appid=06c921750b9a82d8f5d1294e1586276f&lang=pt_br")
        clima = json.loads(req.text)
        return clima
    except:
        print("Erro Na Conexão")
        return None

def printar(tempo):
    condicao = tempo["weather"][0]["description"]
    temperatura = tempo["main"]["temp"]- 273.15

    print("Tempo: ", condicao)
    print(f"Temperatura: {temperatura:.2f}")


while True:
    op = input("Escreva a cidade que deseja consultar ou SAIR para fechar: ")

    if op == "SAIR":
        print("Saindo...")
        break
    else:
        temp = requisicao(op)
        if temp["cod"] == "404":
            print("Cidade não Encontrada, tente novamente")
        else:
            printar(temp)