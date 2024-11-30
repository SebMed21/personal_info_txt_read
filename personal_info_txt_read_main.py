
#once again for the sake of simplicity and convinience I am using an array for the retry
retry_array = ["Y," "N"]
       
while True:
    #prompt the user for a name to search in the text file
    name_search = input("Please enter the name you are looking for here: ").strip()
    
    #open the text file
    with open("output.txt", "r") as output:
        #this reads all the lines
        lines = output.read()
        for i, line in enumerate(lines):
            # check if the name matches in lines that start with "Name:"
            if "Name:" in line and name_search.lower() in line.lower():
                #prints the name when found
                print(f"\nRecord found:\n{line.strip()}")
                #prints the birthday and age after the name
                print(lines[i + 1].strip())
                print(lines[i + 2].strip())
                break
        
        #if there is no no name found it will print this 
        else:
            print("Name not found. Please try again.")
            
            
                
        #this is what progresses the loop
      #  while not retry_input in retry_array:
       #     retry_input = input("Would you like to try more? ( Y / N ) : ")
            
        #if the user answers "N" the loop will stop
       # if retry_input in retry_array[1]: 
        #    break
            
#    break


        
        