file=open("file3.txt","w")
file.write("This is the first line\n This is the second line \n This is the third line \n this the fourthline")
file.close()
file=open("file3.txt","r")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()
with open("file3.txt","r") as file1:
    with open("filee4.txt","w") as file2:
        line_number=1
        for line in file1:
            if line_number % 2 != 0:
                file2.write(line)
            line_number += 1
print("odd lines written to filee4.txt:")
with open("filee4.txt","r")as file2:
    for line in file2:
        print(line.strip())