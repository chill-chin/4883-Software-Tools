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
|   4   | [input_1.png](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A07/input_1.png) | Query 1 Input |
|   5   | [output_1.png](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A07/output_1.png) | Query 1 Output |
|   6   | [input_2.png](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A07/input_2.png) | Query 2 Input |
|   7   | [output_2.png](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A07/output_2.png) | Query 2 Output |
|   8   | [input_3.png](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A07/input_3.png) | Query 3 Input |
|   9   | [output_3.png](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A07/output_3.png) | Query 3 Output |

## Declarations:
-> This Assignment modifies the code already provided [in the class](https://github.com/rugbyprof/4883-Software-Tools/tree/master/Assignments/A07).

-> ChatGPT was additionally used to get help with the Python syntax for [gui.py](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A07/gui.py).

## Instructions:
1. Install Selenium, beautifulsoup4 and Chromedriver and pysimplegui.
2. Download and save the following files in single folder: [airport-codes.csv](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A07/airport-codes.csv), [get_weather_data.py](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A07/get_weather_data.py) and [gui.py](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A07/gui.py).
3. Open the folder in VSCode.
4. Edit the chromedriver executable path in line 12 in file [get_weather_data.py](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A07/get_weather_data.py).
5. Run the file [gui.py](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A07/gui.py).
6. Enter appropriate values for 'Month', 'Day', 'Year' and 'Airport Code'.

## Example Queries & Output:

### Example 1:
**- Enter Values:** Day=1, Month=1, Year=2012, Airport Code=KABQ, Filter=daily

<img align="left" width="150" height="310" src="https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A07/input_1.png">
<img align="center" width="830" height="310" src="https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A07/output_1.png">

### Example 2:
**- Enter Values:** Day=6, Month=6, Year=2016, Airport Code=BIKF, Filter=daily

<img align="left" width="150" height="310" src="https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A07/input_2.png">
<img align="center" width="830" height="310" src="https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A07/output_2.png">

### Example 3:
**- Enter Values:** Day=2, Month=3, Year=2021, Airport Code=CYEG, Filter=daily

<img align="left" width="150" height="310" src="https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A07/input_3.png">
<img align="center" width="830" height="310" src="https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A07/output_3.png">

