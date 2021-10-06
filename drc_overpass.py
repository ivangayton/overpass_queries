#!/usr/bin/python3

import sys, os
import requests
import json

def query(query_string):
    """Accept a query in Overpass API query language, 
    return a JSON string of the data from an Overpass server
    """
    overpass_url = "http://overpass-api.de/api/interpreter"
    #overpass_url = "https://lz4.overpass-api.de/api/interpreter"
    try:
        response = requests.get(overpass_url,
                                params={'data': query_string})
    except:
        print("overpass did not want to answer that one\n")
        print(e)
    print(response)
    data = response.json()
    return data

def raw_json_to_geojson_points(overpass_json):
    """Accept a raw JSON string of data from an Overpass API query.
    Return a GeoJSON of the same data, after converting all polygons
    to points.
    """
    

def geojsons_to_geopackage(geojson):
    """Accept one or more GeoJSON files, return geopackage"""

if __name__ == "__main__":
    """return a bunch of data from Overpass API"""

    health_zones = """
    [out:json];
    area["ISO3166-1"="CD"][admin_level=2];
    (nwr["boundary"="health"]
        ["health_level"="6"]
        ["type"="boundary"](area);
    );
    out body;
    >;
    out body;
    """

    health_areas = """
    [out:json];
    area["ISO3166-1"="CD"][admin_level=2];
    (nwr["boundary"="health"]
        ["health_level"="8"]
        ["type"="boundary"](area);
    );
    out body;
    >;
    out body;
    """
    
    health_cells = """
    [out:json];
    area["ISO3166-1"="CD"][admin_level=2];
    (nwr["boundary"="health"]
        ["health_level"="10"]
        ["type"="boundary"](area);
    );
    out body;
    >;
    out body;
    """

    health_facilities = """
    [out:json][timeout:200];
    (
    area["ISO3166-1"="CD"][admin_level=2];
    nwr["amenity"="health_post"](area)(-2.05,27,3.8,31.1);
    area["ISO3166-1"="CD"][admin_level=2];
    nwr["amenity"="doctors"](area)(-2.05,27,3.8,31.1);
    area["ISO3166-1"="CD"][admin_level=2];
    nwr["amenity"="clinic"](area)(-2.05,27,3.8,31.1);
    area["ISO3166-1"="CD"][admin_level=2];
    nwr["amenity"="hospital"](area)(-2.05,27,3.8,31.1);
    );
    out body;
    >;
    out body;
    """

        
    education = """
    [out:json][timeout:200];
    (
    area["ISO3166-1"="CD"][admin_level=2];
    nwr["amenity"="college"](area)(-2.05,27,3.8,31.1);
    area["ISO3166-1"="CD"][admin_level=2];
    nwr["amenity"="kindergarten"](area)(-2.05,27,3.8,31.1);
    area["ISO3166-1"="CD"][admin_level=2];
    nwr["amenity"="university"](area)(-2.05,27,3.8,31.1);
    area["ISO3166-1"="CD"][admin_level=2];
    nwr["amenity"="school"](area)(-2.05,27,3.8,31.1);
    );
    out body;
    >;
    out body;
    """

    vaccination = """
    [out:json][timeout:200];
    (
    area["ISO3166-1"="CD"][admin_level=2];
    nwr["vaccination"](area)(-2.05,27,3.8,31.1);
    );
    out body;
    >;
    out body;
    """
    
    overpass_url = "http://overpass-api.de/api/interpreter"
    data = query(health_facilities)

    with open('results.json', 'w') as of:
        of.writelines(json.dumps(data))
