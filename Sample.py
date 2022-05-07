import csv

with open('Height-Weight.csv',newline='') as f :
    #csv.reader method reads & returns current row and then moves on to the next
    r = csv.reader(f)
    # add the data to the list
    file_data = list(r)


from collections import Counter
#Counter is a sub class in dictionary, using Counter tool you can count key-value pair
new_data = "Hellocodershaurya"
data = Counter(new_data)
#print(data)

#return the list with all dictionary keys with values. It returns a tuple of key value pairs
print( data.items() )

#returns the list of all the values in the dictionary. 
print(data.values())
