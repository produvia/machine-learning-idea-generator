from pytrends.request import TrendReq
import pprint
import pdb
import pandas as pd
import sys

# Configure pprint
pp = pprint.PrettyPrinter(depth=10)

# Configure pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Define search google search phrases
kw_list = ['predict earthquakes', 'prediction hurricanes', 'predicting earthquakes']
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')

# Find Interest Over Time
interest_over_time_df = pytrends.interest_over_time()
pp.pprint(interest_over_time_df)
df = pd.DataFrame(interest_over_time_df)
df.to_csv("output.csv")

# Interest by Region
# interest_by_region_df = pytrends.interest_by_region()
# pp.pprint(interest_by_region_df)

# Related Queries, returns a dictionary of dataframes
# related_queries_dict = pytrends.related_queries()
# pp.pprint(related_queries_dict)

# Get Google Keyword Suggestions
# suggestions_dict = pytrends.suggestions(keyword='predict')
# pp.pprint(suggestions_dict)
