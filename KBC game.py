questions = [["who won worldcup 2023?","india","england","aus","sa","c"],
["who won ipl 2023?","rcb","gt","csk","rr","c"],
["who won pkl 2022?","gujarat","u mumba","jaipur","bangal","c"],
["who pm of india?","modi","rahul gandhi","amit shah","kejriwal","a"],
["who is CEO of tesla:","sundar pichai","elon musk","mark zukarberg","steve jobs","b"],
["what is the longest river in the world?","ganga","amazon","nile","sabarmati","c"],
["who is the biggest animal on earth?","elephant","blue whale","ziraf","tiger","b"]
]

levels=[1000,2000,3000,10000,20000,10000000,70000000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"\n\nquestion for Rs.{levels[i]}")
    print(question[0])
    print(f" a.{question[1]}        b.{question[2]} ")
    print(f" c.{question[3]}         d.{question[4]} ") 

    reply=input("enter your answer(a/b/c/d):")
    if(reply=="q" ):
        print("you are quite the game")
        money=levels[i-1]

    if(reply==question[5]):
        print(f"\n\ncongratulations! , you won Rs.{levels[i]}")
        if(i==4):
            money=20,000
        elif(i==5):
            money=10000000  
        elif(i==6):
            money=70000000      
    else:
        print("sorry,wrong answer.(go your home.)")    
        break

print(f"your winning money is {money}")    


