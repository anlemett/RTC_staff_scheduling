import pandas as pd

year = 2020

month = 2

airport = "Kiruna"
#airport = "Umeo"
#airport = "Ovik"
#airport = "Sundsvall"
#airport = "Malmo"



# cbh, lcc, tp, i10fg, cape, cp


input_csv_filename = 'data/' + airport + '/' + airport + '_' + str(year) + '_' + str(month) + '_ensemble.csv'
output_csv_filename = 'data/' + airport + '/' + airport + '_' + str(year) + '_' + str(month) + '_ensemble_24hours.csv'


df = pd.read_csv(input_csv_filename, sep=' ')


df['month'] = df['month'].astype(int)
df['day'] = df['day'].astype(int)
df['hour'] = df['hour'].astype(int)
df['date'] = df['date'].astype(int)

print(df.head())

cols = df.columns

lst = []    #list of lists

for index, row in df.iterrows():

    row_hour = row['hour']
    
    previous_hour = row_hour - 1 if row_hour > 0 else 23
    date = row['date'] if row_hour > 0 else row['date'] - 1
    day = row['day'] if row_hour > 0 else row['day'] - 1
    row_lst = row.values.tolist()
    row_lst[1] = day
    row_lst[3] = date
    row_lst[2] = previous_hour
    lst.append(row_lst)
    
    row_lst = row.values.tolist()
    row_lst[2] = row_hour
    lst.append(row_lst)
    
    row_lst = row.values.tolist()
    next_hour = row_hour + 1
    row_lst[2] = next_hour
    lst.append(row_lst)

new_df = pd.DataFrame(lst, columns=cols)

# remove the first row
new_df = new_df.drop(new_df.index[0])

# copy the last row
new_data = pd.DataFrame(new_df[-1:].values, columns=new_df.columns)
new_data['hour'] = 23
new_df = new_df.append(new_data)


tp_ens = ['tp0', 'tp1', 'tp2', 'tp3', 'tp4', 'tp5', 'tp6', 'tp7', 'tp8', 'tp9']

for tp in tp_ens:
    tp_list = new_df[tp].tolist()
    tp_list[0] = tp_list[0] / 3

    for i in range(1, len(tp_list)-2, 3):
        tp_list[i] = tp_list[i+2] / 3
        tp_list[i+1] = tp_list[i+2] / 3
        tp_list[i+2] = tp_list[i+2] / 3
    
    #here we actually need data from the first day of the next month but we do not use the last day of the month
    tp_list[-1] = tp_list[-1] / 3
    tp_list[-2] = tp_list[-2] / 3

    new_df[tp] = tp_list
sf_ens = ['sf0', 'sf1', 'sf2', 'sf3', 'sf4', 'sf5', 'sf6', 'sf7', 'sf8', 'sf9']

for sf in sf_ens:
    sf_list = new_df[sf].tolist()
    sf_list[0] = sf_list[0] / 3

    for i in range(1, len(sf_list)-2, 3):
        sf_list[i] = sf_list[i+2] / 3
        sf_list[i+1] = sf_list[i+2] / 3
        sf_list[i+2] = sf_list[i+2] / 3
    
    #here we actually need data from the first day of the next month but we do not use the last day of the month
    sf_list[-1] = sf_list[-1] / 3
    sf_list[-2] = sf_list[-2] / 3

    new_df[sf] = sf_list


# linear interpolation for other metrics
# Y at 03h and Z at 06h, then a value for 04h would be (Y+(Z-Y)/3), and a value for 05h would be (Y+2*(Z-Y)/3)
# last two hours of the last day of the months untouched but we do not use them

cbh_ens = ['cbh0', 'cbh1', 'cbh2', 'cbh3', 'cbh4', 'cbh5', 'cbh6', 'cbh7', 'cbh8', 'cbh9']

for cbh in cbh_ens:
    cbh_list = new_df[cbh].tolist()

    for i in range(0, len(cbh_list)-5, 3):
        cbh_list[i+1] = cbh_list[i] + (cbh_list[i+3] - cbh_list[i])/3
        cbh_list[i+2] = cbh_list[i] + 2 * (cbh_list[i+3] - cbh_list[i])/3
    
    new_df[cbh] = cbh_list

lcc_ens = ['lcc0', 'lcc1', 'lcc2', 'lcc3', 'lcc4', 'lcc5', 'lcc6', 'lcc7', 'lcc8', 'lcc9']

for lcc in lcc_ens:
    lcc_list = new_df[lcc].tolist()

    for i in range(0, len(lcc_list)-5, 3):
        lcc_list[i+1] = lcc_list[i] + (lcc_list[i+3] - lcc_list[i])/3
        lcc_list[i+2] = lcc_list[i] + 2 * (lcc_list[i+3] - lcc_list[i])/3
    
    new_df[lcc] = lcc_list

i10fg_ens = ['i10fg0', 'i10fg1', 'i10fg2', 'i10fg3', 'i10fg4', 'i10fg5', 'i10fg6', 'i10fg7', 'i10fg8', 'i10fg9']

for i10fg in i10fg_ens:
    i10fg_list = new_df[i10fg].tolist()

    for i in range(0, len(i10fg_list)-5, 3):
        i10fg_list[i+1] = i10fg_list[i] + (i10fg_list[i+3] - i10fg_list[i])/3
        i10fg_list[i+2] = i10fg_list[i] + 2 * (i10fg_list[i+3] - i10fg_list[i])/3
    
    new_df[i10fg] = i10fg_list


new_df.to_csv(output_csv_filename, sep=' ', float_format='%.9f', encoding='utf-8', header=True, index=False)
