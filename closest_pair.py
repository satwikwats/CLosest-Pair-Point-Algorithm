import math
import random
import matplotlib.pyplot as plt

##Using pythagorean distance formula to calculate distance between two point on a cartesian plane

def dist(p1, p2): # p1 and p2 are points on the plane
    
    return math.sqrt(((p2[1]-p1[1])**2)+((p2[0]-p1[0])**2)) 
#defining a function to compute shortest distance

def shortdist(points):
    mindist=float('inf') ##meaning inifinte value is assigned to the variable
    p1=None #no value is assigned
    p2=None #no value is assigned
    n=len(points)
    for x in range(n):
        for y in range(x+1, n):
            d=dist(points[x],points[y]) #computes the distance between the coordinates
            if d< mindist:
                mindist=d
                p1=points[x]
                p2=points[y]
    return p1, p2, mindist
  
##Defining a fucntion to separate sorted parts of x and y

def sortpart(x,y):
    n=len(x)
    if n<=3:
        return shortdist(x)
    else:
        mid=x[n//2] # dividing the list in half
        x_left=x[:n//2] #left part sub-array
        x_right=x[n//2:] #right part sub-array
        y_left=[]
        y_right=[]
        for i in y:
            if i[0]<=mid[0]: ##if the element is less than mid value then append it to left side
                y_left.append(i)
            else:
                y_right.append(i)
        (p1_left,p2_left, di)=sortpart(x_left,y_left) #di minimum distance of left array
        (p1_right,p2_right, dr)=sortpart(x_right,y_right)# dr minimum distance of right array
        #delta=min(di,dr)
        if di<dr:
            
            (p1,p2,delta)=(p1_left,p2_left,di)
            
        else:
            
                
            (p1,p2,delta)=(p1_right,p2_right,dr)
            
        two_delta=[i for i in y if mid[0]-delta<i[0]<mid[0]+delta]# defining the strip
#         for i in y:
#             if mid[0]-delta<i[0] and mid[0]+delta>i[0]:
#                 two_delta=i
        n=len(two_delta)
        for i in range(n):# using basic distance formula
            for j in range(i+1, min(i+7, n)):
                d=dist(two_delta[i], two_delta[j])
                if d<delta:
                    (p1,p2,delta)=(two_delta[i], two_delta[j],d)
        return p1,p2,delta
 
def closest_pair(points): #sorts list according to x and y value and return the points of closest distance
#     xpar=[]
#     for i in points:
#         xpar.append(i[0])
#     ypar=[]
#     for i in points:
#         ypar.append(i[1])
# print(xpar)
# print(ypar)
# print(QuickSort(xpar))




    x=sorted(points, key=lambda point:point[0]) #lambda just points the function sorted to the first part of tuple that is x 
    y=sorted(points, key=lambda point:point[1]) #Lambda just points the function sorted to the second part of tuple that is y 
    return sortpart(x,y)
  
#generating random numbers for x and y
%matplotlib
x = []
y = []
for _ in range(1000):
    x.append(random.randint(0, 1002))
    y.append(random.randint(0, 2000))
# print(x)
# print(y)

#putting points x and y together and storing them in another list
points=[(a,b) for (a,b) in zip(x,y)]
#print(points)



# closest_pair gives three values so we stores p1 in a, p2 in b and dist in c
a,b,c=closest_pair(points)

n,m=a # a is a coordinate value containing x and y so we separate them as n and m
q,w=b  # b is a coordinate value containing x and y so we separate them as q and w
print(closest_pair(points))

plt.scatter(x,y, s=20, label="Random points") #plotting the set of randomly generated points

plt.scatter(n,m, color='m',s =20)#plotting x and y coordinates of a
plt.scatter(q,w,color='m',s=20)# plotting x and y coordinates of b
plt.style.use('dark_background')
plt.plot(n,m, color= 'royalblue', label="P1") # plotting the graph obtained by the normal method
plt.plot(q,w, color='firebrick', label="P2")
plt.legend()
plt.grid()

    
