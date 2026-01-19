def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int) -> str:
    """Vérifie la santé d'une plante et lève des erreurs si nécessaire."""
    if plant_name == "":
        raise ValueError("Plant name cannot be empty!\n")

    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)\n")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)\n")

    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)\n")
    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too high (max 12)\n")

    return f"Plant '{plant_name}' is healthy!\n"


def test_plant_checks() -> None:
    """Teste les vérifications de santé des plantes."""
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        message: str = check_plant_health("tomato", 5, 6)
        print(message)
    except ValueError as error:
        print(f"Error: {error}")

    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 6)
    except ValueError as error:
        print(f"Error: {error}")

    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 6)
    except ValueError as error:
        print(f"Error: {error}")

    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as error:
        print(f"Error: {error}")

    print("All error raising tests completed!")

def main() -> None:
    test_plant_checks()

if __name__ == "__main__":
    main()