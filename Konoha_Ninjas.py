Konoha_Ninjas = []

for ninja in range(5):
    Naruto = {
        "Normal Attack" : "Rasengan", 
        "Advanced Mode" : "Sage Mode", 
        "Ultimate Attack" :"Baryon Mode"
        }
    Konoha_Ninjas.append(Naruto())

    Sasuke = {
        "Normal Attack" : "Rinnegan", 
        "Advanced Mode" : "Mangekyō Sharingan", 
        "Ultimate Attack" :"Amaterasu"
        }
    Konoha_Ninjas.append(Sasuke())

    Sakura = {
        "Normal Attack" : "Superhuman strength", 
        "Advanced Mode" : "Creation Rebirth", 
        "Ultimate Attack" :"Chakra scalpel"
        }
    Konoha_Ninjas.append(Sakura())

    Hinata = {
        "Normal Attack" : "Byakugan", 
        "Advanced Mode" : "Eight-Trigrams Sixty-Four Palms", 
        "Ultimate Attack" :"Usurper"
        }
    Konoha_Ninjas.append(Hinata())

    Neji = {
        "Normal Attack" : "Byakugan", 
        "Advanced Mode" : "Taijutsu", 
        "Ultimate Attack" :"Eight Trigrams Palms"
        }
    Konoha_Ninjas.append(Neji)

for ninja in Konoha_Ninjas[:5]:
    print(ninja())
  
