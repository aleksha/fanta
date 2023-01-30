search_for = (2022, "A.Rodgers")
x_pos = -0.5 ; y_pos = 7


import matplotlib.pyplot as plt
from parse_epa import stats
import ROOT

MVPs =  [ (2010,"T.Brady"), (2011,"A.Rodgers"), (2012, "A.Peterson"),
          (2013,"P.Manning"), (2014,"A.Rodgers"), (2015,"C.Newton"),
          (2016,"M.Ryan"), (2017,"T.Brady"), (2018,"P.Mahomes"),
          (2019,"L.Jackson"), (2020,"A.Rodgers"), (2021,"A.Rodgers") ]

h  = ROOT.TH1F("h",";EPA/play;QBs with >300 plays in regular season (since 2010)",45,-0.45,0.45)
hm = ROOT.TH1F("hm",";;",45,-0.45,0.45)
hm.SetLineColor(2), hm.SetFillColor(2), hm.SetFillStyle(3005)

epa = []
for pl in stats:
    if pl["plays"]>300:
        epa.append( pl["EPApp"] )
        h.Fill( pl["EPApp"] )
        if (pl["season"],pl["name"]) in MVPs:
            hm.Fill( pl["EPApp"] )
        if (pl["season"],pl["name"])==search_for:
            x_pos = pl["EPApp"]
        if pl["EPApp"]>0.25:
            print( str(pl["season"]) + "  " + pl["name"] + "\t\t"+ str(pl["EPApp"]) )

h.GetXaxis().SetTitleSize(0.04) ; h.GetXaxis().SetTitleOffset(1.15)
h.GetYaxis().SetTitleSize(0.04) ; h.GetYaxis().SetTitleOffset(1.15)

canv = ROOT.TCanvas("canv","canv",800,800)
h.Draw("E1")
r = h.Fit("gaus","S")
hm.Draw("hist same")

print( r )

t_MVPs = ROOT.TLatex(0.125,2,"MVPs")
t_MVPs.SetTextSize(0.04)
t_MVPs.SetTextColor(2)
t_MVPs.Draw()

#t_mu = ROOT.TLatex(-0.4,30,"#mu = "+"{:.3f}".format(r[1].value()) + " #pm "+ "{:.3f}".format(r[1].error()) )
t_mu = ROOT.TLatex(-0.4,30,"mean = "+"{:.3f}".format(h.GetMean() )  )
t_mu.SetTextSize(0.04)
t_mu.Draw()

#t_st = ROOT.TLatex(-0.4,27,"#sigma = "+"{:.3f}".format(r[2].value()) + " #pm "+ "{:.3f}".format(r[2].error()) )
t_st = ROOT.TLatex(-0.4,27,"rms  = "+"{:.3f}".format(h.GetRMS() ) )
t_st.SetTextSize(0.04)
t_st.Draw()

l_search = ROOT.TArrow( x_pos, y_pos , x_pos, 0 )
l_search.SetLineWidth(3)
l_search.SetLineColor(4)
l_search.Draw()

t_search = ROOT.TLatex(x_pos-0.025, y_pos + 1, search_for[1]+", "+str(search_for[0]) )
t_search.SetTextSize(0.04)
t_search.SetTextColor(4)
t_search.Draw()


print(search_for)
print(x_pos)



#num_bins = 30
#n, bins, patches = plt.hist(epa, num_bins, facecolor='blue', alpha=0.5)
#plt.show()
