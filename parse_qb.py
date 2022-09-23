import re
import statistics as stat

players = []
stats   = []
player_num = 0

# rk id name team pos gms cmp pas pct yds avg td int rat att yds avg td ppg ppr
#            0    1   2   3   4   5   6   7   8  9   10  11  12  13  14  15  16
for season_year in range(2010,2022):
    fname_full = "./data/season/qb/" + str(season_year) + ".txt"

    f = open(fname_full,"r")


    is_header = True

    for line in f:
        if len(line)>1:
            w = line[:-1].split("\t")
            if is_header and w[1]=="QB":
                is_header = False
            if is_header:
                players.append( w )
            if not is_header:
                player = {
                    "id"    : int( players[player_num][1] ) ,
                    "name"  : players[player_num][2]        ,
                    "season": season_year                   ,
                    "team"  : w[0]                          ,
                    "pos"   : w[1]                          ,
                    "gm"    : int( w[2] )                   ,
                    "pas"   : int( w[4] )                   ,
                    "cmt"   : int( w[3] )                   ,
                    "paY"   : int( w[6] )                   ,
                    "paTD"  : int( w[8] )                   ,
                    "int"   : int( w[9] )                   ,
                    "att"   : int( w[11] )                  ,
                    "ruY"   : int( w[12] )                  ,
                    "ruTD"  : int( w[14] )                  ,
                    "fum"   : 0                             }
                stats.append( player )
                player_num+=1

    c=0
    print("\t Season " + str(season_year) + " top 3 QB:")
    for pl in stats:
        if c<3 and pl["season"]==season_year:
            print(pl)
            c+=1

    f.close()

for pl in stats:
    if pl["id"]==18018:
        print( "\t" + str(pl["season"]) + "\t" + str(pl["paY"]) + "  " + str(pl["paY"]/pl["pas"]) + "  " + str(pl["paY"])  )
