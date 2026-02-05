num1=10

def main():
    global num2
    num2=556
    print(num1)

main()
print(num2)


myfile=open("main.py","r")
file=myfile.read()
print(file)



myfile=open("sunny.txt","w")
file=myfile.write("Programming make life easy")
print(file)

