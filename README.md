# World GDP Visualisation tool
Creates a world map for the year selected by the user and plots the GDP information for each country on the map. Implemented in python

dataset source: https://datahub.io/core/gdp

World map created with aid of Pygal Maps

To invoke program: 'python world_gdp.py'

When prompted, enter a year between 1960 and 2016 inclusive
The program will output to an svg file. To view this, open the file in a browser (e.g. Chrome, Firefox, ...). 

This can be seen in the image below
![2013 GDP Data](/../screenshots/screenshots/2013_full.png?raw=true "2013 GDP Data")

The map is interactive: Hovering over each country shows the GDP in $bn.

This can be seen in the image below
![2013 GDP Labels](/../screenshots/screenshots/2013_label.png?raw=true "2013 GDP Data showing country label and information")

Filters can also be applied based on the GDP ranges, allowing the user to view specific countries in each GDP bracket. If a country is filled with white, then that country's GDP data was unavailable for that year.

This can be seen in the images below
![2013 GDP with 1 filter applied](/../screenshots/screenshots/2013_filter_1.png?raw=true "2013 GDP Data")
![2013 GDP with 2 filters applied](/../screenshots/screenshots/2013_filter_2.png?raw=true "2013 GDP Data")
