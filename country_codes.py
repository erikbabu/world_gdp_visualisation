from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
  """Return Pygal 2 letter country code for given country."""
  for code, name in COUNTRIES.items():
    if name == country_name:
      return code
  return get_mismatched_code(country_name)

def get_mismatched_code(country_name):
  """
  Return Pygal 2 letter country code for countries named differently
  to those in JSON file
  """
  return {
     'Bolivia': 'bo',
     'Cabo Verde': 'cv',
     'Congo, Dem. Rep.': 'cd',
     'Congo, Rep.': 'cg',
     'Dominica': 'do',
     'Egypt, Arab Rep.': 'eg',
     'Gambia, The': 'gm',
     'Hong Kong SAR, China': 'hk',
     'Iran, Islamic Rep.': 'ir',
     'Korea, Rep.': 'kr',
     'Kyrgyz Republic': 'kg',
     'Lao PDR': 'la',
     'Libya': 'ly',
     'Macao SAR, China': 'mo',
     'Macedonia, FYR': 'mk',
     'Moldova': 'md',
     'Slovak Republic': 'sk',
     'Tanzania': 'tz',
     'Venezuela, RB': 've',
     'Vietnam': 'vn',
     'West Bank and Gaza': 'ps',
     'Yemen, Rep.': 'ye',
  }.get(country_name, None) #None is default value to return
