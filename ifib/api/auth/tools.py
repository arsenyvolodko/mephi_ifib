import random


def generate_confirmation_code() -> str:
    return "".join(map(str, [random.randint(0, 9) for _ in range(4)]))
