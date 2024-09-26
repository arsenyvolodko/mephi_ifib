from enum import Enum


class RoleEnum(Enum):
    SCHOOL_STUDENT = 1
    UNIVERSITY_STUDENT = 2
    ADMIN = 3

    @property
    def formatted_name(self):
        role_names = {
            self.SCHOOL_STUDENT: "Школьник",
            self.UNIVERSITY_STUDENT: "Студент",
            self.ADMIN: "Админ",

        }
        return role_names[self]
