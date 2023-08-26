

# Create a new file and write content to it
with open("new_file.txt", "w") as file:
    file.write("This is some content in the new file.")

# Access the file for reading
with open("new_file.txt", "r") as file:
    contents = file.read()
    print(contents)

import random
with open("petnames.txt","r") as f:
    f_content = f.read()
    #usually the content will be display as it is inside the file but with split it will create an array!
    f_content_list = f_content.split("\n")
    #The random.choice is imported from random
    print(random.choice(f_content_list))