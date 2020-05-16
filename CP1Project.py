#CPSC1301 Project: MovingTool
#Created by: Paul B Thorne $ LaCretia Murry

#lists apartments within a 5-mile radius from CSU Main Campus.
def apartmentFinder(file1):
    newList1=[]
    for line in file1:
        newList1.append(line)
    for i in newList1:
        print(i,end="")
#lists shopping centers within a 5-mile radius from CSU Main Campus.
def shopFinder(file2):
    newList2=[]
    for line in file2:
        newList2.append(line)
    for i in newList2:
        print(i,end="")
#lists churches within a 5-mile radius from CSU Main Campus.
def churchFinder(file3):
    newList3=[]
    for line in file3:
        newList3.append(line)
    for i in newList3:
        print(i,end="")










#Prints user options
def printMenu(file1,file2,file3):
    user_choice=""
    while user_choice!="4":
        user_choice=input("Please select from the following list: \n1. Apartments near campus\n2. Shopping centers near campus\n3. Churches near campus\n4. Quit\n")
        if user_choice=="1":
            apartmentFinder(file1)
        elif user_choice=="2":
            shopFinder(file2)
        elif user_choice=="3":
            churchFinder(file3)
        elif user_choice=="4":
            print ("Goodbye and thank you for using MovingTool!!")
        else:
            print("Invalid choice. Choose again.\n")
                
#initiates program; opens files.
def main():
    file1=open("apartments.txt","r")
    file2=open("shopping.txt.","r")
    file3=open("churches.txt.","r") 
    print("Hello and thank you for using MovingTool!\n")
    print ("MovingTool assists new CSU students settle into their new environment with no stress and no worries!")
    printMenu(file1,file2,file3)
main()
