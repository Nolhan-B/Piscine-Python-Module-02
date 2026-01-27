class GardenError(Exception):
    """Erreur de base liée au jardin."""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Erreur de base liée aux plantes."""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    """Erreur de base liée a l'eau."""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterTank:
    def __init__(
        self,
        name: str,
        capacity: int,
        current_volume: int = 0
    ) -> None:
        self.name = name
        self.capacity = capacity

        if current_volume < 0:
            raise ValueError("Volume cannot be negative")
        if current_volume > capacity:
            raise ValueError("Volume exceeds tank capacity")

        self.__current_volume = current_volume

    def water(self) -> None:
        if self.__current_volume == 0:
            raise WaterError("Not enough water in tank")
        self.__current_volume -= 1

    def fill(self, amount: int) -> None:
        """Adds water to the tank"""
        if amount <= 0:
            raise WaterError("Amount must be positive")

        if self.__current_volume + amount > self.capacity:
            raise WaterError("Tank overflow")

        self.__current_volume += amount

    def get_current_volume(self) -> int:
        """Returns the current water volume"""
        return self.__current_volume


class Plant:
    def __init__(
        self,
        name: str,
        water_level: int,
        sunlight_hours: int
    ) -> None:
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours

    def water(self) -> None:
        self.water_level += 1

    def check_health(self) -> None:
        if self.water_level < 1:
            raise PlantError(
                f"Error checking {self.name}: "
                f"Water level {self.water_level} is too low (min 1)"
            )
        if self.water_level > 10:
            raise PlantError(
                f"Error checking {self.name}: "
                f"Water level {self.water_level} is too high (max 10)"
            )

        if self.sunlight_hours < 2:
            raise PlantError(
                f"Sunlight hours {self.sunlight_hours} "
                "is too low (min 2)"
            )
        if self.sunlight_hours > 12:
            raise PlantError(
                f"Sunlight hours {self.sunlight_hours} "
                "is too high (max 12)"
            )

        print(
            f"{self.name}: healthy (water: {self.water_level}, "
            f"sun: {self.sunlight_hours})"
        )


class Garden:
    def __init__(self, name: str) -> None:
        self.name = name
        self.plant_collection: list[Plant] = []

    def add_plant(self, new_plant: Plant) -> None:
        if (new_plant is None):
            raise ValueError("Plant cannot be none!")
        if (new_plant.name == ""):
            raise ValueError("Plant name cannot be empty!")
        self.plant_collection.append(new_plant)
        print(f"Added {new_plant.name} successfully")

    def water_plants(self, water_tank: WaterTank) -> None:
        if not self.plant_collection:
            raise GardenError("There is no plant to water!")
        if water_tank is None:
            raise GardenError("No WaterTank provided!")
        for plant in self.plant_collection:
            water_tank.water()
            plant.water()
            print(f"Watering {plant.name} - success")

    def check_plant_health(self) -> None:
        if not self.plant_collection:
            raise GardenError("There is no plant to check health!")
        for plant in self.plant_collection:
            try:
                plant.check_health()
            except PlantError as e:
                print(e)


class GardenManager:

    @staticmethod
    def create_garden(name: str) -> Garden:
        return Garden(name)

    @staticmethod
    def add_multiple_plant_to_garden(
        plants_to_add: list[Plant | None],
        garden: Garden
    ) -> None:
        print("Adding plants to garden...")
        for plant in plants_to_add:
            try:
                garden.add_plant(plant)
            except ValueError as e:
                print(f"Error adding plant: {e}")

    @staticmethod
    def water_garden_plants(garden: Garden, water_tank: WaterTank) -> None:
        try:
            print("Opening Watering system")
            garden.water_plants(water_tank)
        except WaterError as e:
            print(f"Caught WaterError: {e}")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("Closing watering system (cleanup)\n")

    @staticmethod
    def water_plant(plant: Plant, water_tank: WaterTank) -> None:
        error: int = 0
        try:
            water_tank.water()
            plant.water()
        except GardenError as e:
            print(f"Caught GardenError: {e}")
            error += 1
        except WaterError as e:
            print(f"Caught WaterError: {e}")
            error += 1
        finally:
            if error != 0:
                print("System recovered and continuing...\n")

    @staticmethod
    def check_garden_plants_health(garden: Garden) -> None:
        try:
            garden.check_plant_health()
        except GardenError as e:
            print(f"Caught GardenError: {e}")


def test_garden_management():
    print("=== Garden Management System ===\n")

    my_water_tank = WaterTank("nbilyj watertank",  10, 10)
    my_garden = GardenManager.create_garden("nbilyj garden")
    tomato = Plant("tomato", 8, 10)
    lettuce = Plant("lettuce", 0, 0)
    empty = Plant("", 0, 0)
    plant_arr = [tomato, lettuce, empty, None]
    GardenManager.add_multiple_plant_to_garden(plant_arr, my_garden)

    print("\nWatering plants...")
    GardenManager.water_garden_plants(my_garden, my_water_tank)

    print("\nChecking plant health...")
    GardenManager.check_garden_plants_health(my_garden)

    print("\nTesting error recovery...")
    empty_tank = WaterTank("nbilyj watertank", 10, 0)
    GardenManager.water_plant(tomato, empty_tank)

    print("Garden management system test complete!")


def main() -> None:
    test_garden_management()


if __name__ == "__main__":
    main()
