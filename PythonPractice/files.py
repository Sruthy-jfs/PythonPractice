#my_file=open('test.txt')
#print(my_file.read())
#my_file.close()


#instead of manually calling close file we can use with statement

#with open ('test.txt') as myfile:
 #   print(myfile.readlines())


#by default it will be in read mode if not specified

#with open ('test.txt', mode='r') as myfile:
#    print(myfile.readlines())

#to read and write we need to give r+ but the cursor will write from starting of the file and override everythign that was present in the file earlier


# with open ('test.txt','r+') as myfile:
#     text2=myfile.write('heya')
#     myfile.seek(0)#to bring cursor to beginning of the file
#     print(myfile.read())


#a appends to the end of the line to prevent overrding

#
# with open ('test.txt','a') as my_file:
#    text2=my_file.write('with lomu and kukuddu')
#    print(my_file.readline())


#w can be used to write. it allows to write to file. It will override everything that was present existing
#or creates a new file


# with open ('test2.txt','w') as myfile:
#     text2=myfile.write('testing write fucntionality in python')



#file paths

#c:/user/sruthy/python/text.text
#./text.txt this tells to move forward from the current working directory
#.. tells to move backward from the current working directory

#pathlib library works with both windows and mac and takes file path for you based on your OS


#ERROR HANDLING

try:
    with open ('test3.txt','r') as myfile:
        print(myfile.read())
except FileNotFoundError as err:
    print('File not found')
    raise err

