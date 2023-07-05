
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import csv
import pandas as pd
import os


description = """🚀
## 4883 Software Tools - Chintan Mehta
"""

app = FastAPI(
    description=description,
)

"""Open CSV file using Pandas' method. Replace path to appropriate Directory path below"""
os.chdir(r"C:\Users\hameh\Downloads\4883-Software-Tools\Assignments\A08")
data = pd.read_csv('data.csv')

"""Route 1"""
@app.get("/")
async def documentation():
    """Api's base route that displays the information created above in the ApiInfo section."""
    return RedirectResponse(url="/docs")

"""Route 2"""
@app.get("/countries")
async def countries():
    """
    This method will return a list of unique countries in the Covid data file.
    
    - **Params:**
      - None

    - **Returns:**
      - (object) : List of countries

    #### Request URL:

    [http://127.0.0.1:5000/countries](http://127.0.0.1:5000/countries)

    #### Success:

    {
        "countries": [
            "Afghanistan",
            "Albania",
            "Algeria",
            "American Samoa"
            ],
        "success": True
    }

    #### Error: 
    // Change 'Country' to 'Contry' in main.py (line 65)
    
    {
        "error": "'Contry'",
        "success": False
    }   
    """
    try:
        unique_countries = data['Country'].unique().tolist()
        return {"countries": unique_countries,"success": True}
    except Exception as err:
            return {"error": str(err),"success": False}

"""Route 3"""
@app.get("/regions")
async def regions():
    """
    This method will return a list of WHO regions.
    
    - **Params:**
      - None

    - **Returns:**
      - (object) : List of regions

    #### Request URL:

    [http://127.0.0.1:5000/regions](http://127.0.0.1:5000/regions)

    #### Success:

    {
        "regions": [
            "EMRO",
            "EURO",
            "AFRO",
            "WPRO",
            "AMRO",
            "SEARO",
            "Other"
        ],
        "success": True
    }

    #### Error: 
    // Change 'WHO_region' to 'WHO' in main.py (line 110)
    
    {
        "error": "'WHO'",
        "success": False
    }  
    """
    try:
        regions = data['WHO_region'].unique().tolist()
        return {"regions": regions,"success": True}
    except Exception as err:
            return {"error": str(err),"success": False}

"""Route 4"""
@app.get("/deaths")
async def total_deaths(country: str = None, region: str = None, year: int = None):
    """
    This method will return total deaths, and can also return deaths by country, region or year.

    - **Params:**
      - Country (str) : A Country name
      - Region (str)  : A Region name
      - Year (int)    : A 4 digit year

    - **Returns:**
      - (int) : Total deaths based on the parameters

    #### Request URL 1:

    [http://127.0.0.1:5000/deaths](http://127.0.0.1:5000/deaths)

    #### Success Response 1:

        {
        "total_deaths": 6945714,
        "params": {
            "country": null,
            "region": null,
            "year": null
        },
        "success": true
        }

    #### Request URL 2:

    [http://127.0.0.1:5000/deaths?region=EURO&year=2021](http://127.0.0.1:5000/deaths?region=EURO&year=2021)
  
    #### Success Response 2:

        {
        "total_deaths": 1087689,
        "params": {
            "country": null,
            "region": "EURO",
            "year": 2021
        },
        "success": true
        }

    """
    try:
        new_data = data

        if country:
            new_data = new_data[new_data['Country'] == country]
        
        if region:
            new_data = new_data[new_data['WHO_region'] == region]
        
        if year:
            new_data = new_data[new_data['Date_reported'].str.startswith(str(year))]

        # Total Deaths
        total_deaths = new_data['New_deaths'].sum()
        
        return {
            "total_deaths":  int(total_deaths),
            "params": {
                    "country": country,
                    "region": region,
                    "year": year
                },
                "success": True,
            }
    except Exception as err:
        return {"error": str(err),"success": False}

"""Route 5"""
@app.get("/cases")
async def total_cases(country: str = None, region: str = None, year: int = None):
    """
    This method will return total cases, and can also return cases by country, region or year.

    - **Params:**
      - Country (str) : A Country name
      - Region (str)  : A Region name
      - Year (int)    : A 4 digit year

    - **Returns:**
      - (int) : Total cases based on the parameters

    #### Request URL 1:

    [http://127.0.0.1:5000/cases](http://127.0.0.1:5000/cases)

    #### Success Response 1:

        {
        "total_cases": 768187096,
        "params": {
            "country": null,
            "region": null,
            "year": null
        },
        "success": true
        }

    #### Request URL 2:

    [http://127.0.0.1:5000/cases?region=EURO&year=2021](http://127.0.0.1:5000/cases?region=EURO&year=2021)
  
    #### Success Response 2:

        {
        "total_cases": 74824714,
        "params": {
            "country": null,
            "region": "EURO",
            "year": 2021
        },
        "success": true
        }
    """
    try:
        new_data = data

        if country:
            new_data = new_data[new_data['Country'] == country]
        
        if region:
            new_data = new_data[new_data['WHO_region'] == region]
        
        if year:
            new_data = new_data[new_data['Date_reported'].str.startswith(str(year))]

        # Total Cases
        total_cases = new_data['New_cases'].sum()
        
        return {
            "total_cases":  int(total_cases),
            "params": {
                    "country": country,
                    "region": region,
                    "year": year
                },
                "success": True,
            }
    except Exception as err:
        return {"error": str(err),"success": False}

"""Route 6"""
@app.get("/max_deaths")
def max_deaths(min_date: str = None, max_date: str = None):
    """
    This method will return the country with most deaths cumulatively or between a date range.

    - **Params:**
      - min_date (str) : Start Date
      - max_date (str) : End Date

    - **Returns:**
      - (int) : Cumulative deaths

    #### Request URL 1:

    [http://127.0.0.1:5000/max_deaths](http://127.0.0.1:5000/max_deaths)

    #### Success Response 1:
        {
        "max_deaths_country": "United States of America",
        "cumulative_deaths": 1127152,
        "params": {
            "min_date": null,
            "max_date": null
        },
        "success": true
        }
        
    #### Request URL Example 2:

    [http://127.0.0.1:5000/max_deaths?min_date=2022-01-01&max_date=2023-01-01](http://127.0.0.1:5000/max_deaths?min_date=2022-01-01&max_date=2023-01-01)

    #### Success Response 2:

        {
        "max_deaths_country": "United States of America",
        "cumulative_deaths": 1082456,
        "params": {
            "min_date": "2022-01-01",
            "max_date": "2023-01-01"
        },
        "success": true
        }
    """
    try:
        new_data = data

        if min_date and max_date:
            new_data = data[(data["Date_reported"] >= min_date) & (data["Date_reported"] <= max_date)]
        else:
            new_data = data

        max_deaths_per_country = new_data.groupby("Country")["Cumulative_deaths"].max().reset_index()
        max_deaths = max_deaths_per_country.loc[max_deaths_per_country["Cumulative_deaths"].idxmax()]
        
        return {
            "max_deaths_country": max_deaths["Country"],
            "cumulative_deaths": int(max_deaths["Cumulative_deaths"]),
            "params": {
                "min_date": min_date,
                "max_date": max_date
            },
            "success": True,
            }
    except Exception as err:
        return {"error": str(err),"success": False}
    
"""Route 7"""
@app.get("/min_deaths")
def min_deaths(min_date: str = None, max_date: str = None):
    """
    This method will return the country with minimum deaths cumulatively or between a date range.

    - **Params:**
      - min_date (str) : Start Date
      - max_date (str) : End Date

    - **Returns:**
      - (int) : Cumulative deaths

    #### Request URL 1:

    [http://127.0.0.1:5000/min_deaths](http://127.0.0.1:5000/min_deaths)

    #### Success Response 1:

        {
        "min_deaths_country": "Afghanistan",
        "cumulative_deaths": 0,
        "params": {
            "min_date": null,
            "max_date": null
        },
        "success": true
        }
        
    #### Request URL 2:

    [http://127.0.0.1:5000/min_deaths?min_date=2022-01-01&max_date=2023-01-01](http://127.0.0.1:5000/min_deaths?min_date=2022-01-01&max_date=2023-01-01)

    #### Success Response 2:

        {
        "min_deaths_country": "American Samoa",
        "cumulative_deaths": 0,
        "params": {
            "min_date": "2022-01-01",
            "max_date": "2023-01-01"
        },
        "success": true
        }
    """
    try:
        new_data = data

        if min_date and max_date:
            new_data = data[(data["Date_reported"] >= min_date) & (data["Date_reported"] <= max_date)]
        else:
            new_data = data

        min_deaths_per_country = new_data.groupby("Country")["Cumulative_deaths"].min().reset_index()
        min_deaths = min_deaths_per_country.loc[min_deaths_per_country["Cumulative_deaths"].idxmin()]
        
        return {
            "min_deaths_country": min_deaths["Country"],
            "cumulative_deaths": int(min_deaths["Cumulative_deaths"]),
            "params": {
                "min_date": min_date,
                "max_date": max_date
            },
            "success": True,
            }    
    except Exception as err:
        return {"error": str(err),"success": False}

"""Route 8"""
@app.get("/avg_deaths")
def avg_deaths(country: str = None, region: str = None):
    """
    This method will return average deaths by country and region.

    - **Params:**
      - Country (str) : A Country name
      - Region (str)  : A Region name

    - **Returns:**
      - (int) : Average deaths based on the parameters

    #### Request URL 1:

    [http://127.0.0.1:5000/avg_deaths?country=India](http://127.0.0.1:5000/avg_deaths?country=India)

    #### Success Response 1:

        {
        "avg_deaths": 84,
        "params": {
            "country": "India",
            "region": null
        },
        "success": true
        }

    #### Request URL 2:

    [http://localhost:5000/avg_deaths?region=EURO](http://localhost:5000/avg_deaths?region=EURO)
  
    #### Success Response 2:

        {
        "avg_deaths": 123,
        "params": {
            "country": null,
            "region": "EURO"
        },
        "success": true
        }
    """
    try:
        new_data = data

        if country:
            new_data = new_data[new_data['Country'] == country]
        
        if region:
            new_data = new_data[new_data['WHO_region'] == region]
        
        # Average Deaths
        total_cases = new_data['New_cases'].sum()
        total_deaths = new_data['New_deaths'].sum()
        avg_deaths = total_cases/total_deaths

        return {
            "avg_deaths":  int(avg_deaths),
            "params": {
                    "country": country,
                    "region": region,
                },
                "success": True,
            }
    except Exception as err:
        return {"error": str(err),"success": False}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="debug", reload=True) #host="127.0.0.1"
