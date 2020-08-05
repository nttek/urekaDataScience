#import essential libraries 
import requests              #for api request
import pandas as pd
from datetime import datetime, timedelta

#method to get the current url
def get_url(page_number):    
    page = str(page_number)   
    url = 'https://api.stackexchange.com/2.2/questions?page=' + page + '&pagesize=100&order=desc&sort=activity&site=datascience'; 
    return url

#method to check api response validity
def response_validity(api_response):
    try:
        api_status = int(api_response.status_code)
    except ValueError:
        return None
    return True

#method to convert json to dataframe
def json_to_df(api_response):
    data = api_response.json()    
    try:
        df = pd.json_normalize(data['items'])
    except KeyError:
        return None
    df2 = df['tags']
    return df2
    
def update_records():   
    #variable to check no. of entries and df obj. to keep the records
    page_number=1
    records = pd.DataFrame()

    #to receive the required 10000 records from the api
    while page_number<=100:    
        url = get_url(page_number);
        api_response = requests.get(url)   

        #exception handling for failure of call response
        if response_validity(api_response) is None:
            continue

        #converting json to df obj.
        df2 = json_to_df(api_response)    

        #exception handling for error message from the server
        if df2 is None:
            break

        #adding rows to already existing records
        frames = [records, df2]
        records = pd.concat(frames, ignore_index=True)
        page_number+=1;

    #check for missing data for non empty df. object  
    if not records.empty:
        records.columns = ['tags']

    #update the records    
    records.to_csv('Data/tags.csv')

def update_now(now):
    update_records()
    file = open('Data\dateinfo.txt','w')
    new_update = now.strftime('%d/%m/%y %H:%M:%S')
    file.write(new_update)
    file.close()
    
def check_updates():
    now = datetime.now() # current date and time

    try:
        file = open('Data\dateinfo.txt','r')
        update_time = datetime.strptime(file.read(), '%d/%m/%y %H:%M:%S')
        file.close()
    except(FileNotFoundError, ValueError):
        update_now(now)
        update_time = datetime.strptime(file.read(), '%d/%m/%y %H:%M:%S')
        return True

    time_delta = (now - update_time)
    hours_elapsed = time_delta.total_seconds()/3600

    if hours_elapsed > 168:
        update_now(now)
        return True
        
    return False