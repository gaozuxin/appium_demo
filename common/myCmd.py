# coding=utf-8
import os


def excute_cmd_result(command):
    """
    执行command命令，并返回执行结果
    :param command: 传入要执行的命令，字符串格式
    :return:返回执行结果，列表格式
    """
    result_list = []
    result = os.popen(command).readlines()
    for i in result:
        if i == '\n':
            continue
        result_list.append(i.strip('\n'))  # strip() 方法用于移除字符串头尾指定的字符
    return result_list


def excute_cmd(command):
    """
    仅执行command命令，不收集执行结果
    :param command: 传入要执行的命令，字符串格式
    """
    os.system(command)



