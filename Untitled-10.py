import pandas as pd
import csv
import numpy as np
import json

with open("CareAreas-2.csv","r") as f:
    data=csv.reader(f)
    for row in data:
        x=5
        #print(row)

with open("CareAreas-2.csv","r") as f:
    s1,x1,x2,y1,y2=map(float,f.readline().strip().split(","))
    print("x1 is:")
    print(x1)
    for line in f:
        x=5
        #print(line)#or f.readline().strip()

data=pd.read_csv("CareAreas-2.csv")

#print(data)

#data=data.to_numpy()
#print(data)
#print(data.iloc[:,:])

with open("ink.txt","r") as f:
    data=f.read()
    #print(data)



#Standard working example :-

def rotate_matrix(mat):
    matrix=mat[::-1]
    return np.transpose(matrix)

mat=[]
with open("ink.txt","r") as f:
    for line in f:
        if line.startswith("ORIENTATION"):
            orientation=int(line.split(":")[1]) #when using two or more variables only u must use map xxx becoz it might consider 9 0 separately
        elif line.startswith("ROWDATA"):
            matrix=list(map(int,line.split(":")[1].split()))
            mat.append(matrix)

matrix=rotate_matrix(mat)
#print(orientation)
#mat1=mat.to_numpy()
with open("matrix_op.txt","w") as f:
    for row in matrix:
        f.write(" ".join(map(str,row))+"\n")


#read and write json

with open("json_sample.txt","r") as f:
    data1=json.load(f)
    print(data1[0])

new_entry=[]

new_1={
    "name":"one"
}
new_1["age"]=52
new_2={
    "name":"two"
}

new_entry.append(new_1)
new_entry.append(new_2)

with open("json_sample.txt","w") as f:
    #json.dump(new_entry,f,indent=4)
    x=5

### create a 2d matrix in python

mat=[[0 for i in range(3)]for i in range(3)]

mat=[] #initialize ny appending arrays

mat=np.zeros((3,3))