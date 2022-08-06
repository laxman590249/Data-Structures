

string = 'zzzzddaaaabcccxxaa'


def find_next_char(string, i,count):
    if string[i]==string[i+1]:
        return count+1
    else :
        return 0

def main(string):
    char_count={}
    for i in range(0,len(string)) :
        count=1
        next_char = 1
        for j in range (i,len(string)-1):
            val=find_next_char(string, i,count)
            if val==0:
                next_char = j
                break
            else :
                count=val
                continue
        char_count[string[i]] = count
        i = i + next_char
    print(char_count)


main(string)