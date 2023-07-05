
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

"""Open CSV file using Pandas' method"""
os.chdir(r"C:\Users\hameh\Downloads\4883-Software-Tools\Assignments\A08")
data = pd.read_csv('data.csv')


"""Route 1"""
@app.get("/")
async def docs_redirect():
    """Api's base route that displays the information created above in the ApiInfo section."""
    return RedirectResponse(url="/docs")

"""Route 2"""
@app.get("/countries/")
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
        "countries":
            [
            "Afghanistan","Albania","Algeria","American Samoa"
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
@app.get("/regions/")
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
    except Exception as e:
        return {"error": str(e),"success": False}




if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="debug", reload=True) #host="127.0.0.1"
