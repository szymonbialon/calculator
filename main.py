import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def add(a, b):
    result = a + b
    logging.info(f"Dodaję {a} i {b}")
    return result


def subtract(a, b):
    result = a - b
    logging.info(f"Odejmuję {b} od {a}")
    return result


def multiply(a, b):
    result = a * b
    logging.info(f"Mnożę {a} i {b}")
    return result


def divide(a, b):
    if b != 0:
        result = a / b
        logging.info(f"Dzielę {a} przez {b}")
        return result
    else:
        raise ValueError("Nie można dzielić przez zero.")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Błąd: Proszę podać poprawną liczbę.")


def print_menu():
    print("""Podaj działanie, posługując się odpowiednią liczbą:
1 Dodawanie
2 Odejmowanie
3 Mnożenie
4 Dzielenie""")


def execute_operation(calculation_type, a, b):
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }

    return operations[calculation_type](a, b)


def calculator():
    while True:
        print_menu()
        calculation_type = input("Wybierz numer (1-4): ")

        if calculation_type in ['1', '2', '3', '4']:
            perform_calculation(calculation_type)
        else:
            print("Błąd: Proszę wybrać prawidłowy numer.")


def perform_calculation(calculation_type):
    a = get_number("Podaj składnik 1: ")
    b = get_number("Podaj składnik 2: ")

    try:
        result = execute_operation(calculation_type, a, b)
        print(f"Wynik to: {result:.2f}")
    except ValueError as e:
        print(f"Błąd: {e}")


if __name__ == "__main__":
    calculator()
