from classes import Classes

def is_attribute_distribution_optimal(attributes, character_class):
    if validate_distribution_values(attributes, character_class):
        priority_list = define_attribute_priority(character_class)
        attribute_list = []
        counter = 0
        for i in priority_list:
            if attribute_list[counter] != i:
                return False
    else:
        return False

    return True


def validate_distribution_values(attributes, character_class):
    attribute_keys_list = list(attributes.keys())
    attribute_values_list = list(attributes.values())

    for i in attribute_keys_list:
        if type(i) != str:
            return False

    for i in attribute_values_list:
        if type(i) != int:
            return False

    if character_class is Classes:
        return True


def define_attribute_priority(character_class):
    return []
