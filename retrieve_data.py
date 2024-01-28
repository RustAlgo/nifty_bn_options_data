# Imports
import pandas as pd
from maticalgos.historical import historical
import datetime
import time

# http://historical.maticalgos.com/ give your email and username and you will get password on mail.

# Your Inputs

mail_id = "xyz@gmail.com" #Enter your mail here
password_recieved = "123456" #Enter your passowrd here
instrument_name = "banknifty" # Enter instrument name as nifty or banknifty as per your requirement in lower case
from_date = datetime.date(2023, 1, 2) # Enter date in format YY/MM/DD - #Banknifty - Available since 2018, Nifty - Available since 2019
to_date = datetime.date(2023, 1, 5) # Enter date in format YY/MM/DD - Data available till 2023 November 30th when checked on 28/01/2024


# Code starts here

ma= historical(mail_id)

ma.login(password_recieved)  # Use your actual password

df = pd.DataFrame() #Creating a blank df
#Loop and append to Pandas DF

date_check = from_date

while date_check <= to_date:
    print(f"Trying to retrieve date for {date_check}")
    
    try:
        
        data = ma.get_data("banknifty", date_check) 
        
        # Append the data to the DataFrame
        df = pd.concat([df, data], ignore_index=True)
        time.sleep(1)
    
    except Exception as e:
        print({e})
        
    date_check = date_check + datetime.timedelta(days=1) #Increasing by 1 Day
    
    print("Sleeping for 3 Seconds")
    
    time.sleep(3)

csv_name = f'{str(from_date)}_to_{str(to_date)}_{instrument_name}_data.csv'  # File creation

print("Storing data................")
df.to_csv(csv_name, index=False)  #Writing to CSV

print(f'Data Available for dates between {from_date} and {to_date} is stored in {csv_name}')