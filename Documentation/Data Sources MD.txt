# Data Sources for Distributed Wind Valuation Service

## System Production Data

Energy production data is an important input for the valuation service, as it dictates the amount of energy available for sale. Users modeling existing systems can use historical production data, while users modeling hypothetical systems may have to use software tools to create estimated production data. Many private sector tools exist or users can leverage free software, such as the [System Advisor Model](https://sam.nrel.gov/wind.html) (SAM). SAM is a tool created by the National Renewable Energy Laboratory (NREL) which can model many different energy systems using [historical climate data](https://www.nrel.gov/gis/wind-supply-curves.html) and can be adapted based on several common use cases.

## Building Consumption Data

When modeling a behind-the-meter (BTM) system, users have the ability to net system production against their building's electricity consumption on an hourly level. Users looking to use their historic consumption data can typically download their unique data from their utility. The [Green Button](https://www.greenbuttondata.org/) program provides a standard and easy way for users to access their utility data. For users interested in modeling hypothetical buildings, the US Department of Energy maintains a collection of [commercial reference buildings](https://www.energy.gov/eere/buildings/commercial-reference-buildings) for use in analysis. Users interested in more comprehensive analysis of building consumption can also use the [EnergyPlus](https://energyplus.net/) tool, which allows for detailed modelling of energy flows in buildings.

## Energy Cost Data

Users wishing to understand bill savings or electricity sale will need some source for electricity prices. This can come from their local utility or be based on private price projections. Users modeling BTM systems can also download rates from the [Utility Rate Database](https://openei.org/wiki/Utility_Rate_Database) (URDB). The URDB contains rates for over 3,700 U.S. utilities and is updated annually by NREL. Users looking for wholesale energy price projections can download hourly prices from the [Regional Energy Deployment System](https://scenarioviewer.nrel.gov/?project=a3e2f719-dd5a-4c3e-9bbf-f24fef563f45&mode=download&layout=Default). These prices are listed for all US states on an hourly basis through the year 2050. Several different scenarios (each based on differing assumptions) underpin these forecasts, and users can select the one that bests aligns with their analysis. Many ISOs/RTOs also publish hourly wholesale prices for users interested in historical analysis.

## Renewable Energy Credits

Users in states with Renewable Energy Credits (RECs), can also calculate the value associated with this revenue stream. RECs trade based on supply and demand can be traded on spot markets or sold under long-term contracts. The annual [RPS Status Update](https://eta-publications.lbl.gov/sites/default/files/rps_status_update-2021_early_release.pdf), also provides historical REC prices, which can be used in analysis. For states without renewable portfolio standards, [voluntary REC prices](https://www.nrel.gov/docs/fy22osti/81141.pdf) may be used.

## Emissions Data

The valuation service is able to aggregate avoided emissions and the costs associated with avoided carbon emissions. Avoided emissions depends on the times and location at which the wind system is generating. The Environmental Protection Agency's [AVoided Emissions and geneRation Tool](https://www.epa.gov/avert) (AVERT) allows users to estimate the avoided emissions of particulate matter (PM2.5), nitrogen oxides (NOX), sulfur dioxide (SO2), carbon dioxide (CO2), volatile organic compounds (VOCs), and ammonia (NH3) based on these factors.

The savings resulting from reduced carbon dioxide emissions can also be calculated by users. Systems operating in carbon markets such as the [Regional Greenhouse Gas Initiative](https://www.rggi.org/auctions/auction-results/prices-volumes) (RGGI) or the [Western Climate Initiative](https://ww2.arb.ca.gov/our-work/programs/cap-and-trade-program/auction-information)can use the historical clearing prices from their auctions in analyses. Analysts should note whether REC sales limit their participation in carbon markets. [Best practices](https://netzeroanalysis.com/wp-content/uploads/2019/12/RECsOffsetsQA.pdf) exist for dealing with these contracts. Users can also use a social cost of carbon, which represents the present value of long-term damages created by carbon emissions. Disagreements exist about the social cost of carbon, but entities such as the [EPA](https://www.epa.gov/sites/default/files/2016-12/documents/social_cost_of_carbon_fact_sheet.pdf) and the [World Bank](https://documents1.worldbank.org/curated/en/621721519940107694/pdf/2017-Shadow-Price-of-Carbon-Guidance-Note.pdf) provide guidance on how to use these values in analysis.

## References

Barbose, Galen. Rep. U.S. Renewables Portfolio Standards 2021 Status Update: Early Release. Berkeley, CA: Lawrence Berkeley National Laboratory, 2021.

CARB. "Auction Information." Auction Information. California Air Resources Board, 2020. [https://ww2.arb.ca.gov/our-work/programs/cap-and-trade-program/auction-information](https://ww2.arb.ca.gov/our-work/programs/cap-and-trade-program/auction-information).

Center for Resource Solutions. Rep. Renewable Energy Certificates, Carbon Offsets, and Carbon Claims. San Francisco, CA: Center for Resource Solutions, 2012.

Cole, Wesley; Corcoran, Sean; Gates, Nathaniel; Mai, Trieu; Das, Paritosh. 2020. 2020 Standard Scenarios Report: A U.S. Electricity Sector Outlook, Golden, CO: National Renewable Energy Laboratory. NREL/TP-6A20-77442. https://www.nrel.gov/docs/fy21osti/77442.pdf.

Deru, Michael, Kristin Field, Daniel Studer, Kyle Benne, Brent Griffith, Paul Torcellini, Bing Liu, et al. Tech. U.S. Department of Energy Commercial Reference Building Models of the National Building Stock . Golden, CO: National Renewable Energy Laboratory, 2011.

EPA. Rep. AVoided Emissions and GeneRation Tool (AVERT) User Manual Version 3.2. Washington, DC: Environmental Protection Agency, 2022.

EPA. Rep. Fact Sheet: Social Cost of Carbon. Washington, DC: Environmental Protection Agency, 2016.

Heeter, Jenny, Eric O'Shaughnessy, and Rebecca Burd. Rep. Status and Trends in the Voluntary Market (2020 Data). Golden, CO: National Renewable Energy Laboratory, 2021.

Lopez, Anthony, Trieu Mai, Eric Lantz, Dylan Harrison-Atlas, Travis Williams, and Galen Maclaurin. "Land Use and Turbine Technology Influences on Wind Potential in the United States." Energy 223 (2021): 120044. [https://doi.org/10.1016/j.energy.2021.120044](https://doi.org/10.1016/j.energy.2021.120044).

RGGI. "Allowance Prices and Volumes." Allowance Prices and Volumes | RGGI, Inc. Regional Greenhouse Gas Initiative , 2022. https://www.rggi.org/auctions/auction-results/prices-volumes.

System Advisor Model Version 2020.11.29 (SAM 2020.11.29). National Renewable Energy Laboratory. Golden, CO. [https://sam.nrel.gov](https://sam.nrel.gov/).

The Green Button Alliance. "The Green Button - the Standardized Way to Get Your Energy Usage Data." The Green Button - the standardized way to get your energy usage data. The Green Button Alliance. Accessed September 23, 2022. [https://www.greenbuttondata.org/](https://www.greenbuttondata.org/).

World Bank. Rep. Shadow Price of Carbon in Economic Analysis. Washington, DC: The World Bank, 2017.

Zimny-Schmitt, Daniel, Huggins, Jay. 2010. "Utility Rate Database (URDB)". United States. https://data.openei.org/submissions/5.