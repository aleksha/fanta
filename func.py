from load_data import stats as season_data
from load_epa_teams import stats as season_epa_team_data
from parse_epa      import stats as season_epa_QB_data
from scoring import scoring
import re

def find_name( id, season_data = season_data ):
    for p in season_data:
        if p["id"] == id:
            return( p["name"] )

def find_id( request , season_data = season_data ):
    id_list = []
    for p in season_data:
        if re.search( request, p["name"] ) :
            if p["id"] not in id_list:
                id_list.append( p["id"] )
                print( str(p["id"]) + "\t" + p["pos"] + "\t" + p["name"] )

def find( what, season_data = season_data ):
    if type(what) is int:
        return( find_name( what, season_data ) )
    if type(what) is str:
        return( find_id( what, season_data ) )
    return 0

def select( id , season_data = season_data ):
    id_list = []
    for p in season_data:
        if p["id"] == id:
            id_list.append( p )
    return( sorted(id_list, key=lambda d: d['id'])  )

def i2s(n):
    if n<10:
        return( str("    ")+str(n) )
    if n<100:
        return( str("   ")+str(n) )
    if n<1000:
        return( str("  ")+str(n) )
    return( str(" ")+str(n) )


def info( id , season_data = season_data ):
    id_list = select( id, season_data )
    if not len(id_list):
        return( 0 )
    print(" ======================================================================================")
    print(" | " + id_list[0]["name"] + "  ( " + id_list[0]["pos"] + " )" )
    print(" ======================================================================================")
    print(" | year |  GMS |  Cmp  Pas  Yds   TD  Fum | Tgts  Rec  Yds   TD |  Att  Yds   TD  Fum |")
    print(" ======================================================================================")
    for p in id_list:
        ss  = " | " + str(p["season"]) + " |"  + i2s(p["gm"]) + " |"
        ss += i2s(p["cmt"]) + i2s(p["pas"]) + i2s(p["paY"]) + i2s(p["paTD"]) + i2s(p["int"]) + " |"
        ss += i2s(p["tgts"])+ i2s(p["rec"]) + i2s(p["reY"]) + i2s(p["reTD"]) + " |"
        ss += i2s(p["att"]) + i2s(p["ruY"]) + i2s(p["ruTD"]) + i2s(p["fum"]) + " |"
        print( ss )
    print(" ======================================================================================")
    return( 1 )


def calc( p , s = scoring ):
    ss  = p["paY"]*s["paY"] + p["paTD"]*s["paTD"] + p["int"]*s["int"]
    ss += p["rec"]*s["rec"] + p["reY"]*s["reY"]   + p["reTD"]*s["reTD"]
    ss += p["ruY"]*s["ruY"] + p["ruTD"]*s["ruTD"] + p["fum"]*s["fum"]
    return( int(ss) )

def fantasy( id , season_data = season_data , s = scoring ):
    id_list = select( id, season_data )
    if not len(id_list):
        return( 0 )
    print(" =============================================================================================")
    print(" | " + id_list[0]["name"] + "  ( " + id_list[0]["pos"] + " )" )
    print(" =============================================================================================")
    print(" | year |  GMS |                                                                             |")
    print(" =============================================================================================")
    for p in id_list:
        ss  = " | " + str(p["season"]) + " |"  + i2s(p["gm"]) + " |"
        ss += i2s(p["paY"]*s["paY"]) + i2s(p["paTD"]*s["paTD"]) + i2s(p["int"]*s["int"])   + " |"
        ss += i2s(p["rec"]*s["rec"]) + i2s(p["reY"]*s["reY"])   + i2s(p["reTD"]*s["reTD"]) + " |"
        ss += i2s(p["ruY"]*s["ruY"]) + i2s(p["ruTD"]*s["ruTD"]) + i2s(p["fum"]*s["fum"])   + " |"
        ss += i2s( calc(p,scoring) ) + " |"
        print( ss )
    print(" =============================================================================================")
    return( 1 )


def top( year, pos, num=28, season_data = season_data , s = scoring ):
    id_list = []
    for p in season_data:
        if p["season"] == year and p["pos"] == pos:
            id_list.append( { "player": p, "fps": calc(p, scoring) } )
    nl =  sorted(id_list, key=lambda d: -d['fps'])
    print(" Top " + str(num) + " " + pos + " of " + str(year) + " :")
    print(" -------------------------------------------------------")
    for i in range(num):
        print( " " + str( nl[i]["player"]["name"] ) + "\t" + str(nl[i]["fps"]) )

def agregate_fps( years, pos, season_data = season_data , scoring = scoring ):
    id_list = []
    answer = []
    for year in years:
        for p in season_data:
            if p["season"] == year and p["pos"] == pos:
                if p["id"] not in id_list:
                    curret_id = p["id"]
                    np = {"id":p["id"], "name":p["name"], "fps":0., "gm":0}
                    for pp in season_data:
                        if pp["season"] in years:
                            if pp["id"]==curret_id:
                                np["fps"] += calc(pp, scoring)
                                np["gm"] += pp["gm"]
                    id_list.append(curret_id)
                    answer.append( np )
    return(answer)


def make_top(years, pos, max_gm=12, num = 36, season_data=season_data, scoring=scoring):
    a = agregate_fps(years,pos,season_data,scoring)
    b = []
    for p in a:
        p["fpsgm"]=p["fps"]/float(p["gm"])
        if p["gm"]>=max_gm:
            b.append(p)
    c = sorted(b,key=lambda d: -d["fpsgm"])
    for i in range(num):
        print(c[i])
        if i==11 or i==23:
            print()
    return(c)

def search_top(name,lst):
    for p in lst:
        if re.search(name,p["name"]):
            print(lst.index(p)+1)
            print(p)

