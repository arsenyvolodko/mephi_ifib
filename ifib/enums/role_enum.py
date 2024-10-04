from enum import Enum
from typing import Optional


class RoleEnum(Enum):
    SCHOOL_STUDENT = 1
    UNIVERSITY_STUDENT = 2
    ADMIN = 3

    @classmethod
    def from_db_obj(cls, obj: Optional["Role"]) -> Optional["RoleEnum"]:
        return cls(value=obj.id) if obj else None

    def to_db_obj(self) -> "Role":
        from ifib.models import Role
        return Role.objects.get(id=self.value)

    @classmethod
    def choices(cls) -> list[tuple[int, str]]:
        return [(i.value, i.formatted_name) for i in cls]

    @property
    def formatted_name(self):
        role_names = {
            self.SCHOOL_STUDENT: "Школьник",
            self.UNIVERSITY_STUDENT: "Студент",
            self.ADMIN: "Админ",

        }
        return role_names[self]
