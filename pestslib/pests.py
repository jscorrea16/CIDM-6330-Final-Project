class Pest:
    def __init__(self, genus, species):
        self.genus = genus
        self.species = species

    def __str__(self) -> str:
        return f"{self.genus} - {self.species}"


class PestObservation:
    def __init__(self, city, county, obs_date):
        self.city = city
        self.county = county
        self.obs_date = obs_date

    def __str__(self) -> str:
        return f"{self.city} - {self.county} - {self.obs_date}"



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
