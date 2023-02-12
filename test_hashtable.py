# test_hashtable.py

from hashtable import HashTable


def test_should_create_hashtable():
    assert HashTable(capacity=100) is not None
