# Q1/ Write a method that will remove any given character from a string.

input_str = "DivasDwivedi"
   
# Printing original string  
print ("Original string: " + input_str) 
removed_character=''
result_str = '' 
   
for i in range(0, len(input_str)): 
    if i != 3: 
        result_str = result_str + input_str[i] 

    if i==3:
        removed_character=removed_character+input_str[i]
   
# Printing string after removal   
print ("String after removal of 'i'th character : " + result_str)
print("removed character is: "+removed_character)