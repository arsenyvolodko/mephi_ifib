from enum import Enum


class InterestSphereEnum(Enum):
    IT = "IT"
    SCIENCE = "SCIENCE"
    ART = "ART"
    SPORT = "SPORT"
    MUSIC = "MUSIC"

    @property
    def api_name(self):
        return self.name.lower()

    @classmethod
    def choices(cls):
        return [(key.api_name, key.api_name) for key in cls]

    @property
    def formatted_name(self):
        interest_sphere_names = {
            "IT": "IT",
            "SCIENCE": "Наука",
            "ART": "Искусство",
            "SPORT": "Спорт",
            "MUSIC": "Музыка",
        }
        return interest_sphere_names[self.name]