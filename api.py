import requests
import geocoder

destinations = ["The Space Needle",
  "Crater Lake",
  "The Golden Gate Bridge",
  "Yosemite National Park",
  "Las Vegas, Nevada",
  "Grand Canyon National Park",
  "Mount Rushmore",
  "Yellowstone National Park",
  "Sandpoint, Idaho",
  "Banff National Park",
  "Capilano Suspension Bridge"]

for point in destinations:
  loc = geocoder.arcgis(point)

  print("{0} is located at ({1:.4f}, {2: .4f})".format(point, loc.latlng[0], loc.latlng[1]))