
def max(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

max = max(4,9)
# print (max)

def max_three(n1, n2, n3):
    if  n1 > n2:
        return n1
    if  n2 > n3:
        return n2
    if  n3 > n1:
        return n3

max_three = max_three(1,5,7)
# print (max_three)

def string_length(string):
    return len(string)

# text = input("Ingrese la palabra que desea evaluar con string_length(): ")
# string_length = string_length(text)
# print (string_length)

def array_length(array):
    return len(array)

array_length = array_length(['m', 'a', 'n', 'z', 'a', 'n', 'a'])
# print (array_length)

def is_vocal(character):
    list = ['a', 'e', 'i', 'o', 'u']
    if character in list:
        return True
    else:
        return False

# text = input("Ingrese la vocal que desea evaluar con is_vocal(): ")
# is_vocal = is_vocal(text)  
# print (is_vocal)

def sum(array):
    s = 0
    for x in range(0, len(array)):
        s = s + array[x]
    return s

sum = sum([1,2,3,4])
# print (sum)

def multip(array):
    m = 1
    for x in range(0, len(array)):
        m = m * array[x]
    return m

multip = multip([1,2,3,4])
# print (multip)

def reverse_string(string):
    s = string[len(string)::-1] # slicing 
    return s

# text = input("Ingrese la palabra que desea evaluar con reverse_string(): ")
# string = reverse_string(text)
# print (string)

def is_palindromo(string):
    rever = string[::-1]
    if string == rever:
        return True
    else:
        return False

# text = input("Ingrese la palabra que desea evaluar con is_palindromo(): ")
# is_palindromo = is_palindromo(text)
# print (is_palindromo)

def generate_n_characters(n, character):
    s = ''
    for i in range(int(n)):
        s = s + character
    return s

text = input("Ingrese un numero que desea evaluar con generate_n_characters(): ")
character = input("Ingrese un caracter que desea evaluar con generate_n_characters(): ")
characters = generate_n_characters(text, character)
print (characters)
