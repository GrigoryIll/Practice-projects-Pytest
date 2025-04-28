import pytest

@pytest.mark.parametrize("seat, status_capsized, expected_result", [("нос", False, False), ("корма", False, False), 
                                                                    ("нос", True, True), ("корма", True, True), 
                                                                    ("впереди", False, False), ("нос", "на бок", False)],
                                                                    ids = ["valid1", "valid2", "valid3", "valid4","invalid1", "invalid2"])
def test_boat_stability(seat, status_capsized, expected_result, prepare_boat):
    """Тест устойчивости лодки на воде, ТК №5. Также проверяем возможность обработать ошибки"""

    boat_carolina, luke, oar_left, oar_right = prepare_boat
    if seat not in boat_carolina.seats:
        with pytest.raises(ValueError) as excinfo:
            luke.change_seat(seat, boat_carolina)
        assert f"Пересесть невозможно. Доступны места: {boat_carolina.seats}" in str(excinfo.value)
    elif status_capsized not in boat_carolina.capsized_status:
        with pytest.raises(ValueError) as excinfo:
            boat_carolina.check_capsized(status_capsized)
        assert (f"Лодка либо: {boat_carolina.boat_availability_status}") in str(excinfo.value)
    else:
        luke.change_seat(seat, boat_carolina)
        boat_carolina.check_capsized(status_capsized)
        assert boat_carolina.capsized == expected_result