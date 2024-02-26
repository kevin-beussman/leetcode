from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # check = True
        # while check:
        #     out = [accounts[0]]
        #     check = False
        #     for person in accounts[1:]:
        #         name = person[0]
        #         if not any([name in peep for peep in out]):
        #             out.append(person)
        #         else:
        #             for peep in out:
        #                 emails_match = [email in peep[1:] for email in person[1:]]
        #                 if peep[0] == name and any(emails_match):
        #                     peep += person[1:]
        #                     check  = True
        #                     break
        #             else:
        #                 out.append(person)
        #     accounts = out[:]
            
        # for person in out:
        #     emails = list(set(person[1:]))
        #     emails.sort()
        #     person[1:] = emails
        # return out
        
        parent={} # parent links each email to the identifying (root) email
        group=defaultdict(list)
        result=[]
        emailToName={}
        
        def findRoot(x):
            if x==parent[x]:
                return x
            parent[x]=findRoot(parent[x])
            return parent[x]
        
        def union(x,y):
            r1=findRoot(x)
            r2=findRoot(y)
            if r1!=r2:
                parent[r2]=r1
                
        for account in accounts:
            emailToName[account[1]]=account[0]
            for email in account[1:]:
                parent[email]=email           
                
        for account in accounts:
            email1=account[1]
            for email2 in account[2:]:
                union(email1,email2)
        
        for email in parent:
            group[findRoot(email)].append(email)
        
        for key in group:
            result.append([emailToName[key]]+sorted(group[key]))
    
        return result
                        
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# accounts = [["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]
# accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
test = Solution()
print(test.accountsMerge(accounts))