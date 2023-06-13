import sqlite3

conn = sqlite3.connect('passwords.db')


cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS passwords
                  (website TEXT, username TEXT, password TEXT)''')



def add_password():
    website = input("Site Web: ")
    username = input("Nom d'utilisateur: ")
    password = input("Mot de passe: ")


    cursor.execute("INSERT INTO passwords VALUES (?, ?, ?)", (website, username, password))
    conn.commit()
    print("Mot de Passe ajouté avec succès!")



def get_passwords():

    cursor.execute("SELECT DISTINCT website FROM passwords")
    websites = cursor.fetchall()

    if len(websites) > 0:
        print("Sites web récents:")
        for idx, row in enumerate(websites, start=1):
            print(f"{idx}. {row[0]}")


        choice = int(input("Entrez le nombre correspondant au site web: "))

        if choice >= 1 and choice <= len(websites):
            website = websites[choice - 1][0]


            cursor.execute("SELECT * FROM passwords WHERE website=?", (website,))
            passwords = cursor.fetchall()

            if len(passwords) > 0:
                print("Mots de passe")
                for row in passwords:
                    print("Nom d'utilisateur:", row[1])
                    print("Mot de passe:", row[2])
            else:
                print("Aucun mot de passe enregistré dans ce site web!")
        else:
            print("Choix invalide!")
    else:
        print("Pas de sites récents trouvés!")



while True:
    print("\nGestionnaire de mot de passe")
    print("1. Ajouter un mot de passe")
    print("2. Afficher les mots de passes enregistrés")
    print("3. Quitter")

    choice = input("Entrez votre choix (1-3): ")

    options = {
        "1": add_password,
        "2": get_passwords,
        "3": exit
    }

    action = options.get(choice)
    if action:
        action()
    else:
        print("Choix invalide!")


conn.close()
