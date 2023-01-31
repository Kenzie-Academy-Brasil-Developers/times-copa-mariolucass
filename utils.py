def data_processing(dict: dict):

    last_cup = 2022

    first_cup__in_dict: str = dict["first_cup"][:4]
    first_cup: int = int(first_cup__in_dict)

    disputed_cups = (last_cup - first_cup) / 4

    titles_in_dict: str = dict["titles"]
    titles: int = int(titles_in_dict)

    if titles < 0:
        raise KeyError("titles cannot be negative")

    if first_cup < 1930:
        raise KeyError("there was no world cup this year")

    if not (first_cup - 1930) % 4 == 0:
        print("there was no world cup this year")

    if titles > disputed_cups:
        print("impossible to have more titles than disputed cups")
