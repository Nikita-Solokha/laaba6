text = ""
print("Введите текст: ", end="")
while True:
    chan = input()
    if chan == "":
        break
    text += chan
words = []
chan_word = ""
i = 0
while i < len(text):
    chan = text[i]
    if chan != " ":
        chan_word += chan
    else:
        if chan_word != "":
            words.append(chan_word)
            chan_word = ""
    i += 1
if chan_word != "":
    words.append(chan_word)
shifted_words = []
i = 0
while i < len(words):
    word = words[i]
    shifted_word = ""
    j = 0
    while j < len(word):
        shifted_word += word[(j + 1) % len(word)]
        j += 1
    shifted_words.append(shifted_word)
    i += 1
shifted_text = ""
i = 0
while i < len(shifted_words):
    shifted_text += shifted_words[i] + " "
    i += 1
print("Исходный текст:", text)
print("Измененный текст:", shifted_text.rstrip())