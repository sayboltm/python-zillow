# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 09:48:21 2019

basically copied from GH rn
https://www.zillow.com/howto/api/APIOverview.htm
@author: Mike
"""

import zillow

with open("../bin/config/zillow_key.conf", 'r') as f:
    key = f.readline().replace("\n", "")

api = zillow.ValuationApi()

address = "425 Royal Ave, Royal Oak, MI"
postal_code = "48073"

data = api.GetSearchResults(key, address, postal_code)
'''
    api  
     'GetComps',
     'GetDeepComps',
     'GetDeepSearchResults',
     'GetSearchResults',
     'GetZEstimate',
'''

# data holds return object of zillow.place.Place

# Find place using zillow place id
#zpid="2100641621"
#detail_data = api.GetZEstimate(key, zpid)

# Find comps
#zpid="2100641621"
#detail_data = api.GetComps(key, zpid)

##Get Deep Search Results
#address = "3400 Pacific Ave., Marina Del Rey, CA"
#postal_code = "90292"
#
#data = api.GetDeepSearchResults(key, address, postal_code)


#Get Deep Comps
#zws_id = "<your key>"
#zpid = 2100641621
#count=10
#
#data = data = api.GetDeepComps(zws_id, zpid, count)


### zpid royal: 24623647
data.get_dict
data.zpid # None of this seemse super useful

royal_zpid=24623647
data = api.GetZEstimate(key, royal_zpid)

# why doesn't this work?
'''
#[x for x in dir(data) if not x.startswith('__')]

for item in [x for x in dir(data) if not x.startswith('__')]:
    data.item
# err 'Place'missing attribute 'item' (duh)
    
    
    ['debug',
 'extended_data',
 'full_address',
 'get_dict',
 'has_extended_data',
 'links',
 'local_realestate',
 'set_data',
 'set_values_from_dict',
 'similarity_score',
 'zestiamte',
 'zestimate',
 'zpid']
    '''
#target_attrs = [x for x in dir(data) if not x.startswith('__')]
#
#for item in target_attrs:
#    eval(data.item)
    
# hmm no extended_data, all Nonetype, returns false for has_extended_Data
    