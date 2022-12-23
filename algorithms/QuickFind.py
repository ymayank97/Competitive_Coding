#  Quick Find Algorithm

#  3 operations : find, connected and union
# 1. Intialize the array data structure :- constructor
# 2. implement find method just comparing the value stored in an array
# 3. connected
# 4. union

class QuickUnion:
    
    def __init__(self,n):
       self.id = [i for i in range(n)]  #O(N) N array acesses

    def print_list(self):
        print(self.id)

    def connected(self,p,q):
        return self.id[p]==self.id[q]    # 2 array acesses
    
    def union(self,p,q):
        pid = self.id[p]
        qid = self.id[q]
        for i, ele in enumerate(self.id):  # n+2 array acesses
            if ele == pid:
                self.id[i] = qid


obj = QuickUnion(10)
obj.union(3,8)
obj.union(5,6)
obj.union(7,2)
obj.union(1,9)
obj.union(0,1)

print(obj.connected(1,8))
obj.print_list()
