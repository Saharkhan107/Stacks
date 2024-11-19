class Stack:
    def __init__(self):
        # Initialize an empty list to hold the stack elements
        self.stack = []

    def push(self, element):
        # Add an element to the top of the stack
        self.stack.append(element)

    def pop(self):
        # Remove and return the top element of the stack
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def peek(self):
        # Return the top element without removing it
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

# Test case
if __name__ == "__main__":
    # Create a stack instance
    s = Stack()

    # Push three elements
    s.push(10)
    s.push(20)
    s.push(30)

    # Pop one element
    print(f"Popped element: {s.pop()}")  # Expected: 30

    # Peek at the top element
    print(f"Top element: {s.peek()}")  # Expected: 20

