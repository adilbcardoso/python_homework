# Write your code here.

#Task1
def hello():
    return("Hello!")

print (hello ())

#task2

def greet(name):
    return(f"Hello, {name}!")

print(greet("James"))


#Task3 

<<<<<<< HEAD
def calc (x, y, z = None):
    if not isinstance (x, (int, float)) or not isinstance (y, (int, float)): 
        return "You can't multiply those values!"
    if z == "divide":
        if y == 0:
            return "You can't divide by 0!"
        return x/y
    if z == "add":
        return x + y
    if z == "subtract":
        return x - y
    if z == "modulo":
        return x % y
    if z == "multiply":
        return x * y
    if z is None :
        return x * y
=======
def calc (x, y, z = "multiply"):
    try:   
        if z == "add":
            return x + y
        elif z == "subtract":
            return x - y
        elif z == "modulo":
            return x % y
        elif z == "multiply":
            return x * y
        elif z == "divide":
            return x/y
        elif z == "power":
            return x ** y
        else:
            return "Invalid operation!"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    
>>>>>>> main
    
print(calc(2,5,"add"))
print(calc(20,5,"divide"))
print(calc(14,2.0,"multiply"))
print(calc(12.6, 4.4, "subtract"))
print(calc(9,5, "modulo"))
print(calc(10,0,"divide"))
print(calc("first", "second", "multiply"))
print(calc(5,6))

#Task4
def data_type_conversion(value, name):

    conversation = {"int": int, "float": float, "str": str}
    if name in conversation:
        try:
            return conversation [name](value)
        except (TypeError, ValueError):
            return f"You can't convert {value} into a {name}."

print (data_type_conversion("casa", "int"))

#Task5

def grade (*args):
    
    for value in args:
        if not isinstance (value, (int, float)):
             return "Invalid data was provided."
        
    average = sum(args)/len(args)
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C" 
    elif average >= 60:
        return "D" 
    else:
<<<<<<< HEAD
        return "E"
=======
        return "F"
>>>>>>> main
    

        
print (grade(60,80,20))

#Task6

def repeat(value, count):
    i = 0 
    result = ""
    for i in range (count):
        result = result + value
    return result

print (repeat("up", 4))

#Task7

def student_scores(x, **kwargs):
    if x == "mean":
        return sum(kwargs.values())/ len(kwargs)
    if x == "best":
        return max(kwargs,key= kwargs.get)
    
        
    
print(student_scores("best", Tom=75, Dick=89, Angela=91))

#Task8

def titleize(string):
    little_words = ["a", "on", "an", "the", "of", "and", "is"]
    words = string.split()
    for i in range(len(words)):
        
        if i == 0 or i == len(words) - 1:
            words[i] = words[i].capitalize()
       
        elif words[i].lower() in little_words:
            words[i] = words[i].lower()
        else:
            words[i] = words[i].capitalize()

    return " ".join(words)

print(titleize("After On"))

#Task9

def hangman(secret, guess):
    secret_incomplete = ""
    for letter in secret:
        if letter in guess :
            secret_incomplete = secret_incomplete + letter
        else:
            secret_incomplete = secret_incomplete + "_"
    
    return secret_incomplete

print (hangman("difficulty","ic"))



#Task10

def pig_latin(text): 
    words = text.split()
    vowel = ("a","e","i","o","u")
    result = []

    for word in words:
        if word[0] in vowel:
            result.append(word + "ay")
        elif word.startswith("qu"):
            result.append(word[2:] + "qu" + "ay")

        else: 
            for i in range (len(word)):
                if word[i:i+2] == "qu":
                  result.append(word[i+2:] + word[:i+2]  + "ay")
                  break  
                if word[i] in vowel:
                    result.append(word[i:] + word[:i] + "ay")
                    break
            else: 
                result.append(word + "ay")


    return " ".join(result)
                      
    
print(pig_latin("apple"))
print(pig_latin("banana"))
print(pig_latin("cherry"))
print(pig_latin("the quick brown fox"))

print(pig_latin("quiet"))
print(pig_latin("square"))
