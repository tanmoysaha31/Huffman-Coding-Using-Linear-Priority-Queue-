print("Let's do it.........")
print("Testing Huffman encoding and decoding")
print("..........Loading..........")
print("........Almost there........")
class LinearPriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        min_index = 0
        for i in range(1, len(self.queue)):
            if self.queue[i] < self.queue[min_index]:
                min_index = i
        return self.queue.pop(min_index)

    def __len__(self):
        return len(self.queue)

# A Huffman Tree Node
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq
        # symbol name (character)
        self.symbol = symbol
        # node left of current node
        self.left = left
        # node right of current node
        self.right = right
        # tree direction (0/1)
        self.huff = ''

    def __lt__(self, other):
        return self.freq < other.freq

# utility function to print huffman codes for all symbols in the newly created Huffman tree
def print_nodes(node, val=''):
    # huffman code for current node
    new_val = val + str(node.huff)
    # if node is not an edge node then traverse inside it
    if node.left:
        print_nodes(node.left, new_val)
    if node.right:
        print_nodes(node.right, new_val)
    # if node is edge node then display its huffman code
    if not node.left and not node.right:
        print(f"{node.symbol} -> {new_val}")

# dictionary containing characters and their frequencies
x_dict = {'A': 1, 'b': 1, 'f': 1, ',': 1, 'E': 1, '.': 1, 'c': 2, ' ': 2, 'l': 2, 'd': 3, 'e': 3, 'k': 3, 's': 3, 'a': 7}

# list containing unused nodes
nodes = LinearPriorityQueue()

# converting characters and frequencies into huffman tree nodes
for char, freq in x_dict.items():
    nodes.push(Node(freq, char))

while len(nodes) > 1:
    # sort all the nodes in ascending order based on their frequency
    left = nodes.pop()
    right = nodes.pop()

    # assign directional value to these nodes
    left.huff = 0
    right.huff = 1

    # combine the 2 smallest nodes to create new node as their parent
    new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)

    nodes.push(new_node)

# Huffman Tree is ready!
print_nodes(nodes.pop())

