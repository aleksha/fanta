from parse_def import stats
from statistics import mean, stdev

hm = ROOT.TH1F("hm","hm",60,-0.3,+0.3)

best = []
for pl in stats:
    hm.Fill( pl["EPApp"] )

hm.Draw("E1")
hm.Fit("gaus")


