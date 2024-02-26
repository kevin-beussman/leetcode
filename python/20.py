#%% Attempt 1
# class Solution:
#     def isValid(self, s: str) -> bool:
#         char_dict = {"(":")","[":"]","{":"}","}":"?",")":"?","]":"?"}
#         while s:
#             ind = s.find(char_dict[s[0]])
#             if ind == -1:
#                 return False
#             ind2 = s[1:ind].find(s[0])
#             if ind2 != -1:
#                 if self.isValid(s[ind2+1:ind+1]):
#                     s = s[0:ind2+1] + s[ind+1:]
#                 else:
#                     return False
#             elif self.isValid(s[1:ind]):
#                 s = s[ind+1:]
#             else:
#                 return False
#         return True

# test = Solution()
# print(test.isValid("[({(())}[()])]"))

#%% Attempt 2
class Solution:
    def isValid(self, s: str) -> bool:
        char_dict = {"(":")","[":"]","{":"}","}":"?",")":"?","]":"?"}
        while s:
            ind1 = s[::-1].find(char_dict[s[0]])
            if ind1 == -1:
                ind = -1
            else:
                ind  = len(s) - 1 - ind1
            while ind != -1 and ind <= len(s):
                if self.isValid(s[1:ind]):
                    s = s[ind+1:]
                    break
                else:
                    ind2 = s[ind-1::-1].find(char_dict[s[0]])
                    if ind2 == -1:
                        ind = -1
                    else:
                        ind = ind - 1 - ind2
            else:
                return False
        return True

test = Solution()
# print(test.isValid("[({(())}[()])]"))
print(test.isValid("[(])"))
# print(test.isValid("(){}}{"))

#%%
# s = "[({(())}[()])]"
s = "{}}{"
char_dict = {"(":")","[":"]","{":"}","}":"?",")":"?","]":"?"}
ind = len(s) - 1 - s[::-1].find(char_dict[s[0]])
ind2 = ind - 1 - s[ind-1::-1].find(char_dict[s[0]])
