from pymongo import MongoClient
from colorama import init
from termcolor import colored


client=MongoClient("mongodb://localhost:27017/")
mydb=client["Visitors"]
visitors=mydb.visitors
Mydb=client["Doctors"]
doctors=Mydb.doctors
MYdb=client["Staffs"]
staffs=MYdb.staffs
MyDb=client["Patients"]
patients=MyDb.patients
b=1
while(b!=-1):
    print("1.Login as an Admin.")
    print("2.Login as an Doctor.")
    print("3.Login as Reception.")
    print("4.Login as Visitor.")
    choice=int(input("Enter your choice"))
    if(choice==1):
        n=input("Enter ID:")
        p=input("Enter Password:")
        if(n=="admin123" and p=="1234"):
            l=1
            while(l!=-1):
                print("1.Insert Doctors.")
                print("2.Insert Staffs.")
                print("3.Register Patients.")
                print("4.Search Doctors.")
                print("5.Search Patients.")
                print("6.Remove Doctor.")
                print("7.Remove Patients.")
                print("8.Remove Staff.")
                j=int(input("Enter your choice:"))

                def insert_doc():
                    r=int(input("Enter number of records:"))
                    for i in range(0,r):
                        Doctors=dict()
                        Doctors["_id"]=input("Enter Doctor's id:")
                        Doctors["Name"]=input("Enter Doctors's name:")
                        Doctors["Department"]=input("Enter Doctor's field:")
                        Doctors["Password"]="1234"
                        Doctors["Contact"]="To be entered by the doctor."
                        Doctors["Mail"]="To be enterd by the doctor."
                        Doctors["Confirmed_Appointments"]=[]
                        Doctors["Pending_Appointments"]=[]
                        Mydb.doctors.insert_one(Doctors)
                        print("Inserted Succesfully.")

                def insert_staff():
                    r=int(input("Enter number of records:"))
                    for i in range(0,r):
                        Staffs=dict()
                        Staffs["_id"]=input("Enter Staff id:")
                        Staffs["Name"]=input("Enter staff name:")
                        Staffs["Field"]=input("Enter position:")
                        Staffs["Password"]="1234"
                        Staffs["Contact"]="To be entered by the staff."
                        MYdb.staffs.insert_one(Staffs)
                    

                def register():
                    r=int(input("Enter number of records:"))
                    for i in range(0,r):
                        Patients=dict()
                        Patients["_id"]=input("Enter id:")
                        Patients["Name"]=input("Enter name:")
                        Patients["Department"]=input("Enter department:")
                        Patients["Ward"]=input("Enter ward:")
                        Patients["Age"]=int(input("Enter age:"))
                        Patients["contact"]=input("Contact Number:")
                        Patients["Doctor"]=input("To be supervised by doctor:")
                        MyDb.patients.insert_one(Patients)

                def search_doc():
                    print("1.Search Departments.")
                    print("2.Search Doctors.")
                    print("3.Search through id.")
                    k=int(input("Enter choice:"))
                    if(k==1):
                        dep=input("Enter the Department:")
                        query={"Department":dep}

                        for doctor in doctors.find(query):
                            print(doctor)



                    if(k==2):
                        n=input("Doctor name:")
                        query={"Name":n}
                        for doctor in doctors.find(query):
                            print(doctor)
                        
                    if(k==3):
                        i=input("Enter id:")
                        query={"_id":i}
                        for doctor in doctors.find(query):
                            print(doctor)
                        

                def search_pat():

                    i=input("Enter ID:")
                    query={"_id":i}
                    for patient in patients.find(query):
                        print(patient)
                    

                def rem_doc():
                    i=input("Enter id of the doctor to be removed:")
                    query={"_id":i}
                    for doctor in doctors.find(query):
                        print(doctor)
                    sure=int(input("Are you sure you want to remove?Press 1 to continue"))
                    if(sure==1):
                        doctors.delete_one(query)
                        print("Deleted")
                    else:
                        print("cancelled")

                def rem_staff():
                    i=input("Enter id of the staff to be removed:")
                    query={"_id":i}
                    for staff in staffs.find(query):
                        print(staff)
                    sure=int(input("Are you sure you want to remove?Press 1 to continue"))
                    if(sure==1):
                        staffs.delete_one(query)
                        print("Deleted")
                    else:
                        print("cancelled")

                def rem_pat():
                    i=input("Enter id of the patient to be removed:")
                    query={"_id":i}
                    for patient in patients.find(query):
                        print(patient)
                    sure=int(input("Are you sure you want to remove?Press 1 to continue"))
                    if(sure==1):
                        patients.delete_one(query)
                        print("Deleted")
                    else:
                        print("cancelled")

                if(j==1):
                    insert_doc()
                if(j==2):
                    insert_staff()
                if(j==3):
                    register()
                if(j==4):
                    search_doc()
                if(j==5):
                    search_pat()
                if(j==6):
                    rem_doc()
                if(j==7):
                    rem_staff()
                if(j==8):
                    rem_pat()

                l=int(input("Enter -1 to exit as an admin"))

    if(choice==2):
        n=input("Enter your id:")
        p=input("Enter your password:")
        query={"_id":n}
        for doctor in doctors.find(query):
            if(p==doctor["Password"]):
                l=1
                while(l!=-1):
                    print("Welcome "+doctor["Name"])
                    print("1.Update your account")
                    print("2.Check apointments")
                    print("3.Manage appointments")
                    print("4.Search patients")
                    c=int(input("Enter your choice"))

                    def update():
                        pa=input("Enter your new password")
                        email=input("Enter your valid mail id:")
                        contact=input("Enter your contact number:")
                        doctors.update_many({"_id":n},{"$set":{"Password":pa,"Mail":email,"Contact":contact}})

                    def check():
                        for doctor in doctors.find(query,{"_id":0,"Password":0,"Name":0,"Department":0,"Mail":0,"Contact":0,"Pending_Appointments":0}):
                            print(doctor)

                    def manage():
                        for doctor in doctors.find(query):
                            for i in doctor["Pending_Appointments"]:
                                print(i)
                                k=int(input("Press 1 if you want to confirm appointment. Else press 0"))
                                if(k==1):
                                    doctor["Confirmed_Appointments"].append(i)
                                    doctor["Pending_Appointments"].remove(i)
                                    _query={"_id":i[0]}
                                    for visitor in visitors.find(_query):
                                        new_query={"$set":{"Message":"Your appointment is booked"}}
                                        visitors.update_many(_query,new_query)
                                else:
                                    doctor["Pending_Appointments"].remove(i)
                                    _query={"_id":i[0]}
                                    for visitor in visitors.find(_query):
                                        new_query={"$set":{"Message":"Sorry,the doctor is unavailable."}}
                                        visitors.update_many(_query,new_query)

                            newquery={"$set":{"Confirmed_Appointments":doctor["Confirmed_Appointments"],"Pending_Appointments":doctor["Pending_Appointments"]}}
                            doctors.update_many(query,newquery)

                    def search():
                        new_query={"Doctor":doctor["Name"],"Department":doctor["Department"]}
                        for patient in patients.find(new_query,{"Doctor":0}):
                            print(patient)

                    if(c==1):
                        update()

                    if(c==2):
                        check()

                    if(c==3):
                        manage()

                    if(c==4):
                        search()

                    l=int(input("Press -1 to exit"))
                
                                
                
                        
                        
                        
                        
    if(choice==3):
        n=input("Enter id:")
        p=input("Enter password:")
        query={"_id":n}
        for staff in staffs.find(query):
            if(p==staff["Password"]):
                l=1
                while(l!=-1):
                    print("1.Search Patients")
                    print("2.List all Patients")
                    k=int(input("Enter choice:"))
                    def search():
                        _id=input("Enter ID:")
                        _query={"_id":_id}
                        for patient in patients.find(_query):
                            print(patient)

                    def search_all():
                        for patient in patients.find({}):
                            print(patient)

                    if(k==1):
                        search()

                    if(k==2):
                        search_all()

                    l=int(input("Enter -1 to exit"))
                    
        
        
        
                
        
                        
                    
    
    if(choice==4):
        print('Welcome to XYZ Hospital.Our vission is to be an Ethical and Integrated SuperSpecialty Hospital Mission.To be amongst the Top Hospitals of our region Values.Patient First shall be the guiding philosophy - everytime by everyone.')
        print('*******More Information*****.')
        print('You can book your appointments here.')
        print("1.Sign In.")
        print("2.SIgn Up.")
        i=int(input("Enter your choice"))
        if(i==1):
            n=input("Enter user ID:")
            p=input("Enter your password:")
            query={"_id":n}
            for visitor in visitors.find(query):
                if(p==visitor["Password"]):
                    l=1
                    while(l!=-1):
                        print("1.Show details.")
                        print("2.Book an appointments")
                        print("3.Check your confirmation.")
                        k=int(input("Enter your choice"))
                        def show():
                            print("**** Details *****")
                            print(''' Department
                                        1. Anesthiology
                                        2. Dermatology
                                        3.General surgery
                                        4.Hematology
                                        ........''')
                            print("Contact Details")
                            print("Rate details.")

                        def book():
                            L=[]
                            date=input("Enter Date of appointment:")
                            day=input("Enter the day:")
                            time=input("Enter time:")
                            name=input("Enter name of the doctor")
                            L.append(n)
                            L.append(visitor["Name"])
                            L.append(date)
                            L.append(day)
                            L.append(time)
                            for doctor in doctors.find( { "Name": { "$regex":name } },{"Confirmed_Appointments":0,"Pending_Appointments":0} ):
                                print(doctor)
                                
                                ID=input("Enter the ID of the doctor you want to visit:")
                                
                                _query={"_id":ID}
                                for doctor in doctors.find(_query):
                                    doctor["Pending_Appointments"].append(L)
                                    doctors.update_many(_query,{"$set":{"Pending_Appointments":doctor["Pending_Appointments"]}})
                                    print("Request sent. Check your message section for reply.")
                        def check():
                            for visitor in visitors.find(query,{"_id":0,"Password":0,"Name":0,}):
                                print(visitor)

                        if(k==1):
                            show()

                        if(k==2):
                            book()

                        if(k==3):
                            check()

                        l=int(input("Enter -1 to exit"))

        if(i==2):
            Visitors=dict()
            Visitors["_id"]=input("Enter user name:")
            Visitors["Name"]=input("Enter name:")
            Visitors["Password"]=input("Set password:")
            Visitors["Message"]="None"
            mydb.visitors.insert_one(Visitors)
            print("Succesfully Registered.")
            
    b=int(input("Enter -1 to exit"))
                                
                            
        
