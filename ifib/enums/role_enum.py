from enum import Enum


class RoleEnum(Enum):
    SCHOOL_STUDENT = 1
    UNIVERSITY_STUDENT = 2
    STAFF = 3
    ADMIN = 4

    @property
    def formatted_name(self):
        role_names = {
            "SCHOOL_STUDENT": "Школьник",
            "UNIVERSITY_STUDENT": "Студент",
            "STAFF": "Сотрудник",
            "ADMIN": "Менеджер (Админ)",
        }
        return role_names[self.name]
