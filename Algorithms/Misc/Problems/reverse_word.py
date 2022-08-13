

words = "    This is the best  "

def reverse_words_1(line: str):
        return " ".join(reversed(line.strip().split()))


def reverse_words_2(line: str):
    return " ".join(line.strip().split()[::-1])


def reverse_words_3(line: str):
    rev_words = []
    word_end = len(line)
    for i in range(len(line)-1, -2, -1):
        if i == -1 or line[i] == ' ':
            word = line[i+1:word_end]
            if word != ' ' and word != '':
                rev_words.append(word)
            word_end = i

    print(rev_words)
    return ' '.join(rev_words)


print(reverse_words_3(words))
print(reverse_words_2(words))