#def fact(n):
#    res = 1
#    for i in range(1, n+1):
#        res = res*i
#    return res


#n = int(input("Enter a number"))
#r = fact(n)
#print(r)


#add friend Function




def add_friend()
    friend_name = []
    friend_age = []
    friend_rating = []
    friend_online = []

    new_name = input("Enter your friend name")
    new_salutation = input(" what should we call your friend (Mr./Miss.)?")
    new_name = new_salutation+" "+new_name
    new_age =  input("Enter your friend age")
    new_rating = input("Enter your friend name")

    if new_name > 0 and new_age > 12 and new_age < 60:
        friend_name.append(new_name)
        friend_age.append(new_age)
        friend_rating.append(new_rating)
        friend_online.append(True)
    else:
        print("Soory! your friend does not fullfill neccessary criteria to be a spy")
return len(friend_name)
