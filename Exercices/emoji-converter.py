# creating function for this program
def emoji_converter(message):
    words = msg.split(' ')
    emoji = {
        ":)": "😀",
        ":(": "😭"
    }
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output


msg = input("Enter> ")
print("Result: ", emoji_converter(msg))
