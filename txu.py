import random
import math
# manhattan distance
def man_dis(x,y):
    return sum(abs(a-b) for a,b in zip(x,y))

# l = the list of all location coordinates
l=[]
# n = events
n=0
# p = the list of all prices
# assume the ticket price is within 9 - 75 USD
p=[]
# dis = distance
dis=[]
# t = tickets
t=[]

# randomly generate points where events are happening
# within given range from -10 to +10 in both x and y axis

for x in range(-10, 11):
	for y in range(-10, 11):
		l.append((x,y))
random.shuffle(l)


# cl = locations coordinates
# assume to be the current location 
cl=raw_input("please enter the location in the form- a,b:")
ori=map(int,cl.split(','))

for i in range(0, 20):
	dis.append(man_dis(ori,l[i]))



for i in range(len(l)):
	p.append(random.uniform(9, 175))
	t.append(random.randint(1,100))

k = sorted(dis)[4]

idx=[]


for i in range(0, 20):
	if dis[i] <= k:
		 idx.append(i)

cp=[]
for i in idx:
	cp.append(p[i])

b=sorted(cp)[4]

idxx=[]

for i in idx:
	if p[i] <= b:
		idxx.append(i)
		
for i in idxx:
	print "Distance", dis[i], "Event ",i, "$", format(p[i], '.2f')
