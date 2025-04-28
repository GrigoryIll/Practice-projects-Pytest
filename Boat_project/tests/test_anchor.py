import pytest


@pytest.mark.parametrize("boat_is_afloat, anchor_in_boat, boat_is_anchored, expected_result",
                         [(True, True, False, False), (False, True, False, True),
                          (False, True, True, True),
                          (False, False, False, True),
                          (False, False, True, True)],
                         ids=["valid1", "invalid1", "invalid2", "invalid3", "invalid4"])
def test_boat_anchor_func(boat_is_afloat, anchor_in_boat, boat_is_anchored,
                          expected_result, prepare_boat):
    """Тест возможности опустить и поднять якорь, ТК №11. 
    Также, проверка на возможность обрабатывать ошибки"""

    boat_carolina, luke, oar_left, oar_right = prepare_boat
    boat_carolina.is_afloat = boat_is_afloat
    boat_carolina.is_anchored = boat_is_anchored
    boat_carolina.anchor = anchor_in_boat
    if boat_carolina.anchor and boat_carolina.is_afloat and not boat_carolina.is_anchored:
        boat_carolina.set_anchor()
        boat_carolina.unset_anchor()
        assert boat_carolina.is_anchored == expected_result
    else:
        with pytest.raises(ValueError) as excinfo:
            boat_carolina.set_anchor()
        assert "Лодка не на воде, либо якорь уже установлен/якоря нет" in str(
            excinfo.value)
    if not boat_carolina.is_afloat:
        boat_carolina.is_afloat = True
