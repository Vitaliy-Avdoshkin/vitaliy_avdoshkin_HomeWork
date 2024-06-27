from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(state):
    assert filter_by_state(state)


def test_filter_by_state_empty():
    assert filter_by_state([])


def test_sort_by_date(date):
    assert sort_by_date(date)


def test_sort_by_date_empty():
    assert sort_by_date([])
