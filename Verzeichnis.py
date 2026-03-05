import os

def directory_create(path):
    try:
        os.makedirs(path)
        print(f"Verzeichnis {path} erstellt")
    except:
        print(f"Verzeichnis {path} existiert bereits!")

if __name__ == "__main__":
    first_name = input("Bitte Vornamen eingeben: ")
    last_name = input("Bitte Nachnamen eingeben: ")
    name = (first_name[:2] + last_name[:2]).lower()
    path = os.path.normcase("project/user")
    new_path = os.path.join(os.getcwd(), path, name)
    directory_create(new_path)
    print(name)
    print(new_path)

input()
