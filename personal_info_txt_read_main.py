while True:
    #prompt the user for a name to search in the text file
    name_search = input("\nPlease enter the name you are looking for here: ").strip()
    
    #open the text file
    with open("output.txt", "r") as output:
        #this reads all the lines
        lines = output.readlines()
        for i, line in enumerate(lines):
            # check if the name matches in lines that start with "Name:"
            if "Name:" in line: 
                if name_search.lower() in line.lower():
                    #prints the name when found
                    print(f"\nName found:\n{line.strip()}")
                    #prints the birthday and age after the name
                    print(lines[i + 1].strip())
                    print(lines[i + 2].strip())
                    break
                
            #if there is no no name found it will print this 
        else:
            print("Name not found. Please try again.")
        

        
        