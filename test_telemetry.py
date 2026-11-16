import pytest
from robot_telemetry import validate

def test_validate_valid_battery():
    data = {"robot_id": "robot1", "battery_pct": 50}
    assert validate(data) is True


def test_validate_lower_boundary():
    data = {"robot_id": "robot1", "battery_pct": 0}
    assert validate(data) is True


def test_validate_upper_boundary():
    data = {"robot_id": "robot1", "battery_pct": 100}
    assert validate(data) is True


def test_validate_battery_too_high():
    data = {"robot_id": "robot1", "battery_pct": 101}
    assert validate(data) is False


def test_validate_battery_negative():
    data = {"robot_id": "robot1", "battery_pct": -1}
    assert validate(data) is False


def test_validate_battery_is_string():
    data = {"robot_id": "robot1", "battery_pct": "50"}
    assert validate(data) is False


def test_validate_battery_is_bool():
    data = {"robot_id": "robot1", "battery_pct": True}
    assert validate(data) is False


def test_validate_missing_battery():
    data = {"robot_id": "robot1"}
    assert validate(data) is False