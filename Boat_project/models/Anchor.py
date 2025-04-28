from .boat import Boat


class Anchor:
    """Класс для создания объекта якоря (прикрепляем, открепляем)"""

    def __init__(self, is_attached=False):
        self.is_attached = is_attached

    def attach(self, boat: Boat):
        """Прикрепляем якорь к лодке"""

        if self.is_attached or boat.anchor is not None:
            raise ValueError("Якорь уже закреплен")
        boat.anchor = True
        self.is_attached = True
        print("Якорь и веревка прикреплены к лодке")

    def detach(self, boat: Boat):
        """Открепляем якорь от лодки"""

        if not self.is_attached:
            raise ValueError("Якорь уже откреплен")
        self.is_attached = False
        boat.anchor = None
        print("Якорь и веревка сняты с лодки")
