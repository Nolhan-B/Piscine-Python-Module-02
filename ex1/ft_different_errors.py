def garden_operations() -> None:
    """Déclenche et gère différents types d'erreurs Python."""
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError...")
        result: float = 10 / 0
        print(result)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        print("Testing FileNotFoundError...")
        file = open("missing.txt", "r")
        file.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    try:
        print("Testing KeyError...")
        plants: dict[str, int] = {"rose": 3}
        print(plants["missing_plant"])
    except KeyError:
        print("Caught KeyError: 'missing_plant'\n")


def test_error_types() -> None:
    """Teste chaque erreur et montre que le programme continue."""
    print("=== Garden Error Types Demo ===\n")
    garden_operations()

    print("Testing multiple errors together...")
    try:
        value: int = int("abc")
        result: float = 5 / 0
        print(value, result)
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


def main():
    """Point d’entrée principal du programme."""
    test_error_types()


if __name__ == "__main__":
    main()
