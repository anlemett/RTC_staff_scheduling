import pandas as pd

year = 2019

month = 11

#airport = "Kiruna"
#airport = "Malmo"
#airport = "Ovik"
#airport = "Sundsvall"
airport = "Umeo"

metric1 = 'sd'
#old thresholds
sf_threshold_mod = 0.001
sf_threshold_sev = 0.002
#sf_threshold_mod = 0.001
#sf_threshold_sev = 0.0025

metric2 = 'cbh'
cbh_threshold_mod = 500
cbh_threshold_sev = 61    # 200 feet

metric3 = 'lcc'
lcc_threshold_mod = 0.9
lcc_threshold_sev = 1

metric4 = 'tp'
#old thresholds
tp_threshold_mod = 0.001
tp_threshold_sev = 0.002
#tp_threshold_mod = 0.0025
#tp_threshold_sev = 0.01

metric5 = 'i10fg'
i10fg_threshold_light = 7.716667 # 15 knots
i10fg_threshold_mod = 12.86111 # 25 knots
i10fg_threshold_sev = 18.00556 # 35 knots

if airport == "Kiruna":
    metric1_threshold = sf_threshold_mod
    metric2_threshold = cbh_threshold_sev
    metric3_threshold = lcc_threshold_sev
    metric4_threshold = tp_threshold_mod
    metric5_threshold = i10fg_threshold_light
elif airport == "Umeo":
    metric1_threshold = sf_threshold_mod
    metric2_threshold = cbh_threshold_sev
    metric3_threshold = lcc_threshold_sev
    metric4_threshold = tp_threshold_mod
    metric5_threshold = i10fg_threshold_mod
elif airport == "Sundsvall":
    metric1_threshold = sf_threshold_sev
    metric2_threshold = cbh_threshold_sev
    metric3_threshold = lcc_threshold_sev
    metric4_threshold = tp_threshold_sev
    metric5_threshold = i10fg_threshold_mod
elif airport == "Ovik":
    metric2_threshold = cbh_threshold_sev
    metric3_threshold = lcc_threshold_sev
else: #Malmo
    metric2_threshold = cbh_threshold_mod
    metric3_threshold = lcc_threshold_mod
    metric5_threshold = i10fg_threshold_sev

input_csv_filename = 'data/' + airport + '/' + airport + '_' + str(year) + '_' + str(month) + '_ensemble_24hours.csv'
output_csv_filename = 'data/' + airport + '/' + airport + '_' + str(year) + '_' + str(month) + '_closed.csv'


def isOvikClosed(row, ens_member):
    
    if row[14+ens_member] >= metric2_threshold and row[24+ens_member] == metric3_threshold:
        return 1

    return 0

def isMalmoClosed(row, ens_member):
    
    if row[14+ens_member] >= metric2_threshold and row[24+ens_member] >= metric3_threshold:
        return 1

    if row[44+ens_member] >= metric5_threshold:
        return 1

    return 0


def isClosed(row, ens_member):
    
    if airport == "Ovik":
        return isOvikClosed(row, ens_member)
    
    if airport == "Malmo":
        return isMalmoClosed(row, ens_member)


    if row[4+ens_member] >= metric1_threshold:
        return 1;

    if row[14+ens_member] >= metric2_threshold and row[24+ens_member] == metric3_threshold:
        return 1;

    if row[34+ens_member] >= metric4_threshold:
        return 1;

    if row[44+ens_member] >= metric5_threshold:
        return 1;

    return 0



df = pd.read_csv(input_csv_filename, sep=' ')

temp = df.isnull().sum()
#print(temp)


ensemble = ['ens0', 'ens1', 'ens2', 'ens3', 'ens4', 'ens5', 'ens6', 'ens7', 'ens8', 'ens9']

for ens in range(0,10):
    df[ensemble[ens]] = df.apply(lambda row: isClosed(row, ens), axis=1)
    
cols = ['date', 'hour'] + ensemble
df = df[cols]

#print(df.head())

df.to_csv(output_csv_filename, sep=' ', encoding='utf-8', header=True, index=False)

