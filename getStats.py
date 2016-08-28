#author: Laurence Armstrong
import json

''' Example stop data
{
    'stop_code': '3382',
    'stop_id': '3382',      # Has leading zeros compared to stop code
    'parent_station': '41344',
    'the_geom': '0101000020E61000007767EDB60BD8654072DC291DAC6342C0',
    'stop_lat': -36.77869,
    'stop_lon': 174.75143,
    'stop_name': '9 Nile Rd',
    'location_type': 0,
    'stop_city': None,              # Unused
    'stop_region': None,            # Unused
    'stop_street': None,            # Unused
    'zone_id': None,                # Unused
    'stop_country': None,           # Unused
    'stop_desc': None,              # Unused
    'direction': None,              # Unused
    'wheelchair_boarding': None,    # Unused
    'stop_postcode': None,          # Unused
    'stop_url': None,               # Unused
    'stop_timezone': None,          # Unused
    'position': None                # Unused
}
'''

stop_data = None
with open("stopData") as f:
    stop_data = json.load(f)

print("There are {} bus stops in Auckland".format(len(stop_data)))
