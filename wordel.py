import urllib.request
import random
import enchant
import time
correct_w_wr_pos=[]
correct_w_corr_pos=[]

def timers(t):
    while t:
        mins, secs=divmod(t, 60)
        times= '{:02d}:{:02d}'.format(mins, secs)
        print(times, end="\r")
        time.sleep(1)
        t-=1
        if t==0:
            rand_word=random_gen()
            return rand_word

def random_gen():
    'Generating random word from the file'
    
    url="https://raw.githubusercontent.com/charlesreid1/five-letter-words/master/sgb-words.txt"

    file=urllib.request.urlopen(url)
    text=file.read()
    words=list(map(str,text.split()))
    random_word=random.choice(words)
    print(random_word)
    return random_word
    

def wordel(w,rand_word):

    count=0

    'comparing random word with given word'
    
    for i in range(2,len(rand_word)-1):
        for j in range(0,len(w)):
            if rand_word[i]== w[j] and i!=j+2:
                if not correct_w_wr_pos:
                    correct_w_wr_pos.append(w[j])
                else:
                    for k in range(0,len(correct_w_wr_pos)):
                        if correct_w_wr_pos[k]!=w[j]:
                            correct_w_wr_pos.append(w[j])
            elif rand_word[i]== w[j] and i==j+2:
                correct_w_corr_pos.append(w[j])
                if len(correct_w_corr_pos)==5:
                    count=5
                else:
                    count+=1
    if correct_w_wr_pos ==[] and correct_w_corr_pos==[]:
        print("No correct word")
        
    print("Correct alpha with wrong pos",correct_w_wr_pos)
    print("Correct alpha with wright pos",correct_w_corr_pos)
    correct_w_corr_pos.clear()
    correct_w_wr_pos.clear()
    return count
                
i=6
rand_word=random_gen()
ran_word = timers(10)
while(i!=0):
    s=input("Enter your word")
    d=enchant.Dict("en_US")
    if d.check(s)==False:
        print("Word does not exist")
        continue
    if len(s)!=5:
        print("len should be 5")
        continue
    correct=wordel(s,ran_word)
    if correct!=5:
        i=i-1
        print("no of remaining tern=",i)
    else:
        print("you word is coorect")
        break
    if i==0:
        print("next time")
    
