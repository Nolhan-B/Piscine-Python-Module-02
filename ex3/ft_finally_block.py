def water_plants(plant_list: list[str | None]) -> None:
    """Arrose les plantes et ferme toujours le système d'arrosage."""
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as error:
        print(f"Error: {error}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Teste le système d'arrosage avec et sans erreurs."""
    print("=== Garden Watering System ===")

    print("Testing normal watering...")
    good_plants: list[str] = ["tomato", "lettuce", "carrots"]
    water_plants(good_plants)
    print("Watering completed successfully!")

    print("Testing with error...")
    bad_plants: list[str | None] = ["tomato", None, "lettuce"]
    water_plants(bad_plants)
    print("Cleanup always happens, even with errors!")


def main():
    """Point d’entrée principal du programme."""
    test_watering_system()


if __name__ == "__main__":
    main()