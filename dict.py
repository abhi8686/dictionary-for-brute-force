
text_file = open("Output.txt", "w")

wordlist="$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

import itertools
p=input("enter the length of string")
for string in itertools.imap(''.join, itertools.product(wordlist, repeat=p)):
    print string

    text_file.write("%s" % string+'\n')
                
                
    

text_file.close()
