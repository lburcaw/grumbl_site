#!/usr/bin/env python

# coding: utf-8

#Import packages
import urllib
import json
import re

def googleGeocoding(address):
    """This function takes an address and returns the latitude and longitude from the Google geocoding API."""
    baseURL = 'http://maps.googleapis.com/maps/api/geocode/json?'
    geocodeURL = baseURL + 'address=' + address + '&components=administrative_area:NY|country:US'
    geocode = json.loads(urllib.urlopen(geocodeURL).read())
    return geocode

#Example usage
#f = googleGeocoding('308 Hemlock St, Brooklyn, NY')

def getGeocodeLatLong(geocodeJSON):
    """This function takes the json output of a googleGeocoding function call and
    parses it to output the latitude and longitude"""
    latlong = geocodeJSON['results'][0]['geometry']['location']
    return latlong

#Example usage
#addressLatLong getGeocodeLatLong(f)
