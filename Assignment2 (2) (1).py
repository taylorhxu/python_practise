import random
from collections import deque

def assignment1():
    while True:
        try:
            A = float(input("Enter the wanted average arrival time: "))
            if A <= 0:
                print "Value too low, try again!"
                continue
            break
        except:
            print "Invalid input, try again!"
            
    while True:
        try:
            P = float(input("Enter the wanted average packet size: "))
            if P <= 0:
                print "Value too low, try again!"
                continue
            break
        except:
            print "Invalid input, try again!"
    

    def Arrivaltimes():
        return random.expovariate(1/A)

    def Packetsize():
        return random.expovariate(1/P)

    while True:
        try:
            x = int(input("Enter number of desired packet departures: "))
            if x <= 0:
                print "Value too low, try again!"
                continue
            break
        except:
            print "Invalid input, try again!"
    
    while True:
        firstarrival = Arrivaltimes()
        firstpacketsize = Packetsize()
        
        try:
            if firstarrival < firstpacketsize:
                print "First condition met!"
                break
        except:
            continue
        
    queue = deque([])

    queue.append(firstpacketsize)

    loopcount = 0
    emptyqueue = 0
    while True:
        loopcount = loopcount + 1
        secondarrival = Arrivaltimes()
        totalarrival = secondarrival + firstarrival
        
        if totalarrival < firstpacketsize:
            print "Second condition met!"
            secondpacketsize = Packetsize()
            queue.append(secondpacketsize)
            break
        else:
            emptyqueue = emptyqueue + 1
            continue

    print queue 
    ##Total packet size is also the same as departure/processing duration 
    totalpacketsize = firstpacketsize + firstarrival  
    diffsecondpacket = firstpacketsize - secondarrival

    queuesizelist = [1]
    waitingtimes = [diffsecondpacket]

    ##Main while loop code
    NotFinished = True
    arrcount = 2
    depcount = 0

    while NotFinished:
        loopcount = loopcount + 1
        if totalarrival < totalpacketsize:
            print "Arrival!"
            nextarrival = Arrivaltimes()
            totalarrival = totalarrival + nextarrival
            arrcount = arrcount + 1
            newpacket = Packetsize()
            waitingtimes.append(sum(queue)-queue[0]+(totalpacketsize-totalarrival))
            queue.append(newpacket)
            length = len(queue) - 1
            if length == -1:
                queuesizelist.append(0)
            else:
                queuesizelist.append(length)
        else:
            print "Departure!"
            depcount = depcount + 1
            queue.popleft()
            length = len(queue) - 1
            if length == -1:
                queuesizelist.append(0)
            else:
                queuesizelist.append(length)
            try:
                totalpacketsize = totalpacketsize + queue[0]
            except:
    ##Fail safe code for empty queue      
                emptyqueue = emptyqueue + 1
                queuesizelist.append(0)
                print "Filler arrival!"
                arrcount = arrcount + 1
                newarrival = Arrivaltimes()
                totalarrival = totalarrival + newarrival
                fillerpacket = Packetsize()
                waitingtimes.append(0)
                queue.append(fillerpacket)
                totalpacketsize = totalpacketsize + newarrival + fillerpacket
                print arrcount
                print depcount
                if depcount == x:
                    NotFinished = False
                    print "Finished!"
                continue 
        if depcount == x:
            NotFinished = False
            print "Finished!"

        print arrcount
        print depcount

    fivetimes_queue= 0

    for i in queuesizelist:
        if i > (5*P):
            fivetimes_queue = fivetimes_queue + 1

    percentempty = (float(emptyqueue)/float(loopcount))*(100)
    percent5times = (float(fivetimes_queue)/float(loopcount))*100

    print "Average waiting time:", float(sum(waitingtimes)/len(waitingtimes)) 
    print "Average queue size:", float(sum(queuesizelist)/(len(queuesizelist)))
    print "The probability of the queue being empty is", percentempty,"%"  
    print "The probability of the queue being greater than 5 times the average packet size is", percent5times,"%"

def assignment2():
    while True:
        try:
            A = float(input("Enter the wanted average arrival time: "))
            if A <= 0:
                print "Value too low, try again!"
                continue
            break
        except:
            print "Invalid input, try again!"
            
    while True:
        try:
            P = float(input("Enter the wanted average packet size: "))
            if P <= 0:
                print "Value too low, try again!"
                continue
            break
        except:
            print "Invalid input, try again!"
    

    def Arrivaltimes():
        return random.expovariate(1/A)

    def Packetsize():
        return random.expovariate(1/P)

    while True:
        try:
            x = int(input("Enter number of desired packet departures: "))
            if x <= 0:
                print "Value too low, try again!"
                continue
            break
        except:
            print "Invalid input, try again!"

    queue1 = deque([])
    queue2 = deque([])
    queue3 = deque([])
    queue4 = deque([])

    loopcount = 0
    totalarrival = 0
    totalpacketsize1 = 0
    totalpacketsize2 = 0
    totalpacketsize3 = 0
    totalpacketsize4 = 0
    depcount = 0
    emptyqueuetime = 0

    print "First Arrival!"
    firstarrival = Arrivaltimes()
    totalarrival = totalarrival + firstarrival
    firstpacket = Packetsize()
    firstselection = random.choice([1,2,3,4])
    if firstselection == 1:
        queue1.append(firstpacket)
        totalpacketsize1 = totalpacketsize1 + firstarrival + firstpacket
    elif firstselection == 2:
        queue2.append(firstpacket)
        totalpacketsize2 = totalpacketsize2 + firstarrival + firstpacket
    elif firstselection == 3:
        queue3.append(firstpacket)
        totalpacketsize3 = totalpacketsize3 + firstarrival + firstpacket
    elif firstselection == 4:
        queue4.append(firstpacket)
        totalpacketsize4 = totalpacketsize4 + firstarrival + firstpacket

    arrcount = 1

    if len(queue1) == 0:
        totalpacketsize1 = totalpacketsize1 + firstarrival
        emptyqueuetime = emptyqueuetime + firstarrival
    if len(queue2) == 0:
        totalpacketsize2 = totalpacketsize2 + firstarrival
        emptyqueuetime = emptyqueuetime + firstarrival
    if len(queue3) == 0:
        totalpacketsize3 = totalpacketsize3 + firstarrival
        emptyqueuetime = emptyqueuetime + firstarrival
    if len(queue4) == 0:
        totalpacketsize4 = totalpacketsize4 + firstarrival
        emptyqueuetime = emptyqueuetime + firstarrival

    waitingtimes = []
    queuesizelist = []

    NotDone = True

    while NotDone:
        loopcount = loopcount + 1
        if totalarrival < totalpacketsize1 or totalarrival < totalpacketsize2 or totalarrival < totalpacketsize3 or totalarrival < totalpacketsize4:
            print "Arrival!"
            arrcount = arrcount + 1
            nextarrival = Arrivaltimes()
            totalarrival = totalarrival + nextarrival
            selection = random.choice([1,2,3,4])
            print "Queue", selection, "chosen." 
            newpacket = Packetsize()
            if selection == 1:
                queue1.append(newpacket)
                length1 = len(queue1) - 1
                if length1 == -1:
                    queuesizelist.append(0)
                else:
                    queuesizelist.append(length1)
                if len(queue1) == 1:
                    totalpacketsize1 = totalpacketsize1 + nextarrival + newpacket
                    waitingtimes.append(0)
                else:
                    waitingtimes.append(sum(queue1)-queue1[0]+(totalpacketsize1-totalarrival))
            elif selection == 2:
                queue2.append(newpacket)
                length2 = len(queue2) - 1
                if length2 == -1:
                    queuesizelist.append(0)
                else:
                    queuesizelist.append(length2)
                if len(queue2) == 1:
                    totalpacketsize2 = totalpacketsize2 + nextarrival + newpacket
                    waitingtimes.append(0)
                else:
                    waitingtimes.append(sum(queue2)-queue2[0]+(totalpacketsize2-totalarrival))
            elif selection == 3:
                queue3.append(newpacket)
                length3 = len(queue1) - 1
                if length3 == -1:
                    queuesizelist.append(0)
                else:
                    queuesizelist.append(length3)
                if len(queue3) == 1:
                    totalpacketsize3 = totalpacketsize3 + nextarrival + newpacket
                    waitingtimes.append(0)
                else:
                    waitingtimes.append(sum(queue3)-queue3[0]+(totalpacketsize3-totalarrival))
            elif selection == 4:
                queue4.append(newpacket)
                length4 = len(queue4) - 1
                if length4 == -1:
                    queuesizelist.append(0)
                else:
                    queuesizelist.append(length4)
                if len(queue4) == 1:
                    totalpacketsize4 = totalpacketsize4 + nextarrival + newpacket
                    waitingtimes.append(0)
                else:
                    waitingtimes.append(sum(queue4)-queue4[0]+(totalpacketsize4-totalarrival))

            if len(queue1) == 0:
                totalpacketsize1 = totalpacketsize1 + nextarrival
                emptyqueuetime = emptyqueuetime + nextarrival
            if len(queue2) == 0:
                totalpacketsize2 = totalpacketsize2 + nextarrival
                emptyqueuetime = emptyqueuetime + nextarrival
            if len(queue3) == 0:
                totalpacketsize3 = totalpacketsize3 + nextarrival
                emptyqueuetime = emptyqueuetime + nextarrival
            if len(queue4) == 0:
                totalpacketsize4 = totalpacketsize4 + nextarrival
                emptyqueuetime = emptyqueuetime + nextarrival
        else:
            print "Potential Departure!"
            queue1ready = False
            queue2ready = False
            queue3ready = False
            queue4ready = False
            if totalpacketsize1 < totalarrival and len(queue1) > 0:
                queue1ready = True 
            if totalpacketsize2 < totalarrival and len(queue2) > 0:
                queue2ready = True
            if totalpacketsize3 < totalarrival and len(queue3) > 0:
                queue3ready = True
            if totalpacketsize4 < totalarrival and len(queue4) > 0:
                queue4ready = True

            if queue1ready == False and queue2ready == False and queue3ready == False and queue4ready == False:
                print "Filler Arrival!"
                fillerarrival = Arrivaltimes()
                totalarrival = totalarrival + fillerarrival
                fillerpacket = Packetsize()
                fillerselection = random.choice([1,2,3,4])
                if fillerselection == 1:
                    queue1.append(fillerpacket)
                    if len(queue1) == 1:
                        totalpacketsize1 = totalpacketsize1 + fillerarrival + fillerpacket
                        waitingtimes.append(0)
                elif fillerselection == 2:
                    queue2.append(fillerpacket)
                    if len(queue2) == 1:
                        totalpacketsize2 = totalpacketsize2 + fillerarrival + fillerpacket
                        waitingtimes.append(0)
                elif fillerselection == 3:
                    queue3.append(fillerpacket)
                    if len(queue3) == 1:
                        totalpacketsize3 = totalpacketsize3 + fillerarrival + fillerpacket
                        waitingtimes.append(0)
                elif fillerselection == 4:
                    queue4.append(fillerpacket)
                    if len(queue4) == 1:
                        totalpacketsize4 = totalpacketsize4 + fillerarrival + fillerpacket
                        waitingtimes.append(0)
                if len(queue1) == 0:
                    totalpacketsize1 = totalpacketsize1 + fillerarrival
                if len(queue2) == 0:
                    totalpacketsize2 = totalpacketsize2 + fillerarrival
                if len(queue3) == 0:
                    totalpacketsize3 = totalpacketsize3 + fillerarrival
                if len(queue4) == 0:
                    totalpacketsize4 = totalpacketsize4 + fillerarrival
                continue 

            queuereadylist = []
            ifreadylist = [queue1ready, queue2ready, queue3ready, queue4ready]
            for i in ifreadylist:
                if queue1ready == True:
                    queuereadylist.append(totalpacketsize1)
                if queue2ready == True:
                    queuereadylist.append(totalpacketsize2)
                if queue3ready == True:
                    queuereadylist.append(totalpacketsize3)
                if queue4ready == True:
                    queuereadylist.append(totalpacketsize4)

            duepacketdep = min(queuereadylist)

            if duepacketdep == totalpacketsize1:
                queue1.popleft()
                length1 = len(queue1) - 1
                if length1 == -1:
                    queuesizelist.append(0)
                    emptyqueuetime = emptyqueuetime + (totalarrival - totalpacketsize1)
                else:
                    queuesizelist.append(length1)
                if len(queue2) == 0:
                    totalpacketsize2 = totalpacketsize2 + (totalarrival - totalpacketsize1)
                    emptyqueuetime = emptyqueuetime + (totalarrival - totalpacketsize1)
                if len(queue3) == 0:
                    totalpacketsize3 = totalpacketsize3 + (totalarrival - totalpacketsize1)
                    emptyqueuetime = emptyqueuetime + (totalarrival - totalpacketsize1)
                if len(queue4) == 0:
                    totalpacketsize4 = totalpacketsize4 + (totalarrival - totalpacketsize1)
                    emptyqueuetime = emptyqueuetime + (totalarrival - totalpacketsize1)
                depcount = depcount + 1
                try:
                    totalpacketsize1 = totalpacketsize1 + queue1[0]
                except:
                    continue
                print "Queue 1 departed a packet!"
            elif duepacketdep == totalpacketsize2:
                queue2.popleft()
                length2 = len(queue2) - 1
                if length2 == -1:
                    queuesizelist.append(0)
                    emptyqueuetime = emptyqueuetime + (totalarrival - totalpacketsize2)
                else:
                    queuesizelist.append(length2)
                if len(queue1) == 0:
                    totalpacketsize1 = totalpacketsize1 + (totalarrival - totalpacketsize2)
                    emptyqueuetime = emptyqueuetime + (totalarrival - totalpacketsize2)
                if len(queue3) == 0:
                    totalpacketsize3 = totalpacketsize3 + (totalarrival - totalpacketsize2)
                    emptyqueuetime = emptyqueuetime + (totalarrival - totalpacketsize2)
                if len(queue4) == 0:
                    totalpacketsize4 = totalpacketsize4 + (totalarrival - totalpacketsize2)
                    emptyqueuetime = emptyqueuetime + (totalarrival - totalpacketsize2)
                depcount = depcount + 1
                try:
                    totalpacketsize2 = totalpacketsize2 + queue2[0]
                except:
                    continue
                print "Queue 2 departed a packet!"
            elif duepacketdep == totalpacketsize3:
                queue3.popleft()
                length3 = len(queue1) - 1
                if length3 == -1:
                    queuesizelist.append(0)
                    emptyqueuetime = emptyqueuetime + (totalarrival - totalpacketsize3)
                else:
                    queuesizelist.append(length3)
                if len(queue1) == 0:
                    totalpacketsize1 = totalpacketsize1 + (totalarrival - totalpacketsize3)
                    emptyqueuetime = emptyqueuetime + (totalarrival - totalpacketsize3)
                if len(queue2) == 0:
                    totalpacketsize2 = totalpacketsize2 + (totalarrival - totalpacketsize3)
                    emptyqueuetime = emptyqueuetime + (totalarrival - totalpacketsize3)
                if len(queue4) == 0:
                    totalpacketsize4 = totalpacketsize4 + (totalarrival - totalpacketsize3)
                    emptyqueuetime = emptyqueuetime + (totalarrival - totalpacketsize3)
                depcount = depcount + 1
                try:
                    totalpacketsize3 = totalpacketsize3 + queue3[0]
                except:
                    continue
                print "Queue 3 departed a packet!"
            elif duepacketdep == totalpacketsize4:
                queue4.popleft()
                length4 = len(queue4) - 1
                if length4 == -1:
                    queuesizelist.append(0)
                    emptyqueuetime = emptyqueuetime + (totalarrival - totalpacketsize4)
                else:
                    queuesizelist.append(length4)
                if len(queue1) == 0:
                    totalpacketsize1 = totalpacketsize1 + (totalarrival - totalpacketsize4)
                    emptyqueuetime = emptyqueuetime + (totalarrival - totalpacketsize4)
                if len(queue2) == 0:
                    totalpacketsize2 = totalpacketsize2 + (totalarrival - totalpacketsize4)
                    emptyqueuetime = emptyqueuetime + (totalarrival - totalpacketsize4)
                if len(queue3) == 0:
                    totalpacketsize3 = totalpacketsize3 + (totalarrival - totalpacketsize4)
                    emptyqueuetime = emptyqueuetime + (totalarrival - totalpacketsize4)
                depcount = depcount + 1
                try:
                    totalpacketsize4 = totalpacketsize4 + queue4[0]
                except:
                    continue
                print "Queue 4 departed a packet!"
            if depcount == x:
                NotDone = False
                print "Finished!"

            print arrcount
            print depcount
            
    fivetimes_queue= 0

    for i in queuesizelist:
        if i > (5*P):
            fivetimes_queue = fivetimes_queue + 1

    percent5times = (float(fivetimes_queue)/float(loopcount))*100

    print "Average waiting time:", abs(float(sum(waitingtimes)/len(waitingtimes)))
    print "Average queue size:", float(sum(queuesizelist)/(len(queuesizelist)))
    print "The probability of the queues being greater than 5 times the average packet size is", percent5times,"%" 
    print "The probability of the queues being empty is", (emptyqueuetime/(totalpacketsize1 + totalpacketsize2 +totalpacketsize3 +totalpacketsize4))*100,"%"
                
def assignment3():
    while True:
        try:
            A = float(input("Enter the wanted average arrival time: "))
            if A <= 0:
                print "Value too low, try again!"
                continue
            break
        except:
            print "Invalid input, try again!"
            
    while True:
        try:
            P = float(input("Enter the wanted average packet size: "))
            if P <= 0:
                print "Value too low, try again!"
                continue
            break
        except:
            print "Invalid input, try again!"
    

    def Arrivaltimes():
        return random.expovariate(1/A)

    def Packetsize():
        return random.expovariate(1/P)

    while True:
        try:
            x = int(input("Enter number of desired packet departures: "))
            if x <= 0:
                print "Value too low, try again!"
                continue
            break
        except:
            print "Invalid input, try again!"

    queue = deque([])

    print "First Arrival!"
    firstarrival = Arrivaltimes()
    totalarrival = 0
    totalarrival = totalarrival + firstarrival
    firstpacket = Packetsize()
    totalpacketsize1 = Packetsize()
    totalpacketsize2 = 0
    totalpacketsize3 = 0
    totalpacketsize4 = 0

    depcount = 0
    loopcount = 0
    server1 = 0
    server2 = 0
    server3 = 0
    server4 = 0

    NotDone = True

    while NotDone:
        loopcount = loopcount + 1
        if totalarrival < totalpacketsize1 or totalarrival < totalpacketsize2 or totalarrival < totalpacketsize3 or totalarrival < totalpacketsize4:
            print "Arrival!"
            nextarrival = Arrivaltimes()
            totalarrival = totalarrival + nextarrival
            newpacket = Packetsize()
            if server1 == 0:
                server1 = newpacket
            elif server2 == 0:
                server2 = newpacket
            elif server3 == 0:
                server3 = newpacket
            elif server4 == 0:
                server4 = newpacket
            else:
                queue.append(newpacket)
        else:
            print "Potential Departure!"
            server1ready = False
            server2ready = False
            server3ready = False
            server4ready = False
            if server1 > 0:
                server1ready = True
            if server2 > 0:
                server2ready = True
            if server3 > 0:
                server3ready = True
            if server4 > 0:
                server4ready = True
            serverreadylist = []
            ifreadylist = [server1ready, server2ready, server3ready, server4ready]

            for i in ifreadylist:
                if server1ready == True:
                    serverreadylist.append(server1)
                if server2ready == True:
                    serverreadylist.append(server2)
                if server3ready == True:
                    serverreadylist.append(server3)
                if server4ready == True:
                    serverreadylist.append(server4)

            try:
                duepacketdep = min(serverreadylist)
            except:
                continue 
            if duepacketdep == server1:
                totalpacketsize1 = totalpacketsize1 + server1
                server1 = 0
                if server2 == 0:
                    totalpacketsize2 = totalpacketsize2 + (totalarrival - totalpacketsize1)
                if server3 == 0:
                    totalpacketsize3 = totalpacketsize3 + (totalarrival - totalpacketsize1)
                if server4 == 0:
                    totalpacketsize4 = totalpacketsize4 + (totalarrival - totalpacketsize1) 
                print "Server 1 departed a packet!"
                depcount = depcount + 1
            elif duepacketdep == server2:
                totalpacketsize2 = totalpacketsize2 + server2
                server2 = 0
                if server1 == 0:
                    totalpacketsize1 = totalpacketsize1 + (totalarrival - totalpacketsize2)
                if server3 == 0:
                    totalpacketsize3 = totalpacketsize3 + (totalarrival - totalpacketsize2)
                if server4 == 0:
                    totalpacketsize4 = totalpacketsize4 + (totalarrival - totalpacketsize2)
                print "Server 2 departed a packet!"
                depcount = depcount + 1
            if duepacketdep == server3:
                totalpacketsize3 = totalpacketsize3 + server3
                server3 = 0
                if server1 == 0:
                    totalpacketsize1 = totalpacketsize1 + (totalarrival - totalpacketsize3)
                if server2 == 0:
                    totalpacketsize2 = totalpacketsize2 + (totalarrival - totalpacketsize3)
                if server4 == 0:
                    totalpacketsize4 = totalpacketsize4 + (totalarrival - totalpacketsize3)
                print "Server 3 departed a packet!"
                depcount = depcount + 1
            if duepacketdep == server4:
                totalpacketsize4 = totalpacketsize4 + server4
                server4 = 0
                if server1 == 0:
                    totalpacketsize1 = totalpacketsize1 + (totalarrival - totalpacketsize4)
                if server2 == 0:
                    totalpacketsize2 = totalpacketsize2 + (totalarrival - totalpacketsize4)
                if server4 == 0:
                    totalpacketsize3 = totalpacketsize3 + (totalarrival - totalpacketsize4)
                print "Server 4 departed a packet!"
                depcount = depcount + 1
            if server1 == 0:
                try:
                    server1 = queue[0]
                    queue.popleft()
                except:
                    continue
            if server2 == 0:
                try:
                    server2 = queue[0]
                    queue.popleft()
                except:
                    continue
            if server3 == 0:
                try:
                    server3 = queue[0]
                    queue.popleft()
                except:
                    continue
            if server4 == 0:
                try:
                    server4 = queue[0]
                    queue.popleft()
                except:
                    continue
            if depcount == x:
                NotDone = False
                print "Finished!"
            
while True: 
    prompt = raw_input("Type in 1 for assignment 1, type in 2 for assignment 2 and type in 3 for assignment 3. Type 0 to exit: ")

    try:
        ans = int(prompt)
    except:
        ans = -1 

    if ans == 1:
        assignment1()
    elif ans == 2:
        assignment2()
    elif ans == 3:
        assignment3()
    elif ans == 0:
        exit()
    elif ans < 0:
        print "Invalid input, try again."
    else:
        print "Invalid input, try again."



