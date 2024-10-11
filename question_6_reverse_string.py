# This code contains errors that you need to fix it. Read carefully and do necessary corrections.
# Run the code at online-python.com or IDLE PYTHON before you commit the changes at github.com

# This program is used to reverse a string.

def string_reverse(str1):
    rstr1 = ''
    
    index = len(str1) - 1
    
    while index >= 0:
        rstr1 += str1[index]
        index -= 1
    
    return rstr1

def main():    
    print("String reverse for \'12345abcde\' is", string_reverse('12345abcde'))

# Don't change the code below!
if __name__ == "__main__":
    main()
