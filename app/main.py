from abc import ABC


class IntegerRange:
    def __init__(self, min_amount: int, max_amount: int) -> None:
        self.min_amount = min_amount
        self.max_amount = max_amount

    def __set_name__(self, owner: str, name: str) -> None:
        self.name = name

    def __get__(self, instance: object, owner: object) -> str:
        return instance.__dict__.get(self.name)

    def __set__(self, instance: object, value: int) -> int:
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer")
        if not (self.min_amount <= value <= self.max_amount):
            raise ValueError(f"{self.name} "
                             f"must be between {self.min_amount} "
                             f"and {self.max_amount}")
        instance.__dict__[self.name] = value


class Visitor:
    def __init__(self, name: str, age: int, height: int, weight: int) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


class SlideLimitationValidator(ABC):
    def __init__(self, age: int, weight: int, height: int) -> None:
        self.age = age
        self.weight = weight
        self.height = height


class ChildrenSlideLimitationValidator:
    @staticmethod
    def validate(visitor: "Visitor") -> bool:
        if visitor.age < 4 or visitor.age > 14:
            return False

        if visitor.height < 80 or visitor.height > 120:
            return False

        if visitor.weight < 20 or visitor.weight > 50:
            return False

        return True


class AdultSlideLimitationValidator:
    @staticmethod
    def validate(visitor: Visitor) -> bool:
        if visitor.age < 14:
            return False
        if visitor.height < 120:
            return False
        if visitor.weight < 50:
            return False
        if visitor.age > 60:
            return False
        if visitor.height > 220:
            return False
        if visitor.weight > 120:
            return False
        return True


class Slide:
    def __init__(self, name: str, limitation_class: object) -> None:
        self.name = name
        self.limitation_class = limitation_class

    def can_access(self, visitor: Visitor) -> bool:
        return self.limitation_class.validate(visitor)
