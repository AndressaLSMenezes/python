from datetime import datetime


def data_processing(country):
    current_year = datetime.now().year
    for year in range(1930, current_year + 1):
        if year == 1930 or year == 1934 or year == 1938:
            print(year)
        elif (year - 1950) % 4 == 0 and year >= 1950:
            print(year)
    first_cup = datetime.strptime(country["first_cup"], "%Y-%m-%d").year
    if country["titles"] < 0:
        return "NegativeTitlesError: titles cannot be negative"
    elif first_cup < 1930:
        return "InvalidYearCupError: there was no world cup this year"
    return "SOBREVIVI"


data = {
    "name": "França",
    "titles": 3,
    "top_scorer": "Zidane",
    "fifa_code": "FRA",
    "first_cup": "2012-10-18",
}
print(data_processing(data))
