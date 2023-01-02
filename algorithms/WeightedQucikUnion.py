# List containing parent of i

class WeightedQuickUnion:

    def __init__(self,N):
        self.id = [i for i in range(N)]
        self.sz = [1 for i in range(N)]


    def root(self, p):
        while p!=self.id[p]:
            p = self.id[p]
        return p


    def connected(self,p,q):
        return self.root(p)==self.root(q)


    def union(self,p,q):
        proot = self.root(p)
        qroot = self.root(q)

        if proot == qroot:
            return

        if self.sz[proot] < self.sz[qroot]:
            self.id[proot] = qroot
            self.sz[qroot]+=self.sz[proot]
            
        else:
            self.id[qroot] = proot
            self.sz[proot]+=self.sz[qroot]



obj = WeightedQuickUnion(10)
obj.union(4,6)
obj.union(3,8)
obj.union(5,6)
obj.union(7,2)
obj.union(1,9)
obj.union(0,1)

print(obj.connected(1,8))
print(obj.id)
