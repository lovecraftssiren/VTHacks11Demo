### Print
#print("Hello World")

### Input
#input("What's your favorite color? : ")
#print(input("What's your favorite color? : "))

def verify_color(color:str) -> bool: #input string, output true or false
    list_of_all_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    if color not in list_of_all_colors:
        print("Hmm, that's not a color.")
        return False
    return True

if __name__ == "__main__":
    print("---- Main ----")
    color = input("What's your favorite color? : ")

    color = color.lower()

    if (verify_color(color) == True):
        print("Your favorite color is " + color.lower() + ".")
        if color == "blue":
            print("Mine too!")
        elif color == "green":
            print("Oh, I really don't like green. Blue is better.")
        else:
            print("Oh, that's cool. I like blue.")