# Coded By Ansley Paul Sze
# Debugged and Tested By Teodoro Jose Cruz

class PDA:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'}
        self.input_alphabet = {'<', '>', '{', '}', '[', ']', '(', ')', '!'}

        self.transitions = {
            ('q0', '!', 'Z'): ('q1', '!'),

            ('q1', '<', '!'): ('q1', '<'),  # Push '<' to the stack when encountering 'Z'
            ('q1', '<', '<'): ('q1', '<'),  # Push '<' to the stack when encountering '<'
            ('q1', '<', '{'): ('q1', '<'),  # Push '<' to the stack when encountering '{'
            ('q1', '<', '['): ('q1', '<'),  # Push '<' to the stack when encountering '['
            ('q1', '<', '('): ('q1', '<'),  # Push '<' to the stack when encountering '()'

            ('q1', '{', '!'): ('q1', '{'),  # Push '{' to the stack when encountering 'Z'
            ('q1', '{', '{'): ('q1', '{'),  # Push '{' to the stack when encountering '<'
            ('q1', '{', '<'): ('q1', '{'),  # Push '{' to the stack when encountering '<'
            ('q1', '{', '['): ('q1', '{'),  # Push '{' to the stack when encountering '['
            ('q1', '{', '('): ('q1', '{'),  # Push '{' to the stack when encountering '['

            ('q1', '[', '!'): ('q1', '['),  # Push '[' to the stack when encountering 'Z'
            ('q1', '[', '<'): ('q1', '['),  # Push '[' to the stack when encountering '<'
            ('q1', '[', '{'): ('q1', '['),  # Push '[' to the stack when encountering '{}'
            ('q1', '[', '['): ('q1', '['),  # Push '[' to the stack when encountering '[]'
            ('q1', '[', '('): ('q1', '['),  # Push '[' to the stack when encountering '()'

            ('q1', '(', '!'): ('q1', '('),  # Push '(' to the stack when encountering 'Z'
            ('q1', '(', '<'): ('q1', '('),  # Push '(' to the stack when encountering '<'
            ('q1', '(', '{'): ('q1', '('),  # Push '(' to the stack when encountering '{'
            ('q1', '(', '['): ('q1', '('),  # Push '(' to the stack when encountering '['
            ('q1', '(', '('): ('q1', '('),  # Push '(' to the stack when encountering '('

            ('q1', '>', '<'): ('q1', ''),   # Pop '<>' from the stack when encountering '>'
            ('q1', '}', '{'): ('q1', ''),   # Pop '{}' from the stack when encountering '>'
            ('q1', ']', '['): ('q1', ''),   # Pop '[]' from the stack when encountering ']'
            ('q1', ')', '('): ('q1', ''),   # Pop '()' from the stack when encountering ')'

            ('q1', '!', '!'): ('q2', '')    # Transition to final state with empty stack when encountering '!'

        }

    def process_input(self, input_string):
        if not input_string.startswith('!'):
            print("Processing", input_string)
            print("Invalid string. Failed at position 1.")
            print(f"Remaining unprocessed input string: {input_string}")
            return

        stack = ['Z']
        current_state = 'q0'
        position = 0

        print("Processing", input_string)

        while position < len(input_string):
            stack = [item for item in stack if item != '']
            char = input_string[position]
            #print("Current stack:", stack) # for debugging

            if (current_state, char, stack[-1]) in self.transitions:
                current_state, stack_top = self.transitions[(current_state, char, stack[-1])]
                if stack_top:
                    stack.append(stack_top)

                if stack_top == '':
                    # Convert stack to list, pop the last item sinec tuple does not have pop, then convert it back to tuple
                    stack = list(stack)
                    stack.pop()
                
                if input_string[position+1:] == '':
                  #if q1 is empty already
                  print("ID:", f"({current_state}, E, {''.join(stack[::-1])})")
                else:
                  print("ID:", f"({current_state}, {input_string[position+1:]}, {''.join(stack[::-1])})")

                position += 1
            else:
              if current_state in {'q0', 'q1', 'q2'}:
                  print(f"Invalid string. Failed at position {position + 1}.")
                  print(f"Remaining unprocessed input string: {input_string[position:]}")
              else:
                  print(f"Invalid string. {current_state} is not a final state.")
              return

        if current_state == 'q2' and position == len(input_string) and stack == ['Z']:
             print("q2 is a final state.")
             print(input_string, "is valid and has balanced brackets.")

        else:
            print(f"Invalid string. {current_state} is not a final state.")

def read_input_from_file(filename):
    inputs = []
    with open(filename, 'r') as file:
        # strip whitespaces
        for line in file:
            inputs.append(line.strip())
    return inputs

def main():
    pda = PDA()
    filename = "input.txt"
    input_strings = read_input_from_file(filename)
    # process each string
    for input_string in input_strings:
        pda.process_input(input_string)
        print()

if __name__ == "__main__":
    main()
