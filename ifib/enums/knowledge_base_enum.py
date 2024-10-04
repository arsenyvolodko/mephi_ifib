from enum import Enum


class KnowledgeBaseEnum(Enum):
    RADIONUCLIDES_DIAGNOSIS = 1
    RADIATION_THERAPY = 2
    ULTRA_SOUND_DIAGNOSIS = 3
    MRI_DIAGNOSIS = 4
    SAFETY = 5
    REGULATORY_DOCUMENTS = 6

    @classmethod
    def from_api_name(cls, api_name: str) -> "KnowledgeBaseEnum":
        return _API_NAME_DICT.get(api_name)

    @classmethod
    def api_choices(cls) -> list[str]:
        return list(_API_NAME_DICT.keys())

    @classmethod
    def from_db_obj(cls, obj: "KnowledgeBase") -> "KnowledgeBaseEnum":
        return cls(value=obj.id)

    def to_db_obj(self) -> "KnowledgeBase":
        from ifib.models import KnowledgeBase

        return KnowledgeBase.objects.get(id=self.value)

    @classmethod
    def choices(cls) -> list[tuple[int, str]]:
        return [(i.value, i.formatted_name) for i in cls]

    @property
    def formatted_name(self) -> str:
        interest_sphere_names = {
            self.RADIONUCLIDES_DIAGNOSIS: "Радионуклидная диагностика и терапия",
            self.RADIATION_THERAPY: "Лучевая терапия",
            self.ULTRA_SOUND_DIAGNOSIS: "УЗИ",
            self.MRI_DIAGNOSIS: "МРТ",
            self.SAFETY: "Техника безопасности",
            self.REGULATORY_DOCUMENTS: "Нормативно-правовые документы",
        }
        return interest_sphere_names[self]


_API_NAME_DICT: dict[str, KnowledgeBaseEnum] = {
    "radionuclidesDiagnosis": KnowledgeBaseEnum.RADIONUCLIDES_DIAGNOSIS,
    "radiationTherapy": KnowledgeBaseEnum.RADIATION_THERAPY,
    "ultraSoundDiagnosis": KnowledgeBaseEnum.ULTRA_SOUND_DIAGNOSIS,
    "mriDiagnosis": KnowledgeBaseEnum.MRI_DIAGNOSIS,
    "safety": KnowledgeBaseEnum.SAFETY,
    "regulatoryDocuments": KnowledgeBaseEnum.REGULATORY_DOCUMENTS,
}
