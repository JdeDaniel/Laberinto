
from matriz import escojer_mapa


def menu():
    print("Menu")
    print("1. Resolver por BFS")
    print("2. Resolver por DFS")
    print("3. Cambiar laberinto")
    print("4. Salir")

    choice = input("Please select an option (1-3): ")

    if choice == '1':
        print("You selected Option 1.")
    elif choice == '2':
        print("You selected Option 2.")
    elif choice == '3':
        escojer_mapa()
    elif choice == '4':
        print("Exiting the menu. Goodbye!")
    else:
        print("Invalid choice, please try again.")


if __name__ == "__main__":
    while True:
        menu()
        if input("Do you want to return to the menu? (yes/no): ").lower() != 'yes':
            break