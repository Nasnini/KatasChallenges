# 8 Excercise: Frame some text

# function taking 2 parameters  
def print_in_a_frame(words, borderchar = '*'):
    size = max(len(word) for word in words)
    print(borderchar * (size + 4))
    for word in words:
        print('{bc} {:<{}} {bc}'.format(word, size, bc = borderchar))
    print(borderchar * (size + 4))

# print the list
print_in_a_frame(["Write", "good", "code", "every", "day"])
