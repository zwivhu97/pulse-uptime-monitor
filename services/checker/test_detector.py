from detector import is_outage


def r(is_up):
    return {"is_up": is_up}


def test_not_enough_history_is_not_an_outage():
    assert is_outage([r(False), r(False)], failures_needed=3) is False


def test_three_failures_in_a_row_is_an_outage():
    assert is_outage([r(False), r(False), r(False)], failures_needed=3) is True


def test_one_success_breaks_the_streak():
    assert is_outage([r(False), r(True), r(False)], failures_needed=3) is False