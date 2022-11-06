stats   = []

mnl = 0
mnn = ""

def upn(p, m, n):
    if len(p["name"])>m:
        m = len(p["name"])
        n = p["name"]
    return m, n

def short_name( name, max_length = 25 ):
    v = name.split(" ")
    a = v[0] + " " + v[1]
    while len(a)<max_length:
        a += " "
    return a

players = []
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
                    "name"  : short_name( players[player_num][2] )        ,
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
                    "gm"    : int( w[2] )                   ,
                    "tgts"  : 0                             ,
                    "rec"   : 0                             ,
                    "reY"   : 0                             ,
                    "reTD"  : 0                             ,
                    "fum"   : 0                             }
                stats.append( player )
                mnl, mnn = upn( player, mnl, player["name"] )
                player_num+=1

print("\t Season data is loaded for QB")

players = []
player_num = 0
# rk id name team pos gms att yds avg td tgts rec yds td fum lst ppg ppr
for season_year in range(2010,2022):
    fname_full = "./data/season/rb/" + str(season_year) + ".txt"

    f = open(fname_full,"r")


    is_header = True

    for line in f:
        if len(line)>1:
            w = line[:-1].split("\t")
            if is_header and w[1]=="RB":
                is_header = False
            if is_header:
                players.append( w )
            if not is_header:
                player = {
                    "id"    : int( players[player_num][1] ) ,
                    "name"  : short_name( players[player_num][2] )        ,
                    "season": season_year                   ,
                    "team"  : w[0]                          ,
                    "pos"   : w[1]                          ,
                    "gm"    : int( w[ 2] )                  ,
                    "tgts"  : int( w[ 7] )                  ,
                    "rec"   : int( w[ 8] )                  ,
                    "reY"   : int( w[ 9] )                  ,
                    "reTD"  : int( w[10] )                  ,
                    "att"   : int( w[ 3] )                  ,
                    "ruY"   : int( w[ 4] )                  ,
                    "ruTD"  : int( w[ 6] )                  ,
                    "pas"   : 0                             ,
                    "cmt"   : 0                             ,
                    "paY"   : 0                             ,
                    "paTD"  : 0                             ,
                    "int"   : 0                             ,
                    "fum"   : int( w[11] )                  }
                stats.append( player )
                mnl, mnn = upn( player, mnl, player["name"] )
                player_num+=1


print("\t Season data is loaded for WR")

players = []
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
                    "name"  : short_name( players[player_num][2] )        ,
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
                    "pas"   : 0                             ,
                    "cmt"   : 0                             ,
                    "paY"   : 0                             ,
                    "paTD"  : 0                             ,
                    "int"   : 0                             ,
                    "fum"   : int( w[15] )                  }
                stats.append( player )
                mnl, mnn = upn( player, mnl, player["name"] )
                player_num+=1

print("\t Season data is loaded for TE")

players = []
player_num = 0
# rk id name team pos gms tgts rec pct yds td lng y/t y/r att yds avg td fum lst ppg ppr
for season_year in range(2010,2022):
    fname_full = "./data/season/wr/" + str(season_year) + ".txt"

    f = open(fname_full,"r")


    is_header = True

    for line in f:
        if len(line)>1:
            w = line[:-1].split("\t")
            if is_header and w[1]=="WR":
                is_header = False
            if is_header:
                players.append( w )
            if not is_header:
                player = {
                    "id"    : int( players[player_num][1] ) ,
                    "name"  : short_name( players[player_num][2] )        ,
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
                    "pas"   : 0                             ,
                    "cmt"   : 0                             ,
                    "paY"   : 0                             ,
                    "paTD"  : 0                             ,
                    "int"   : 0                             ,
                    "fum"   : int( w[15] )                  }
                stats.append( player )
                player_num+=1
                mnl, mnn = upn( player, mnl, player["name"] )

print("\t Season data is loaded for RB")

#print("\t Name with max length : "+str(mnn))
#print("\t               length : "+str(mnl))

