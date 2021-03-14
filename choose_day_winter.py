import pandas as pd
import os

year = 2020

month = 2


Kiruna_input_dir = os.path.join('data', 'Kiruna')
Umeo_input_dir = os.path.join('data', 'Umeo')
Sundsvall_input_dir = os.path.join('data', 'Sundsvall')
Ovik_input_dir = os.path.join('data', 'Ovik')
Malmo_input_dir = os.path.join('data', 'Malmo')

Kiruna_input_filename = os.path.join(Kiruna_input_dir, 'Kiruna_' + str(year) + '_' + str(month) + '_ensemble.csv')
Umeo_input_filename = os.path.join(Umeo_input_dir, 'Umeo_' + str(year) + '_' + str(month) + '_ensemble.csv')
Sundsvall_input_filename = os.path.join(Sundsvall_input_dir, 'Sundsvall_' + str(year) + '_' + str(month) + '_ensemble.csv')
Ovik_input_filename = os.path.join(Ovik_input_dir, 'Ovik_' + str(year) + '_' + str(month) + '_ensemble.csv')
Malmo_input_filename = os.path.join(Malmo_input_dir, 'Malmo_' + str(year) + '_' + str(month) + '_ensemble.csv')


df_Kiruna = pd.read_csv(Kiruna_input_filename, sep=' ')
df_Umeo = pd.read_csv(Umeo_input_filename, sep=' ')
df_Sundsvall = pd.read_csv(Sundsvall_input_filename, sep=' ')
df_Ovik = pd.read_csv(Ovik_input_filename, sep=' ')
df_Malmo = pd.read_csv(Malmo_input_filename, sep=' ')


sf_threshold_mod = 0.001
sf_threshold_sev = 0.0025
sf_threshold_dummy = 1000000

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


sf_threshold = sf_threshold_mod

cbh_threshold = cbh_threshold_sev
lcc_threshold = lcc_threshold_sev

tp_threshold = tp_threshold_mod

i10fg_threshold = i10fg_threshold_mod


def isClosed(row, ens_member):
    
    if row[4+ens_member] > sf_threshold:
        if row['day'] == 16 and row['hour'] == 15: # 18, 21
            print(ens_member, 'snow')
        return 1

    if row[14+ens_member] < cbh_threshold and row[24+ens_member] > lcc_threshold:
        if row['day'] == 16 and row['hour'] == 15: # 18, 21
            print(ens_member, 'visibility')
        return 1

    if row[34+ens_member] > tp_threshold:
        if row['day'] == 16 and row['hour'] == 15: # 18, 21
            print(ens_member, 'tp')
        return 1

    if row[44+ens_member] > i10fg_threshold:
        if row['day'] == 16 and row['hour'] == 15: # 18, 21
            print(ens_member, 'wind')
        return 1

    return 0


ensemble = ['ens0', 'ens1', 'ens2', 'ens3', 'ens4', 'ens5', 'ens6', 'ens7', 'ens8', 'ens9']

for ens in range(0,10):
    df_Kiruna[ensemble[ens]] = df_Kiruna.apply(lambda row: isClosed(row, ens), axis=1)
    df_Umeo[ensemble[ens]] = df_Umeo.apply(lambda row: isClosed(row, ens), axis=1)
    df_Sundsvall[ensemble[ens]] = df_Sundsvall.apply(lambda row: isClosed(row, ens), axis=1)
    df_Ovik[ensemble[ens]] = df_Ovik.apply(lambda row: isClosed(row, ens), axis=1)
    df_Malmo[ensemble[ens]] = df_Malmo.apply(lambda row: isClosed(row, ens), axis=1)

#df_Kiruna = df_Kiruna[['day', 'hour', 'ens0', 'ens1', 'ens2', 'ens3', 'ens4', 'ens5', 'ens6', 'ens7', 'ens8', 'ens9']]
#df_Umeo = df_Umeo[['day', 'hour', 'ens0', 'ens1', 'ens2', 'ens3', 'ens4', 'ens5', 'ens6', 'ens7', 'ens8', 'ens9']]
#df_Sundsvall = df_Sundsvall[['day', 'hour', 'ens0', 'ens1', 'ens2', 'ens3', 'ens4', 'ens5', 'ens6', 'ens7', 'ens8', 'ens9']]
#df_Ovik = df_Ovik[['day', 'hour', 'ens0', 'ens1', 'ens2', 'ens3', 'ens4', 'ens5', 'ens6', 'ens7', 'ens8', 'ens9']]
#df_Malmo = df_Malmo[['day', 'hour', 'ens0', 'ens1', 'ens2', 'ens3', 'ens4', 'ens5', 'ens6', 'ens7', 'ens8', 'ens9']]

df_Kiruna = df_Kiruna[['day', 'hour', 'ens0']]
df_Umeo = df_Umeo[['ens0']]
df_Sundsvall = df_Sundsvall[['ens0']]
df_Ovik = df_Ovik[['ens0']]
df_Malmo = df_Malmo[['ens0']]

temp_df = pd.concat([df_Kiruna, df_Umeo, df_Sundsvall, df_Ovik, df_Malmo], axis = 1)

temp_df.to_csv('choose_day_winter_temp.csv', sep=' ', encoding='utf-8', header=True, index=False)
