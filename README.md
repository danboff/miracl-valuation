# miracl-valuation-tool

## Prerequisites
Following packages should be installed: 
```` 
pip install Pyomo
pip install pandas
pip install python-csv
````

## Installation
Clone the repository using:
```` 
git clone https://github.com/BilalAhmad-Bhatti/miracl-valuation-tool.git
````

## Configuring the Input Files
The tool reads the data from the .csv files which are provided in the InputFiles folder. Before running the tool, ensure that the inputs are provided in the correct format to the .csv files:
1. BuildingProfile.csv contains the hourly data for consumption, demand without system, demand with system, retail rate, demand charge, resale price, system peaking charge hour, and system peaking charge.
2. SystemProfile.csv contains the hourly data for system production, energy price, and REC price.
3. Prices.csv contains the hourly ancillary service prices (to be used in co-optimization). They include regulation up, regulation down, spinning reserve, non-spinnig reserve, regulation mileage up, regulation mileage down, and LMP.
4. To capture costs that change annually, AnnualCosts.csv is defined. Currently there is only one cost i.e. the social cost of carbon.
5. The flags and constants are defined in file StaticInputs.csv

The units of all input parameters can be found in the corresponding .csv files.

## Running the Tool

## Viewing the Results
