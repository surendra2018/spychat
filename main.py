#Writing code for project on SPY_CHAT
#Date-18/06/2018
#Author-Surendra Chokotiya
#============================import files and library=========================================================

import sys            #import sys library for exit application
from default import spy_name,spy_salutation,spy_age,spy_rating  #import default.py file (default user info)


#==================================start_chat()  function method==============================================================

def start_chat(spy_name,spy_age,spy_rating):           #define start_chat() function
    print("Authantication Complete!\nWelcome\n%s\nage - %d\nrating - %.2f" %(spy_name,spy_age,spy_rating))
    current_status_msg = None                              #current_status none
    if spy_age>12 and spy_age<60:                           # validation for spy_age

        show_menu = True
        while show_menu == True:
            print("================================MENU===============================\n")
            menu = """What do you want to do?
                      1. Update a Status
                      2. Add a new friend
                      3. Send a secret message
                      4. Read a personal message
                      5. Read chats from users
                      6. Press '0' for Exit"""

            menu_choice = input(menu)                     # choosing menu_choice
            menu_choice = int(menu_choice)                #typecasting string to integer

            if menu_choice == 1:                  #status update module

                current_status = add_status(current_status_msg)            #current_status updated
                print("YOUR CURRENT STATUS IS %s" %current_status)

            elif menu_choice == 2:                 #add new friend
                print("Add friend")
                add_your_friend = add_friend()
                print("YOUR FRIEND %s IS SUCCESFULLY ADDED" %friend_name[len(friend_name)-1])
                print("YOU HAVE %d FRIENDS NOW" %add_your_friend)

            elif menu_choice == 3:                   #send a secret message
                print("send secret messages")

            elif menu_choice == 4:                    #read personal message
                print("read personal message")

            elif menu_choice == 5:                    #read chats from users
                print("read chats")

            elif menu_choice == 0:
                show_menu == False
                sys.exit()

            else:                                      #default message
                print("Ooops! you have entered a wrong choice")

#=================================.add_status() function method===========================================
def add_status(current_status_msg):
    if current_status_msg != None:
        print("your current status is %s" %current_status_msg)
    else:
        print("you don't have any status right now")
        default = input("Do you want to select from your older status(Y/N)?")
        if default.upper() == "N":
            new_status_msg = input("What is on your mind?")
            if len(new_status_msg)>0:
                updated_status = new_status_msg
                STATUS_MSG.append(new_status_msg)
            else:
                print("you have not entered any status\nPlease try again")
        elif default.upper() == 'Y':
            item_pos = 1
            if STATUS_MSG == []:
                print("you don't have any older choice")
            else:
                for msg in STATUS_MSG:
                    print('%d. %s' %(item_pos,msg))
                    item_pos = item_pos + 1
            while True :
                status_sel = int(input("select your choice from above status?"))
                if status_sel > len(STATUS_MSG):
                    print('Invalid  choice\nPlease try again')
                else:
                    updated_status = STATUS_MSG[status_sel-1]
                    break
        else:
            print('Invalid entry\nTry again')
    return updated_status

#==============================add_friend() function=======================================================

def add_friend():

    new_name = input("Enter your friend name")
    new_salutation = input(" what should we call your friend (Mr./Miss.)?")
    new_name = new_salutation+" "+new_name
    new_age =  int(input("Enter your friend age"))
    new_rating = float(input("Enter your friend new rating"))

    if len(new_name) > 0 and new_age > 12 and new_age < 60:
        friend_name.append(new_name)
        friend_age.append(new_age)
        friend_rating.append(new_rating)
        friend_online.append(True)
    else:
        print("Soory! your friend does not fullfill neccessary criteria to be a spy")
    return len(friend_name)

#===============================main function start=========================================================
question = "Welcome to SPY_CHAT /n Are you a default user (Y/N)?"
choice = input(question)
STATUS_MSG = ['PLEASE LEAVE MESSAGE','I AM BUSY','SECRET IS ALWAYS GOOD','Every day give a secret']
                                                                #older status messages list
friend_name = []
friend_age = []                                    #friend information lists
friend_rating = []
friend_online = []

if choice.upper() == "Y":
    #print("PLEASE signup")
    start_chat(spy_name,spy_age,spy_rating)
    #Continue with default user information
elif choice.upper() == "N":

    spy_name = input("Tell me your Name first: ")
         #for take input of spy name
    if len(spy_name)>0:
         #use for count len. use if condition for camparing
        spy_salutation = input("Welcome %s What should I call you Mr./Miss.?" %spy_name)
             #Use for take input of spy salutation
        spy_name = '%s%s' %(spy_salutation,spy_name)
             #use for give message to spy name with salutation
        spy_age = input("Ok %s Enter your age:" %spy_name)
             #use for take input of spy age
        spy_age = int(spy_age)
             #use for convert spy sge into integer
        if spy_age>12 and spy_age<60:
         #use if for comparing spy age

            spy_rating = input("How much you like it %s" %spy_name)
             #use for enter rating by spy
            spy_rating = float(spy_rating)
            if spy_rating>=4.5:
         #use if for give message to spy according entered rating
                print("Great")
            elif spy_rating<4.5 and spy_rating>=3.5:
                print("Better")
            elif spy_rating<3.5 and spy_rating>=2.5:
                print("good")
            else:
                print("You can do better")
            is_online = True
          #checking spy is online or not by define a boolean datatype
            print("Welcome,")
            print("%s age: %d and rating: %g We are proud to have you onboard" %(spy_name,spy_age,spy_rating))
         #use place holder %s,%d,%f
        else:
            print("Ooops! Sorry,you are not of correct age to be our spy")
    else:
        print("Sorry,you have entered an invalid Name!")
