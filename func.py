from load_data import stats as season_data
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

def fantasy( id , season_data = season_data , s = scoring ):
    id_list = select( id, season_data )
    if not len(id_list):
        return( 0 )
    print(" ======================================================================================")
    print(" | " + id_list[0]["name"] + "  ( " + id_list[0]["pos"] + " )" )
    print(" ======================================================================================")
    print(" | year |  GMS |                                                                      |")
    print(" ======================================================================================")
    for p in id_list:
        ss  = " | " + str(p["season"]) + " |"  + i2s(p["gm"]) + " |"
        ss += i2s(p["paY"]*s["paY"]) + i2s(p["paTD"]*s["paTD"]) + i2s(p["int"]*s["int"]) + " |"
        ss += i2s(p["rec"]*s["rec"]) + i2s(p["reY"]*s["reY"]) + i2s(p["reTD"]*s["reTD"]) + " |"
        ss += i2s(p["ruY"]*s["ruY"]) + i2s(p["ruTD"]*s["ruTD"]) + i2s(p["fum"]*s["fum"]) + " |"
        print( ss )
    print(" ======================================================================================")
    return( 1 )


