# Trocando nós simétricos de lugar
class Node:
    def __init__(self, _data):
        self.data = _data
        self.nxt = None
        self.prev = None


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def append(self, _data):
        new_node = Node(_data)
        
        if self.head == None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.nxt = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    
    def print_list(self):
        list_info = ""
        aux = self.head
        
        while aux:
            if aux == self.head:
                list_info += f'<- {aux.data} <-> '
                print(f'Nó: {aux}\nValor: {aux.data}\nNó anterior: {None}\nPróximo nó: {aux.nxt.data}\n')
            elif aux == self.tail:
                list_info += f'{aux.data} -> '
                print(f'Nó: {aux}\nValor: {aux.data}\nNó anterior: {aux.prev.data}\nPróximo nó: {None}\n')
            else:
                list_info += f'{aux.data} <-> '
                print(f'Nó: {aux}\nValor: {aux.data}\nNó anterior: {aux.prev.data}\nPróximo nó: {aux.nxt.data}\n')
            aux = aux.nxt
        
        print(list_info + '\n')
    
    
    def swap_symmetric(self, _pos):
        count = 0
        a = self.head
        b = self.tail
        
        while count != _pos:
            a = a.nxt
            b = b.prev
            count += 1
            
            if a == None:
                print("NOPE!\n")
                return
        
        if a.prev != None:
            a.prev.nxt = b
            
            if a.nxt != None:
                a.nxt.prev = b
        else:
            self.head = b
            self.tail = a
            a.nxt.prev = b
        
        if b.nxt != None:
            b.nxt.prev = a
        
        if b.prev != None:
            b.prev.nxt = a
            
            if b.nxt != None:
                b.nxt.prev = a
        else:
            self.head = a
            self.tail = b
            b.prev.nxt = a
        
        temp_nxt = a.nxt
        temp_prev = a.prev
        
        a.nxt = b.nxt
        a.prev = b.prev
        b.nxt = temp_nxt
        b.prev = temp_prev


list1 = Linked_List()
list1.append(65)
list1.append(71)
list1.append(26)
list1.append(84)
list1.append(12)
list1.append(90)
list1.append(36)
list1.print_list()

# list1.swap_symmetric(2)
# list1.print_list()

list1.swap_symmetric(3)
list1.print_list()

# list1.swap_symmetric(0)
# list1.print_list()

# list1.swap_symmetric(12)
# list1.print_list()

# list1.swap_symmetric(5)
# list1.print_list()
