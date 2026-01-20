def check_temperature(temp_str: str) -> int:
    """Vérifie si la température est valide et comprise entre 0 & 40 degrés."""
    try:
        temp: int = int(temp_str)
    except ValueError:
        raise ValueError(f"'{temp_str}' is not a valid number")

    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")

    return temp


def test_temperature_input() -> None:
    """Teste le vérificateur de température avec différentes valeurs."""
    print("=== Garden Temperature Checker ===\n")

    test_collection: list[str] = ["25", "abc", "100", "-50"]
    for temp_str in test_collection:
        print(f"Testing temperature: {temp_str}")
        try:
            temp: int = check_temperature(temp_str)
            print(f"Temperature {temp}°C is perfect for plants!\n")
        except ValueError as error:
            print(f"Error: {error}\n")

    print("All tests completed - program didn't crash!")


def main():
    test_temperature_input()


if __name__ == "__main__":
    main()
