from enums.classes import Classes


def is_attribute_distribution_optimal(attributes, character_class):
    if validate_distribution_values(attributes, character_class):
        ordered_attributes = reorder_attribute_list(attributes, define_attribute_priority())
        counter = 0
        for i in ordered_attributes:
            if i < ordered_attributes[counter + 1]:
                return False
            counter += 1
            if counter > len(ordered_attributes):
                break
    else:
        return False

    return True


def validate_distribution_values(attributes, character_class):
    attribute_keys_list = list(attributes.keys())
    attribute_values_list = list(attributes.values())
    attribute_order = ["str", "dex", "con", "int", "wis", "cha"]
    counter = 0

    for i in attribute_keys_list:
        if type(i) != str or i != attribute_order[counter]:
            return False
        counter += 1

    for i in attribute_values_list:
        if type(i) != int:
            return False

    if character_class not in Classes:
        return False

    return True


def define_attribute_priority(character_class):
    #utilizar uma hashtable com a ordem dos valores?
    return []


def reorder_attribute_list(attribute_list, priority_list):
    #utilizar a lista priority_list para reordernar os valores do dicionário attribute_list baseando-se em suas chaves
    return []

