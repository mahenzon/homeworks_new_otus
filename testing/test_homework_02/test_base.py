import pytest
from faker import Faker

fake = Faker()

homework = pytest.importorskip("homework_02")
base = homework.base
exceptions = homework.exceptions


CONSUMPTION_MIN = fake.pyint(9, 13)


@pytest.fixture
def vehicle():
    weight = fake.pyint(150, 1000)
    fuel = fake.pyint(30, 80)
    fuel_consumption = fake.pyint(CONSUMPTION_MIN, 18)
    vehicle = base.Vehicle(weight, fuel, fuel_consumption)
    return vehicle


class TestVehicle:

    def test_create_vehicle(self):
        weight = fake.pyint()
        fuel = fake.pyint()
        fuel_consumption = fake.pyint()
        vehicle = base.Vehicle(weight, fuel, fuel_consumption)
        assert vehicle.weight == weight
        assert vehicle.fuel == fuel
        assert vehicle.fuel_consumption == fuel_consumption

    def test_start_ok(self, vehicle):
        assert vehicle.fuel > 0
        assert vehicle.started is False
        vehicle.start()
        assert vehicle.started is True

    def test_cannot_start_low_fuel(self, vehicle):
        assert vehicle.started is False
        vehicle.fuel = 0
        with pytest.raises(exceptions.LowFuelError):
            vehicle.start()
        assert vehicle.started is False

    def test_move_ok(self, vehicle):
        assert vehicle.fuel_consumption > 0
        assert vehicle.fuel > 0
        assert vehicle.fuel > vehicle.fuel_consumption
        max_distance = vehicle.fuel // vehicle.fuel_consumption
        distance = fake.pyint(1, max_distance)
        expected = vehicle.fuel - distance * vehicle.fuel_consumption
        vehicle.move(distance)
        assert vehicle.fuel == expected

    @pytest.mark.parametrize("fuel", [
        pytest.param(0, id="move_when_zero_fuel"),
        pytest.param((CONSUMPTION_MIN - 1), id="fuel_just_a_bit_lower_than_consumption"),
    ])
    def test_move_low_fuel(self, fuel, vehicle):
        vehicle.fuel = fuel
        assert vehicle.fuel_consumption > 0

        with pytest.raises(exceptions.NotEnoughFuel):
            vehicle.move(1)

    def test_move_not_enough_fuel(self, vehicle):
        # set fuel enough only for 2
        assert vehicle.fuel_consumption > 1
        vehicle.fuel = vehicle.fuel_consumption * 2 + 1

        with pytest.raises(exceptions.NotEnoughFuel):
            vehicle.move(3)
