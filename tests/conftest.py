import pytest


@pytest.fixture
def test_expected_count():
    return 2


@pytest.fixture
def sort_date_false():
    return [
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2020-06-30T02:08:58.425572'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2021-10-14T08:21:33.419441'},
                {'id': 594226727, 'state': 'NONE', 'date': '2022-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'NONE', 'date': '2023-10-14T08:21:33.419441'}]


@pytest.fixture
def sort_date_true():
    return [
                {'id': 615064591, 'state': 'NONE', 'date': '2023-10-14T08:21:33.419441'},
                {'id': 594226727, 'state': 'NONE', 'date': '2022-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2021-10-14T08:21:33.419441'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2020-06-30T02:08:58.425572'},
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            ]
