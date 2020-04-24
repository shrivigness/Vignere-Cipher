# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 19:25:58 2020

@author: Shri
"""
#python vdecrypt.py -i encryptedtext.txt -o decryptedtext.txt -k lemon
def originalText(cipher_text, key): 
    orig_text = [] 
    for i in range(len(cipher_text)): 
        x = (ord(cipher_text[i]) - 
             ord(key[i]) + 26) % 26
        x += ord('A') 
        orig_text.append(chr(x)) 
    return("" . join(orig_text)) 
    return ''.join(cipher_text)

import sys, getopt

def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) - len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 
      
def main(argv):
   inputfile = ""
   outputfile = ""
   keyword = ""
   plaintext = ""
   words = []
   try:
      opts, args = getopt.getopt(argv,"hi:o:k:",["ifile=","ofile=","keyword="])
   except getopt.GetoptError:
      print ('test.py -i <inputfile> -o <outputfile> -k <keyword>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <inputfile> -o <outputfile> -k <keyword>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      elif opt in ("-k", "--keyword"):
         keyword = arg
   
   f = open(inputfile, 'r')
   words = f.read().strip().split(' ')
   f.close()
   keyword = keyword.upper()
   #print(words)
   for word in words:
       word = word.upper()
       key = generateKey(word, keyword) 
       plain_text = originalText(word,key)
       plaintext = plaintext+plain_text+" "
   plaintext = plaintext.lower()
   #print(plaintext)
   f = open(outputfile, 'w+')
   f.write(plaintext)
   f.close 
   print("Fin") 

if __name__ == "__main__":
   main(sys.argv[1:])    
