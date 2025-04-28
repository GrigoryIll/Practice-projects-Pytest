import pytest


@pytest.mark.parametrize("boat_is_afloat, oars_hands, expected_result",
                         [(True, {"лев", "прав"}, 125), (True, {"прав"}, 125),
                          (False, {"лев", "прав"}, 125)],
                         ids=["valid1", "invalid1", "invalid2"])
def test_boat_move_straight(boat_is_afloat, oars_hands, expected_result, prepare_boat):
    """Тест движения лодки по прямой, ТК №9. Также, проверка на возможность обрабатывать ошибки"""

    boat_carolina, luke, oar_left, oar_right = prepare_boat
    boat_carolina.is_afloat = boat_is_afloat
    boat_carolina.oars = oars_hands
    if oar_left.hand not in oars_hands:
        oar_left.is_attached = False
    if oar_right.hand not in oars_hands:
        oar_right.is_attached = False
    if boat_carolina.is_afloat and len(boat_carolina.oars) > 1:
        boat_carolina.row_straight(5, 5)
        boat_carolina.row_straight(20, 5)
        assert boat_carolina.location == expected_result
    else:
        with pytest.raises(ValueError) as excinfo:
            boat_carolina.row_straight(5, 5)
        assert "Лодка не на воде либо нет весел, грести нельзя" in str(
            excinfo.value)
    if not boat_carolina.is_afloat:
        boat_carolina.is_afloat = True


@pytest.mark.parametrize("boat_is_afloat, oars_hands, expected_result",
                         [(True, {"лев"}, 720), (True, set(), 720),
                          (False, {"лев"}, 720)],
                         ids=["valid1", "invalid1", "invalid2"])
def test_boat_turn(boat_is_afloat, oars_hands, expected_result, prepare_boat):
    """Тест возможности лодки поворачивать, ТК №10. Также, проверка на возможность 
    обрабатывать ошибки"""

    boat_carolina, luke, oar_left, oar_right = prepare_boat
    boat_carolina.is_afloat = boat_is_afloat
    boat_carolina.oars = oars_hands
    if oar_left.hand not in oars_hands:
        oar_left.is_attached = False
    if oar_right.hand not in oars_hands:
        oar_right.is_attached = False
    if boat_carolina.is_afloat and len(boat_carolina.oars) > 0:
        boat_carolina.row_turn(360, 2)
        assert boat_carolina.location == expected_result
    else:
        with pytest.raises(ValueError) as excinfo:
            boat_carolina.row_straight(5, 5)
        assert "Лодка не на воде либо нет весел, грести нельзя" in str(
            excinfo.value)
    if not boat_carolina.is_afloat:
        boat_carolina.is_afloat = True
