from models import Weather, Anchor


class Boat:
    """Класс для создания объекта лодки"""

    def __init__(self, max_weight=300, max_speed=20, oars=None, anchor=None, rowlocks=None, weights=None):
        self.max_weight = max_weight
        self.max_speed = max_speed
        self.oars = oars if oars is not None else set()
        self.anchor = anchor
        self.rowlocks = rowlocks if rowlocks is not None else set()
        self.seats = ("нос", "центр", "корма")
        self.is_afloat = False
        self.current_weight = 0
        self.location = 0
        self.is_anchored = False
        self.boat_availability = False
        self.boat_availability_status = {True, False}
        self.water_in_boat = False
        self.water_in_boat_status = {True, False}
        self.capsized = False
        self.capsized_status = {True, False}
        self.weights = weights if weights is not None else set()


    def set_afloat(self, weather: Weather):
        """Определяем что лодка на воде"""

        if self.is_afloat:
            raise ValueError("Лодка уже спущена на воду")
        elif weather.weather_status and self.boat_availability: 
            self.is_afloat = True
            print("Лодка спущена на воду")
        else:
            raise ValueError("Лодку спустить нельзя")
    
    def set_ashore(self):
        """Отправляем лодку на берег"""

        if not self.is_afloat:
            raise ValueError("Лодка уже на берегу")
        else:
            self.is_afloat = False
        print("Лодку вытащена на берег")

    def row_straight(self, speed: int, time: int):
        """Гребем прямо"""

        if self.is_afloat and len(self.oars) > 1: 
            self.location += speed*time
            print(f"Гребем в заданном направлении со скоростью {speed} км/ч")
        else:
            raise ValueError("Лодка не на воде либо нет весел, грести нельзя")
    
    def row_turn(self, degree: int, time: int):
        """Поворачиваем лодку"""

        if self.is_afloat and len(self.oars) > 0:
            self.location += degree*time
            print(f"Поворачиваем")
        else:
            raise ValueError("Лодка не на воде либо нет весел, грести нельзя")

    def row_degree(self, speed: int, degree: int, time: int):
        """Гребем под углом, работая веслами поочередно"""

        if self.is_afloat and len(self.oars) > 1: 
            self.location += speed*degree*time
            print(f"Гребем в заданном направлении со скоростью {speed} км/ч")
        else:
            raise ValueError("Лодка не на воде либо нет весел, грести нельзя")

    def set_anchor(self):
        """Устанавливаем якорь"""

        if not self.is_afloat or self.is_anchored or not self.anchor:
            raise ValueError("Лодка не на воде, либо якорь уже установлен/якоря нет")
        else:
            self.is_anchored = True
            print(f"Якорь установлен")
    
    def unset_anchor(self):
        """Поднимаем якорь со дна"""

        if not self.is_afloat or not self.is_anchored or not self.anchor:
            raise ValueError("Лодка не на воде, либо якорь уже поднят/якоря нет")
        self.is_anchored = False
        print(f"Якорь поднят, очищен от грязи, уложен в лодку")
    
    def check_boat_availability(self, status: str):
        """Проверка доступности лодки для использования(свободна)"""

        if status not in self.boat_availability_status:
            raise ValueError(f"Лодка либо: {self.boat_availability_status}")
        elif status:
            self.boat_availability = True
            print(f"Лодку можно взять")
        else:
            print(f"Лодку нельзя взять.")
    
    def check_water_in_boat(self, status: str):
        """Проверка наличия воды в лодке"""

        if status not in self.water_in_boat_status:
            raise ValueError(f"Вода либо: {self.water_in_boat_status}")
        elif status:
            self.water_in_boat = True
            print(f"Вода в лодке")
        else:
            self.water_in_boat = False
            print(f"Воды в лодке нет")
    
    def check_capsized(self, status: str):
        """Проверка что лодка не перевернулась"""

        if status not in self.capsized_status:
            raise ValueError(f"Лодка либо: {self.capsized_status}")
        if status:
            self.capsized = True
            print(f"Лодка перевернулась")
        else:
            print(f"Лодка не перевернулась")