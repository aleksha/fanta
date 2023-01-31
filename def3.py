from parse_def import stats
from statistics import mean, stdev

h2 = ROOT.TH2F("hm","hm",18,-0.3,+0.3,18,-0.3,+0.3)

best = []
for pl in stats:
    if pl["season"]>2010 or pl["season"]<2022:
        best.append(pl)


reg = []
for bs in best:
    for pl in stats:
        if pl["team"]==bs["team"]:
            if pl["season"]+1==bs["season"]:
                h2.Fill( -bs["EPApp"], -pl["EPApp"]+bs["EPApp"])


h2.Draw()
print( "Correlation: " + str( h2.xycorr() ) )


