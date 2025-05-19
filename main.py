from main_utils import addition

def main():
    print("Bienvenue !")
    a = int(input("Entrez un nombre : "))
    b = int(input("Entrez un autre nombre : "))

    print("Résultat :", addition(a, b))

    if __name__ == '__main__':
        main()