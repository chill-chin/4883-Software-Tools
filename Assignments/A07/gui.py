''' 
Description: 
This GUI code allows the user to enter parameters & produce an appropriate URL.
Furthermore, the weather data from is retrieved from Wunderground and printed in Tabular format.
'''

import PySimpleGUI as sg      
import csv
from bs4 import BeautifulSoup                           # used to parse the HTML
from get_weather_data import asyncGetWeather

airport_codes = []

def loadAirportCodes():
    global airport_codes  # Use the global keyword to access the airport_codes list
    with open('airport-codes.csv', encoding="utf8", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['type'] == 'large_airport':
                airport_codes.append(row['ident'])

def currentDate(returnType='tuple'):

    from datetime import datetime
    if returnType == 'tuple':
        return (datetime.now().month, datetime.now().day, datetime.now().year)
    elif returnType == 'list':
        return [datetime.now().month, datetime.now().day, datetime.now().year]

    return {
        'day':datetime.now().day,
        'month':datetime.now().month,
        'year':datetime.now().year
    }

def buildWeatherURL(month=None, day=None, year=None, airport=None, filter=None):

    current_month,current_day,current_year = currentDate('tuple')
    
    if not month:
        month = current_month
    if not day:
        day = current_day
    if not year:
        year = current_year
    
    # Create the GUI layout
    layout = [
        [sg.Text('Month')], [sg.Combo(list(range(1, 13)), default_value=month, key='-MONTH-')],
        [sg.Text('Day')], [sg.Combo(list(range(1, 32)), default_value=day, key='-DAY-')],
        [sg.Text('Year')], [sg.Combo(list(range(2012, current_year + 1)), default_value=year, key='-YEAR-')],
        [sg.Text('Airport Code')], [sg.Combo(airport_codes, key='-AIRPORT-', enable_events=True)],
        [sg.Text('Daily / Weekly / Monthly')], [sg.Combo(['daily', 'weekly', 'monthly'], default_value='daily', key='-FILTER-')],
        [sg.Submit(), sg.Cancel()]
    ]   

    window = sg.Window('Weather Data', layout)    

    event, values = window.read()
    window.close()
        
    global code
    month = values['-MONTH-']
    day = values['-DAY-']
    year = values['-YEAR-']
    code = values['-AIRPORT-']
    filter = values['-FILTER-']

    sg.popup('You entered', f"Month: {month}, Day: {day}, Year: {year}, Code: {code}, Filter: {filter}")

    # Produce a URL for quering based on the GUI user input
    base_url = "https://wunderground.com/history"
    dt = "date"
    f = filter
    c = code
    y = year
    m = month
    d = day
    url = f"{base_url}/{f}/{c}/{dt}/{y}-{m}-{d}"
    print(url)
    return url


if __name__=='__main__':
    loadAirportCodes()                                   # Call the function to populate airport_codes
    url = buildWeatherURL(1,1)                           # Call function to open GUI and create appropriate URL
    page = asyncGetWeather(url)                          # Get the page source HTML from the URL    

    soup = BeautifulSoup(page, 'html.parser')            # Parse the HTML
    data=[]
    datahead=[]

    
    history = soup.find('lib-city-history-observation')  # Find the appropriate tag that contains the weather data
    
    for row in history:
        if row:
            cellsHead = row.find_all('th')
            datahead = [cell.get_text(strip=True) for cell in cellsHead]
            tbody=row.find('tbody')
            cells = tbody.find_all('tr')
            for tr in cells:
                data_row_td=[]
                for td in tr.find_all('td'):
                    data_row_td.append(td.get_text(strip=True) )
                data.append(data_row_td)
    print("+++++++",data)
    print("-------",datahead)

    
    layout = [
        [sg.Table(values=data, headings=datahead, auto_size_columns=True,
                   justification='left')],
        [sg.OK()]
    ]
    
    title = 'Weather Data for Station Code: ' + code
    window = sg.Window(title, layout)
    event, _ = window.read()
    window.close()