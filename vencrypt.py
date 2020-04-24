import sys, getopt
#python vencrypt.py -i plaintext.txt -o encryptedtext.txt -k lemon
def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) - len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 
    
def cipherText(string, key): 
    cipher_text = [] 
    for i in range(len(string)): 
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A') 
        cipher_text.append(chr(x)) 
    return("" . join(cipher_text)) 
    
def main(argv):
   inputfile = ""
   outputfile = ""
   keyword = ""
   ciphertext = ""
   words = []
   try:
      opts, args = getopt.getopt(argv,"hi:o:k:",["ifile=","ofile=","keyword="])
   except getopt.GetoptError:
      print ('vencrypt.py -i <inputfile> -o <outputfile> -k <keyword>')
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
       cipher_text = cipherText(word,key)
       ciphertext = ciphertext+cipher_text+" "
   ciphertext = ciphertext.lower()
   #print(ciphertext)
   f = open(outputfile, 'w+')
   f.write(ciphertext)
   f.close 
   print("Fin") 

if __name__ == "__main__":
   main(sys.argv[1:])    
