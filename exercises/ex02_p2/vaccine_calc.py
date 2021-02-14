"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "930410205"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    days_until: int = days_to_target(population, doses, doses_per_day, target)
    days_left: str = future_date(days_until)
    print("We will reach " + str(target) + "% vaccination in " + str(days_until) + " days, which falls on " + days_left)


def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    days_needed = ((((2 * (target / 100) * (population)) - doses)) / (doses_per_day))
    days_needed = round(days_needed)
    return int(days_needed)


def future_date(days: int) -> str:
    today: datetime = datetime.today()
    days_until_vaccination: timedelta = timedelta(days)
    vaccination_date: datetime = today + days_until_vaccination
    dia_de_vacuna: str = str(vaccination_date.strftime("%B %d, %Y"))
    return str(dia_de_vacuna)

    
if __name__ == "__main__":
    main()
