def list_id( season_data, id ):
    for p in season_data:
        if p["id"] == id:
            print( p )
