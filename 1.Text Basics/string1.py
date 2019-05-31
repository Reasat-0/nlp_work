name = "Prantosss"

print(f"His name is {name}")


#Dictionary 

dictionary = { 'a': 123 , 'b':234}

print(f"My number is {dictionary['a']}")
      
#list 
      
li = [ 12 , 22, 31 ]
      
print(f"My list element is {li[0]}")
      
#list vast
      
showroom = [ ('Brand' , 'Model', 'Seats') , ('Ferrari' , 'F50', 122) , ('Mclearn' , 'F50', 122) , ('Mclearn' , 'F50', 122)] 
'''     
for allCars in showroom:
    print(allCars)
      
for allCars in showroom:
    print(f"Brand : {allCars[0]}")
'''
      
for var1 , var2, var3 in showroom:
    print(f"{var1:{20}} {var2:{10}} {var3:->{10}}")  #the var1:{10} this will take 10 charcter space after var1 and :<{10} will take 10 charctr space before var3