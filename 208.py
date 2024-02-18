# class Trie:

#     def __init__(self):
#         pass

#     def insert(self, word: str) -> None:
        

#     def search(self, word: str) -> bool:
        

#     def startsWith(self, prefix: str) -> bool:
        

n = 19

steps = []
new = n
while new not in steps:
    steps.append(new)
    new = sum([int(k)**2 for k in str(new)])
if new == 1:
    print('True')
else:
    print('False')