

def word_list(word, list_w, output = []):

    if len(word) == 0:
        return output
    else:
        l_word = ""
        for letter in word:
            l_word += letter
            if l_word in list_w:
                output.append(l_word)
                return word_list(word[len(l_word):], list_w, output)
        else:
            return []

print(word_list('HeyJack', ['Hey', 'Jack']))


