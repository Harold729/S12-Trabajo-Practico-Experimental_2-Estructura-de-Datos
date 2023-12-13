
class Node:

    def __init__(self, label, parent, code):
        self.label = label
        self.left = None
        self.right = None
        self.parent = parent
        self.code = code

    def getLabel(self):
        return self.label
    
    def getCode(self):
        return self.code

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def setParent(self, parent):
        self.parent = parent


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, label, code):
        # Creamos un nuevo nodo
        new_node = Node(label, None, code)
        # Si el árbol esta vacio
        if self.empty():
            self.root = new_node
        else:
            # Si el árbol no esta vacio
            curr_node = self.root
            while curr_node is not None:
                parent_node = curr_node
                if new_node.getLabel() < curr_node.getLabel():
                    curr_node = curr_node.getLeft()
                else:
                    curr_node = curr_node.getRight()
            if new_node.getLabel() < parent_node.getLabel():
                parent_node.setLeft(new_node)
            else:
                parent_node.setRight(new_node)
            new_node.setParent(parent_node)      

    def empty(self):
        if self.root is None:
            return True
        return False

    def __InOrderTraversal(self, curr_node):
        nodeList = []
        if curr_node is not None:
            nodeList.insert(0, curr_node)
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getLeft())
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getRight())
        return nodeList

    def __str__(self):
        list = self.__InOrderTraversal(self.root)
        str = ""
        for x in list:
            str = str + " " + x.getCode().__str__()
        return str

def InPreOrder(curr_node):
    nodeList = []
    if curr_node is not None:
        nodeList = nodeList + InPreOrder(curr_node.getLeft())
        nodeList.insert(0, curr_node.getLabel())
        nodeList = nodeList + InPreOrder(curr_node.getRight())
    return nodeList

# Función para probar las clases
def testBinarySearchTree():
    # Instancia del árbol binario de búsqueda
    t = BinarySearchTree()
    #Insertamos los elementos
    t.insert(15, "Pablo")
    t.insert(8, "Pedro")
    t.insert(10, "Pepe")
    t.insert(5, "Carlos")
    t.insert(22, "Ramon")
    t.insert(17, "Anibal")
    t.insert(18, "Ines")
    t.insert(9, "Pamela")
    t.insert(11, "Clara")
    t.insert(4, "Lady")
    t.insert(6, "Luis")
    t.insert(25, "Sandra")
    t.insert(24, "Juan")

    #Este es el modelo que tomara el arbol segun sus codigos
    #                     15
    #                    /  \
    #                   /    \
    #                  /      \
    #                 /        \
    #                /          \
    #               /            \
    #              /              \
    #             8               22
    #            / \              /\
    #           /   \            /  \
    #          /     \          /    \
    #         /       \        /      \
    #        /         \      /        \
    #       5          10    17        25
    #      / \         / \    \        /
    #     /   \       /   \    \      /
    #    4     6     9    11    18  24

    print(t.__str__())


if __name__ == "__main__":
    testBinarySearchTree()