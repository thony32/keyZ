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
        print("Sites web enregistrés")
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
        print("Aucun site récent trouvé!")


def delete_password():

    cursor.execute("SELECT DISTINCT website FROM passwords")
    websites = cursor.fetchall()

    if len(websites) > 0:
        print("Sites web enregistrés")
        for idx, row in enumerate(websites, start=1):
            print(f"{idx}. {row[0]}")


        choice = int(input("Entrez le nombre correspondant au site web: "))

        if choice >= 1 and choice <= len(websites):
            website = websites[choice - 1][0]


            cursor.execute("SELECT * FROM passwords WHERE website=?", (website,))
            passwords = cursor.fetchall()

            if len(passwords) > 0:
                print("Mots de passe")
                for idx, row in enumerate(passwords, start=1):
                    print(f"{idx}. Nom d'utilisateur: {row[1]}, Mot de passe: {row[2]}")


                password_choice = int(input("Entrez le nombre correspondant au mot de passe: "))

                if password_choice >= 1 and password_choice <= len(passwords):
                    password = passwords[password_choice - 1]
                    cursor.execute("DELETE FROM passwords WHERE website=? AND username=? AND password=?",
                                   (password[0], password[1], password[2]))
                    conn.commit()
                    print("Mot de passe supprimé avec succès!")
                else:
                    print("Choix invalide!")
            else:
                print("Aucun mot de passe enregistré sur le site selectionné!")
        else:
            print("Choix invalide!")
    else:
        print("Aucun site récent trouvé!")


def edit_password():

    cursor.execute("SELECT DISTINCT website FROM passwords")
    websites = cursor.fetchall()

    if len(websites) > 0:
        print("Sites web enregistrés")
        for idx, row in enumerate(websites, start=1):
            print(f"{idx}. {row[0]}")


        choice = int(input("Entrez le nombre correspondant au site web: "))

        if choice >= 1 and choice <= len(websites):
            website = websites[choice - 1][0]


            cursor.execute("SELECT * FROM passwords WHERE website=?", (website,))
            passwords = cursor.fetchall()

            if len(passwords) > 0:
                print("Mots de passe")
                for idx, row in enumerate(passwords, start=1):
                    print(f"{idx}. Username: {row[1]}, Password: {row[2]}")


                password_choice = int(input("Entrez le nombre correspondant au mot de passe: "))

                if password_choice >= 1 and password_choice <= len(passwords):
                    password = passwords[password_choice - 1]

                    new_username = input("Nouveau nom d'utilisateur: ")
                    new_password = input("Nouveau mot de passe: ")

                    cursor.execute(
                        "UPDATE passwords SET username=?, password=? WHERE website=? AND username=? AND password=?",
                        (new_username, new_password, password[0], password[1], password[2]))
                    conn.commit()
                    print("Mot de passe modifié avec succès!")
                else:
                    print("Choix invalide!")
            else:
                print("Aucun mot de passe enregistré dans ce site web.")
        else:
            print("Choix invalide!")
    else:
        print("Aucun site web enregistré.")


while True:
    print("\nGestionnaire de mot de passe")
    print("1. Ajouter un mot de passe")
    print("2. Afficher les mots de passes enregistrés")
    print("3. Modifier un mot de passe enregistré")
    print("4. Supprimer un mot de passe enregistré")
    print("5. Quitter")

    choice = input("Entrez votre choix (1-5): ")

    options = {
        "1": add_password,
        "2": get_passwords,
        "3": edit_password,
        "4": delete_password,
        "5": exit
    }

    action = options.get(choice)
    if action:
        action()
    else:
        print("Choix invalide!")


conn.close()
