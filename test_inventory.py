import pytest
from inventory import Inventory

def test_add_item():
    inventory = Inventory()
    inventory.add_item("apple", 10)
    assert inventory.get_inventory() == {"apple": 10}

def test_add_existing_item():
    inventory = Inventory()
    inventory.add_item("banana", 5)
    inventory.add_item("banana", 3)
    assert inventory.get_inventory() == {"banana": 8}

def test_add_negative_quantity():
    inventory = Inventory()
    with pytest.raises(ValueError, match="Quantity cannot be negative"):
        inventory.add_item("orange", -5)

def test_remove_item():
    inventory = Inventory()
    inventory.add_item("apple", 10)
    inventory.remove_item("apple", 5)
    assert inventory.get_inventory() == {"apple": 5}

def test_remove_item_not_found():
    inventory = Inventory()
    with pytest.raises(ValueError, match="Item not found in inventory"):
        inventory.remove_item("banana", 1)

def test_remove_item_insufficient_quantity():
    inventory = Inventory()
    inventory.add_item("apple", 3)
    with pytest.raises(ValueError, match="Not enough quantity in inventory"):
        inventory.remove_item("apple", 5)

def test_remove_item_entire_quantity():
    inventory = Inventory()
    inventory.add_item("grape", 4)
    inventory.remove_item("grape", 4)
    assert inventory.get_inventory() == {}
