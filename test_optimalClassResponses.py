import unittest
import optimalClassResponses


class TestOptimalClassResponses(unittest.TestCase):
    def test_valid_attribute_values_and_keys_with_valid_character_class_should_return_true(self):
        attributes = {"str": 5, "dex": 5, "con": 5, "int": 5, "wis": 5, "cha": 5}
        character_class = "cleric"
        result = optimalClassResponses.validate_distribution_values(attributes, character_class)
        self.assertTrue(result)

    def test_valid_attribute_values_and_keys_with_invalid_character_class_should_return_false(self):
        attributes = {"str": 5, "dex": 5, "con": 5, "int": 5, "wis": 5, "cha": 5}
        character_class = "cyborg"
        result = optimalClassResponses.validate_distribution_values(attributes, character_class)
        self.assertFalse(result)

    def test_invalid_attribute_values_and_keys_with_valid_character_class_should_return_false(self):
        attributes = {"char": "not_valid", "dex": 5, "con": 5, "int": 5, "wis": 5, "cha": 5}
        character_class = "cleric"
        result = optimalClassResponses.validate_distribution_values(attributes, character_class)
        self.assertFalse(result)

    def test_invalid_attribute_values_and_keys_with_invalid_character_class_should_return_false(self):
        attributes = {"char": "not_valid", "dex": 5, "con": 5, "int": 5, "wis": 5, "cha": 5}
        character_class = "cyborg"
        result = optimalClassResponses.validate_distribution_values(attributes, character_class)
        self.assertFalse(result)

    def test_valid_attribute_values_with_invalid_keys_with_invalid_character_class_should_return_false(self):
        attributes = {"char": 5, "dex": 5, "con": 5, "int": 5, "wis": 5, "cha": 5}
        character_class = "cyborg"
        result = optimalClassResponses.validate_distribution_values(attributes, character_class)
        self.assertFalse(result)

    def test_invalid_attribute_values_with_valid_keys_with_valid_character_class_should_return_false(self):
        attributes = {"str": "not_valid", "dex": 5, "con": 5, "int": 5, "wis": 5, "cha": 5}
        character_class = "cleric"
        result = optimalClassResponses.validate_distribution_values(attributes, character_class)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
