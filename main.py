import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

def calculator():
    print("Podaj działanie, posługując się odpowiednią liczbą:")
    print("1 Dodawanie")
    print("2 Odejmowanie")
    print("3 Mnożenie")
    print("4 Dzielenie")

    calculation_type = input("Wybierz numer (1-4): ")

    if calculation_type in ['1', '2', '3', '4']:
        a = float(input("Podaj składnik 1: "))
        b = float(input("Podaj składnik 2: "))

        if calculation_type == '1':
            operation = "Dodaję"
            result = a + b
            logging.info(f"{operation} {a} i {b}")
            print(f"Wynik to: {result:.2f}")
        elif calculation_type == '2':
            operation = "Odejmuję"
            result = a - b
            logging.info(f"{operation} {a} od {b}")
            print(f"Wynik to: {result:.2f}")
        elif calculation_type == '3':
            operation = "Mnożę"
            result = a * b
            logging.info(f"{operation} {a} i {b}")
            print(f"Wynik to: {result:.2f}")
        elif calculation_type == '4':
            if b != 0:
                operation = "Dzielę"
                result = a / b
                logging.info(f"{operation} {a} przez {b}")
                print(f"Wynik to: {result:.2f}")
            else:
                print("Błąd: Nie można dzielić przez zero.")
                return

    else:
        print("Błąd: Proszę wybrać prawidłowy numer.")

if __name__ == "__main__":
    calculator()
