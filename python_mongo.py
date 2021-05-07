#Como fazer integração de python com o banco de dados mongo

#Necessário instalação do pymongo: python3 -m pip install pymongo

#Importação do pymongo
from pymongo import MongoClient

#O "localhost", 27017 é o que irá fazer a conexão com o mongoDB
client = MongoClient("localhost", 27017)

#Criação de uma coleção de músicas, esse código é um exemplo de programa de adicionar músicas
#e filtrar por artista.
db = client.Musicas

print("1.Adicionar, 2.Filtrar")

opcao = int(input("Escolha a opção: "))

if opcao == 1:
    nomeMusica = str(input("Digite o nome da música: "))
    nomeArtista = str(input("Digite o nome do artista: "))

    #O insert_many() é a função que irá inserir as músicas e os artistas
    #Os valores dos atributos são o as variaveis acima.
    db.teste.insert_many(
        [
            {
                "Nome" : nomeMusica,
                "Artista" : nomeArtista
            }
        ]
    )
    
elif opcao == 2:
    nomeArtista = str(input("Digite o nome do artista: "))
    #O laço for foi utilizado para filtrar todas as músicas do mesmo artista.
    for x in db.teste.find({"Artista" : nomeArtista}):
        print(x)

