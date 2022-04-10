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


class Illness:
    def __init__(self, suspect_pathogen):
        self.suspect_pathogen = suspect_pathogen

    def __str__(self) -> str:
        return self.suspect_pathogen


class DiagnosticTesting:
    def __init__(self, test_type, antibody_type, test_results, record_date):
        self.test_type = test_type
        self.antibody_type = antibody_type
        self.test_results = test_results
        self.record_date = record_date

    def __str__(self) -> str:
        return f"{self.test_type} - {self.antibody_type} - {self.test_results} - {self.record_date}"
