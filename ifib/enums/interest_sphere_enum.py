from enum import Enum


class InterestSphereEnum(Enum):
    IT = "it"
    SCIENCE = "science"

    @classmethod
    def choices(cls):
        return [(key.value, key.value) for key in cls]

    @property
    def formatted_name(self) -> str:
        interest_sphere_names = {
            self.IT: "it",
            self.SCIENCE: "Наука",
        }
        return interest_sphere_names[self]
