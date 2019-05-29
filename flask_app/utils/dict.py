from collections import defaultdict


def group_by_key(original_dict, group_key, alternative_value="unregistered"):
    new_dict = defaultdict(list)
    for element in original_dict:
        key = element.get(group_key, alternative_value)
        new_dict[key].append(element)
    return new_dict
