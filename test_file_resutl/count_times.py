from test_case import get_res_count_data, read_rstrip_data, get_one_key, get_start_time_list_str
from scripts.base_path import FILES_PATH


if __name__ == "__main__":
    file_path = FILES_PATH + '\\' + '1.log'
    log_path = FILES_PATH + '\\' + 'compare.log'
    data = read_rstrip_data(file_path)  # list
    _data = get_res_count_data(data)  # 含有中文记录
    count = []
    for i in _data:
        if get_one_key(i) != '你好小美':
            count.append(1)
    print(len(count))

    # log_data = read_rstrip_data(log_path)
    # print(len(log_data))
    # all_time = get_start_time_list_str(log_data)
    # print(len(all_time))
