
#"3",1,"Antonio Brown",FA,"WR1","1","11","4.3","1.7","+2"
player1 = "Antonio Brown"
player2 = "Julio Jones"
player3 = "A.J. Green"
player4 = "Dez Bryant"
player5 = "Demaryius Thomas"
player6 = "Odell Beckham Jr."
player7 = "DeAndre Hopkins"

import re
import matplotlib.pyplot as plt

path         = "data/fpros/Dynasty/"
name_prefix  = "FantasyPros_"
name_postfix = "_Dynasty_ALL_Rankings.csv"

x1 = [] ; y1 = []
x2 = [] ; y2 = []
x3 = [] ; y3 = []
x4 = [] ; y4 = []
x5 = [] ; y5 = []
x6 = [] ; y6 = []
x7 = [] ; y7 = []

for year in range(2012,2023):
    name_suffix = str(year)
    full_path = path + name_prefix + name_suffix + name_postfix
    with open(full_path,"r") as fl:
        for line in fl:
            w = line[:-1].split(",")
            if w[2][1:-1] == player1:
                x1.append( year )
                y1.append( int(w[4][3:-1]))
            if w[2][1:-1] == player2:
                x2.append( year )
                y2.append( int(w[4][3:-1]))
            if w[2][1:-1] == player3:
                x3.append( year )
                y3.append( int(w[4][3:-1]))
            if w[2][1:-1] == player4:
                x4.append( year )
                y4.append( int(w[4][3:-1]))
            if w[2][1:-1] == player5:
                x5.append( year )
                y5.append( int(w[4][3:-1]))
            if w[2][1:-1] == player6:
                x6.append( year )
                y6.append( int(w[4][3:-1]))
            if w[2][1:-1] == player7:
                x7.append( year )
                y7.append( int(w[4][3:-1]))

plt.plot(x1,y1,"r-",label=player1)
plt.plot(x2,y2,"b-",label=player2)
plt.plot(x3,y3,"g-",label=player3)
plt.plot(x4,y4,"y-",label=player4)
plt.plot(x5,y5,"c-",label=player5)
plt.plot(x6,y6,"m-",label=player6)
plt.plot(x7,y7,"k-",label=player7)
plt.legend(loc="upper left")
plt.xlabel("Season")
plt.ylabel("End of season FantasyPros dynasty ranking at position")
plt.grid()
plt.show()
