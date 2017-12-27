"""
This program displays the GDP for each country
for the year input by the user (within range 1960 - 2016 inclusive).
The output is a .svg file. To view the results, open the file with a browser.
"""

import json

import pygal

from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

from collections import OrderedDict

from country_codes import get_country_code

def get_year(lower_bound, upper_bound):
  """Returns the year that the user would like to see the GDP for."""
  valid_year = False
  while not valid_year:
    try:
      print("Please enter the year you would like to calculate GDP for.")
      message = "The year should be between " + str(lower_bound) + " and " \
        + str(upper_bound) + " (inclusive): "
      year = raw_input(message)
      year = int(year)
    except ValueError:
      display_invalid_year_msg()
      continue
    else:
      #check in range
      if year >= lower_bound and year <= upper_bound:
        return year
      else:
        display_invalid_year_msg()

def get_json_formatted_data(filename):
  """Returns a list of JSON formatted GDP data."""
  try:
    with open(filename) as f:
      gdp_data = json.load(f)
  except IOError:
    print("Error. File " + filename + " does not exist.")
    quit()
  else:
    return gdp_data

def display_invalid_year_msg():
  """Notifies the user that their input is not a valid year. """
  print("Sorry, you did not enter a valid year.")

def get_cc_gdps(gdp_data, year):
  """Returns a dictionary storing all country gdp data for year."""
  country_gdps = {}
  for gdp_dict in gdp_data:
    if gdp_dict['Year'] == year:
      country_name = gdp_dict['Country Name']
      gdp_val = gdp_in_billions(gdp_dict['Value'])
      code = get_country_code(country_name)
      if code:
        country_gdps[code] = gdp_val
  return country_gdps

def gdp_in_billions(gdp_val):
  """Returns GDP in $bn as an integer."""
  billion = 1000000000
  return int(float(gdp_val) / billion)

def group_gdps_by_level(full_set, subset_ranges, levels):
  """Partitions the data into the correct levels."""
  #validate subsets and levels
  num_ranges = len(subset_ranges)
  num_levels = len(levels)
  validate_subsets_and_levels(num_ranges, num_levels)

  #map each range to one of the subset dictionaries
  gdps = [{}, {}, {}, {}] #list of dictionaries stores gdp info for each range
  gdp_partition = OrderedDict()
  for index in range(0, num_ranges):
    curr_range = subset_ranges[index]
    gdp_partition[curr_range] = gdps[index]

  #partition into appropriate subsets
  for country, gdp in full_set:
    for index in range(0, num_levels):
      if gdp < levels[index]:
        update_gdp_partition(gdp_partition, subset_ranges[index], country, gdp)
    update_gdp_partition(gdp_partition, subset_ranges[index + 1], country, gdp)
  return gdp_partition

def validate_subsets_and_levels(num_ranges, num_levels):
  """
  Checks that there is 1 more range defined than the number of levels defined.
  """
  if num_ranges != num_levels + 1:
    print("Number of subsets must be 1 greater than number of levels")
    quit()

def update_gdp_partition(partition, subset_range, country, gdp):
  """Maps the correct gdp value to the subset range for each country."""
  partition[subset_range][country] = gdp

def format_wm(colour_scheme, str_year, gdp_partition):
  """
  Formats and saves the world map according to colour, year and datasets.
  """
  wm_style = RS(colour_scheme, base_style=LCS)
  wm = pygal.maps.world.World(style=wm_style)
  wm.title = 'World GDP in ' + str_year + ', by Country (labels in $bn)'
  for label, dataset in gdp_partition.items():
    wm.add(label, dataset)

  save_name = 'world_gdp_' + str_year + '.svg'
  wm.render_to_file(save_name)


#Capture and validate the year
year_lower_bound = 1960
year_upper_bound = 2016
year = get_year(year_lower_bound, year_upper_bound)

#load data into a list
filename = 'gdp_json.json'
gdp_data = get_json_formatted_data(filename)

#build dictionary of gdp data
country_gdps = get_cc_gdps(gdp_data, year)

#group gdp data by ranges using levels (in billions)
ranges = ['$0 - $100bn', '$100bn - $1tn', '$1tn - $10tn', '>$10tn']
levels = [100, 1000, 10000]
gdp_subsets = group_gdps_by_level(country_gdps.items(), ranges, levels)

#format and save the world map
colour_scheme = '#a02c09'
format_wm(colour_scheme, str(year), gdp_subsets)
