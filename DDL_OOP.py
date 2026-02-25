
class Node:
    def __init__(self, value: str):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value: str) -> Node:
        new_node = Node(value)
        
            
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
        self.size += 1
        
        return new_node


    def truncate_after(self, node: Node) -> None:
        dzesamo_skaits = 0
        temp = node.next

        while temp is not None:
            dzesamo_skaits += 1
            temp = temp.next
            
        self.size = self.size - dzesamo_skaits 
        
        node.next = None
        self.tail = node

    def __len__(self) -> int:
        return self.size


class ActionHistory:

    def __init__(self):
        self.dll = DoublyLinkedList()
        self.current = None  

    def add(self, text: str) -> None:

        if self.current is not None and self.current.next is not None:
            self.dll.truncate_after(self.current)
        
        new_node = self.dll.append(text)
        self.current = new_node
        

    def undo(self) -> None:

        if self.current is not None and self.current.prev is not None:
            self.current = self.current.prev

    def redo(self) -> None:

        if self.current is not None and self.current.next is not None:
            self.current = self.current.next

    def current_value(self) -> str:

        if self.current is None:
            return "EMPTY"
        return self.current.value
            

def run_demo() -> None:

    commands = [
        ("CURRENT",),
        ("ADD", "Versija 1"),
        ("ADD", "Versija 2"),
        ("ADD", "Versija 3"),
        ("CURRENT",),
        ("UNDO",),
        ("CURRENT",),
        ("UNDO",),
        ("CURRENT",),
        ("REDO",),
        ("CURRENT",),
        ("ADD", "Versija 2.1"),
        ("CURRENT",),
        ("REDO",),     
        ("CURRENT",),
    ]

    history = ActionHistory()

    for cmd in commands:
        op = cmd[0]

        if op == "ADD":
            history.add(cmd[1])
        elif op == "UNDO":
            history.undo()
        elif op == "REDO":
            history.redo()
        elif op == "CURRENT":
            print(history.current_value())
        else:
            pass


if __name__ == "__main__":
    run_demo()