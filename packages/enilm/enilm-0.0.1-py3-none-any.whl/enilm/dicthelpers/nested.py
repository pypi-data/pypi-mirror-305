def check_in_nested_dict(_dict, _dict_path) -> bool:
    if len(_dict_path) == 1:
        return _dict_path[0] in _dict
    if not _dict_path[0] in _dict:
        return False
    return check_in_nested_dict(_dict[_dict_path[0]], _dict_path[1:])


def put_in_nested_dict(_dict, _dict_path, _val):
    curr_dict = _dict
    for curr_path_lvl in range(len(_dict_path)):
        curr_subpath = _dict_path[curr_path_lvl]
        if not curr_subpath in curr_dict:
            curr_dict[curr_subpath] = {}
        if curr_path_lvl == len(_dict_path) - 1:
            curr_dict[curr_subpath] = _val
        curr_dict = curr_dict[curr_subpath]
