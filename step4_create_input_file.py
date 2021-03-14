import pandas as pd
import os

year = 2020
'''
month = 2
date = 20200216
hour_start = 6
hour_end = 14

month = 7
date = 20200729
hour_start = 14
hour_end = 22

month = 7
date = 20200709
hour_start = 6
hour_end = 14
'''
month = 8
date = 20200819
hour_start = 6
hour_end = 14


Kiruna_input_dir = os.path.join('data', 'Kiruna')
Umeo_input_dir = os.path.join('data', 'Umeo')
Sundsvall_input_dir = os.path.join('data', 'Sundsvall')
Ovik_input_dir = os.path.join('data', 'Ovik')
Malmo_input_dir = os.path.join('data', 'Malmo')

cutoffs = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7]


for cutoff in cutoffs:
    
    output_dir = os.path.join('data', str(date) + '_hours_' + str(hour_start) + '_' + str(hour_end) + '_cutoff_' + str(cutoff))

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    Kiruna_input_filename = os.path.join(Kiruna_input_dir, 'Kiruna_' + str(year) + '_' + str(month) + '_cutoff_' + str(cutoff) +  '_closed.csv')
    Umeo_input_filename = os.path.join(Umeo_input_dir, 'Umeo_' + str(year) + '_' + str(month) + '_cutoff_' + str(cutoff) +  '_closed.csv')
    Sundsvall_input_filename = os.path.join(Sundsvall_input_dir, 'Sundsvall_' + str(year) + '_' + str(month) + '_cutoff_' + str(cutoff) +  '_closed.csv')
    Ovik_input_filename = os.path.join(Ovik_input_dir, 'Ovik_' + str(year) + '_' + str(month) + '_cutoff_' + str(cutoff) +  '_closed.csv')
    Malmo_input_filename = os.path.join(Malmo_input_dir, 'Malmo_' + str(year) + '_' + str(month) + '_cutoff_' + str(cutoff) +  '_closed.csv')
                                                                   

    df_Kiruna = pd.read_csv(Kiruna_input_filename, sep=' ')
    df_Malmo = pd.read_csv(Malmo_input_filename, sep=' ')
    df_Ovik = pd.read_csv(Ovik_input_filename, sep=' ')
    df_Sundsvall = pd.read_csv(Sundsvall_input_filename, sep=' ')
    df_Umeo = pd.read_csv(Umeo_input_filename, sep=' ')


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
        
        ens_dir = os.path.join(output_dir, 'ens' + str(ens))
        if not os.path.exists(ens_dir):
            os.makedirs(ens_dir)
            
        output_filename = os.path.join(ens_dir, 'input.dat')
        
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
        
        #print(Malmo_lst)
        
        ampl_input_df.to_csv(output_filename, sep=' ', encoding='utf-8', header=False, index=False)
        
        #print(ampl_input_df.head())
        

        '''
        df_Kiruna = df_Kiruna.drop('date', 1)
        df_Malmo = df_Malmo.drop('date', 1)
        df_Ovik = df_Ovik.drop('date', 1)
        df_Sundsvall = df_Sundsvall.drop('date', 1)
        df_Umeo = df_Umeo.drop('date', 1)
        pd.set_option('display.max_columns', 500)
        print(df_Kiruna)
        print(df_Malmo)
        print(df_Ovik)
        print(df_Sundsvall)
        print(df_Umeo)
        '''