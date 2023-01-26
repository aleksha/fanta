#who="Mahom"
#who="J.Allen"
who="Burrow"
who="Tagovailoa"
who="J.Goff"
import re
import statistics as stat

stats   = []
player_num = 0

#"","Player","Team","Plays","EPA+CPOE composite","Adj. EPA/play","EPA/play","Success rate","Cmp%","Expected cmp%","CPOE","Air yards"
#"1","M.Stafford","","37","0.283","0.547","0.547","51.4%","73.3","63.6","9.7","10.7"
#data/EPA/2014/rbsdm.comstats_2014_01.csv

#"","Player","Team","Plays","EPA+CPOE composite","Adj. EPA/play","EPA/play","Success rate","Cmp%","Expected cmp%","CPOE","Air yards"
#"1","L.Jackson","","606","0.191","0.344","0.342","51.8%","68.7","64.8","3.8","8.8"
#data/EPA/seasons/rbsdm.comstats_2019.csv

def get_str( s ):
    return( s[1:-1] )

def get_int( s ):
    return( int( get_str(s) ) )

def get_float( s ):
    return( float( get_str(s) ) )

def get_pct( s ):
    return( float( 100.*float( get_str(s)[:-1] ) ) )

for season_year in range(2010,2023):
#    fname_full = "./data/EPA/" + str(season_year) + "/rbsdm.comstats_" + str(season_year) + "_" + str(week)+ ".txt"
    fname_full = "./data/EPA/seasons/rbsdm.comstats_" + str(season_year) + ".csv"

    f = open(fname_full,"r")


    is_header = True

    for line in f:
        if len(line)>1:
            w = line[:-1].split(",")
            if not is_header:
#"","Player","Team","Plays","EPA+CPOE composite","Adj. EPA/play","EPA/play","Success rate","Cmp%","Expected cmp%","CPOE","Air yards"
#"1","L.Jackson","","606","0.191","0.344","0.342","51.8%","68.7","64.8","3.8","8.8"
#data/EPA/seasons/rbsdm.comstats_2019.csv
                player = {
                    "name"  : get_str  ( w[ 1] ) ,
                    "season": season_year        ,
                    "plays" : get_int  ( w[ 3] ) ,
                    "pos"   : "QB"               ,
                    "aEPApp": get_float( w[ 5] ) ,
                    "EPApp" : get_float( w[ 6] ) ,
                    "air"   : get_float( w[11] ) }
                stats.append( player )
                player_num+=1
            if is_header and get_str(w[0])=="":
                is_header = False

    c=0
#    print("\t Season " + str(season_year) + " top 3 QB:")
    for pl in stats:
        if c<3 and pl["season"]==season_year:
#            print(pl)
            c+=1

    f.close()

for pl in stats:
    if re.search(who,pl["name"]):
        print( "\t" + str(pl["season"]) + "\t" + str(pl["plays"]) + "  " + str(pl["EPApp"]) + "  " + str(pl["EPApp"]*pl["plays"])  )
