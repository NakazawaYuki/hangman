def hangman(word):
    wrong = 0
    stages = [
        "",
        "__________          ",
        "|         |         ",
        "|         |         ",
        "|         0         ",
        "|        /|\        ",
        "|        / \        ",
        "|                   "
    ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}.".format(word))

import random
import csv
word_list = []
with open("hangman.txt", "r") as f:
    word_list = f.read()
    word_list = word_list.split(",")
num = random.randint(0, len(word_list)-1)
hangman(word_list[num])
new_word = input("よろしければ単語を教えてください。(dで単語を全削除)\n")
if new_word == "d":
    word_list = []
    print("遊んでくれてありがとう！")
elif len(new_word) == 1 or 2:
    print("遊んでくれてありがとう！")
elif new_word not in word_list:
    word_list.append(new_word)
    print("遊んでくれてありがとう！")
else:
    print("遊んでくれてありがとう！")
with open("hangman.txt", "w") as f:
    for word in word_list:
        f.write(word)
        if word_list.index(word)+1 == len(word_list):
            break
        f.write(",")