ch = input("Enter a character: ").lower()

match ch:
    case "a" | "e" | "i" | "o" | "u":
        print("Vowel")

    case _ if ch.isalpha():
        print("Consonant")

    case _ if ch.isdigit():
        print("Digit")

    case _:
        print("Special Character")