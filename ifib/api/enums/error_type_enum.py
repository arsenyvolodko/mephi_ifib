from enum import Enum


class ErrorTypeEnum(Enum):
    # /api/v1/auth/register
    USER_ALREADY_EXISTS = 1

    # /api/v1/auth/register/confirm
    INVALID_CONFIRMATION_CODE = 2
    TOO_MANY_CONFIRMATION_CODE_INPUT_ATTEMPTS = 3

