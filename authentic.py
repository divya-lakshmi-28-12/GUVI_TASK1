
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
regex1="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$"

def check(email):
    if(re.fullmatch(regex, email)):
        return 1

    else:
        return 0

def check_pwd(password):
    if(re.fullmatch(regex1,password)):
        return 1
    else:
        return 0

def register():
    db=open("database.txt","r")
    email=input("Create UserID/Email: ")    
    a=check(email)
    if a==1:
        print('Valid Email')
    else:
        print('Invalid Email,Please enter a valid email')
        register()
    password=input("Create password: ")
    password1=input("Confirm password: ")
    b=check_pwd(password)


    if password != password1:
        print("Password doesn't match")
        register()
    else:
        if len(password)<=5:
            print("Password too short,type more than 5 characters")
            register()
        elif len(password)>=16:
            print("Password length should be less than 16 characters")
            register()
        else:
            
            if b==1:
                print('Valid Password')
                db=open("database.txt","a")
                db.write(email+","+password+"\n")
                print("Successfully created")
            else:
                print("Password should contain minimum of one upper case,one lower case,one digit,one special character")
    





def login():
    db=open("database.txt","r")
    email=input("Enter Your Email: ")
    
    d=[]
    f=[]
    for i in db:
        a,b = i.split(",")
        b=b.strip()
        d.append(a)
        f.append(b)
    data =dict(zip(d, f))
    if email in d:
        print("Useraccount exists")
        

    else:
        print("Useraccount not exists Please register")
        register()

    password=input("Enter Your Password: ")
    if password in f:
            print("Password match")
            print("Login successfull")


    else:
        print("Password does not match")
        
        pwd=input("Try again: |  Forgot Password: ")
        if pwd=="Try again":
            login()

        else:
            for k,v in data.items():
                if email in k:
                    p=data[email]
                    print("Password is ",p)
                
        


def home():
    print("Please select an option")
    option=input("Login: | Register:")
    if option=="Login":
        login()
    else:
        register()


home()