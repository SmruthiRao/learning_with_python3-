
fruit = 'banana'
m = fruit[0]
print(m)

print(list(enumerate(fruit)))

i = 0
while i < len(fruit):
    letter = fruit[i]
    print(letter)
    i +=1

prefixes = "JKLMNOPQ"
suffix = "ack"
for p in prefixes:
    print(p + suffix)

string = 'Hello World'
new_string = 'J' + string[1:]
print(new_string)

def remove_vowels(str):
    """ Reove vowels from a string"""
    vowels = "aeiouAEIOU"
    final_str = ''
    for let in str:
        if let not in vowels:
            final_str += let
    return final_str

print(remove_vowels('Smruthi'))
print(remove_vowels('Harry Potter'))
print(remove_vowels('Hermoine'))

def find_str(string, let):
    """ find position of a letter in string"""
    i = 0
    while i < len(string):
        if string[i] == let:
            return i
        i += 1
    return -1

print(find_str('Smruthi','r'))
print(find_str('Hello','l'))
print(find_str('Harry','g'))


def count_str(string, let):
    """ find number of time of a letter appears in string"""
    i = 0
    cnt = 0
#    while i < len(string):
#        if string[i] == let:
#            cnt += 1
#        i += 1
    for i in string:
        if i ==  let:
            cnt += 1
    return cnt

print(count_str('Smruthi','r'))
print(count_str('Hello','l'))
print(count_str('Harry','g'))
print()

string = 'banana'
print(string.find('nan'))
string = 'Smruthi'
print(string.find('th'))

punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
def remove_punc(str):
    """ Remove punctuations"""
    clean_str = ""
    for s in str:
        if s not in punctuation:
            clean_str += s
    return clean_str

print(remove_punc('My name is Smruthi. I am a potterhead!!'))





