class LinkedList:

    #Начало связанного списка
    head = None

    #Класс узла списка. Имеет значение и ссылку на следующий узел
    class Node:
        element = None
        next_node = None

        def __init__(self, element, next_node=None):
            self.element = element
            self.next_node = next_node

    #Для создания экземпляра класса связанного списка передаем обычный список
    def __init__(self, some_arr):
        if some_arr:
            for value in some_arr:
                self.add_to_end(value)
        else:
            self.head = self.Node(None)

    #Проходим по списку до тех пор пока не наткнемся на конечный узел. Затем просто привязываем к нему следующий узел
    def add_to_end(self, element):
        if not self.head:
            self.head = self.Node(element)
            return element
        node = self.head

        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element)

    #Заменяем начало нашего списка на нужное нам значение
    def add_to_head(self, element):
        if not self.head:
            self.head = self.Node(element)
            return element

        self.head = self.Node(element, self.head)

    #Добавление нового узла после нужного нам значения. Если этого значения нет в списке, то элемент не добавится
    def add_after_v(self, v, element):
        if not self.head:
            self.head = self.Node(element)
            return element
        node = self.head

        while node.next_node:
            if node.element == v:
                node.next_node = self.Node(element, node.next_node)
            node = node.next_node

    def delete_list(self):
        self.head = None
        
    def print_list(self):
        node = self.head

        while node.next_node:
            print(node.element, end=', ')
            node = node.next_node
        print(node.element)


linked_list = LinkedList([1, 2, 3, 4, 5])
linked_list.print_list() # 1, 2, 3, 4, 5

linked_list.add_to_end(10)
linked_list.print_list() # 1, 2, 3, 4, 5, 10

linked_list.add_to_head(100)
linked_list.print_list() # 100, 1, 2, 3, 4, 5, 10

linked_list.add_after_v(100, 500)
linked_list.print_list() # 100, 500, 1, 2, 3, 4, 5, 10

linked_list.delete_list()
linked_list.print_list() # Error


