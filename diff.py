"""
1. output [A,A] means output one number A;
2. input format could be [A,A], means one number A;

"""

def get_diff(union_of_include, union_of_exclude):
    res = []
    if len(union_of_include) > 0:
        for include_interval in union_of_include:
            tmp_res = include_interval
            if len(union_of_exclude) > 0:
                for exclude_interval in union_of_exclude:
                    if exclude_interval[1] < include_interval[0]:
                        continue
                    else:  # exclude_interval[1] >= include_interval[0]
                        if exclude_interval[0] > include_interval[1]:
                            break
                        else:  # exclude_interval[1] >= include_interval[0] and exclude_interval[0] <= include_interval[1]
                            if exclude_interval[0] <= include_interval[0]:
                                if exclude_interval[1] >= include_interval[1]:
                                    tmp_res = []
                                    break
                                else:  # exclude_interval[0] <= include_interval[0] and exclude_interval[1] < include_interval[1]
                                    tmp_res[0] = exclude_interval[1] + 1
                                    continue
                            else:  # exclude_interval[0] > include_interval[0]
                                if exclude_interval[1] >= include_interval[1]:
                                    tmp_res[1] = exclude_interval[0] - 1
                                    break
                                else:  # exclude_interval[1] < include_interval[1]
                                    res.append([tmp_res[0], exclude_interval[0] - 1])
                                    tmp_res[0] = exclude_interval[1] + 1
                                    continue
            if tmp_res:
                res.append(tmp_res)
    return res








