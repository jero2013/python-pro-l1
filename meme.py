meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "Una forma de reir o reaccionar a algo gracioso",
            "RANDOM": "algo aleatorio ",
            "AURA" : "Una vibra o puntos de fama",
            "CREEPY" : "algo aterrador, siniestro"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print (word,": ",meme_dict[word])
    # ¿Qué debemos hacer si se encuentra la palabra?
else:
    print ("palabra no encontrada")
    # ¿Qué hacer si no se encuentra la palabra?
