from load_data import stats as season_data
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

def select( id , season_data = season_data ):
    id_list = []
    for p in season_data:
        if p["id"] == id:
            id_list.append( p )
    return( sorted(id_list, key=lambda d: d['id'])  )
