'''
snake = -1 
water = 0
gun = 1

'''
import random
computer_letter =  random.choice([1, 0, -1])
com_dict = {
    1 : "Gun" ,  
    0 : "Water" ,
   -1 : "Snake"
}

computer_choice = com_dict[computer_letter]


user_dict = {
    "s" : -1 ,
    "w" : 0 ,
    "g" : 1
}

user_letter = input("ENTER YOUR CHOICE in (s,w,g): ").lower()
user_choice = user_dict[user_letter]

print(f"USER CHOICE IS : {com_dict[user_choice]}")
print(f"COMPUTER CHOICE IS : {computer_choice}")


if (computer_letter == user_choice):
    print(f"MATCH DRAW BEACUSE USER AND COMPUTER CHOICE ARE SAME : {computer_choice}")
else:
     #nested loop
    if(( computer_letter == 0 and user_choice == -1 ) or (computer_letter == 1 and user_choice==0) or (computer_letter==-1 and user_choice == 1)):
        print(f"USER IS WINNER 🎉")
    else:
        print(f"COMPUTER IS WINNER ☕👾\nTRY agin!!!!")       