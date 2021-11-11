# Criando e inserindo nós em uma lista ligada dupla
class Node:
    def __init__(self, _data):
        self.data = _data
        self.nxt = None
        self.prev = None


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
    
    
    def push(self, _data):
        new_node = Node(_data)
        
        if self.head == None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.nxt = self.head
            self.head.prev = new_node
            self.head = new_node
    
    
    def append(self, _data):
        new_node = Node(_data)
        
        if self.head == None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.nxt = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    
    def insert(self, _data, _target, _position = 'a'):
        new_node = Node(_data)
        aux = self.head
        
        while aux.data != _target:
            aux = aux.nxt
            
        if _position == 'a':
            if aux != self.tail:
                new_node.nxt = aux.nxt
                aux.nxt.prev = new_node
                aux.prev = new_node
                new_node.prev = aux
                aux.nxt = new_node
            else:
                self.append(_data)
        elif _position == 'b':
            if aux != self.head:
                new_node.nxt = aux
                new_node.prev = aux.prev
                aux.prev.nxt = new_node
                aux.prev = new_node
            else:
                self.push(_data)
        else:
            print("Posição inválida, jumento!")

    
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


list1 = Linked_List()
list1.append(65)
list1.append(71)
list1.append(26)
list1.append(84)
list1.append(12)
list1.append(90)
list1.append(36)
list1.print_list()

list1.push(72)
list1.push(64)
list1.insert(17, 26)
list1.insert(89, 71, 'b')
list1.insert(35, 64, 'b')
list1.insert(96, 36, 'a')
list1.push(51)
list1.print_list()
