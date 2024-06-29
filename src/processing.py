from typing import Any


def filter_by_state(input_list: list[Any], state="EXECUTED") -> Any:
    """Функция фильтрации операций по ключу state"""

    filtered_list = []
    if len(input_list) > 0:
        for element in input_list:
            if element["state"] == state:
                filtered_list.append(element)

            return filtered_list
    else:
        return "Список пуст"


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
            },
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2018-10-14T08:21:33.419441",
            },
        ],
        "CANCELED",
    )
)


def sort_by_date(input_list: list[Any], descending=True) -> Any:
    """Функция сортировки операций по дате"""
    if len(input_list) > 0:
        sorted_list = sorted(
            input_list, key=lambda x: x.get("date"), reverse=descending
        )
        return sorted_list
    else:
        return "Список пуст"


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
            },
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2018-10-14T08:21:33.419441",
            },
        ]
    )
)
