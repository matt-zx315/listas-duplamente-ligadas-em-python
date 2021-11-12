# Copiando uma lista com 1 ponteiro aleatório
import random

class Node:
    def __init__(self, _data):
        self.data = _data
        self.nxt = None
        self.rand = None


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
    
    
    def set_random(self):
        aux = self.head
        data = []
        
        while aux:
            data.append(aux)
            aux = aux.nxt
        
        aux = self.head
        
        while aux:
            aux.rand = random.choice(data)
            del data[data.index(aux.rand)]
            aux = aux.nxt
    
    
    def append(self, _data):
        new_node = Node(_data)
        
        if self.head == None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.nxt = new_node
            self.tail = new_node
    
    
    def set_head(self, _head):
        self.head = _head
    
    
    def copy_list(self):
        list_copy = Linked_List()
        aux = self.head
        original = self.head
        
        while aux:
            new = Node(aux.data)
            new.nxt = aux.nxt
            aux.nxt = new
            
            print(f'{aux.data} -> {aux.nxt.data}')
            
            aux = aux.nxt.nxt
            
            if new.nxt:
                print(f'{new.data} -> {new.nxt.data}')
            else:
                print(f'{new.data} -> {new.nxt}\n')
        
        while original:
            print(f'{original.data} ? {original.rand.data}')
            original.nxt.rand = original.rand.nxt
            
            if original.nxt:
                print(f'{original.nxt.rand.data} ? {original.rand.nxt.data}')
            else
                print(f'{original.nxt.rand.data} ? {original.rand.nxt.data}')
            
            original = original.nxt.nxt
        
        print()
        original = self.head
        dupe = original.nxt
        
        while original.nxt:
            temp = original.nxt
            original.nxt = original.nxt.nxt
            original = temp
        
        list_copy.set_head(dupe)
        return list_copy
    
    
    def print_random_list(self):
        aux = self.head
        list_info = ""
        
        while aux:
            if aux.nxt is not None:
                info = f'Nó:{aux}\nValor {aux.data}\nPróximo valor:{aux.nxt.data}\nNó aleatório: {aux.rand.data}'
            else:
                info = f'Nó:{aux}\nValor {aux.data}\nPróximo valor:{None}\nNó aleatório: {aux.rand.data}'
            
            print(info)
            list_info += f'{aux.data} -> '
            aux = aux.nxt
        
        print()
        print(list_info, '\n')


list1 = Linked_List()
list1.append(65)
list1.append(71)
list1.append(26)
list1.append(84)
list1.append(12)
list1.append(90)
list1.append(36)

list1.set_random()
list1.print_random_list()

list2 = list1.copy_list()
list1.print_random_list()
list2.print_random_list()
