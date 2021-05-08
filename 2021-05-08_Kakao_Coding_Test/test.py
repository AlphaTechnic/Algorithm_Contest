from collections import OrderedDict

ordered_dict = OrderedDict([('d', 1), ('a', 1), ('b', 2), ('c', 2),  ('e', 3)])
print(ordered_dict.keys())
print(list(ordered_dict.keys())[2])