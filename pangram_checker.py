def pangram(): 
   Alphabet = "abcdefghijklmonpqrstuvwxyz" 
   for letter in Alphabet : 
     if letter not in sentence.lower() : 
       return False 
     return True 
     
sentence = input("Enter the sentence:") 
if pangram()== True: 
    print(f"{sentence } is a prangram") 
else:
     print(f"{sentence } is not a prangram") 
