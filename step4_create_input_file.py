import pandas as pd

year = 2020

#month = 7
#date = 20200729
#hour_start = 8
#hour_end = 16

month = 2
date = 20200216
hour_start = 12
hour_end = 20


output_csv_dir = 'data/' + str(year) + '_' + str(month)

Kiruna_input_csv_filename = 'data/Kiruna/Kiruna_' + str(year) + '_' + str(month) + '_closed.csv'
Malmo_input_csv_filename = 'data/Malmo/Malmo_' + str(year) + '_' + str(month) + '_closed.csv'
Ovik_input_csv_filename = 'data/Ovik/Ovik_' + str(year) + '_' + str(month) + '_closed.csv'
Sundsvall_input_csv_filename = 'data/Sundsvall/Sundsvall_' + str(year) + '_' + str(month) + '_closed.csv'
Umeo_input_csv_filename = 'data/Umeo/Umeo_' + str(year) + '_' + str(month) + '_closed.csv'


df_Kiruna = pd.read_csv(Kiruna_input_csv_filename, sep=' ')
df_Malmo = pd.read_csv(Malmo_input_csv_filename, sep=' ')
df_Ovik = pd.read_csv(Ovik_input_csv_filename, sep=' ')
df_Sundsvall = pd.read_csv(Sundsvall_input_csv_filename, sep=' ')
df_Umeo = pd.read_csv(Umeo_input_csv_filename, sep=' ')


df_Kiruna = df_Kiruna[df_Kiruna['date']==date]
df_Kiruna = df_Kiruna[df_Kiruna['hour']>=hour_start]
df_Kiruna = df_Kiruna[df_Kiruna['hour']<=hour_end]

df_Malmo = df_Malmo[df_Malmo['date']==date]
df_Malmo = df_Malmo[df_Malmo['hour']>=hour_start]
df_Malmo = df_Malmo[df_Malmo['hour']<=hour_end]

df_Ovik = df_Ovik[df_Ovik['date']==date]
df_Ovik = df_Ovik[df_Ovik['hour']>=hour_start]
df_Ovik = df_Ovik[df_Ovik['hour']<=hour_end]

df_Sundsvall = df_Sundsvall[df_Sundsvall['date']==date]
df_Sundsvall = df_Sundsvall[df_Sundsvall['hour']>=hour_start]
df_Sundsvall = df_Sundsvall[df_Sundsvall['hour']<=hour_end]

df_Umeo = df_Umeo[df_Umeo['date']==date]
df_Umeo = df_Umeo[df_Umeo['hour']>=hour_start]
df_Umeo = df_Umeo[df_Umeo['hour']<=hour_end]


col_lst = []
for h in range(hour_start, hour_end+1):
    col_lst.append(str(h))


for ens in range(0,10):
    
    ampl_input_df = pd.DataFrame(columns=col_lst)
    
    col = 'ens' + str(ens)
    output_csv_filename = output_csv_dir + '/ens' + str(ens) + '/input.dat'
    
    Kiruna_lst = df_Kiruna[col].tolist()
    ampl_input_df = ampl_input_df.append(pd.DataFrame([Kiruna_lst], columns=ampl_input_df.columns), ignore_index=True)

    Umeo_lst = df_Umeo[col].tolist()
    ampl_input_df = ampl_input_df.append(pd.DataFrame([Umeo_lst], columns=ampl_input_df.columns), ignore_index=True)

    Sundsvall_lst = df_Sundsvall[col].tolist()
    ampl_input_df = ampl_input_df.append(pd.DataFrame([Sundsvall_lst], columns=ampl_input_df.columns), ignore_index=True)

    Ovik_lst = df_Ovik[col].tolist()
    ampl_input_df = ampl_input_df.append(pd.DataFrame([Ovik_lst], columns=ampl_input_df.columns), ignore_index=True)

    Malmo_lst = df_Malmo[col].tolist()
    ampl_input_df = ampl_input_df.append(pd.DataFrame([Malmo_lst], columns=ampl_input_df.columns), ignore_index=True)
    
    ampl_input_df.to_csv(output_csv_filename, sep=' ', encoding='utf-8', header=False, index=False)


