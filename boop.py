import os,time
a=0
while True:
    os.mkdir(os.getcwd()+"/VIRUS infected file {}".format(a))
    a+=1
    time.sleep(1.0) # comment this line for full power of this code
