#!/usr/bin/env python3

import requests

dois = [
    "10.1016/S0020-7519(02)00022-X", "10.1371/journal.pone.0174632", "10.7717/peerj.8853",
    "10.1038/srep30349", "10.1007/s11274-011-0979-9", "10.1099/mic.0.2008/017665-0",
    "10.1371/journal.pone.0193720", "10.1016/j.pbi.2008.05.005", "10.3389/fmicb.2020.00857",
    "10.1007/s00248-009-9511-2", "10.3389/fpls.2016.00144", "10.1111/tpj.12777",
    "10.3389/fpls.2016.00144", "10.1186/s13568-017-0453-7", "10.1128/AEM.00295-09",
    "10.1128/AEM.67.5.2380-2383.2001", "10.1038/s41598-017-08589-4", "10.1038/ismej.2011.69",
    "10.1021/ar900127h", "10.1371/journal.pgen.1002430", "10.1073/pnas.1706371114",
    "10.1126/science.1162018", "10.1128/AEM.71.5.2530-2538.2005", "10.1093/nar/gkq652",
    "10.3390/molecules24244613", "10.1093/aob/mcx162", "10.1093/aob/mcx162",
    "10.1128/AEM.03160-15", "10.1186/2193-1801-2-587", "10.3389/fphys.2017.00667",
    "10.1016/j.btre.2019.e00406", "10.1186/2193-1801-1-26", "10.1007/s42770-019-00043-z",
    "10.1371/journal.pone.0060075", "10.1016/j.tplants.2010.05.007", "10.1038/srep12732",
    "10.1371/journal.pone.0208975", "10.1371/journal.pone.0210478", "10.1371/journal.pone.0210478",
    "10.1590/s1517-83822014000300019", "10.1186/s40168-017-0390-3"
]

def get_bibtex(doi):
    url = f"https://doi.org/{doi}"
    headers = {"Accept": "application/x-bibtex"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return f"Error retrieving DOI {doi}: {response.status_code}"

#write results to a file
with open("references.bib", "w", encoding="utf-8") as bibfile:
    for doi in dois:
        bibtex = get_bibtex(doi)
        bibfile.write(bibtex + "\n\n")
        print(f"Retrieved: {doi}")

print("Done! check 'references.bib' file")
