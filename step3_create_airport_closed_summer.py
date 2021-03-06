import pandas as pd
import os

year = 2020

month = 8

airports = ["Kiruna", "Umeo", "Sundsvall", "Ovik", "Malmo"]


cbh_threshold_mod = 92
cbh_threshold_sev = 60
cbh_threshold_Malmo_mod = 60    #for Malmo moderate threshold is the same as severe for other aiports
cbh_threshold_Malmo_sev = 30
cbh_threshold_dummy = -1

lcc_threshold_mod = 0.625
lcc_threshold_sev = 0.625
lcc_threshold_dummy = 2

tp_threshold_mod = 0.0025
tp_threshold_sev = 0.01
tp_threshold_dummy = 1000000

i10fg_threshold_light = 7.716667 # 15 knots
i10fg_threshold_mod = 12.86111 # 25 knots
i10fg_threshold_sev = 18.00556 # 35 knots
i10fg_threshold_dummy = 1000000

cape_threshold_light = 1000
cape_threshold_mod= 1000
cape_threshold_sev = 1000
cape_threshold_dummy = 100000000

#cp_threshold_light = 0.000075 ##0.075mm == 0.000075m
#cp_threshold_mod = 0.0025 ##2.5mm == 0.0025m
#cp_threshold_sev = 0.01 ##10mm = 0.01m
#cp_threshold_dummy = 1000000

cp_threshold_light = 0.00025
cp_threshold_mod = 0.00025
cp_threshold_sev = 0.00025
cp_threshold_dummy = 1000000





def set_thresholds(airport, cutoff):
    if cutoff == 0.5:
        if airport == "Kiruna":
            cbh_threshold = cbh_threshold_sev
            lcc_threshold = lcc_threshold_sev
            tp_threshold = tp_threshold_mod
            i10fg_threshold = i10fg_threshold_mod
            cape_threshold = cape_threshold_sev
            cp_threshold = cp_threshold_sev
        elif airport == "Umeo":
            cbh_threshold = cbh_threshold_sev
            lcc_threshold = lcc_threshold_sev
            tp_threshold = tp_threshold_mod
            i10fg_threshold = i10fg_threshold_sev
            cape_threshold = cape_threshold_sev
            cp_threshold = cp_threshold_sev
        elif airport == "Sundsvall":
            cbh_threshold = cbh_threshold_sev
            lcc_threshold = lcc_threshold_sev
            tp_threshold = tp_threshold_sev
            i10fg_threshold = i10fg_threshold_dummy
            cape_threshold = cape_threshold_sev
            cp_threshold = cp_threshold_sev
        elif airport == "Ovik":
            cbh_threshold = cbh_threshold_sev
            lcc_threshold = lcc_threshold_sev
            tp_threshold = tp_threshold_dummy
            i10fg_threshold = i10fg_threshold_dummy
            cape_threshold = cape_threshold_dummy
            cp_threshold = cp_threshold_dummy
        else: #Malmo
            cbh_threshold = cbh_threshold_Malmo_mod
            lcc_threshold = lcc_threshold_mod
            tp_threshold = tp_threshold_dummy
            i10fg_threshold = i10fg_threshold_sev
            cape_threshold = cape_threshold_light
            cp_threshold = cp_threshold_light
    elif cutoff == 0.4:
        if airport == "Kiruna":
            cbh_threshold = cbh_threshold_mod
            lcc_threshold = lcc_threshold_mod
            tp_threshold = tp_threshold_mod
            i10fg_threshold = i10fg_threshold_mod
            cape_threshold = cape_threshold_sev
            cp_threshold = cp_threshold_sev
        elif airport == "Umeo":
            cbh_threshold = cbh_threshold_mod
            lcc_threshold = lcc_threshold_mod
            tp_threshold = tp_threshold_mod
            i10fg_threshold = i10fg_threshold_mod
            cape_threshold = cape_threshold_sev
            cp_threshold = cp_threshold_sev
        elif airport == "Sundsvall":
            cbh_threshold = cbh_threshold_sev
            lcc_threshold = lcc_threshold_sev
            tp_threshold = tp_threshold_sev
            i10fg_threshold = i10fg_threshold_mod
            cape_threshold = cape_threshold_sev
            cp_threshold = cp_threshold_sev
        elif airport == "Ovik":
            cbh_threshold = cbh_threshold_sev
            lcc_threshold = lcc_threshold_sev
            tp_threshold = tp_threshold_sev
            i10fg_threshold = i10fg_threshold_dummy
            cape_threshold = cape_threshold_dummy
            cp_threshold = cp_threshold_dummy
        else: #Malmo
            cbh_threshold = cbh_threshold_Malmo_mod
            lcc_threshold = lcc_threshold_mod
            tp_threshold = tp_threshold_dummy
            i10fg_threshold = i10fg_threshold_mod
            cape_threshold = cape_threshold_light
            cp_threshold = cp_threshold_light
    elif cutoff == 0.3:
        if airport == "Kiruna":
            cbh_threshold = cbh_threshold_mod
            lcc_threshold = lcc_threshold_mod
            tp_threshold = tp_threshold_mod
            i10fg_threshold = i10fg_threshold_mod
            cape_threshold = cape_threshold_sev
            cp_threshold = cp_threshold_sev
        elif airport == "Umeo":
            cbh_threshold = cbh_threshold_mod
            lcc_threshold = lcc_threshold_mod
            tp_threshold = tp_threshold_mod
            i10fg_threshold = i10fg_threshold_mod
            cape_threshold = cape_threshold_sev
            cp_threshold = cp_threshold_sev
        elif airport == "Sundsvall":
            cbh_threshold = cbh_threshold_sev
            lcc_threshold = lcc_threshold_sev
            tp_threshold = tp_threshold_sev
            i10fg_threshold = i10fg_threshold_mod
            cape_threshold = cape_threshold_sev
            cp_threshold = cp_threshold_sev
        elif airport == "Ovik":
            cbh_threshold = cbh_threshold_sev
            lcc_threshold = lcc_threshold_sev
            tp_threshold = tp_threshold_sev
            i10fg_threshold = i10fg_threshold_mod
            cape_threshold = cape_threshold_sev
            cp_threshold = cp_threshold_sev
        else: #Malmo
            cbh_threshold = cbh_threshold_Malmo_mod
            lcc_threshold = lcc_threshold_mod
            tp_threshold = tp_threshold_dummy
            i10fg_threshold = i10fg_threshold_light
            cape_threshold = cape_threshold_light
            cp_threshold = cp_threshold_light
    elif cutoff == 0.2:
        if airport == "Kiruna":
            cbh_threshold = cbh_threshold_mod
            lcc_threshold = lcc_threshold_mod
            tp_threshold = tp_threshold_mod
            i10fg_threshold = i10fg_threshold_mod
            cape_threshold = cape_threshold_sev
            cp_threshold = cp_threshold_sev
        elif airport == "Umeo":
            cbh_threshold = cbh_threshold_mod
            lcc_threshold = lcc_threshold_mod
            tp_threshold = tp_threshold_mod
            i10fg_threshold = i10fg_threshold_mod
            cape_threshold = cape_threshold_sev
            cp_threshold = cp_threshold_sev
        elif airport == "Sundsvall":
            cbh_threshold = cbh_threshold_mod
            lcc_threshold = lcc_threshold_mod
            tp_threshold = tp_threshold_mod
            i10fg_threshold = i10fg_threshold_mod
            cape_threshold = cape_threshold_sev
            cp_threshold = cp_threshold_sev
        elif airport == "Ovik":
            cbh_threshold = cbh_threshold_sev
            lcc_threshold = lcc_threshold_sev
            tp_threshold = tp_threshold_sev
            i10fg_threshold = i10fg_threshold_light
            cape_threshold = cape_threshold_mod
            cp_threshold = cp_threshold_mod
        else: #Malmo
            cbh_threshold = cbh_threshold_Malmo_mod
            lcc_threshold = lcc_threshold_mod
            tp_threshold = tp_threshold_mod
            i10fg_threshold = i10fg_threshold_light
            cape_threshold = cape_threshold_light
            cp_threshold = cp_threshold_light
    elif cutoff == 0.6:
        if airport == "Kiruna":
            cbh_threshold = cbh_threshold_sev
            lcc_threshold = lcc_threshold_sev
            tp_threshold = tp_threshold_sev
            i10fg_threshold = i10fg_threshold_sev
            cape_threshold = cape_threshold_sev
            cp_threshold = cp_threshold_sev
        elif airport == "Umeo":
            cbh_threshold = cbh_threshold_sev
            lcc_threshold = lcc_threshold_sev
            tp_threshold = tp_threshold_sev
            i10fg_threshold = i10fg_threshold_dummy
            cape_threshold = cape_threshold_sev
            cp_threshold = cp_threshold_sev
        elif airport == "Sundsvall":
            cbh_threshold = cbh_threshold_sev
            lcc_threshold = lcc_threshold_sev
            tp_threshold = tp_threshold_sev
            i10fg_threshold = i10fg_threshold_dummy
            cape_threshold = cape_threshold_sev
            cp_threshold = cp_threshold_sev
        elif airport == "Ovik":
            cbh_threshold = cbh_threshold_dummy
            lcc_threshold = lcc_threshold_dummy
            tp_threshold = tp_threshold_dummy
            i10fg_threshold = i10fg_threshold_dummy
            cape_threshold = cape_threshold_dummy
            cp_threshold = cp_threshold_dummy
        else: #Malmo
            cbh_threshold = cbh_threshold_Malmo_sev
            lcc_threshold = lcc_threshold_sev
            tp_threshold = tp_threshold_dummy
            i10fg_threshold = i10fg_threshold_dummy
            cape_threshold = cape_threshold_light
            cp_threshold = cp_threshold_light
    elif cutoff == 0.7:
        if airport == "Kiruna":
            cbh_threshold = cbh_threshold_dummy
            lcc_threshold = lcc_threshold_dummy
            tp_threshold = tp_threshold_sev
            i10fg_threshold = i10fg_threshold_dummy
            cape_threshold = cape_threshold_sev
            cp_threshold = cp_threshold_sev
        elif airport == "Umeo":
            cbh_threshold = cbh_threshold_sev
            lcc_threshold = lcc_threshold_sev
            tp_threshold = tp_threshold_sev
            i10fg_threshold = i10fg_threshold_dummy
            cape_threshold = cape_threshold_sev
            cp_threshold = cp_threshold_sev
        elif airport == "Sundsvall":
            cbh_threshold = cbh_threshold_dummy
            lcc_threshold = lcc_threshold_dummy
            tp_threshold = tp_threshold_dummy
            i10fg_threshold = i10fg_threshold_dummy
            cape_threshold = cape_threshold_dummy
            cp_threshold = cp_threshold_dummy
        elif airport == "Ovik":
            cbh_threshold = cbh_threshold_dummy
            lcc_threshold = lcc_threshold_dummy
            tp_threshold = tp_threshold_dummy
            i10fg_threshold = i10fg_threshold_dummy
            cape_threshold = cape_threshold_dummy
            cp_threshold = cp_threshold_dummy
        else: #Malmo
            cbh_threshold = cbh_threshold_Malmo_sev
            lcc_threshold = lcc_threshold_sev
            tp_threshold = tp_threshold_dummy
            i10fg_threshold = i10fg_threshold_dummy
            cape_threshold = cape_threshold_light
            cp_threshold = cp_threshold_light
            
    return (cbh_threshold, lcc_threshold, tp_threshold, i10fg_threshold, cape_threshold, cp_threshold)




def isClosed(row, ens_member, cbh_threshold, lcc_threshold, tp_threshold, i10fg_threshold, cape_threshold, cp_threshold):
    
    #if row[4+ens_member] > cbh_threshold and row[14+ens_member] == lcc_threshold:
    if row[4+ens_member] < cbh_threshold and row[14+ens_member] > lcc_threshold:
        return 1

    if row[24+ens_member] > tp_threshold:
        return 1

    if row[34+ens_member] > i10fg_threshold:
        return 1

    if row[44+ens_member] > cape_threshold and row[54+ens_member] > cp_threshold:
        return 1

    return 0



def create_airport_close_file(airport, cutoff):
    
    data_dir = os.path.join("data", airport)

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    input_filename = os.path.join(data_dir, airport + '_' + str(year) + '_' + str(month) + '_ensemble_24hours.csv')

    output_filename = os.path.join(data_dir, airport + '_' + str(year) + '_' + str(month) + '_cutoff_' + str(cutoff) + '_closed.csv')


    df = pd.read_csv(input_filename, sep=' ')

    (cbh_threshold, lcc_threshold, tp_threshold, i10fg_threshold, cape_threshold, cp_threshold) = set_thresholds(airport, cutoff)

    ensemble = ['ens0', 'ens1', 'ens2', 'ens3', 'ens4', 'ens5', 'ens6', 'ens7', 'ens8', 'ens9']

    for ens in range(0,10):
        df[ensemble[ens]] = df.apply(lambda row: isClosed(row, ens, cbh_threshold, lcc_threshold, tp_threshold, i10fg_threshold, cape_threshold, cp_threshold), axis=1)
        
    cols = ['date', 'hour'] + ensemble
    df = df[cols]

    df['date'] = df['date'].astype(int)
    df['hour'] = df['hour'].astype(int)

    #print(df.head())

    df.to_csv(output_filename, sep=' ', encoding='utf-8', header=True, index=False)
    
    

cutoffs = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7]


for cutoff in cutoffs:
    for airport in airports:
        create_airport_close_file(airport, cutoff)
        

