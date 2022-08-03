import csv

import HSTB.resources

NOAAhydroaddresses = {}
fyle = open(HSTB.resources.PathToResource('forms/NOAAaddresses.csv'))

r = csv.reader(fyle)
for line in r:
    hydroUnitName, streetAddr, cityStateZip = line[1:4]
    NOAAhydroaddresses[hydroUnitName] = "\n".join([hydroUnitName, streetAddr, cityStateZip])

fyle.close()
NOAAfieldunitsAIbase = [" ".join(v.replace("NOAA", "").strip().replace("Ship", "").strip().split()[:-1]).lower() for v in NOAAhydroaddresses]

NOAAfieldunits = list(NOAAhydroaddresses.keys())
NOAAfieldunits.sort()  # attempt to list field units first, followed by offices
NOAAfieldunits.reverse()
NOAAfieldunits.append(NOAAfieldunits.pop(0))  # hack: PHB goes next to AHB
NOAAfieldunitsAIbase = [" ".join(v.replace("NOAA", "").strip().replace("Ship", "").strip().split()[:-1]).lower() for v in NOAAfieldunits]
