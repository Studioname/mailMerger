#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt

with open("./Input/Names/invited_names.txt") as list_of_names:

    list = list_of_names.readlines()
    for name in list:
        name = name.strip("\n")
        with open("./Input/Letters/starting_letter.txt") as starting_letter:
            data = starting_letter.read()
            data = data.replace("[name]", name)
            print(starting_letter)
        with open("./Output/ReadyToSend/Letter_To_" + name, "w") as letter:
            letter.write(data)









#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp