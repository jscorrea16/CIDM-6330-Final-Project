class Pest:
    def __init__(self, x):
        self.x = x


pest = Pest("Culex pipiens")
print(pest.x)
pest = Pest("Loxosceles reclusa")
print(pest.x)


class PestObservation:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


pestobservation = PestObservation("Amarillo,", "Randall", "3/22/2022")
print(pestobservation.x, pestobservation.y, pestobservation.z)
pestobservation = PestObservation("Canyon,", "Randall", "3/27/2022")
print(pestobservation.x, pestobservation.y, pestobservation.z)


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
