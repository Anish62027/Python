import geocoder

# Get the location based on the IP address
g = geocoder.ip('me')

# Get latitude and longitude
latlng = g.latlng

# Get the detailed location information
location = g.address

# Display the results
print(f"Latitude and Longitude: {latlng}")
print(f"Location: {location}")
