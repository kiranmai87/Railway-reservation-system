#create data of users with usernames and passwords
#create data of trains and its numbers ,time,seat availability in all coaches 
#after selection of train display ticket fares 
# book ticket,update number of seats and print ticket
#cancel ticket,update number of seats and print ticket

from datetime import (date,datetime)
import random
# dictionary with numcer of user with paswords
users={"ramesh":"1234","suresh":"2345","ganesh":"3456","devi":"4567","kumar":"2349","kiran":"2012"}
# Nested dictionary with list of trains and information
trains_list={"Konark express":[123456,"06:45",{'1AC':[70,1000],'2AC':[150,750],'3AC':[200,500],'sleeper':[500,350]}],"East coast":[777250,"13:15",{'1AC':[70,1500],'2AC':[150,1050],'3AC':[200,750],'sleeper':[500,520]}],"Godavari express":[450346,"08:05",{'1AC':[70,1600],'2AC':[150,1150],'3AC':[200,700],'sleeper':[500,550]}],"Simhadri":[623456,"18:35",{'1AC':[70,1200],'2AC':[150,1050],'3AC':[200,800],'sleeper':[500,550]}]}
booking={}   # Dictionary to store all the bookings for all users

while True:
    username=input("Enter username: ")
    password=input("Enter your password: ")
    if username in users and password==users[username]:  # validating username and password
        print("Hello {} ,".format(username))
        print("Welcome to railway reservation portal")

    
        m=input("Continue your transaction? y or n: ")
        if m=="n":
            break
        elif m=='y':
            for k, v in trains_list.items():     # for loop to display all trains with train no. and time
                print(k,15*" ",v[0],15*" ",v[1])
            print('''

                Press 1 to check Availability
                Press 2 to Book ticket
                Press 3 to cancel ticket
                ''')
            n=input("Enter your option: ")   # input  from user for transaction
            if n=="1":
                train=input("Please enter train name: ")
                if train in trains_list:
                        print("Train number:",trains_list[train][0])
                        print("Train time:",trains_list[train][1])
                        print("Details",20*" ","1AC",20*" ","2AC",20*" ","3AC",20*" ","sleeper") 
                        print("Fare",24*" ",trains_list[train][2]['1AC'][1],20*" ",trains_list[train][2]['2AC'][1],20*" ",trains_list[train][2]['3AC'][1],20*" ",trains_list[train][2]['sleeper'][1])
                        print("seats available",11*" ",trains_list[train][2]['1AC'][0],20*" ",trains_list[train][2]['2AC'][0],20*" ",trains_list[train][2]['3AC'][0],20*" ",trains_list[train][2]['sleeper'][0])
                else:print("train not found")    
            elif n=='2':
                #input from user (train name, date)    
                train=input("Please enter train name: ")
                
                if train in trains_list:
                    print("Train number:",trains_list[train][0])
                    print("Train time:",trains_list[train][1])
                    print("Details",20*" ","1AC",20*" ","2AC",20*" ","3AC",20*" ","sleeper") 
                    print("Fare",22*" ",trains_list[train][2]['1AC'][1],20*" ",trains_list[train][2]['2AC'][1],20*" ",trains_list[train][2]['3AC'][1],20*" ",trains_list[train][2]['sleeper'][1])
                    print("seats available",12*" ",trains_list[train][2]['1AC'][0],20*" ",trains_list[train][2]['2AC'][0],20*" ",trains_list[train][2]['3AC'][0],20*" ",trains_list[train][2]['sleeper'][0])
                    coach=input("Select your coach:")
                    travel_date=int(input("Enter date of travel: "))
                    travel_month=int(input("enter month of travel: "))
                    journey_date=date(2023,travel_month,travel_date)
                    # if user selects 1AC
                    if coach=='1AC':  
                        list1=[]    #creste nested list for booking information                      
                        passengers=int(input("Enter number of passengers: "))  
                        if passengers <= trains_list[train][2]['1AC'][0]: 
                            for i in range(passengers):                                 
                                l1=[]                              
                                name=input("Enter passengers name: ")
                                age=int(input("Enter age: "))
                                l1.append(name)
                                l1.append(age)
                                l1.append(trains_list[train][2]['1AC'][1]) #gives fare for each ticket
                                l1.append(coach)
                                list1.append(l1) 
                                booking[username]=list1  #add the nested list to bookings dictionary                               
                        else:print('"Required number of seats not available"')                                                                                         
                        fare=passengers * trains_list[train][2]['1AC'][1]   #total cost of tickets                         
                        trains_list[train][2]['1AC'][0]-=passengers   #deducting number of seats from that coach                                                         
                        # print (booking) 
                #2AC  
                    elif coach=='2AC':   
                        list1=[]                         
                        passengers=int(input("Enter number of passengers: "))
                        if passengers <= trains_list[train][2]['2AC'][0]:
                            for i in range(passengers):
                                l1=[]
                                name=input("Enter passengers name: ")
                                age=int(input("Enter age: "))
                                l1.append(name)
                                l1.append(age)
                                l1.append(trains_list[train][2]['2AC'][1])
                                l1.append(coach)
                                list1.append(l1) 
                                booking[username]=list1
                        else:print("Required number of seats not available") 
                        fare=passengers * trains_list[train][2]['2AC'][1]                            
                        trains_list[train][2]['2AC'][0]-=passengers                            
                #3AC            
                    elif coach=='3AC':
                        list1=[]                            
                        passengers=int(input("Enter number of passengers: "))
                        if passengers <= trains_list[train][2]['3AC'][0]:
                            for i in range(passengers):
                                l1=[]
                                name=input("Enter passengers name: ")
                                age=int(input("Enter age: "))
                                l1.append(name)
                                l1.append(age)
                                l1.append(trains_list[train][2]['3AC'][1])
                                l1.append(coach)
                                list1.append(l1) 
                                booking[username]=list1 
                        else:print("Required number of seats not available")
                        fare=passengers * trains_list[train][2]['3AC'][1]                             
                        trains_list[train][2]['3AC'][0]-=passengers
                #sleeper                                                               
                    elif coach=='sleeper':
                        list1=[]
                        passengers=int(input("Enter number of passengers: "))
                        if passengers <= trains_list[train][2]['1AC'][0]:
                            for i in range(passengers):
                                l1=[]
                                name=input("Enter passengers name: ")
                                age=int(input("Enter age: "))
                                l1.append(name)
                                l1.append(age)
                                l1.append(trains_list[train][2]['sleeper'][1])
                                l1.append(coach)
                                list1.append(l1)
                                booking[username]=list1 
                        else:print("Required number of seats not available") 
                        fare=passengers * trains_list[train][2]['sleeper'][1]                              
                        trains_list[train][2]['sleeper'][0]-=passengers
                    else:print("Selected coach not available")  

                else:print("Train not available")  
                            
                #print ticket         
                print(50*'*','WELCOME TO INDIAN RAILWAYS',50*'*')
                print("NAME: ",username.upper(),75*' ',date.today(),2*" ",datetime.now().strftime("%H:%M:%S"))
                print("Train name:  ",train,50*' ',"Train no.",trains_list[train][0])
                print("Date of journey: ",journey_date)
                print("Train time:",trains_list[train][1],50*" ","PNR NO.",random.randint(11111,1000000))
                print(120*"-")                
                print("Sno.",22*' ',"name",22*' ',"Age",24*" ","coach",22*" ","fare")
                print('\n')
                for i in range(len(list1)):
                    print(i+1,24*' ',list1[i][0],23*' ',list1[i][1],25*" ",list1[i][3],23*" ",list1[i][2])
                print('\n')                              
                print ("Total price: ",95*" ",fare)                 
                print(55*'*','HAPPY JOURNEY',60*'*')
            # cancellation of ticket      
            elif n=='3':                      
                if username in booking:  #check if the user have booked tickt 
                    x=int(input("Enter number of tickets want to cancel"))   
                    if x<len((booking[username])):   #to check weather number of tickets to cancel is less tha number of tickets booked
                        
                        #eprint(c)
                        for i in range(x):
                            c=booking.get(username)    #from booking dictionary get values of that user and store in c(it will be nested list )
                            n1=input("Enter the passenger name to be cancelled: ") #taking user input for calcelling no. of tickets
                            #to update number of seats in each coach after cancellation         
                            for i in range(len(c)):
                                if n1 in c[i] and c[i][3]=='1AC':
                                    trains_list[train][2]['1AC'][0]+=x
                                elif n1 in c[i] and c[i][3]=='2AC': 
                                    trains_list[train][2]['2AC'][0]+=x
                                elif n1 in c[i] and c[i][3]=='3AC': 
                                    trains_list[train][2]['3AC'][0]+=x   
                                elif n1 in c[i] and c[i][3]=='sleeper': 
                                    trains_list[train][2]['sleeper'][0]+=x          
                                if n1 in c[i]: #if name to be cancelled found in nested list during iteration break the iteration                                                                                    n
                                    break                                                                                                                                                                                                        
                            c.remove(c[i]) # remove that list from the nested list
                                                                                                        
                    else:print('you have entered more tickets than booked')  

                    # print the ticket after cancellation for remaining passengers     
                    print(50*'*','WELCOME TO INDIAN RAILWAYS',50*'*')
                    print("NAME: ",username.upper(),80*' ',date.today(),2*" ",datetime.now().strftime("%H:%M:%S"))
                    print("Train name:  ",train,50*' ',"Train no.",trains_list[train][0])
                    print("Date of journey: ",journey_date)
                    print("Train time:",trains_list[train][1],30*" ","PNR NO.",random.randint(11111,1000000))
                    print(120*"-") 
                    print("Sno.",22*' ',"name",22*' ',"Age",24*" ","coach",23*" ","fare")
                    print('\n')
                    for i in range(len(c)):
                        print(i+1,24*' ',c[i][0],23*' ',c[i][1],25*" ",c[i][3],23*" ",c[i][2])  
                    print('\n')                      
                    print ("Total price: ",95*" ",(i+1)*c[i][2]) 
                    print(55*'*','HAPPY JOURNEY',60*'*') 
                else:print("You have no booking history")
                        
            else:print("Invaid input")           
                                
    else:print("Invalid credentials")
