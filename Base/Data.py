import yaml


def get_yml_data(file_name, data_name):
    '''
    核心功能: 调用当前函数时会返回一个列表嵌套字典的数据,供参数化直接使用
    :param: file_name 就是某一个目标yml文件的名称
    :param: data_name 就是yml中某一个最外层的键名
    :return:
    '''
    data_list = list()
    with open("./Data/{}.yml".format(file_name), 'r', encoding='utf8') as f:
        data = yaml.load(f)[data_name]
        for item in data.values():
            data_list.append(item)
    return data_list


if __name__ == '__main__':
    print(get_yml_data("data_pub_art", "pub_art"))
