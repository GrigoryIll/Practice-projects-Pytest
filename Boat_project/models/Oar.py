from models import Boat

class Oar:
    """Класс для создания весел"""

    def __init__(self, hand: str, is_attached=False):
        self.hands_variants = {"лев", "прав"}
        if hand not in self.hands_variants:
            raise ValueError(f"Весло либо: {self.hands_variants}")
        self.hand = hand
        self.is_attached = is_attached


    def attach(self, boat: Boat):
        """Прикрепляем весло к лодке"""

        if self.is_attached:
            raise ValueError(f"{self.hand} весло уже вставлено в уключину")
        elif not self.is_attached and self.hand not in boat.oars:
            boat.oars.add(self.hand)
            self.is_attached = True
            print(f"{self.hand} весло вставлено в уключину")
        else:
            print(f"{self.hand} уключина не установлена, весло вставить нельзя")

    
    def detach(self, boat: Boat):
        """Открепляем весло от лодки"""

        if not self.is_attached:
            raise ValueError(f"{self.hand} весло уже снято с уключины")
        boat.oars.remove(self.hand)
        self.is_attached = False
        print(f"{self.hand} весло снято из уключины")