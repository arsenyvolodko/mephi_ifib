from enum import Enum


class EquipmentGroupEnum(Enum):
    SCINTIGRAPHY = 1
    SINGLE_PHOTON_EMISSION_TOMOGRAPHY = 2
    POSITRON_EMISSION_TOMOGRAPHY = 3
    COMPUTED_TOMOGRAPHY = 4
    MRI = 5
    RADIATION_THERAPY = 6

    @classmethod
    def from_api_name(cls, api_name: str) -> "EquipmentGroupEnum":
        return _API_NAME_DICT.get(api_name)

    @classmethod
    def api_choices(cls) -> list[str]:
        return list(_API_NAME_DICT.keys())

    @classmethod
    def from_db_obj(cls, obj: "EquipmentGroup") -> "EquipmentGroupEnum":
        return cls(value=obj.id)

    def to_db_obj(self) -> "EquipmentGroup":
        from ifib.models import EquipmentGroup

        return EquipmentGroup.objects.get(id=self.value)

    @classmethod
    def choices(cls) -> list[tuple[int, str]]:
        return [(i.value, i.formatted_name) for i in cls]

    @property
    def formatted_name(self) -> str:
        interest_sphere_names = {
            self.SCINTIGRAPHY: "Сцинтиграфия",
            self.SINGLE_PHOTON_EMISSION_TOMOGRAPHY: "Однофотонная эмиссионная томография",
            self.POSITRON_EMISSION_TOMOGRAPHY: "Позитронная эмиссионная томография",
            self.COMPUTED_TOMOGRAPHY: "Компьютерная томография",
            self.MRI: "Магнитно-резонансная томография",
            self.RADIATION_THERAPY: "Дистанционная лучевая терапия",
        }
        return interest_sphere_names[self]


_API_NAME_DICT: dict[str, EquipmentGroupEnum] = {
    "scintigraphy": EquipmentGroupEnum.SCINTIGRAPHY,
    "singlePhotonEmissionTomography": EquipmentGroupEnum.SINGLE_PHOTON_EMISSION_TOMOGRAPHY,
    "positronEmissionTomography": EquipmentGroupEnum.POSITRON_EMISSION_TOMOGRAPHY,
    "computedTomography": EquipmentGroupEnum.COMPUTED_TOMOGRAPHY,
    "MRI": EquipmentGroupEnum.MRI,
    "radiationTherapy": EquipmentGroupEnum.RADIATION_THERAPY,
}
