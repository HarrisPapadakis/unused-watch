Konoha_Ninjas = []

# Define dictionaries for each ninja and append them to the list as tuples with their names
Konoha_Ninjas.append(("Naruto", {  # Adds Naruto to the list with a dictionary of his abilities
    "Normal Attack": "Rasengan",  # Naruto's normal attack
    "Advanced Mode": "Sage Mode",  # Naruto's advanced mode
    "Ultimate Attack": "Baryon Mode"  # Naruto's ultimate attack
}))

Konoha_Ninjas.append(("Sasuke", {  # Adds Sasuke to the list with a dictionary of his abilities
    "Normal Attack": "Rinnegan",  # Sasuke's normal attack
    "Advanced Mode": "Mangekyō Sharingan",  # Sasuke's advanced mode
    "Ultimate Attack": "Amaterasu"  # Sasuke's ultimate attack
}))

Konoha_Ninjas.append(("Sakura", {  # Adds Sakura to the list with a dictionary of her abilities
    "Normal Attack": "Superhuman strength",  # Sakura's normal attack
    "Advanced Mode": "Creation Rebirth",  # Sakura's advanced mode
    "Ultimate Attack": "Chakra scalpel"  # Sakura's ultimate attack
}))

Konoha_Ninjas.append(("Hinata", {  # Adds Hinata to the list with a dictionary of her abilities
    "Normal Attack": "Byakugan",  # Hinata's normal attack
    "Advanced Mode": "Eight-Trigrams Sixty-Four Palms",  # Hinata's advanced mode
    "Ultimate Attack": "Usurper"  # Hinata's ultimate attack
}))

Konoha_Ninjas.append(("Neji", {  # Adds Neji to the list with a dictionary of his abilities
    "Normal Attack": "Byakugan",  # Neji's normal attack
    "Advanced Mode": "Taijutsu",  # Neji's advanced mode
    "Ultimate Attack": "Eight Trigrams Palms"  # Neji's ultimate attack
}))

# Print details of each ninja in the list
for name, ninja in Konoha_Ninjas:  # Iterate over the list of tuples containing names and dictionaries
    print(f"Ninja Name: {name}")  # Display the ninja's name
    print(f"Normal Attack: {ninja['Normal Attack']}")  # Display the normal attack
    print(f"Advanced Mode: {ninja['Advanced Mode']}")  # Display the advanced mode
    print(f"Ultimate Attack: {ninja['Ultimate Attack']}")  # Display the ultimate attack
    print("-" * 40)  # Print a separator for better readability
