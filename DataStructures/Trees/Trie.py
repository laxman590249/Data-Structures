class TrieNode:
    def __init__(self):
        self.end_of_word = 'N'
        self.nodes = {}

    def add_char(self, char):
        self.nodes[char] = None
        return self

    def is_present(self, char):
        node = self.nodes.get(char, None)
        if node:
            return True
        else:
            False


class Trie:

    def __init__(self):
        self.root = None

    def add_word(self, word):
        node = self.root
        for char in word.capitalize():
            if not self.root:
                self.root = TrieNode().add_char(char)
                node = TrieNode()
                self.root.nodes[char] = node
            else:
                if node.is_present(char):
                    node = node.nodes[char]
                else:
                    node.add_char(char)
                    new = TrieNode()
                    node.nodes[char] = new
                    node = new
        node.end_of_word = 'Y'

    def traverse(self):
        node = self.root
        queue = []
        if not node:
            print('Empty Trie')
        else:
            queue.append(node)
            while len(queue) > 0:
                node = queue[0]
                for key in node.nodes.keys():
                    print(key, end='')
                    queue.append(node.nodes[key])
                print('', end=' ')
                del queue[0]
            print()

    def search(self, word):
        node = self.root
        for char in word.capitalize():
            node = node.nodes.get(char, None)
            if not node:
                break
        else:
            if node.end_of_word == 'Y':
                print('Word is Present')
                return
        print('Word is not Present')

    def delete_word(self, word):
        word = word.capitalize()
        stack = []
        node = self.root
        for char in word:
            child = node.nodes.get(char, None)
            if child:
                stack.append(node)
                node = child
            else:
                break
        else:
            stack.append(child)
            count = len(stack)-1
            for i in range(len(stack)-1, -1, -1):
                node = stack.pop()
                if i == count:
                    if len(node.nodes) > 0:
                        node.end_of_word = 'N'
                        break
                    else:
                        del node
                else:
                    if len(node.nodes) > 1:
                        del node.nodes[word[i]]
                        break
                    else:
                        if node.end_of_word == 'Y':
                            del node.nodes[word[i]]
                            break
                        del node



t = Trie()
t.add_word('AIR')
t.add_word('AIO')
t.add_word('AIRK')
t.add_word('AIRM')
t.add_word('AIRMLMN')
t.add_word('Ball')
# t.traverse()
# t.delete_word('ball')
# t.delete_word('AIR')
# t.delete_word('AI')
t.search('AIRK')
t.traverse()









