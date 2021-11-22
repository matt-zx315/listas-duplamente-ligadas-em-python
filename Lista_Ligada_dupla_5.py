# Adicionando e ordenando uma lista ligada dupla
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
            elif aux == self.tail:
                list_info += f'{aux.data} -> '
            else:
                list_info += f'{aux.data} <-> '
            aux = aux.nxt
        
        print(list_info)
    
    
    def set_head(self, _head):
        self.head = _head
    
    
    def sorted_insert(self, _data):
        new = Node(_data)
        
        # Lista vazia
        if self.head == None:
            self.head = new
            self.tail = new
        
        # Lista com um nó apenas
        elif self.head.nxt == None:
            if self.head.data <= _data:
                self.head.nxt = new
                new.prev = self.head
                self.tail = new
            else:
                new.nxt = self.head
                self.head.prev = new
                self.tail = self.head
                self.head = new
        
        # Lista com dois ou mais nós
        else:
            if _data < self.head.data:
                self.head.prev = new
                new.nxt = self.head
                self.head = new
            elif _data > self.tail.data:
                self.tail.nxt = new
                new.prev = self.tail
                self.tail = new
            else:
                aux = self.head
                
                while _data > aux.data:
                    aux = aux.nxt
                
                new.nxt = aux
                new.prev = aux.prev
                aux.prev.nxt = new
                aux.prev.nxt = new
    
    
    def sort_list(self):
        new = Linked_List()
        aux = self.head
        
        while aux:
            new.sorted_insert(aux.data)
            aux = aux.nxt
        
        return new


list1 = Linked_List()
list1.append(65)
list1.append(71)
list1.append(26)
list1.append(84)
list1.append(12)
list1.append(90)
list1.append(36)
list1.print_list()

list1 = list1.sort_list()
list1.print_list()
