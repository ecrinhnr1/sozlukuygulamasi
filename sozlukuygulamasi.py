meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "SHEESH": "onaylamamak",
            "ROFL": "bir şakaya karşılık cevap",
            "AGGRO": "agresifleşmek"
            }

for i in range(0, 5):
    word = input("Lütfen öğrenmek istediğiniz kelimenin ismini giriniz: ")

    if word in meme_dict.keys():
        print("İstediğiniz kelimenin anlamı: ", meme_dict[word])
    else:
        print("İstediğiniz kelime sözlükte yok.")
