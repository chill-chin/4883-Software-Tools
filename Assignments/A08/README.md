# A08 - Fast Api with Covid Data

### Chintan Mehta

### Description:
* This Assignment creates a RESTful API using FastAPI. 
* The goal is to 
    1. Fetch Covid related data from a CSV file
    2. Expose endpoints using FastAPI in order to get the necessary data. 
    3. Lastly, uvicorn is used to locally host the API.


### Files:

|   #   | File     | Description                                      |
| :---: | -------- | ------------------------------------------------ |
|   1   | [main.py](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A08/main.py)  | RESTful API file          |
|  2    | [data.csv](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A08/data.csv) | Covid-19 Data

### Declarations
* ChatGPT was used to generate some of the functions in [main.py](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A08/main.py).

### Instructions:
1. Download the files [main.py](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A08/main.py), [data.csv](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A08/data.csv).
2. Open the downloaded files in VSCode.
3. Change the Directory path in [main.py](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A08/main.py) file (Line 20).
4. Run [main.py](https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A08/main.py)
5. Open any browser. Access the [default link](http://127.0.0.1:5000) or any of the below mentioned **_route links_**.
6. Interface shown below shown load up.

<img align="center" width="800" height="400" src="https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A08/FastAPI.png">


### Generic Routes

* Route: /
    * Retrieves the documentation provided by swagger.

#

* Route: /countries
    * This route will return a list of unique countries in the Covid data file.
    
    - **Params:**
      - None

    - **Returns:**
      - (object) : List of countries

    #### Request URL: [http://127.0.0.1:5000/countries](http://127.0.0.1:5000/countries)

    #### Success:
    ```
    {
        "countries": [
            "Afghanistan",
            "Albania",
            "Algeria",
            "American Samoa"
            ],
        "success": True
    }
    ```

    #### Error: 
    // Change 'Country' to 'Contry' in main.py (line 65)
    ```
    {
        "error": "'Contry'",
        "success": False
    }   
    ```

#

* Route: /regions
    * Retrieves a list of available WHO regions from the "db"




### Summary
* Implementation process: 


* Challenges faced: Filtering by Date (first 4 integers). Had to use ChatGPT to find 'startswith(str(year))'
, Writing the function to handle filtering
Writing function to find the country with min/max deaths
* Additional functionality: