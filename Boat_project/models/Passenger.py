from models import Boat, Weight, Equipment
from typing import Union

class Passenger:
    """Класс для создания человека(пассажира)"""

    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    
    def change_seat(self, seat: str, boat: Boat):
        """Пересаживаемся на другое место в лодке"""

        if seat not in boat.seats:
            raise ValueError(f"Пересесть невозможно. Доступны места: {boat.seats}")
        print(f"Вы пересели на место: {seat}")


    def to_aboard(self, item: Union[Weight, Equipment], boat: Boat) :
        """Грузим объекты в лодку"""

        boat.weights.add(item)
        boat.current_weight += item.weight
        print(f"На борт принят груз {item.weight} кг., вес лодки {boat.current_weight} кг")
        if boat.current_weight > boat.max_weight:
            raise ValueError(f"Превышен допустимый максимальный вес лодки в {boat.max_weight} кг")
        

    def to_disaboard(self, item: Union[Weight, Equipment], boat: Boat):
        """Выгружаем объекты из лодки"""

        if boat.current_weight <= 0:
            raise ValueError(f"Лодка пуста.")
        boat.weights.remove(item)
        boat.current_weight -= item.weight
        print(f"C борта снят груз {item.weight} кг, вес лодки {boat.current_weight} кг")