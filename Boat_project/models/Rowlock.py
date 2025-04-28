from .boat import Boat


class Rowlock:
    """Класс для создания улючин для лодки"""

    def __init__(self, hand: str, is_attached=False):
        self.hands_variants = {"лев", "прав"}
        if hand not in self.hands_variants:
            raise ValueError(f"Уключина либо: {self.hands_variants}")
        self.hand = hand
        self.is_attached = is_attached
        self.functionality = True

    def attach(self, boat: Boat):
        """Прикрепляем уключину к лодке"""

        if self.is_attached or self.hand in boat.rowlocks:
            raise ValueError(f"{self.hand} уключина уже установлена")
        boat.rowlocks.add(self.hand)
        self.is_attached = True
        print(f"{self.hand} уключина установлена")

    def detach(self, boat: Boat):
        """Открепляем уключину от лодки"""

        if not self.is_attached:
            raise ValueError(f"{self.hand} уключина уже демонтирована")
        if self.hand in boat.oars:
            raise ValueError(
                f"Сначало нужно вытащить весло из {self.hand} уключины")
        boat.rowlocks.remove(self.hand)
        self.is_attached = False
        print(f"{self.hand} уключина демонтирована")

    def check_functionality(self, status: bool):
        """Проверяем функциональность уключин"""

        STATUS = {True, False}
        if status not in STATUS:
            raise ValueError(f"Функциональность может быть: {STATUS}")
        if status:
            self.functionality = True
            print("Функционально")
        else:
            self.functionality = False
            print("Нефункционально")
