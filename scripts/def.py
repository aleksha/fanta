from parse_def import stats
from statistics import mean, stdev

hm = ROOT.TH1F("hm","hm",18,-0.3,+0.3)
hp = ROOT.TH1F("hp","hp",18,-0.3,+0.3)

best = []
for pl in stats:
    if pl["EPApp"]<-0.1:
        best.append(pl)


reg = []
for bs in best:
    for pl in stats:
        if pl["team"]==bs["team"] and pl["season"]-1==bs["season"]:
            #print(pl)
            #print(bs)
            #print("  ------- ")
            reg.append(pl["EPApp"]-bs["EPApp"])
            hp.Fill(pl["EPApp"]-bs["EPApp"])


reg2 = []
for bs in best:
    for pl in stats:
        if pl["team"]==bs["team"] and pl["season"]+1==bs["season"]:
            reg2.append(bs["EPApp"]-pl["EPApp"])
            hm.Fill(bs["EPApp"]-pl["EPApp"])
            if (bs["EPApp"]-pl["EPApp"])>0:
                print(pl)
                print(bs)
                print("  ======== ")


hm.red()

hp.Draw()
hm.Draw("same")


