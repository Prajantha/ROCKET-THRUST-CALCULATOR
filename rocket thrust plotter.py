#program to measure the thrust of a rocket 

def thrustcal():
    #formula  F= m * ve
    i=int(input("Enter the number of data:"))
    F=0
    dict1={}
    for i in range(i):
        m=int(input("Enter the mass flow rate:"))
        ve=int(input("Enter the exhaust velocity:"))
        F=m*ve 
        print("Thrust produced is "+str(F)+" Newtons")
        dict1[i]=F
    return dict1

def plotthrustvstime(dict1):
    import matplotlib.pyplot as plt 
    x=[]
    y=[]
    for i in dict1:
        x.append(i)
        y.append(dict1[i])
    plt.plot(x,y, marker="o", linestyle="-", color="red")
    plt.title("Thrust vs Time for Rocket Launch")
    plt.xlabel("Time (s)")
    plt.ylabel("Thrust (N)")
    plt.grid(True)
    plt.show()

#mains
dict1=thrustcal()
plotthrustvstime(dict1)
