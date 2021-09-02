import pyperclip

def main():
    while True:
        word = input("Enter word: \n")
        output = ""
        # output += str(ord(char) - 96) for char in word.lower()
        for char in word.lower():
            output += str(ord(char) - 96)
        pyperclip.copy(output)
        print(output)

if __name__ == "__main__":
    main()
