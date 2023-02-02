
stats   = []

def get_str( s ):
    return( s[1:-1] )

def get_int( s ):
    return( int( get_str(s) ) )

def get_float( s ):
    return( float( get_str(s) ) )

def get_pct( s ):
    return( float( 0.01*float( get_str(s)[:-1] ) ) )

for season_year in range(2010,2023):
#    fname_full = "./data/EPA/" + str(season_year) + "/rbsdm.comstats_" + str(season_year) + "_" + str(week)+ ".txt"
    fname_full = "./data/EPA/seasons/rbsdm.comstats_def_" + str(season_year) + ".csv"

    f = open(fname_full,"r")


    is_header = True

    for line in f:
        if len(line)>1:
            w = line[:-1].split(",")
            if not is_header:
#"","Team","Abbr","EPA/play","Success Rate (SR)","Dropback EPA","Dropback SR","Rush EPA","Rush SR"

                player = {
                    "team"  : get_str  ( w[ 2] ) ,
                    "unit"  : "defense"          ,
                    "season": season_year        ,
                    "EPApp" : get_float( w[ 3] ) ,
                    "SR"    : get_pct  ( w[ 4] ) ,
                    "dEPA"  : get_float( w[ 5] ) ,
                    "dSR"   : get_pct  ( w[ 6] ) ,
                    "rEPApp": get_float( w[ 7] ) ,
                    "rSR"   : get_pct  ( w[ 8] ) }
                stats.append( player )
            if is_header and get_str(w[0])=="":
                is_header = False


    f.close()


    fname_full = "./data/EPA/seasons/rbsdm.comstats_off_" + str(season_year) + ".csv"
    f = open(fname_full,"r")

    is_header = True

    for line in f:
        if len(line)>1:
            w = line[:-1].split(",")
            if not is_header:
#"","Team","Abbr","EPA/play","Success Rate (SR)","Dropback EPA","Dropback SR","Rush EPA","Rush SR"

                player = {
                    "team"  : get_str  ( w[ 2] ) ,
                    "unit"  : "offense"          ,
                    "season": season_year        ,
                    "EPApp" : get_float( w[ 3] ) ,
                    "SR"    : get_pct  ( w[ 4] ) ,
                    "dEPA"  : get_float( w[ 5] ) ,
                    "dSR"   : get_pct  ( w[ 6] ) ,
                    "rEPApp": get_float( w[ 7] ) ,
                    "rSR"   : get_pct  ( w[ 8] ) }
                stats.append( player )
            if is_header and get_str(w[0])=="":
                is_header = False

    f.close()
