meme_dict = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            "SHEESH": "leggera disapprovazione",
            "CREEPY": "spaventoso o inquietante",
            "PARA": "preoccuparsi per qualcosa, paranoiarsi"
            }
parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")

if parola in meme_dict.keys():
    print(meme_dict[parola])
else:
    print("non è stata trovata la seguente parola: ", parola)
