from enum import Enum


class EducationalStatusEnum(Enum):
    SCHOOL_STUDENT = "school_student"
    UNIVERSITY_STUDENT = "university_student"

    @classmethod
    def choices(cls):
        return [(key.value, key.value) for key in cls]

    @property
    def formatted_name(self) -> str:
        role_names = {
            self.SCHOOL_STUDENT: "Школьник",
            self.UNIVERSITY_STUDENT: "Студент",
        }
        return role_names[self]
