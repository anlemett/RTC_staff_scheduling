import pandas as pd

year = 2020

month = 7

airport = "Kiruna"
#airport = "Malmo"
#airport = "Ovik"
#airport = "Sundsvall"
#airport = "Umeo"


# cbh, lcc, tp, i10fg, cape, cp


input_csv_filename = 'data/' + airport + '/' + airport + '_' + str(year) + '_' + str(month) + '_ensemble.csv'
output_csv_filename = 'data/' + airport + '/' + airport + '_' + str(year) + '_' + str(month) + '_ensemble_24hours.csv'


df = pd.read_csv(input_csv_filename, sep=' ')


df['date'] = df['date'].astype(int)

print(df.head())

cols = df.columns

lst = []    #list of lists

for index, row in df.iterrows():

    row_hour = row['hour']
    
    previous_hour = row_hour - 1 if row_hour > 0 else 23
    date = row['date'] if row_hour > 0 else row['date'] - 1
    row_lst = row.values.tolist()
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

new_df.to_csv(output_csv_filename, sep=' ', float_format='%.9f', encoding='utf-8', header=True, index=False)
