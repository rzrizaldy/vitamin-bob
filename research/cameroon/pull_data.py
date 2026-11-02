"""Pull the Cameroon indicators used in the Cameroon brief.

Sources: World Bank WDI API and the DHS Program API (2018 Cameroon DHS, EDSC-V).
Writes wdi_cmr.csv and dhs_cmr_2018.csv next to this file. Standard library only.

    python3 research/cameroon/pull_data.py
"""

import csv
import json
import urllib.request
from pathlib import Path

OUT = Path(__file__).parent

WDI = [
    "SP.POP.TOTL", "SP.RUR.TOTL.ZS", "NY.GDP.PCAP.CD",
    "IT.CEL.SETS.P2", "IT.NET.USER.ZS", "IT.NET.BBND.P2",
    "EG.ELC.ACCS.ZS", "EG.ELC.ACCS.RU.ZS", "EG.ELC.ACCS.UR.ZS",
    "SH.MED.PHYS.ZS", "SH.MED.NUMW.P3", "SH.XPD.CHEX.PC.CD", "SH.XPD.CHEX.GD.ZS", "SH.XPD.OOPC.CH.ZS",
    "SH.DYN.MORT", "SH.STA.MMRT", "SH.MLR.INCD.P3", "SH.TBS.INCD", "SH.STA.BRTC.ZS",
    "SP.DYN.LE00.IN", "SI.POV.DDAY",
]

DHS = {
    "RH_PAHC_W_PR1": "Women: any problem accessing health care",
    "RH_PAHC_W_MON": "Women: problem getting money for treatment",
    "RH_PAHC_W_DIS": "Women: problem with distance to facility",
    "HC_HEFF_H_MPH": "Households possessing a mobile phone",
    "CO_MOBB_W_MOB": "Women who own a mobile phone",
    "CO_MOBB_M_MOB": "Men who own a mobile phone",
    "ML_FEVT_C_ADV": "Children with fever: advice or treatment sought",
    "ML_FEVT_C_ADS": "Children with fever: advice or treatment sought same or next day",
    "ML_PMAL_C_RDT": "Malaria prevalence in children 6-59 months (RDT)",
}


def get(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.load(r)


def pull_wdi():
    rows = []
    for ind in WDI:
        data = get(f"https://api.worldbank.org/v2/country/CMR/indicator/{ind}?format=json&mrv=12&per_page=60")
        latest = next((r for r in (data[1] or []) if r["value"] is not None), None)
        if latest:
            rows.append({"indicator": ind, "name": latest["indicator"]["value"],
                         "year": latest["date"], "value": round(latest["value"], 2)})
    with open(OUT / "wdi_cmr.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["indicator", "name", "year", "value"])
        w.writeheader()
        w.writerows(rows)
    return len(rows)


def pull_dhs():
    url = ("https://api.dhsprogram.com/rest/dhs/data?countryIds=CM&surveyIds=CM2018DHS"
           f"&indicatorIds={','.join(DHS)}&breakdown=all&f=json&perpage=5000"
           "&returnFields=IndicatorId,Value,CharacteristicCategory,CharacteristicLabel")
    rows = [{"indicator": r["IndicatorId"], "name": DHS[r["IndicatorId"]],
             "breakdown": r["CharacteristicCategory"], "group": r["CharacteristicLabel"].lstrip("."),
             "value": r["Value"]}
            for r in get(url)["Data"]
            if r["CharacteristicCategory"] in ("Total", "Residence", "Region")]
    with open(OUT / "dhs_cmr_2018.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["indicator", "name", "breakdown", "group", "value"])
        w.writeheader()
        w.writerows(rows)
    return len(rows)


if __name__ == "__main__":
    print(f"WDI rows: {pull_wdi()}")
    print(f"DHS rows: {pull_dhs()}")
