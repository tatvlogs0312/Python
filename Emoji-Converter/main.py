# example with emoji + dictionary

message = input(">")
words = message.split(" ")
emojis = {
    ":)": "đ",
    ":(": "âšī¸"
}

out = ""
for word in words:
    out += emojis.get(word, word) + " "

print(out)


def convert_emoji(message):
    words = message.split(" ")
    out = ""
    for word in words:
        out += emojis.get(word, word) + " "
    return out


result = convert_emoji(message)
print(result)