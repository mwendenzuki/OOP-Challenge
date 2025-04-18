
# main.py
from pet import Pet

def main():
    my_pet = Pet("Amari")

    print("\nInitial Status:")
    my_pet.get_status()

    print("\nAmari eats:")
    my_pet.eat()

    print("\nAmari sleeps:")
    my_pet.sleep()

    print("\nAmari plays:")
    my_pet.play()

    print("\nTraining Amari:")
    my_pet.train("roll over")
    my_pet.train("sit")

    print("\nAmari's Tricks:")
    my_pet.show_tricks()

    print("\nFinal Status:")
    my_pet.get_status()

if __name__ == "__main__":
    main()
