from functools import partial

def read_in_chunks(size_in_bytes):

    s = 'Lets say i have a text file of 1000 GB'
    with open('data.txt', 'r+b') as f:
        prev = ''
        count = 0
        f_read  = partial(f.read, size_in_bytes)
        for text in iter(f_read, ''):
            if not text.endswith('\n'):
                # if file contains a partial line at the end, then don't
                # use it when counting the substring count.
                text, rest = text.rsplit('\n', 1)
                # pre-pend the previous partial line if any.
                text =  prev + text
                prev = rest
            else:
                # if the text ends with a '\n' then simple pre-pend the
                # previous partial line.
                text =  prev + text
                prev = ''
            count += text.count(s)
        count += prev.count(s)
        print(count)