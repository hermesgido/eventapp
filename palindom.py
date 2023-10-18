def isPalindom(word:str):
    reversed_word = ''
    new_word = ''
    position  = len(word)
    word_len = len(word)
    while word_len != 0:
        for i in range(word_len):
            print(word[i])
            print(i, position)
            if i == position:
                print("Yes itsb in the position")
                new_word= new_word + word[i]
                word = word.replace(word[i], '')
            position = position - 1
        # break-

    print("WWWWWWWWWWWWWWWWWWW")
    print(new_word)
    print("WWWWWWWWWWWWWWWWWWW")
    print(word)
    print("Above is replaced.........")

isPalindom(word="makez")