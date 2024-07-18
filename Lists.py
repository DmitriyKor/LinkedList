class Node:
    def __init__(self, data):
      self.data = data
      self.next = None

    def __str__(self):
        return str(self.data)

class LLIterator:
    def __init__(self, head):
        self.node=head

    def __next__(self):
        res = self.node
        if not (res is None):
            self.node = self.node.next
            return res
        else:
            raise StopIteration


class LinkedList:
    def __init__(self):
        self.last = None
        self.head = None
        self.length = 0

    def add_node(self, data):
        self.length+=1
        if self.last is None:
            self.last = Node(data)
            self.head = self.last
        else:
            self.last.next = Node(data)
            self.last = self.last.next

    def __iter__(self):
        return LLIterator(self.head)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return [self[i] for i in range(*key.indices(len(self)))]
        elif isinstance(key, int):
            cur_ind=0
            for n in self:
                if cur_ind==key:
                    return n
                else:
                    cur_ind+=1
        else:
            return NotImplemented

    def __len__(self):
        return self.length

    def __str__(self):
        res=''
        for n in self:
            res+=str(n)
            if not (n.next is None): res+='->'
        return res

ll=LinkedList()
ll.add_node('node A')
ll.add_node('node B')
ll.add_node('node C')
print(ll)

for node in ll:
    print(node)

node_list=ll[0:3]
print (node_list)




