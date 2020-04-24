import getpass
import pickle
bList = []
sList = [] 
fList = []
issuebook=[]


class Books:
    def __init__(self, book_title='', book_author='', book_publication='', book_publication_year='', book_number=''):
        self.book_title = book_title
        self.book_author = book_author
        self.book_publication = book_publication
        self.book_publication_year = book_publication_year
        self.book_number = book_number
        
tb=Books()
        
class Student(Books):
    def __init__(self, username = '', enrollment = '', admissionYear = '', semester = '', branch = '', issueBook = '', booknumber = '', fine = ''):
        self.username = username
        self.enrollment = enrollment
        self.admissionYear = admissionYear
        self.semester = semester
        self.branch = branch
        self.issueBook = 0
        self.booknumber = []
        self.fine = 0

class Faculty(Books):
    def __init__(self, facultyname = '', department = '' , fissueBook = '', fbooknumber = '', ffine = ''):
        self.facultyname = facultyname
        self.department = department
        self.fissueBook = 0
        self.fbooknumber = []
        self.ffine = 0

        
def registration():
    username = input("Enter Your Name : ")
    password = getpass.getpass(prompt = "Enter New Password: ")
    f = open("registeredUser.txt", "a")
    f.write(username)
    f.write(" ")
    f.write(password)
    f.write("\n")
    f.close()
    
def displayUsers():
    f = open("registeredUser.txt", "r")
    for line in open("registeredUser.txt", "r").readlines():
        login_info = line.split()
        username = login_info[0]
        password = login_info[1]
        print(username, password)
    f.close()


#############################################################################################################

def Add_book():
    print("Enter New Book's Detail: ")
    with open('bookList.pkl', 'ab') as f:
        n = int(input("Enter Number of Books to be Entered: "))
        for x in range(n):
            book_title = input("Enter Book Title: ")
            book_author = input("Enter Author Name of %s Book: " % book_title)
            book_publication = input("Enter Publication of %s Book: " % book_title)
            book_publication_year = input("Enter Publication Year of %s Book: " % book_title)
            book_number = input("Enter Book Number : ")
            bObj=Books(book_title, book_author, book_publication, book_publication_year, book_number)
            bList.append(bObj)
        pickle.dump(bList,f)
        print("Record updated successfully")
    f.close()

#############################################################################################################


def bookDelete():
    obj = None
    with open('bookList.pkl','rb') as f:
        n = input("Enter Books Name to be Removed: ")
        while (1):
            try:
                obj = pickle.load(f)
                for i in obj:
                    print(i.book_title)
                    if i.book_title == n:
                        obj.remove(i)
            except EOFError:
                print("Book Removed")
                break
    with open("bookList.pkl", "wb") as f:
        pickle.dump(obj, f)
    f.close()

#############################################################################################################


def displayBooks():
    with open('bookList.pkl','rb') as f:
        while (1):
            try:
                obj = pickle.load(f)
                for i in obj:
                    print(i.book_title, i.book_author, i.book_publication, i.book_publication_year, i.book_number)
            except EOFError:
                print("\n")
                break
    f.close()

#############################################################################################################


def bookSearch():
    print("*"*50)
    print("\t\t\tSearch Book Panel\t\t\t")
    print("*" * 50)
    s=input("Enter Book Name Search your Book: ")
    with open('bookList.pkl','rb') as f:
        while (1):
            try:
                obj = pickle.load(f)
                for i in obj:
                    if s == i.book_title:
                        print(i.book_title, i.book_author, i.book_publication, i.book_publication_year, i.book_number)
                        print("\n")
                else:
                        print("Not Found !!")
            except EOFError:
                break
    f.close()

#############################################################################################################


#def bookIssue():
#    print("*" * 50)
#    print("\t\t\tBook Issue Panel\t\t\t")
#    print("*" * 50)
#    s = input("Enter Book Name to be Issued: ")
#    with open('bookList.pkl', 'rb') as f:
#        while (1):
#            try:
#                obj = pickle.load(f)
#                for i in obj:
#                    if s == i.book_title:
#                        print("\n")
#                        i.book_copies=str(int(i.book_copies)-1)
#                        print("Book Issued")
#                    else:
#                        print("Book is not Available")
#                        #break
#            except EOFError:
#                print("Book Details Updated")
#                break
#    with open('bookList.pkl', 'wb') as f:
#        pickle.dump(obj, f)
#    f.close()

def issue_st():
    En=input("Enter Your Enrollment Number : ")
    with open('studentList.pkl','rb') as f:
        with open('bookList.pkl', 'rb') as f1:
                sobj = pickle.load(f)
                bobj = pickle.load(f1)
                for i in sobj:
                    if i.enrollment == En:
                        if i.issueBook == 10:
                            print("You Issued Miximum Books")
                            break
                        else:    
                            s = input("Enter Book Number Which You want to Issu : ")
                            for j in bobj:
                                if s == j.book_number:
                                    i.issueBook += 1
                                    i.booknumber.append(s)
                                    tb = (j.book_title, j.book_author, j.book_publication, jbook_publication_year, jbook_number)
                                    bobj.remove(j)
                                    print("Book Issued Successfull.")
                                else:
                                    print("Enter Book Are Not Awalabe !! ")
                                    tb=None
                                    break
    
                        with open("studentList.pkl", "wb") as f:
                            pickle.dump(sobj,f)
                        with open('bookList.pkl', 'wb') as f1:    
                            pickle.dump(bobj,f1)
                        with open('issubookList.pkl', 'ab') as f2:
                            pickle.dump(tb,f2)
                        f2.close()    
                        f.close()
                        f1.close()
                                            
                    else:
                        print("Student Not Find")
def issue_f():
    En=input("Enter Your Name : ")
    with open('facultyList.pkl','rb') as f:
        with open('bookList.pkl', 'rb') as f1:
                sobj = pickle.load(f)
                bobj = pickle.load(f1)
                for i in sobj:
                    if i.facultyname == En:
                        if i.issueBook == 10:
                            print("You Issued Miximum Books")
                            break
                        else:    
                            s = input("Enter Book Number Which You want to Issu : ")
                            for j in bobj:
                                if s == j.book_number:
                                    i.issueBook += 1
                                    i.booknumber.append(s)
                                    tb = (j.book_title, j.book_author, j.book_publication, jbook_publication_year, jbook_number)
                                    bobj.remove(j)
                                    print("Book Issued Successfull.")
                                else:
                                    print("Enter Book Are Not Awalabe !! ")
                                    tb=None
                                    break
    
                        with open("facultyList.pkl", "wb") as f:
                            pickle.dump(sobj,f)
                        with open('bookList.pkl', 'wb') as f1:    
                            pickle.dump(bobj,f1)
                        with open('issubookList.pkl', 'ab') as f2:
                            pickle.dump(tb,f2)
                        f2.close()    
                        f.close()
                        f1.close()
                                            
                    else:
                        print("Faculty Not Find")



def issue():
    while(True):
        print("1 for Faculty")
        print("2 for student")
        print("3 for exit")
        c=input()
        if c=='1':
            issue_st()
        elif c=='2':
            issue_f()
        elif c=='3':
            break

################################################################################################################


#def bookReturn():
#    print("*" * 50)
#    print("\t\t\tBook Return Panel\t\t\t")
#    print("*" * 50)
#    s = input("Enter Book Name to be returned : ")
#    with open('bookList.pkl', 'rb') as f:
#        while (1):
#            try:
#                obj = pickle.load(f)
#                for i in obj:
#                    if s == i.book_title:
#                        print("\n")
#                        i.book_copies = str(int(i.book_copies) + 1)
#                        print("Book Returned")
#                    else:
#                        print("Book is not Available")
#                        # break
#            except EOFError:
#                print("Book Details Updated")
#                break
#    with open('bookList.pkl', 'wb') as f:
#        pickle.dump(obj, f)
#    f.close()

def ST_bookReturn():
    print("*" * 50)
    print("\t\t\tBook Return Panel\t\t\t")
    print("*" * 50)
    s = input("Enter Book Number : ")
    En = input("Enter Your Enrollment Number : ")
    with open('studentList.pkl','rb') as f:
        sobj = pickle.load(f)
        for i in sobj:
            if i.enrollment == En:
                if s == i.book_number:
                    i.issueBook -= 1
                    i.booknumber.append(0)
                    print("Book Return Succesfully !!!")
                else:
                    print("The Book Not Issue You !!")
    with open('studentList.pkl','ab') as f:
        pickle.dump(bobj, f)
    f.close()
    
    with open('bookList.pkl', 'ab') as f:
        with open('issubookList', 'rb') as f1:
            bobj = pickle.load(f)
            issobj = pickle.load(f1)
            for i in issobj:
                if s == i.book_number:
                    bobj = (i.book_title, i.book_author, i.book_publication, i.book_publication_year, i.book_number)
            for i in issobj:
                if s == i.book_number:
                    bobj.remove(j)
    with open('bookList.pkl', 'wb') as f1:    
        pickle.dump(bobj,f1)
    with open('issubookList.pkl', 'ab') as f2:
        pickle.dump(tb,f2)
    f2.close()    
    f1.close() 

    
def F_bookReturn():
    print("*" * 50)
    print("\t\t\tBook Return Panel\t\t\t")
    print("*" * 50)
    s = input("Enter Book Number : ")
    En = input("Enter Your Namw : ")
    with open('facultyList.pkl','rb') as f:
        sobj = pickle.load(f)
        for i in sobj:
            if i.enrollment == En:
                if s == i.book_number:
                    i.issueBook -= 1
                    i.booknumber.append(0)
                    print("Book Return Succesfully !!!")
                else:
                    print("The Book Not Issue You !!")
    with open('facultyList.pkl','ab') as f:
        pickle.dump(bobj, f)
    f.close()
    
    with open('bookList.pkl', 'ab') as f:
        with open('issubookList', 'rb') as f1:
            bobj = pickle.load(f)
            issobj = pickle.load(f1)
            for i in issobj:
                if s == i.book_number:
                    bobj = (i.book_title, i.book_author, i.book_publication, i.book_publication_year, i.book_number)
            for i in issobj:
                if s == i.book_number:
                    bobj.remove(j)
    with open('bookList.pkl', 'wb') as f1:    
        pickle.dump(bobj,f1)
    with open('issubookList.pkl', 'ab') as f2:
        pickle.dump(tb,f2)
    f2.close()    
    f1.close() 

    
def bookReturn():
    while(True):
        print("1 for Faculty")
        print("2 for student")
        print("3 for exit")
        c=input()
        if c=='1':
            F_bookReturn()
        elif c=='2':
            ST_bookReturn()
        elif c=='3':
            break
    
    
    
################################################################################################################

def inputStudent():
    print("Enter New Student's Detail: ")
    with open('studentList.pkl', 'ab') as f:
        s = 1
        for x in range(s):
            username = input("Enter Student Name: ")
            enrollment = input("Enter Enrollment Number of %s: " % username)
            admissionYear = input("Enter admission year of %s : " % username)
            semester = input("Enter semester of %s: " % username)
            branch = input("Enter branch of %s: " % username)
            issueBook = input("Enter Issue Books of %s: " % username)
            booknumber = input("Enter Book Number of %s: " % username)
            fine = input("Enter Book Fine of %s: " % username)
            sObj=Student(username, enrollment, admissionYear , semester, branch , issueBook , booknumber , fine )
            sList.append(sObj)
        pickle.dump(sList,f)
        print("Record updated successfully")
    f.close()

        
def studentDelete():
    obj = None
    with open('studentList.pkl','rb') as f:
        q = input("Enter Student's enrollment number to be Removed: ")
        while (1):
            try:
                obj = pickle.load(f)
                for i in obj:
                    #print(i.enrollment)
                    if i.enrollment == q:
                        obj.remove(i)
            except EOFError:
                print("Student Data Removed")
                break
    with open("studentList.pkl", "wb") as f:
        pickle.dump(obj, f)
    f.close()
        
def displayStudent():
    with open('studentList.pkl','rb') as f:
        while (1):
            try:
                obj = pickle.load(f)
                for i in obj:
                    print("Name of Student : ", i.username)
                    print("Entolment No : ", i.enrollment)
                    print("Admission Year : ", i.admissionYear) 
                    print("Semester : ", i.semester)
                    print("Branch : ", i.branch)
                    print("Issued Books : ", i.issueBook)
                    print("Book Number : ", i.booknumber)
                    print("Fine : ",i.fine)
            except EOFError:
                print("\n")
                break
    f.close()
                
def studentSearch():
    print("*"*50)
    print("\t\t\tSearch Student Panel\t\t\t")
    print("*" * 50)
    s=input("Enter Enlloment Name: ")
    with open('studentList.pkl','rb') as f:
        while (1):
            try:
                obj = pickle.load(f)
                for i in obj:
                    if s == i.enrollment:
                        print(i.username, i.enrollment, i.admissionYear, i.semester, i.branch, i.issueBook, i.booknumber, i.fine)
                        print("\n")
                    else:
                        print("Not Found !!")
            except EOFError:
                break
                
    f.close()
    
######################################################################################################################################


#Faculty

def inputFaculty():
    print("Enter New Faculty's Detail: ")
    with open('facultyList.pkl', 'ab') as f:
        s = 1
        for x in range(s):
            facultyname = input("Enter Faculty Name: ")
            department = input("Enter Department of %s: " % facultyname)
            fissueBook = input("Enter Number of Issued Books of %s: " % facultyname)
            fbooknumber = input("Enter Book Number of %s: " % facultyname)
            ffine = input("Enter Fine of %s: " % facultyname)
            fObj=Faculty(facultyname, department, fissueBook, fbooknumber, ffine)
            fList.append(fObj)
        pickle.dump(fList,f)
        print("Record updated successfully")
    f.close()

        
def facultyDelete():
    obj = None
    with open('facultyList.pkl','rb') as f1:
        q = input("Enter Faculty Name to be Removed: ")
        while (1):
            try:
                obj = pickle.load(f1)
                for i in obj:
                    #print(i.enrollment)
                    if i.facultyname == q:
                        obj.remove(i)
            except EOFError:
                print("Faculty Data Removed")
                break
    with open("facultyList.pkl", "wb") as f1:
        pickle.dump(obj, f1)
    f1.close()
        
def displayFaculty():
    with open('facultyList.pkl','rb') as f1:
        while (1):
            try:
                obj = pickle.load(f1)
                for i in obj:
                    print("Name of Faculty : ", i.facultyname)
                    print("Department : ", i.department)
                    print("Number oF Issued Books : ",i.fissueBook)
                    print("Book Number : ",i.fbooknumber)
                    print("Books Fine: ",i.ffine)
            except EOFError:
                print("\n")
                break
    f1.close()
                
def facultySearch():
    print("*"*50)
    print("\t\t\tSearch Faculty Panel\t\t\t")
    print("*" * 50)
    s=input("Enter Faculty Name: ")
    with open('facultyList.pkl','rb') as f:
        while (1):
            try:
                obj = pickle.load(f)
                for i in obj:
                    if s == i.facultyname:
                        print("Name of Faculty : ", i.facultyname)
                        print("Department : ", i.department)
                        print("Number oF Issued Books : ",i.fissueBook)
                        print("Book Number : ",i.fbooknumber)
                        print("Books Fine: ",i.ffine)
                        print("\n")
                    else:
                        print("Not Found !!")
            except EOFError:
                break
                
    f.close()
    
##############################################################################################################    
 
 