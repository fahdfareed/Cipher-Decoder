# Copyright 2021 Fahad Farid fahadf@bu.edu

"""
Problem Description
-------------------

A ciphertext is the result of encrpytion performed on
a message, called "plaintext"

Here is the encryption algorithm we will implement:

  Each letter a-z and A-Z is transformed in a two step process:

   1. Replace the letter by its "opposite letter" in the alphabet. So a becomes z,
       b becomes y, c becomes x, etc
   2. Adjust the new letter by an offset. If the offset is 2, then every letter is 
   "moved up" in the alphabet by 2, i.e. a becomes c, b becomes d, and so on. 
   (z becomes b i.e. we wrap around)

Other rules:
  1. Characters other than a-z and A-Z are not modified.
  2. The offset is initially 0. Whenever a certain letter appears in the plaintext,
  the offset changes to the count of that letter. The change to the offset is 
  effective for the next letter in the plaintext.
  3. Lower and upper cases should be maintained.
  4. Both the lower and upper case version of the key cause the offset to change.
  5. If the key is not a letter, it should still cause changes to the offset when
     it appears in the plaintext.


Hints:
------
use the built in functions chr and ord


Assignment
----------
Write a function "decoder" that will convert ciphertext back into plaintext.

Both are strings.

This is the function signature:

def decoder(ciphertext, key):

or more formally

def decoder(ciphertext : str, key : str) -> str:

Although key is a string, if it is not a single character, an exception
should be raised by the function.

"""


def decoder(ciphertext : str, key : str) -> str:
    if len(key) != 1:
        raise Exception("Your Key should only contain one letter")
    
    offset = 0
    plaintext = []
    for i in ciphertext:
        ascii_val = ord(i)

        if ascii_val > 64 and ascii_val < 91:
            ascii_val = (ascii_val - offset)
            if ascii_val < 65:
                ascii_val = 90 - (64 - ascii_val)
            new_value = (90 + (65 - ascii_val)) % 90
            letter = chr(new_value)

        elif ascii_val > 96 and ascii_val < 123:
            ascii_val = (ascii_val - offset)
            if ascii_val < 97:
                ascii_val = 122 - (96 -ascii_val) 
            new_value = (122 + (97 - ascii_val)) % 122
            letter = chr(new_value)
        else:
            letter = i
        plaintext.append(letter)
        offset += 1 if (letter.upper() == key.upper()) else 0
        offset %= 26
        
    return ''.join(plaintext)

cipher_plain_examples = {('abcde', 'z'): ('zyxwv', 'z'), ('abcde', 'c'): ('zyxxw', 'c'), ('this is plaintext', 'i'): ('gsri sj mqbtpjyfj', 'i'), ('This Is Plaintext', 'i'): ('Gsri Sj Mqbtpjyfj', 'i'), ('This Is Plaintext', 'I'): ('Gsri Sj Mqbtpjyfj', 'I'), ('I am sending 100 dollars, right now.', 'n'): ('R zn hvmxsnv 100 ynqqbkj, ktvui oog.', 'n'), ('This is a poem.\nAbout nothing,\nat all', ','): ('Gsrh rh z klvn.\nZylfg mlgsrmt,\nah app', ','), ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'a'): ('zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg', 'a'), (None, 'bad key'): ('gsrh urmzo vcznkov droo izrhv zm vcxvkgrlm', 'bad key')}

def main():
  for example,key in cipher_plain_examples:
    cipher,key = cipher_plain_examples[(example,key)]
    try:
      plain = decoder(cipher,key)
    except:
      plain = None
    print(example,key)
    print(cipher)
    print(plain)
    print(plain==example)
    print()
    


if __name__ == '__main__':
  main()