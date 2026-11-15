class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Check whether the character is an operator
def is_operator(ch):
    return ch in "+-*/"


# Build expression tree from postfix expression
def build_tree(postfix):
    stack = []

    for ch in postfix:
        if ch == ' ':
            continue

        # If operand, create a node and push it
        if not is_operator(ch):
            stack.append(Node(ch))

        # If operator, pop two nodes
        else:
            right = stack.pop()
            left = stack.pop()

            new_node = Node(ch)
            new_node.left = left
            new_node.right = right

            stack.append(new_node)

    return stack[-1]


# Inorder traversal
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)


# Preorder traversal
def preorder(root):
    if root is not None:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder traversal
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")


# Evaluate expression tree
def evaluate(root):
    if root is None:
        return 0

    # If node is an operand
    if not is_operator(root.value):
        return int(root.value)

    left = evaluate(root.left)
    right = evaluate(root.right)

    if root.value == '+':
        return left + right

    elif root.value == '-':
        return left - right

    elif root.value == '*':
        return left * right

    elif root.value == '/':
        return left / right


# Main program
postfix = input("Enter postfix expression: ")

root = build_tree(postfix)

print("\nInorder Traversal: ", end="")
inorder(root)

print("\nPreorder Traversal: ", end="")
preorder(root)

print("\nPostorder Traversal: ", end="")
postorder(root)

print("\nExpression Value:", evaluate(root))
