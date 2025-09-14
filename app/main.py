class Visitor:
    def __init__(self, name: str, age: int, height: int, weight: int) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


class ChildrenSlideLimitationValidator:
    @staticmethod
    def validate(visitor: Visitor) -> bool:
        if visitor.age < 4:
            return False
        if visitor.height < 80:
            return False
        if visitor.weight < 20:
            return False
        if visitor.age > 14:
            return False
        if visitor.height > 120:
            return False
        if visitor.weight > 50:
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
    def __init__(self, name: str, limitation_class: str) -> None:
        self.name = name
        self.limitation_class = limitation_class

    def can_access(self, visitor: Visitor) -> bool:
        return self.limitation_class.validate(visitor)
