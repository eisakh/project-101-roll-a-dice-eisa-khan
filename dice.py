import random



response="y"


while response=="y":
    no=random.randint(1,6)
    if no==1:
        print("[------]")
        print("[   0  ]")
        print("[------]")
    if no==2:
        print("[------]")
        print("[0    0]")
        print("[------]")
    if no==3:
        print("[------]")
        print("[0  0 0]")
        print("[------]")
    if no==4:
        print("[--0---]")
        print("[0    0]")
        print("[---0--]")
    if no==5:
        print("[------]")
        print("[00 000]")
        print("[------]")
    if no==6:
        print("[0    0]")
        print("[0    0]")
        print("[0    0]")
    
    a=input("enter y to continue and n to stop= "  )
    if a=="y":
       response="y"
    else:
       response="n"








     
    
    
        
    


        
        
  


