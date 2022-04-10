class Pest:
    def __init__(self, x):
        self.x = x


pest = Pest("Culex pipiens")
print(pest.x)
pest = Pest("Loxosceles reclusa")
print(pest.x)


class PestObservation:
    def __init__(self, city, county, obs_date):
        self.city = city
        self.county = county
        self.obs_date = obs_date


pestobservation = PestObservation("Amarillo,", "Randall", "3/22/2022")
print(pestobservation.city, pestobservation.county, pestobservation.obs_date)


class MaladyType:
    def __init__(self):
        self.known_vectors: Pest = []


class ImpactObservation:
    def __init__(self):
        self.malady_type = None
        self.species = None
        self.city = None
        self.county = None
        self.obs_date = None
