with open("Practice_file_I-O.txt", "r") as f:
    data = f.read()   
new_data = data.replace("Parth" , "Zudo")
print ( new_data)

with open("Practice_file_I-O.txt","w") as f :
    f.write(new_data)

    with open("Practice_file_I-O.txt", "r") as f:
         data1 = f.read()   
         if(data1.find("which")):
             print("The word exist inside the file : ")
         else :
             print("No similar elemnt found : ")
