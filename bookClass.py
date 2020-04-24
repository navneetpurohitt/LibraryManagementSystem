from function import *
import sys
def BooksMain():
    while True:
        print("*"*50)
        print("1.>  Insert Book")
        print("2.>  Display Book List")
        print("3.>  Book Search")
        print("4.>  Book Issue")
        print("5.>  Book Return")
        print("6.>  Delete Book Record")
        print("7.>  Insert New Student")
        print("8.>  Display Student List")
        print("9.>  Student Search")
        print("10.> Delete Student Record")
        print("0> Exit\n")
        print("*" * 50)
        n = int(input("Enter Your Choice: "))
        if n==1:
            bookStore()
        elif n==2:
            displayBooks()
        elif n==3:
            bookSearch()
        elif n==4:
            bookIssue()
        elif n==5:
            bookReturn()
        elif n==6:
            bookDelete()
        elif n==7:
            inputStudent()
        elif n==8:
            displayStudent()
        elif n==9:
            studentSearch()
        elif n==10:
            studentDelete()
        elif n==0:
            sys.exit(0)
        else:
            print("Invalid Option")

BooksMain()