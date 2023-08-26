def divide_by (a,b):
    return a/b

#This will hanlde errors 
try:
    ans= divide_by(40,0)

    #the base class exeption is used to write all  built-in and assign it to e
except Exception as e:
    print("Something is wrong!", e)

    #To print the class of the exeption!
    print(e.__class__)

#another way of handling exceptions is with the specific exeption class
try: 
    ans = divide_by(40,1)
    #this specific exeption now has a customer message
except ZeroDivisionError as e:
    print(e, "we cannot divide by zero")

#but what if we dont get that exeption we want to print a general exeption message
except Exception as e:
    print(e,"something went wrong")

#FileNotFoundError

try: #The code that is executed needs to be inside the try 
    with open("file_none.txt", "r") as file:
        file.read()
except Exception as e:


#methods for reading
#read()  returns the entire contents of the file as a string tahtt will contain all the caracters 
 # readline(n) This method returns a single line with no arguments, with arguments it will determine the caracters of the line
 #  reads the entire content of the files and returns it in an ordered list

#Absolute paths, this includes all the information to access the file, a relavtive path includes only what wee need
with open("sample.txt", "r") as file:
    print(file.read())