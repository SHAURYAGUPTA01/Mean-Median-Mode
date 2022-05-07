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
    
from collections import Counter
data = Counter(new_data)
#n create a dictionary with range of height as keys and the occurrences of the heights .
modeDataRange = {
                    "50-60": 0,
                    "60-70": 0,
                    "70-80": 0
               }
for height,occurrence in data.items():
    if 50 < float(height) < 60:
          modeDataRange["50-60"] += occurrence
          
    elif 60 < float(height)  < 70:
        modeDataRange["60-70"] += occurrence
        
    if 70 < float(height) < 80:
        modeDataRange["70-80"] += occurrence
        
print(modeDataRange)
print(modeDataRange.items())

modeRange,modeOccurence = 0,0
for range,occurrence in modeDataRange.items():
    if occurrence > modeOccurence:
        modeRange, modeOccurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurrence

mode = float( (modeRange[0]+modeRange[1] )/2 )
print(f"mode of the data : {mode}" )