#Huffman Coding (Encoding and Decoding)
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

# utility function to generate huffman codes for all symbols in the newly created Huffman tree
def generate_huffman_codes(node, val='', codes={}):
    # huffman code for current node
    new_val = val + str(node.huff)
    # if node is not an edge node then traverse inside it
    if node.left:
        generate_huffman_codes(node.left, new_val, codes)
    if node.right:
        generate_huffman_codes(node.right, new_val, codes)
    # if node is edge node then store its huffman code
    if not node.left and not node.right:
        codes[node.symbol] = new_val
    return codes

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

# Generate Huffman codes and store them
huffman_codes = generate_huffman_codes(nodes.pop())

# Display Huffman codes
print("Generated Huffman Codes:")
for char, code in huffman_codes.items():
    print(f"{char} -> {code}")

# Take user input for the message to decode
user_input = input("Enter the encoded message: ")

# Decode the message using the stored Huffman codes
decoded_message = ""
temp_code = ""
for bit in user_input:
    temp_code += bit
    for char, code in huffman_codes.items():
        if temp_code == code:
            decoded_message += char
            temp_code = ""
            break

# Display decoded message
print("Decoded Message:", decoded_message)
