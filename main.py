import os

def main():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    text_file = os.path.join(THIS_FOLDER, 'text.txt')

    file = open("text.txt", "w")
    file.write("Your text goes here")
    file.close()
    file = open("text.txt", "r")

    print(file.read())

    while True:
        try:
            estimate_price = int(input("Choose between add, read,  : "))
            return estimate_price
        except ValueError:
            print("You have to enter an estimate price")


if __name__ == '__main__':
    main()
