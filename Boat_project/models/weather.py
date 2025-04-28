class Weather:
    """Класс создания погоды"""

    def __init__(self, wind_speed: int):
        self.wind_speed = wind_speed
        self.weather_status = False

    def check_weather(self):
        """Прикрепляем погоду для возможности проведения тестов"""

        if self.wind_speed > 5:
            raise ValueError("Погода неудовлетворительная")
        self.weather_status = True
        print("Погода удовлетворительная")
