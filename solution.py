import pandas as pd

data = {    
            0: {'tradeID': '001', 'direction': 'buy', 'amount': 1000, 'amount_date': '2023-09-01'}, 
            1: {'tradeID': '001', 'direction': 'sell', 'amount': 2000, 'amount_date': '2023-09-01'}, 
            2: {'tradeID': '002', 'direction': 'buy', 'amount': 15000, 'amount_date': '2023-09-02'}, 
            3: {'tradeID': '002', 'direction': 'sell', 'amount': 24000, 'amount_date': '2023-09-02'}, 
            4: {'tradeID': '003', 'direction': 'buy', 'amount': 5000, 'amount_date': '2023-10-01'} 
        } 


df = pd.DataFrame(data)

# Transpose dataframe
t_df = df.T

# Format dates
def format_date(x):
   return x.replace('-', '') 

t_df['amount_date'] = t_df['amount_date'].apply(format_date)

my_date = '202309'

# Iterate through rows
for index, row in t_df.iterrows():
    if my_date in row["amount_date"]:
        if row["direction"] == 'buy':
            t_df.at[index, "amount"] = row["amount"] * -1
    else:
        t_df = t_df.drop(index, axis=0)
           
result = t_df.groupby('tradeID')['amount'].sum()

print(result)