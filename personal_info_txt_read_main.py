
#once again for the sake of simplicity and convinience I am using an array for the retry
retry_array = ["Y," "N"]

#opens the txt file
with open("output.txt", "r") as output:
   for line in output:
       line = line.strip()
       
       
while True:
    while True:
        
        #asks the user for a name to search in the txt file
        name_search = input("please enter the name you are looking for here: ").strip().lower()
        
         #this is what progresses the loop
        while not retry_input in retry_array:
            retry_input = input("Would you like to try more? ( Y / N ) : ")
            
        #if the user answers "N" the loop will stop
        if retry_input in retry_array[1]: 
            break
            
    break
        
        