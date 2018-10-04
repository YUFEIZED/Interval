from interval import Interval,IntervalException

def get_union(list_of_lists):
    list_of_lists.sort()
    res = []
    list_interval = []
    try:
        for interval in list_of_lists:
            if interval != []:
                list_interval.append(Interval(interval[0], interval[1]))
    except IntervalException as e:
        print e
        return res

    if len(list_interval) > 0:
        for interval_first in list_interval:
            if not interval_first.completed:
                interval_first.complete()
                interval_res = Interval(interval_first.min_val, interval_first.max_val)
                for interval_second in list_interval:
                    if not interval_second.completed:
                        if interval_res.max_val >= interval_second.min_val:
                            if interval_second.max_val >= interval_res.max_val:
                                interval_res.max_val = interval_second.max_val
                            interval_second.complete()
                        else:
                            break
                    else:
                        continue
                res.append(interval_res.format)
            else:
                continue
    return res
