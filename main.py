#Writing code for project on SPY_CHAT
#Date-18/06/2018
#Author-Surendra Chokotiya
from default import spy_name,spy_salutation,spy_age,spy_rating
question = "Welcome to SPY_CHAT /n Are you a default user (Y/N)?"
choice = input(question)
if choice == "Y":
          #Continue with default user information
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