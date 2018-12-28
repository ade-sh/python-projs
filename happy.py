#Happy numbers by Adesh
#still needs work on some parts, added hash where not working
n=0
c=0
seen_numbers=set()
hpn=True
while hpn:

        num1=input("Enter your number=")
        seen_numbers.clear()
        chk=0
        while chk==0:
                for i in str(num1):
                    k=int(i)
                    n=k*k
                    c=c+n
                    seen_numbers.add(c)
                    
                    if c==1:
                        print("Number is happy number")
                        chk=1
                        break
                        
                    elif c in seen_numbers:
                            print("not happy number")
                            chk=1
                            break
                    
        aga=input("Do you want to check again-Yes/no:")
        if aga=="Yes" or aga=="yes" or aga=="Y" or aga=="y":
                hpn=True and seen_numbers.clear()
        elif aga=="No" or aga=="no" or aga=="N" or aga=="n":
                hpn=False
        else:
                print("invalid input")

