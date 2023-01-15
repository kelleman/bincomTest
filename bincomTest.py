from statistics import median
"""
GREEN=10, YELLOW=5, BROWN=6, BLUE=30, PINK=5, ORANGE=9, CREAM=2, RED=9, WHITE=16, ARSH=1, BLACK=1, BLEW=1

"""

weekColors = [["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],

["ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"],

["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"],

["BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"],

["GREEN", "WHITE", "GREEN", "BROWN", 'BLUE', "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"]]

#length =len(week[0]+ week[1] + week[2] + week[3] +week[4])


join = sum(weekColors, [])
join.sort()

'''  ===== QUESTION 2'''
# 2: color mostly worn throughout the week
print(max(set(join), key=join.count))

'''QUESTION 3'''
# 3: median of the colors
print(median(join))


'''Below is the code that arranges data to be sent to postgresql database succesfull for QUESTION 6.'''


#getting frequencies of each color
b2 =(join.count("BLUE"))
b3 =(join.count("BROWN"))
c =(join.count("CREAM"))
b=(join.count("BLACK"))
r =(join.count("RED"))
o =(join.count("ORANGE"))
y =(join.count("YELLOW"))
p =(join.count("PINK"))
g =(join.count("GREEN"))
w =(join.count("WHITE"))
b1 =(join.count("BLEW"))
a =(join.count("ARSH"))

# adding all the frequencies to a list
freqList =[a,b,b1,b2,b3,c,g,o,p,r,w,y]

# removing duplicates of colors to add to the database
newColors = []
for x in join:
    if x not in newColors:
        newColors.append(x)
#print(newColors)
 
# converting lists to dictionary
data = {newColors[i]: freqList[i] for i in range(len(newColors))}
 
# Printing resultant dictionary
print( str(data))