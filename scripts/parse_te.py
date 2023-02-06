import re
import statistics as stat

players = []
stats   = []
player_num = 0

# rk id name team pos gms tgts rec pct yds td lng y/t y/r att yds avg td fum lst ppg ppr
for season_year in range(2010,2022):
    fname_full = "./data/season/te/" + str(season_year) + ".txt"

    f = open(fname_full,"r")


    is_header = True

    for line in f:
        if len(line)>1:
            w = line[:-1].split("\t")
            if is_header and w[1]=="TE":
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
                    "tgts"  : int( w[3] )                   ,
                    "rec"   : int( w[4] )                   ,
                    "reY"   : int( w[6] )                   ,
                    "reTD"  : int( w[7] )                   ,
                    "att"   : int( w[11] )                  ,
                    "ruY"   : int( w[12] )                  ,
                    "ruTD"  : int( w[14] )                  ,
                    "fum"   : int( w[15] )                  }
                stats.append( player )
                player_num+=1

    c=0
    print("\t Season " + str(season_year) + " top 3 TE:")
    for pl in stats:
        if c<3 and pl["season"]==season_year:
            print(pl)
            c+=1

    f.close()

for pl in stats:
    if pl["id"]==18882:
        print( "\t" + str(pl["season"]) + "\t" + str(pl["reY"]) + "  " + str(pl["reY"]/pl["tgts"]) )
