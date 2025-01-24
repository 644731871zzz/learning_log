from random import choice

lottery_words=[]
lottery_number=0
lottery=['1','2','3','4','5','6','7','8','9','0','a','b','c','d']
while lottery_number<4:
    lottery_word=choice(lottery)
    lottery_words.append(lottery_word)
    lottery_number+=1
print(f"this is your word : ")
for lottery_word in lottery_words:
    print(f"{lottery_word}")
   

print("\nif you get a,1,b,2,c,3.you are win!!!!!!!1")
