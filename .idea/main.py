#!/usr/local/bin/python3.9
import sys
import random
import subprocess


all_languages=["af", "am", "ar", "az", "ba", "be", "bg", "bn", "bs", "ca"]
amount_of_steps=int(sys.argv[1])
our_list=[]
for all in range(amount_of_steps):
    new_lang=random.choice(all_languages)
    our_list.append(new_lang)
print(our_list)
f = open("text1")
for new_texts in our_list:
    subprocess.run(["echo $new_texts"])
    print(new_texts)

#k=random.choice(all_languages)
#print(k)
#list_test.append(k)
#print(list_test)
#i=1
#for i in range(amount_of_steps):
 #   print("hi")