# This is just my initial attempt to code my final project.
class Arthropod:
    def __init__(type, insect, arachnid):
        type.insect = insect
        type.arachnid = arachnid


def get_location(city_name, county_name):
    return f"Location: {city_name}, {county_name}"


message = get_location("Amarillo", "Potter")
print(message)


def get_glossary(term):
    return f"Definition of {term}"


message = get_glossary("Culicidae")
print(message)
print("A family, Mosquitoes, of the Order Diptera (Flies).")
