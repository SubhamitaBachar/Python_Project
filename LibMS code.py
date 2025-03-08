import random
import pandas as pd
import pymysql
import string
db_con=pymysql.connect(host="localhost",user="root",password="your password",db="lms")


def issueb():
    sname=input("Enter student name: ")
    sid=input("Enter student ID: ")
    dept=input("Enter department: ")
    year= input("Enter year: ")
    bid= input("Enter book ID : ")
    bname=input("Enter book name: ")
    author_name= input("Enter author name of the book: ")
    issue_date= input("Enter issued date: ")
    sql= "insert into issue_book values(%s,%s,%s,%s,%s,%s,%s,%s)"
    data=(sname,sid,dept,year,bid,bname,author_name,issue_date)
    cursor=db_con.cursor()
    cursor.execute(sql,data)
    db_con.commit()
    print("Book issued to : ",sname)
    main()



def depositb():
    sname=input("Enter student name: ")
    sid=input("Enter student ID: ")
    dept=input("Enter department: ")
    year= input("Enter year: ")
    bid= input("Enter book ID : ")
    bname=input("Enter book name: ")
    author_name= input("Enter author name of the book: ")
    deposit_date= input("Enter deposited date: ")
    sql= "insert into submit_book values(%s,%s,%s,%s,%s,%s,%s,%s)"
    data=(sname,sid,dept,year,bid,bname,author_name,deposit_date)
    cursor=db_con.cursor()
    cursor.execute(sql,data)
    db_con.commit()
    print("Book deposited from : ",sname)
    main()


def newstudent():
    sid = input("Enter student ID: ")
    sname = input("Enter student name: ")
    gender = input("Enter gender: ")
    age = input("Enter AGE: ")
    contact = input("Enter contact details: ")
    dept = input("Enter department: ")
    year = input("Enter year: ")

    sql = "insert into  students values(%s,%s,%s,%s,%s,%s,%s)"
    data=(sid,sname,gender,age,contact,dept,year)
    cursor = db_con.cursor()
    cursor.execute(sql, data)
    db_con.commit()
    print("Student Registered Successfully")
    main()


def DispSRecord():
    st1="show columns from students;"
    cursor=db_con.cursor()
    cursor.execute(st1)
    result1=cursor.fetchall()
    cols=[]
    for row in result1:
        cols.append(row[0])
    print(cols)
    st2 = "select * from students"
    cursor = db_con.cursor()
    cursor.execute(st2)
    result2 = cursor.fetchall()
    for row in result2:
        print(row)
    main()


def Slogin():
    while True:
        verify_userid= input("Enter userid : ")
        verify_username=input("Enter username in capital letters: ")
    
        st1="select sid,sname from students;"
        cursor1 = db_con.cursor()
        cursor1.execute(st1)
        result1 = cursor1.fetchall()
    
        s_info=dict(result1)
    
        for k,v in s_info.items():
            if k == verify_userid and v == verify_username:
                print("Enter Your Password Below")
    
        verify_pswrd = input("Enter password: ")
    
        password = verify_userid+str('@1234')
        if verify_pswrd == password:
                print("STUDENT DETAILS: ")
                st3=f"select * from students where sid='{verify_userid}';"
                cursor3 = db_con.cursor()
                cursor3.execute(st3)
                result3 = cursor3.fetchone()
                print(result3)
        elif verify_pswrd!=password:
            print("Wrong password...")
            break
        main()


def modifyRecord():
    while True:
            verify_userid = input("Enter userid : ")
            verify_username = input("Enter username in capital letters: ")
    
            st1 = "select sid,sname from students;"
            cursor1 = db_con.cursor()
            cursor1.execute(st1)
            result1 = cursor1.fetchall()
    
            s_info = dict(result1)
    
            for k, v in s_info.items():
                if k == verify_userid and v == verify_username:
                    print("Enter Your Password Below")
    
            verify_pswrd = input("Enter password: ")
    
            password = verify_userid + str('@1234')
            if verify_pswrd == password:
                print("Modify your necessary details ")
                sid=verify_userid
                age = input("Enter AGE: ")
                contact = input("Enter contact details: ")
                dept = input("Enter department: ")
                sql = "update students set age=%s, contact=%s, dept=%s where sid=sid;"
                data = (age, contact, dept)
                cursor = db_con.cursor()
                cursor.execute(sql, data)
                db_con.commit()
                print("Student details modified successfully")
            elif verify_pswrd != password:
                print("Wrong password...")
            main()

def DelStudentRec():
    print("Librarian Login")
    while True:
        verify_userid = input("Enter userid : ")
        verify_username = input("Enter username in capital letters: ")
    
        st1 = "select lid,name from librarian;"
        cursor1 = db_con.cursor()
        cursor1.execute(st1)
        result1 = cursor1.fetchall()
    
        l_info = dict(result1)
    
        for k, v in l_info.items():
            if k == verify_userid and v == verify_username:
                print("Enter Your Password Below")
    
        verify_pswrd = input("Enter password: ")
    
        password = verify_userid + str('#1234')
        if verify_pswrd == password:
            sid=input("Enter student ID to delete: ")
            st3 = f"delete from students where sid='{sid}';"
            cursor3 = db_con.cursor()
            cursor3.execute(st3)
            result3 = cursor3.fetchone()
            print(result3)
        elif verify_pswrd != password:
            print("Wrong password...")
            break
        main()


def newBook():
    bid = input("Enter book ID: ")
    bname = input("Enter book name: ")
    author_name = input("Enter author name: ")
    availability= input("Enter availability (yes/no): ")
    copies=input("Enter copies available: ")
    sql = "insert into books details(%s,%s,%s,%s,%s)"
    data = (bid, bname, author_name, availability, copies)
    cursor = db_con.cursor()
    cursor.execute(sql, data)
    db_con.commit()
    print("New Book Created Successfully")
    main()


def DispBooks():

    st1="show columns from books;"
    cursor=db_con.cursor()
    cursor.execute(st1)
    result1=cursor.fetchall()
    cols=[]
    for row in result1:
        cols.append(row[0])


    st2 = "select * from books;"
    cursor = db_con.cursor()
    cursor.execute(st2)
    result2 = cursor.fetchall()
    for row in result2:
        print(row)
    main()


def SpecificBook():
    while True:
        bid = input("Enter book id : ")
        bname = input("Enter book name in capital letters: ")

        st1 = f"select * from books where bid='{bid}' and bname='{bname}';"
        cursor1 = db_con.cursor()
        cursor1.execute(st1)
        result1 = cursor1.fetchall()
        print(result1)
        main()

def modifybooks():
    while True:
        verify_bid = input("Enter book ID for which you want to modify: ")
        print("Librarian Login")
        verify_userid = input("Enter userid : ")
        verify_username = input("Enter username in capital letters: ")

        st1 = "select lid,name from librarian;"
        cursor1 = db_con.cursor()
        cursor1.execute(st1)
        result1 = cursor1.fetchall()

        l_info = dict(result1)

        for k, v in l_info.items():
            if k == verify_userid and v == verify_username:
                print("Enter Your Password Below")

        verify_pswrd = input("Enter password: ")

        password = verify_userid + str('#1234')

        if verify_pswrd == password:

            bid=verify_bid
            print("Modify your necessary details ")
            author_name = input("Enter author name: ")
            availability = input("Enter availability (yes/no): ")
            copies = input("Enter copies available: ")
            sql = "update books set author_name=%s, availability=%s, copies=%s where bid=%s;"
            data = ( author_name, availability, copies, bid)
            cursor = db_con.cursor()
            cursor.execute(sql, data)
            db_con.commit()
            print("Book Details Modified Successfully")
        elif verify_pswrd != password:
                print("Wrong password...")
        main()



def DeleteBookrecord():
    print("Librarian Login")
    while True:
        verify_userid = input("Enter userid : ")
        verify_username = input("Enter username in capital letters: ")

        st1 = "select lid,name from librarian;"
        cursor1 = db_con.cursor()
        cursor1.execute(st1)
        result1 = cursor1.fetchall()

        l_info = dict(result1)

        for k, v in l_info.items():
            if k == verify_userid and v == verify_username:
                print("Enter Your Password Below")

        verify_pswrd = input("Enter password: ")

        password = verify_userid + str('#1234')
        if verify_pswrd == password:
            bid = input("Enter book ID to delete: ")
            st3 = f"delete from books where bid='{bid}';"
            cursor3 = db_con.cursor()
            cursor3.execute(st3)
            result3 = cursor3.fetchone()
            print(result3)
        elif verify_pswrd != password:
            print("Wrong password...")
            break
        main()



def main():
    print("""      LIBRARY MANAGEMENT SYSTEM      
    1. BOOK ISSUE
    2. BOOK DEPOSIT
    3. ADMINISTRATION MENU
    4. EXIT
    """)
    choice1= input("Enter your choice no.: ")
    print("________________________________")
    if choice1=='1':
        issueb()
    elif choice1=='2':
        depositb()
    elif choice1=='3':
        print("""     CHOOSE FROM THE FOLLOWING     
        1. CREATE STUDENT RECORD
        2. DISPLAY ALL STUDENTS RECORD
        3. DISPLAY SPECIFIC STUDENT RECORD
        4. MODIFY STUDENT RECORD
        5. DELETE STUDENT RECORD
        6. CREATE BOOK
        7. DISPLAY ALL BOOKS
        8. DISPLAY SPECIFIC BOOK
        9. MODIFY BOOK
        10.DELETE BOOK RECORD
        """)
        choice2= input("Enter your choice no.: ")
        if choice2=='1':
            newstudent()
        elif choice2=='2':
            DispSRecord()
        elif choice2=='3':
            Slogin()
        elif choice2=='4':
            modifyRecord()
        elif choice2=='5':
            DelStudentRec()
        elif choice2=='6':
            newBook()
        elif choice2== '7':
            DispBooks()
        elif choice2=='8':
            SpecificBook()
        elif choice2=='9':
            modifybooks()
        elif choice2=='10':
            DeleteBookrecord()
    elif choice1=='4':
        exit()
    else:
        print("Wrong Choice")
main()






db_con.close()



