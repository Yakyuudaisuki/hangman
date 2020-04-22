def hangman(word):
    wrong = 0
    stages = ["",
             "_________        1",
             "|        |       2",
             "|        |       3",
             "|        O       4",
             "|       ~|~      5",
             "|       ~ ~      6",
             "|     (lose...)  7"
             ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンにようこそ！")

    while wrong < len(stages)-1:
        print("\n")
        msg = "1文字予想してね"
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
            print("You are winner!!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You are Looser! '{}' is correct".format(word))

import random
words = ["cat", "Horse", "Rabit"]
i = random.randint(0,2)
hangman(words[i])
