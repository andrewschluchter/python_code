some_input = input("Enter something, ideally WITH slashes: ")
print(some_input)
print("Buffered: ")
# buffer slashes
buffered_input_chars = []
for char in some_input:
      #print(char)
      if char == '/':
            char = "//"
      buffered_input_chars.append(char)
      #print(buffered_input)
buffered_input = ''.join(buffered_input_chars)
print(buffered_input)
