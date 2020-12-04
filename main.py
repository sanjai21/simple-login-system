import json #json used to read the database
db = json.load(open("db.txt" , 'r')) #opening the database using json in reading mode
#creating a class to convert the dictionary from single quotes to double qoutes
#bcz in json strings start with double quotes
class db_dict(dict):
        def __str__(self):
            return json.dumps(self)
ask_username = input("Enter your username : \t")
if ask_username  in db:
    ask_password =  input("Enter you password : \t")
    while ask_password not in db[ask_username]:
        print("Login Unsuccessfull :(")
        ask_password = input("The password you enterd is not correct try again: \t ")
    while ask_password in db[ask_username]:
        print("Login Successfull !!! ")
        break        
else:   
    query =  input("Looks like you dont have a account wish to create one now ? (y/n): \t")
    while query == 'n':
        break
    if query == 'y':
        new_username = input("Enter your username : \t")
        while new_username in db: #looping until we get a unique username
            new_username = input("This username is already taken choose different one :")
        while new_username not in db:
            new_password = input("Enter a password for your account :\t")
            db[new_username] = new_password
            print("Account created Successfully !!!")
            new_db =  db_dict(db) #storing the entire database in the variable 
            with open("db.txt" , 'w' ) as k:
                k.write(str(new_db))#writing the updated database 
                k.close()


