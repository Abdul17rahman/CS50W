#dictionaries are python mapping of key and values.

locations = {
    "Abdul":"Buziga",
    "hadija":"Kitintale"
}

print(locations["Abdul"])

#Adding a value to the dict
locations["Birungi"] = "Luzira"

print(locations)

#Removes a key from the dict
locations.pop("Abdul")
print(locations)