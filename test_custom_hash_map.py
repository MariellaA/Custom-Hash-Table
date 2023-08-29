from unittest import TestCase, main

from hash_table import HashTable


class TestHashTable(TestCase):
    def setUp(self):
        self.table = HashTable()

    def test_correct_initialization(self):
        self.assertEqual(4, self.table._HashTable__max_capacity)
        self.assertEqual([None] * 4, self.table._HashTable__keys)
        self.assertEqual([None] * 4, self.table._HashTable__values)
        self.assertEqual(0, self.table._HashTable__length)

    def test_add_expect_correct_add_of_key_value_pair(self):
        self.table.add("name", "Peter")

        self.assertEqual("Peter", self.table["name"])

    def test_get_method_without_message_returns_none_on_non_existing_key(self):
        result = self.table.get("non existing key")

        self.assertIsNone(result)

    def test_get_method_with_message_returns_message_on_non_existing_key(self):
        result = self.table.get("non existing key", "message")

        self.assertEqual("message", result)

    def test_delete_method_removes_key(self):
        self.table["name"] = "Peter"
        self.table["age"] = 25
        index = self.table._HashTable__keys.index("name")

        result = self.table.delete("name")

        self.assertEqual("name deleted", result)
        self.assertEqual(None, self.table._HashTable__keys[index])
        self.assertEqual(None, self.table._HashTable__values[index])

    def test_delete_method_without_message_returns_none_on_non_existing_key(self):
        result = self.table.delete("non existing key")

        self.assertIsNone(result)

    def test_delete_method_with_message_returns_message_on_non_existing_key(self):
        result = self.table.delete("non existing key", "message")

        self.assertEqual("message", result)

    def test_get_returns_value_on_existing_key(self):
        self.table["name"] = "Peter"

        self.assertEqual("Peter", self.table.get("name"))

    def test__getitem__invalid_key_raises_key_error(self):
        self.table["name"] = "Peter"

        with self.assertRaises(KeyError) as ke:
            result = self.table["not existing"]
        self.assertEqual("'not existing is not in the hash table'", str(ke.exception))

    def test_correct_override(self):
        self.table["name"] = "Peter"
        self.table["name"] = "Diyan"

        self.assertEqual("Diyan", self.table["name"])
        self.assertEqual(1, len(self.table))

    def test_resize_wen_table_is_full(self):
        self.table["name"] = "Peter"
        self.table["can_fight"] = True
        self.table["age"] = 25
        self.table["is_pet_owner"] = True

        self.assertEqual(4, self.table._HashTable__max_capacity)

        self.table["is_driver"] = False

        self.assertEqual(8, self.table._HashTable__max_capacity)

    def test_index_creation_on_collision_when_index_is_out_of_range_expect_success(self):
        self.table["name"] = "Peter"
        self.table["age"] = 25
        self.table["is_pet_owner"] = True

        result = self.table._HashTable__calc_index("is_driver")

        self.assertEqual(0, result)

        self.table["is_driver"] = False

    def test__str__(self):
        self.table["name"] = "Peter"
        self.table["age"] = 25

        expected = "{name: Peter, age: 25}"
        result = str(self.table)

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
