from dbconfig import *
import datetime

def callAdmin():
    while True:
        
        print("1. Add Student")
        print("2. Add Technology")
        print("3. Add Question")
        print("4. View Results")
        print("5. Logout")

        ch = int(input("Enter your choice: "))
        if ch == 1:
            un = input("Enter Student Username: ")
            pd = input("Enter Password: ")
            nm = input("Enter Name: ")
            em = input("Enter Email: ")

            mycursor.execute("insert into user_profile(username,pwd,name,email,role) values ('{}', '{}','{}', '{}', 'student')".format(un,pd,nm,em))
            mydb.commit()
            print("Student Added!")
        elif ch == 2:
            try:
                tname = input("Enter Technology: ")
                mycursor.execute("insert into technology(tname) values ('{}') ".format(tname))
                mydb.commit()
                print("Technology Added!")
            except:
                print("Technology already exist!")
        elif ch == 3:
            mycursor.execute("select * from technology")
            all_tech = mycursor.fetchall() #((1, 'Python'), (2, 'Java'))
            for i in all_tech:
                print(i[0], i[1])
            techid = int(input("Select Technology ID: "))

            q = input("Enter Question: ")
            a = input("Enter Option A: ")
            b = input("Enter Option B: ")
            c = input("Enter Option C: ")
            d = input("Enter Option D: ")
            correct = input("Enter Correct (A/B/C/D): ")

            mycursor.execute("insert into questions(question,opta,optb,optc,optd,correct,techid) values ('{}','{}','{}','{}','{}','{}',{})".format(q,a,b,c,d,correct,techid))
            mydb.commit()
            print("Question Added!")            
            
        elif ch == 4:
            mycursor.execute("select * from result")
            res=mycursor.fetchall()
            for i in res:
                mycursor.execute("select NAME from user_profile where uid={}".format(i[1]))
                nm=mycursor.fetchone()
                mycursor.execute("select tname from technology where tid={}".format(i[2]))
                th=mycursor.fetchone()
                if i[5]==1:
                    print(i[0],nm[0],th[0],i[3],i[4],'pass')
                else:
                    print(i[0],nm[0],th[0],i[3],i[4],'fail')
                
        elif ch == 5:
            break

def callStudent(user_id):
    while True: 
        print("1. Start test")
        print("2. Results")
        print("3. Logout")

        ch = int(input("Enter your choice: "))
        if ch == 1:
            mycursor.execute("select * from technology")
            all_tech = mycursor.fetchall() #((1, 'Python'), (2, 'Java'))
            for i in all_tech:
                print(i[0], i[1])
            techid = int(input("Select Technology ID: "))

            mycursor.execute("select * from questions where techid={}".format(techid))
            questions = mycursor.fetchall() #((), (),)
            j = 1
            count = 0
            for i in questions:
                print("====****====")
                print(j, i[1])
                print("A.", i[2])
                print("B.", i[3])
                print("C.", i[4])
                print("D.", i[5])

                ans = input("Enter Answer (A/B/C/D): ")
                if ans == i[6]:
                    count = count + 1
                
                print("====****====")          
                j = j + 1

            per = (count/len(questions))*100
            print("Result: ", per, "%")
            st=1
            if per>=33:
                st=1
                print("Result: ",per,'%','Pass')
            elif per<33:
                st=0
                print("Result: ",per,'%','Fail')
                

                
                
            dt=datetime.date.today()
            mycursor.execute("insert into result (userid,techid,marks,resdate,sts) values({},{},{},'{}',{})".format(user_id,techid,per,dt,st))
            mydb.commit()

            #per, techid, user_id, sts, resdate
            
            
            
            
        elif ch == 2:
            mycursor.execute("select * from result where userid={}".format(user[0]))
            r=mycursor.fetchall()
            for i in r:
                print("result",i[3])
            #Task 3
        elif  ch == 3:
            break

while True:
    un = input("Enter UserName: ")
    pwd = input("Enter Password: ")

    mycursor.execute("select * from user_profile where username='{}' and pwd='{}'".format(un, pwd))
    user = mycursor.fetchone() #Tuple

    print("=======Welcome {}=======".format(user[3]))
    if user[5] == "admin":
        callAdmin()
    elif user[5] == "student":
        callStudent(user[0])



