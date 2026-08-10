# File Handling 

# open('file path', 'mode' )

# p = open (r'/Users/niteshkumar/Desktop/hello.txt.rtf')        # mode -- 'r' , reads the file content 
# print(p.read())

# p = open ('main.py')
# print(p.read())

r = open('superman.txt','w')        # mode  -- 'w' , overwrite the code 
r.write("Hello, i am Nitesh kumar and writing in the superman file ")
r.close()


r = open('superman.txt','a')        # mode  -- 'a' , add the content to the file at last 
r.write("and i am appending some text to the file ")
r.close()