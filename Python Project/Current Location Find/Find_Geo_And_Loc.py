import geocoder
g = geocoder.ip('me')

latlng = g.latlng

location = g.address

print(f"Latitude and Longitude: {latlng}")
print(f"Location: {location}")
