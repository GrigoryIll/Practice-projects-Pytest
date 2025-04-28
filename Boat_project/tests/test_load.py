import pytest
from models import Weight


@pytest.mark.parametrize("total_boat_weight, water_in_boat_status, "
                         "expected_weight, expected_water_in_boat",
                         [(300, False, 300, False), (299, False, 299, False),
                          (301, True, 301, True), (300, "Yes", 300, False)],
                         ids=["valid1", "valid2", "invalid1", "invalid2"])
def test_boat_max_load(total_boat_weight, water_in_boat_status, expected_weight,
                       expected_water_in_boat, prepare_boat):
    """Тест на возможность лодки оставаться на плаву при погрузки на нее максимального веса, ТК №13. 
    Также, проверка на возможность обрабатывать ошибки"""

    boat_carolina, luke, oar_left, oar_right = prepare_boat
    WEIGHTS_COUNT = 8
    weight_each = (total_boat_weight - luke.weight)/WEIGHTS_COUNT
    weight_list = [Weight(weight_each) for _ in range(8)]
    if boat_carolina.max_weight < expected_weight:
        with pytest.raises(ValueError) as excinfo:
            for weight in weight_list:
                luke.to_aboard(weight, boat_carolina)
        assert f"Превышен допустимый максимальный вес лодки в {boat_carolina.max_weight} кг" in str(
            excinfo.value)
    else:
        for weight in weight_list:
            luke.to_aboard(weight, boat_carolina)
        assert boat_carolina.current_weight == expected_weight
    if water_in_boat_status not in boat_carolina.water_in_boat_status:
        with pytest.raises(ValueError) as excinfo:
            boat_carolina.check_water_in_boat(water_in_boat_status)
        assert f"Вода либо: {boat_carolina.water_in_boat_status}" in str(
            excinfo.value)
    else:
        boat_carolina.check_water_in_boat(water_in_boat_status)
        assert boat_carolina.water_in_boat == expected_water_in_boat
