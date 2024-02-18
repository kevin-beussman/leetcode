class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        curnode = self.root
        for letter in word:
            if letter in curnode.children:
                curnode = curnode.children[letter]
            else:
                curnode.children[letter] = TrieNode(letter)
                curnode = curnode.children[letter]

        curnode.is_end = True

    def search(self, word: str) -> bool:
        curnode = self.root
        for letter in word:
            if letter in curnode.children:
                curnode = curnode.children[letter]
            else:
                return False
        return curnode.is_end

    def startsWith(self, prefix: str) -> bool:
        curnode = self.root
        for letter in prefix:
            if letter in curnode.children:
                curnode = curnode.children[letter]
            else:
                return False
        return True
    
    def removeandtrim(self, word: str) -> None:
        curnode = self.root

        stack = [self.root]
        for letter in word:
            if letter in curnode.children:
                curnode = curnode.children[letter]
                stack.append(curnode)
            else:
                break
        else:
            can_delete = True
            stack[-1].is_end = False
            while stack:
                curnode = stack.pop()
                if curnode.children or curnode.is_end or curnode.char == "": # this node is not a leaf
                    can_delete = False

                if can_delete:
                    stack[-1].children.pop(curnode.char)
                else:
                    break

        # # def delete(n,w):
        # #     if n.char == w: # stop, remove tag, prune if no children
        # #         n.is_end = False
            
        # #     if not n.children and not n.is_end:



        # #     if w[0] in n.children:
        # #         delete(n.children[w[0]],w[1:])
        # #     pass
        
        # delete(self.root,word)

def main():
    test = Trie()
    test.insert("apple")
    test.insert("app")
    print(test.search("apple"))
    test.removeandtrim("apple")
    print(test.search("apple"))
    print(test.search("app"))
    print(test.startsWith("app"))

if __name__ == "__main__":
    main()