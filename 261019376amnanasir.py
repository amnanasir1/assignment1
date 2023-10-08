
# login component
user="user"
userpwd="user123"

admin="admin"
adminpwd="admin123"

flag=0
useragent=""
while(flag==0):
    print("LOGIN")
    username=input("Enter username")
    password=input("Enter password")

    if username==user and password==userpwd:
        useragent="user"
        flag=1
    elif username==admin and password==adminpwd:
        useragent="admin"
        flag=1
    else:
        print("Invalid username or password")


def showflight(flightname,flag=0):
    seatsfile=open(flightname,"r")
    seats={}
    rowlen=0
    for line in seatsfile:
        x=line.split(" ")
        a=x[0]
        seats[a]=x[1].split(",")
    seatsfile.close()
    keys=list(seats.keys())
    keysindex=0    
    if flag==0:    
        for row in seats:
            print(keys[keysindex]+" ",end="")
            keysindex=keysindex+1
            for col in seats[row]:
                print(col+" ",end="")
            print("")
    return seats
# user panel
choice=-1
while(1):
    if(useragent=="user"):
        print("Welcome User:")
        print("\t 1. Book A Ticket")
        print("\t 2. Cancel A Booking")
        print("\t 3. Show Flights")
        print("\t 4. Exit")
        choice=int(input("Enter the corresponding number: "))
        while choice<1 or choice>4:
            print("Wrong Input")
            choice=int(input("Enter the corresponding number: "))   

        if choice==1:
            print("Available Flights")
            avbflights=open("flight lists.txt","r")
            numofflights=0
            flightlist=avbflights.readlines()
            for line in flightlist:
                numofflights=numofflights+1
                print(str(numofflights)+":",end="")
                line=line.strip()
                print(line)
            flightchoice=int(input("Choose a flight(enter the corresponding number) "))
            while flightchoice < 1 or flightchoice>numofflights:
                print("wrong input")
                flightchoice=int(input("Choose a flight(enter the corresponding number) ")) 

            seats=showflight(flightlist[flightchoice-1].strip()+".txt") 

            keys=list(seats.keys())
            rownum=input("Enter the row number ")
            seatnum=input("Enter the seat number ")
            seatnumint=-1
            if seatnum>='A' and seatnum<='J': #capital
                seatnumint=(ord(seatnum)-65)
            elif seatnum>='a' and seatnum<='j':
                seatnumint=(ord(seatnum)-97)
            seatnumlimit=len(list(seats["rows"]))-1
            while(int(rownum)<1 or int(rownum)>len(keys)-4) or (seatnumint<0 or seatnumint>seatnumlimit):
                print("Invalid input")
                rownum=input("Enter the row number ")
                seatnum=input("Enter the seat number ")
                if seatnum>='A' and seatnum<='J': #capital
                    seatnumint=(ord(seatnum)-65)
                elif seatnum>='a' and seatnum<='j':
                    seatnumint=(ord(seatnum)-97)        
            reqrow=(seats["row"+rownum])
            if(reqrow[seatnumint]!='x'):
                reqrow[seatnumint]='x' #booked
                print("seat "+ seatnum +" in row "+rownum+" has been successfully booked")
                seats["row"+rownum]=reqrow
                # updating the seats in file
                seatsfile=open(flightlist[flightchoice-1].strip()+".txt","w")
                for key,value in seats.items():                
                    valuestr=",".join(str(el) for el in value)
                    seatsfile.write(key +" "+valuestr) 
                seatsfile.close()
                #saving the ticket
                name=input("enter name ")
                ticketfile=open("ticket.txt","w")
                ticketfile.write("Name: "+name)
                ticketfile.write("\nFlight Company: "+flightlist[flightchoice-1].strip())   
                ticketfile.write("\nTicker: Row "+rownum+" Seat "+seatnum)
                ticketfile.close()                   
            else:
                print("seat is already booked")
                print("choose another flight or another seat in same flight")
            stop=input("")
            
        elif choice==2:
            print("Available Flights")
            avbflights=open("flight lists.txt","r")
            numofflights=0
            flightlist=avbflights.readlines()
            for line in flightlist:
                numofflights=numofflights+1
                print(str(numofflights)+":",end="")
                line=line.strip()
                print(line)
            flightchoice=int(input("Choose a flight(enter the corresponding number) " ))
            while flightchoice < 1 or flightchoice>numofflights:
                print("wrong input")
                flightchoice=int(input("Choose a flight(enter the corresponding number) ")) 

            seats=showflight(flightlist[flightchoice-1].strip()+".txt")

            keys=list(seats.keys())
            rownum=input("Enter the row number ")
            seatnum=input("Enter the seat number ")
            seatnumint=-1
            if seatnum>='A' and seatnum<='J': #capital
                seatnumint=(ord(seatnum)-65)
            elif seatnum>='a' and seatnum<='j':
                seatnumint=(ord(seatnum)-97)
            seatnumlimit=len(list(seats["rows"]))-1
            while(int(rownum)<1 or int(rownum)>len(keys)-4) or (seatnumint<0 or seatnumint>seatnumlimit):
                print("Invalid input")
                rownum=input("Enter the row number ")
                seatnum=input("Enter the seat number ")
                if seatnum>='A' and seatnum<='J': #capital
                    seatnumint=(ord(seatnum)-65)
                elif seatnum>='a' and seatnum<='j':
                    seatnumint=(ord(seatnum)-97)        
            reqrow=(seats["row"+rownum])
            if(reqrow[seatnumint]=='x'):
                reqrow[seatnumint]='*' #unbooked
                print("seat "+ seatnum +" in row "+rownum+" has been successfully cancelled")
                seats["row"+rownum]=reqrow
                # updating the seats in file
                seatsfile=open(flightlist[flightchoice-1].strip()+".txt","w")
                for key,value in seats.items():                
                    valuestr=",".join(str(el) for el in value)
                    seatsfile.write(key +" "+valuestr) 
                seatsfile.close()                        
            else:
                print("seat is already unbooked")
            stop=input("")

        elif choice==3:
            print("Available Flights")
            avbflights=open("flight lists.txt","r")
            numofflights=0
            flightlist=avbflights.readlines()
            for line in flightlist:
                numofflights=numofflights+1
                print(str(numofflights)+":",end="")
                line=line.strip()
                print(line)
                showflight(line.strip()+".txt")
            stop=input("")
        elif choice==4:
            break
    elif useragent=="admin":
        print("Welcome Admin:")
        print("\t 1. Add A Flight")
        print("\t 2. Modify A Flight")
        print("\t 3. Remove A Flight")
        print("\t 4. Exit")
        choice=int(input("Enter the corresponding number: "))
        while choice<1 or choice>4:
            print("Wrong Input")
            choice=int(input("Enter the corresponding number: "))
        if choice==1:
            flightname=input("Enter new flight name: ")
            departuredate=input("Enter departure date: ")
            departuretime=input("Enter departure time: ")
            arrivaldate=input("Enter arrival date: ")
            arrivaltime=input("Enter arrival time: ")
            numofrows=input("Enter number of rows")
            numofcols=input("Enter number of columns(A-J)")
            numofcols=numofcols.upper()
            while(numofcols<'A' or numofcols>'J'):
                print("Invalid number of columns")
                numofcols=input("Enter number of columns(A-J)")
            newfl={}
            newfl["DepartureDate"]=list(departuredate)
            newfl["DepartureTime"]=list(departuretime)
            newfl["ArrivalDate"]=list(arrivaldate)
            newfl["ArrivalTime"]=list(arrivaltime)
            empseat=[]
            colnum=[]
            colchar="A"
            i=0
            limit=(ord(numofcols)-65)

            while i<=limit:
                empseat.append('*')
                colnum.append(colchar)
                colint=ord(colchar)
                print(colint)
                colint=colint+1
                colchar=chr(colint)
                i=i+1

            colnum[limit]=colnum[limit]+'\n'
            empseat[i-1]=empseat[i-1]+'\n'
            newfl["rows"]=colnum
            i=1
            while i<=int(numofrows):
                newfl["row"+str(i)] =empseat
                i=i+1
            print(flightname)
            flightname=flightname+'\n'
            print(newfl)
            avbflights=open("flight lists.txt","r")
            flightlist=avbflights.readlines()
            flightlist.append(flightname)
            avbflights.close()
            avbflights=open("flight lists.txt","w")
            for line in flightlist:
                avbflights.write(line)
            avbflights.close()
            seatsfile=open(flightname.strip()+".txt","w")
            for key,value in newfl.items():
                valuestr=""
                if key=="DepartureTime" or key=="ArrivalTime" or key=="DepartureDate" or key=="ArrivalDate":                
                    valuestr="".join(str(el) for el in value)
                    valuestr=valuestr+"\n"
                else:
                    valuestr=",".join(str(el) for el in value)
                seatsfile.write(key +" "+valuestr) 
            seatsfile.close()   
            stop=input("")
        elif choice==2:
            print("Available Flights")
            avbflights=open("flight lists.txt","r")
            numofflights=0
            flightlist=avbflights.readlines()
            for line in flightlist:
                numofflights=numofflights+1
                print(str(numofflights)+":",end="")
                line=line.strip()
                print(line)
            flightchoice=int(input("Choose a flight(enter the corresponding number) "))
            while flightchoice < 1 or flightchoice>numofflights:
                print("wrong input")
                flightchoice=int(input("Choose a flight(enter the corresponding number) "))
            print("\t 1. Change arrival and departure time")
            print("\t 2. Change flight details")
            print("\t 3. Change the seat layout")
            changechoice=int(input("enter the corresponding number "))
            while changechoice < 1 or changechoice>3:
                print("wrong input")
                changechoice=int(input("enter the corresponding number "))
            if changechoice == 1:
                seats=showflight(flightlist[flightchoice-1].strip()+".txt")
                print(seats)
                departure=input("Enter new departure time ")
                arrival=input("Enter new arrival time ")
                seats["ArrivalTime"]=list(arrival)
                seats["DepartureTime"]=list(departure) 
                print(seats)    

                seatsfile=open(flightlist[flightchoice-1].strip()+".txt","w")
                for key,value in seats.items():
                    valuestr=""
                    if key=="DepartureTime" or key=="ArrivalTime":                
                        valuestr="".join(str(el) for el in value)
                        valuestr=valuestr+"\n"
                    else:
                        valuestr=",".join(str(el) for el in value)
                    seatsfile.write(key +" "+valuestr) 
                seatsfile.close()           
            elif changechoice==2:
                seats=showflight(flightlist[flightchoice-1].strip()+".txt")
                departuredate=input("Enter new departure date")
                arrivaldate=input("Enter new arrival date")
                seats["DepartureDate"]=list(departuredate)
                seats["ArrivalDate"]=list(arrivaldate)
                seatsfile=open(flightlist[flightchoice-1].strip()+".txt","w")
                for key,value in seats.items():                
                    valuestr=""
                    if key=="DepartureDate" or key=="ArrivalDate":                
                        valuestr="".join(str(el) for el in value)
                        valuestr=valuestr+"\n"
                    else:
                        valuestr=",".join(str(el) for el in value)
                    seatsfile.write(key +" "+valuestr) 
                seatsfile.close()
            elif changechoice==3:
                seats=showflight(flightlist[flightchoice-1].strip()+".txt")
                keys=list(seats.keys())
                rownum=input("Enter the row number ")
                seatnum=input("Enter the seat number ")
                seatnumint=-1
                if seatnum>='A' and seatnum<='J': #capital
                    seatnumint=(ord(seatnum)-65)
                elif seatnum>='a' and seatnum<='j':
                    seatnumint=(ord(seatnum)-97)
                seatnumlimit=len(list(seats["rows"]))-1
                while(int(rownum)<1 or int(rownum)>len(keys)-4) or (seatnumint<0 or seatnumint>seatnumlimit):
                    print("Invalid input")
                    rownum=input("Enter the row number ")
                    seatnum=input("Enter the seat number ")
                    if seatnum>='A' and seatnum<='J': #capital
                        seatnumint=(ord(seatnum)-65)
                    elif seatnum>='a' and seatnum<='j':
                        seatnumint=(ord(seatnum)-97)        
                reqrow=(seats["row"+rownum])
                if(reqrow[seatnumint]=='x'):
                    reqrow[seatnumint]='*' #unbooked
                    print("seat "+ seatnum +" in row "+rownum+" has been successfully cancelled")
                elif(reqrow[seatnumint]=='*'):
                    reqrow[seatnumint]='x' #booked
                    print("seat "+ seatnum +" in row "+rownum+" has been successfully booked")  

                seats["row"+rownum]=reqrow
                # updating the seats in file
                seatsfile=open(flightlist[flightchoice-1].strip()+".txt","w")
                for key,value in seats.items():                
                    valuestr=",".join(str(el) for el in value)
                    seatsfile.write(key +" "+valuestr) 
                seatsfile.close()                                   
            stop=input("")

        elif choice==3:
            print("Available Flights")
            avbflights=open("flight lists.txt","r")
            numofflights=0
            flightlist=avbflights.readlines()
            for line in flightlist:
                numofflights=numofflights+1
                print(str(numofflights)+":",end="")
                line=line.strip()
                print(line)
            avbflights.close()
            flightchoice=int(input("Choose a flight(enter the corresponding number) "))
            while flightchoice < 1 or flightchoice>numofflights:
                print("wrong input")
                flightchoice=int(input("Choose a flight(enter the corresponding number) "))  
            idx=flightlist.index(flightlist[flightchoice-1])
            del flightlist[idx]
            avbflights=open("flight lists.txt","w")
            for line in flightlist:
                avbflights.write(line)
            avbflights.close()
            stop=input("")

        elif choice==4:
        
            break


