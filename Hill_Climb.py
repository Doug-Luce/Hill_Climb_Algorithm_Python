import random
import string
'This program tests the monkey therom, and uses the hill climb algorithm'


class Find_string():
    string_to_find = ''
    random_alphabet_list = []
    random_string = ''
    progress_string = []
    mainloop = True

    def __init__(self, string_to_find):
        self.string_to_find = string_to_find
        for i in range(len(self.string_to_find)):
            self.progress_string.append(' ')

    def make_random_letters(self):
        self.random_alphabet_list = []
        self.random_string = ''
        self.alphabet = ['a', 'b', 'c' ,'d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', " ",]
        for i in range(len(self.string_to_find)):
            self.random_alphabet_list.append(random.choice(self.alphabet))
        self.random_string = ''.join(self.random_alphabet_list)

    def progress(self):
        for i in range(len(self.string_to_find)):
            if self.string_to_find[i] == self.random_string[i]:
                self.progress_string[i] = self.random_string[i]
        print((''.join(self.progress_string)))

def main():
    stringFind = Find_string('methinks it is like a weasel')
    i = 0
    j = 0
    while i <= len(stringFind.string_to_find):
        stringFind.make_random_letters()
        stringFind.progress()
        if stringFind.string_to_find[j] == stringFind.progress_string[j]:
            i += 1
            j += 1
            if j== len(stringFind.string_to_find):
               j = 0
    print("String Found",''.join(stringFind.progress_string))


if __name__  == '__main__':
    main()

