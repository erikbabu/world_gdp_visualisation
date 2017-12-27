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
    return None
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
      gdp_val = get_correctly_formatted_gdp(gdp_dict['Value'])
      code = get_country_code(country_name)
      if code:
        country_gdps[code] = gdp_val
  return country_gdps

def get_correctly_formatted_gdp(gdp_val):
  """Returns GDP in $bn as an integer."""
  billion = 1000000000
  return int(float(gdp_val) / billion)

def format_wm(colour_scheme, str_year, gdp_labels):
  """
  Formats and saves the world map according to colour, year and datasets.
  """
  wm_style = RS(colour_scheme, base_style=LCS)
  wm = pygal.maps.world.World(style=wm_style)
  wm.title = 'World GDP in ' + str_year + ', by Country (labels in $bn)'
  for label, dataset in gdp_labels.items():
    wm.add(label, dataset)

  save_name = 'world_gdp_' + str_year + '.svg'
  wm.render_to_file(save_name)

def group_gdps_by_level(full_set):
  """Partitions the data into the correct levels."""
  #numbers were originally divided by 1 billion
  hundred_billion = 100
  one_trillion    = 1000
  ten_trillion    = 10000

  #subset ranges
  range_1 = '$0 - $100bn'
  range_2 = '$100bn - $1tn'
  range_3 = '$1tn - $10tn'
  range_4 = '>$10tn'

  gdps_1, gdps_2, gdps_3, gdps_4 = {}, {}, {}, {}

  #create ordered dictionary to be returned
  gdp_labels = OrderedDict()
  gdp_labels[range_1] = gdps_1
  gdp_labels[range_2] = gdps_2
  gdp_labels[range_3] = gdps_3
  gdp_labels[range_4] = gdps_4

  #partition into appropriate subsets
  for country, gdp in full_set:
    if gdp < hundred_billion:
      gdp_labels[range_1][country] = gdp
    elif gdp < one_trillion:
      gdp_labels[range_2][country] = gdp
    elif gdp < ten_trillion:
      gdp_labels[range_3][country] = gdp
    else:
      gdp_labels[range_4][country] = gdp

  return gdp_labels

#Capture and validate the year
year_lower_bound = 1960
year_upper_bound = 2016
year = get_year(year_lower_bound, year_upper_bound)

#load data into a list
filename = 'gdp_json.json'
gdp_data = get_json_formatted_data(filename)

if not gdp_data:
  quit()

#build dictionary of gdp data
country_gdps = get_cc_gdps(gdp_data, year)

#group gdp data by level
gdp_subsets = group_gdps_by_level(country_gdps.items())

#format and save the world map
colour_scheme = '#a02c09'
format_wm(colour_scheme, str(year), gdp_subsets)
