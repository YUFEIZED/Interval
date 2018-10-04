from union import get_union
from diff import get_diff

include_list_1 = [
    [10, 100]
]
exclude_list_1 = [
    [20, 30]
]
result_1 = get_diff(get_union(include_list_1),get_union(exclude_list_1))
assert result_1 == [[10, 19], [31, 100]]

include_list_2 = [
    [50, 5000],
    [10, 100]
]
exclude_list_2 = []
result_2 = get_diff(get_union(include_list_2),get_union(exclude_list_2))
assert result_2 == [[10, 5000]]

include_list_3 = [
    [10, 100],
    [200, 300]
]
exclude_list_3 = [
    [95, 205]
]
result_3 = get_diff(get_union(include_list_3),get_union(exclude_list_3))
assert result_3 == [[10, 94], [206, 300]]

include_list_4 = [
    [10, 100],
    [200, 300],
    [400, 500]
]
exclude_list_4 = [
    [95, 205],
    [410, 420]
]
result_4 = get_diff(get_union(include_list_4),get_union(exclude_list_4))
assert result_4 == [[10, 94], [206, 300], [400, 409], [421, 500]]
