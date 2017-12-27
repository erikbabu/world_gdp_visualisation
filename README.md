# World GDP Visualisation tool
Creates a world map for the year selected by the user and plots the GDP information for each country on the map. Implemented in python

dataset source: https://datahub.io/core/gdp

World map created with aid of Pygal Maps

To invoke program: 'python world_gdp.py'

When prompted, enter a year between 1960 and 2016 inclusive
The program will output to an svg file. To view this, open the file in a browser (e.g. Chrome, Firefox, ...). 

This can be seen in Figure 1 and Figure 2 below
![2013 GDP Data](/../screenshots/screenshots/2013_full.png?raw=true "Figure 1")

The map is interactive: Hovering over each country shows the GDP in $bn. Filters can also be applied based on the GDP ranges, allowing the user to view specific countries in each GDP bracket. If a country is filled with white, then that country's GDP data was unavailable for that year.
