# A07 - Web Scraping
## Chintan Mehta

## Description:
The following assignment involves creating a **URL** based on the user input (through a **GUI**) and using **_Selenium_** to Asynchronously get data from **Wunderground**. Additionally, a **_Beautiful Soup_** Web Scraper is used to scrape weather data from the URL. The HTML code that is received from the query is then presented in a Table format using **_PySimpleGui_**.


## Files:

|   #   | File     | Description                                      |
| :---: | -------- | ------------------------------------------------ |
|   1   | [airport-codes.csv](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A07/airport-codes.csv) | Necessary data for GUI |
|   2   | [get_weather_data.py](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A07/get_weather_data.py) | Code to get the Weather data  |
|   3   | [gui.py](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A07/gui.py) | Code to create an Input/Output GUI |

## Declarations:
-> This Assignment modifies the code already provided [in the class](https://github.com/rugbyprof/4883-Software-Tools/tree/master/Assignments/A07).

-> ChatGPT was additionally used to get help with the Python syntax for [gui.py](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A07/gui.py).

## Instructions:
1. Install Selenium, beautifulsoup4 and Chromedriver and pysimplegui.
2. Download and open folder [A07](https://github.com/chill-chin/4883-Software-Tools/tree/main/Assignments/A07) in VSCode.
4. Edit the chromedriver executable path in line 12 in file [get_weather_data.py](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A07/get_weather_data.py).
5. Run the file [gui.py](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A07/gui.py).
6. Enter appropriate values for 'Month', 'Day', 'Year' and 'Airport Code'.

## Example Queries & Output:

### Example 1:
- Enter Values: Day=1, Month=1, Year=2012, Airport Code=KABQ, Filter=daily
