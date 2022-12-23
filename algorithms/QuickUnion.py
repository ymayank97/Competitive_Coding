# List containing parent of i

class QuickUnion:

    def __init__(self,N):
        self.id = [i for i in range(N)]


    def root(self, p):
        while p!=self.id[p]:
            p = self.id[p]
        return p


    def connected(self,p,q):
        return self.root(p)==self.root(q)


    def union(self,p,q):
        proot = self.root(p)
        qroot = self.root(q)

        self.id[proot] = qroot
