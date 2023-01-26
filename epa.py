import matplotlib.pyplot as plt
from parse_epa import stats
import ROOT

h = ROOT.TH1F("h",";EPA/play;Entries",45,-0.45,0.45)

epa = []
for pl in stats:
    if pl["plays"]<300:
        epa.append( pl["EPApp"] )
        h.Fill( pl["EPApp"] )
        if pl["EPApp"]>0.25:
            print( str(pl["season"]) + "  " + pl["name"] + "\t\t"+ str(pl["EPApp"]) )

h.Draw("E1")
h.Fit("gaus")
#num_bins = 30
#n, bins, patches = plt.hist(epa, num_bins, facecolor='blue', alpha=0.5)
#plt.show()
