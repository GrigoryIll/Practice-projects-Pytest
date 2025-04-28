from models import Boat

class Anchor:
    """Класс для создания объекта якоря (прикрепляем, открепляем)"""

    def __init__(self, is_attached=False):
        self.is_attached = is_attached


    def attach(self, boat: Boat):
        """Прикрепляем якорь к лодке"""

        if self.is_attached or boat.anchor is not None:
            raise ValueError("Якорь уже закреплен")
        else:
            boat.anchor = True
            self.is_attached = True
            print(f"Якорь и веревка прикреплены к лодке")

    
    def detach(self, boat: Boat):
        """Открепляем якорь от лодки"""
        
        if not self.is_attached:
            raise ValueError("Якорь уже откреплен")
        else:
            self.is_attached = False
            boat.anchor = None
            print(f"Якорь и веревка сняты с лодки")