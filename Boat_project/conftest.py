import pytest
from models import Boat, Weather, Rowlock, Oar, Anchor, Passenger


@pytest.fixture()
def prepare_boat():
    """Фикстура для предподготовки лодки к тесту и отправки на хранение, общие шаги ТК №7-8"""

    boat_carolina = Boat()
    boat_carolina.check_boat_availability(True)
    weather1 = Weather(5)
    weather1.check_weather()
    rowlock_left = Rowlock("лев")
    rowlock_right = Rowlock("прав")
    oar_left = Oar("лев")
    oar_right = Oar("прав")
    anchor1 = Anchor()
    rowlock_left.attach(boat_carolina)
    rowlock_right.attach(boat_carolina)
    anchor1.attach(boat_carolina)
    oar_left.attach(boat_carolina)
    oar_right.attach(boat_carolina)
    luke = Passenger("Luke", 80)
    boat_carolina.set_afloat(weather=weather1)
    luke.to_aboard(luke, boat_carolina)
    yield boat_carolina, luke, oar_left, oar_right
    if oar_left.hand not in boat_carolina.oars:
        oar_left.attach(boat_carolina)
    if oar_right.hand not in boat_carolina.oars:
        oar_right.attach(boat_carolina)
    boat_carolina.row_degree(5, 10, 2)
    boat_carolina.set_ashore()
    print(boat_carolina.weights)
    for item in list(boat_carolina.weights):
        luke.to_disaboard(item, boat_carolina)
    oar_left.detach(boat_carolina)
    oar_right.detach(boat_carolina)
    rowlock_left.detach(boat_carolina)
    rowlock_right.detach(boat_carolina)
