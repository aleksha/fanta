fname = "./data/season/wr/2021.txt"

import re

f = open(fname,"r")

is_header = True

players = []
stats   = []
player_num = 0

for line in f:
    if len(line)>1:
        w = line[:-1].split("\t")
        if is_header and w[1]=="WR":
            is_header = False
        if is_header:
            players.append( w )
            #print(w)
        if not is_header:
            player = {
                "id"    : int( players[player_num][1] ) ,
                "name"  : players[player_num][2]        ,
                "season": int(fname.split(".")[0])      ,
                "team"  : w[0]                          ,
                "pos"   : w[1]                          ,
                "gm"    : int( w[2] )                   ,
                "tgts"  : int( w[3] )                   ,
                "rec"   : int( w[4] )                   ,
                "reY"   : int( w[6] )                   ,
                "reTD"  : int( w[7] )                   ,
                "att"   : int( w[11] )                  ,
                "ruY"   : int( w[12] )                  ,
                "ruTD"  : int( w[14] )                  ,
                "fum"   : int( w[15] )                  
            }
            stats.append( player )
            if player_num<10:
                print(w)
            player_num+=1

c=0
for pl in stats:
    if c<10:
        print(pl)
    c+=1
            
f.close()
