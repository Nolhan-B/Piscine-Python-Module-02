class GardenError(Exception):
    """Erreur de base liée au jardin."""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Erreur liée aux plantes."""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    """Erreur liée à l'arrosage."""
    def __init__(self, message: str) -> None:
        super().__init__(message)


def check_plant_health() -> None:
    """Déclenche une erreur liée à une plante."""
    raise PlantError("The tomato plant is wilting!")


def check_water_level() -> None:
    """Déclenche une erreur liée à l'arrosage."""
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    """Teste les erreurs personnalisées du jardin."""
    print("=== Custom Garden Errors Demo ===\n")

    try:
        print("Testing PlantError...")
        check_plant_health()
    except PlantError as error:
        print(f"Caught PlantError: {error}\n")

    try:
        print("Testing WaterError...")
        check_water_level()
    except WaterError as error:
        print(f"Caught WaterError: {error}\n")

    print("Testing catching all garden errors...")
    try:
        check_plant_health()
    except GardenError as error:
        print(f"Caught a garden error: {error}")

    try:
        check_water_level()
    except GardenError as error:
        print(f"Caught a garden error: {error}\n")

    print("All custom error types work correctly!")


def main():
    """Point d’entrée principal du programme."""
    test_custom_errors()


if __name__ == "__main__":
    main()
