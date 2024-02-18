from typing import List
from functools import lru_cache

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
                if curnode.children or curnode.is_end or curnode.char == "":
                    can_delete = False

                if can_delete:
                    stack[-1].children.pop(curnode.char)
                else:
                    break

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # ## solution 1: works, but slow
        # m = len(board)
        # n = len(board[0])

        # def helper(i,j,s,wordlist,visited): # return true if letter
        #     if i > m-1 or i < 0:
        #         return []
        #     if j > n-1 or j < 0:
        #         return []
        #     if (i,j) in visited:
        #         return []
            
        #     s += board[i][j]
        #     ans = set()
        #     keep = set()
        #     for word in wordlist:
        #         if word == s:
        #             ans.add(word)
        #         elif word[0:len(s)] == s:
        #             keep.add(word)
            
        #     if keep:
        #         visited2 = visited[:]
        #         visited2.append((i,j))
        #         ans.update(helper(i+1,j,s,keep,visited2))
        #         ans.update(helper(i-1,j,s,keep,visited2))
        #         ans.update(helper(i,j+1,s,keep,visited2))
        #         ans.update(helper(i,j-1,s,keep,visited2))
        #     return ans

        # out = []
        # for i in range(m):
        #     for j in range(n):
        #         here = helper(i,j,"",[w for w in words if w not in out],[])
        #         out += list(here)

        # return out

        m = len(board)
        n = len(board[0])

        wordtrie = Trie()
        for word in words:
            wordtrie.insert(word)
        
        stack = []
        for i in range(m):
            for j in range(n):
                stack.append((i,j,"",[]))
        # stack.append((0,0,"",[]))
        
        out = set()
        while stack:
            i,j,s,v = stack.pop()
            if i > m-1 or i < 0:
                continue
            if j > n-1 or j < 0:
                continue
            if (i,j) in v:
                continue

            if not wordtrie.root.children: # no words left to search for
                break
            
            s += board[i][j]
            v2 = v[:]
            v2.append((i,j))
            if wordtrie.search(s):
                out.add(s)
                wordtrie.removeandtrim(s)
            if wordtrie.startsWith(s):
                stack.append((i+1,j,s,v2))
                stack.append((i-1,j,s,v2))
                stack.append((i,j+1,s,v2))
                stack.append((i,j-1,s,v2))
            
        return list(out)



def main():
    # board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    # words = ["oath","pea","eat","rain"]
    # board = ["a","a"]
    # words = ["aaa"]
    # board = [["a","b","c"],["a","e","d"],["a","f","g"]]
    # words = ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade","eaabcdgf"]
    board = [["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"]]
    words = ["b","a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    test = Solution()
    print(test.findWords(board,words))

if __name__ == "__main__":
    main()

