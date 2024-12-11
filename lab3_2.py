# TODO Напишите функцию find_common_participants


def find_common_participants(first_group, second_group, splitter=","):
    first_group_split = set(first_group.split(splitter))
    second_group_split = set(second_group.split(splitter))
    res = list(first_group_split.intersection(second_group_split))
    res.sort()
    return res


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, " "))
