import csv

with open("Height-Weight.csv",newline='') as f :
    r = csv.reader(f)
    file_data = list(r)

file_data.pop(0)
#print(file_data)
new_data=[]
for i in range(len(file_data)):
    num = file_data[i][1]
    #type casting to float or else the value after point will not be there
    new_data.append(float(num))

n=len(new_data)
sum = 0
for i in new_data :
    sum += i
    
mean = sum/n

#print(mean)


import statistics
print( statistics.mean( new_data) )
print( statistics.median(new_data) )
print(  statistics.mode( new_data) )