import re


class Checker:
    """条件方法管理类"""

    def __init__(self,resource):
        """主方法"""
        self.resource = resource

    def check_if(self, string):
        """if语句"""
        checker = string.strip().replace(' ', '')  # 获取条件语句
        check_str = checker.strip('如果').strip(':')
        if re.search('(.*)==(.*)', check_str) != None:
            type = self.check_xd(check_str)

        return type

    def check_xd(self,check_str):
        """相等判断的方法"""
        first = re.search('(.*)==', check_str)  # 获取条件1
        second = re.search('==(.*)', check_str)  # 获取条件2
        if '%' in first.group(1):
            """条件1有变量在其中"""
            first_change = first.group(1).strip('%')
            first_change = self.resource.value_list[first_change]
        else:
            first_change = first.group(1)
        if '%' in second.group(1):
            """条件2有变量在其中"""
            second_change = second.group(1).strip('%')
            second_change = self.resource.value_list[second_change]
        else:
            second_change = second.group(1)

        if first_change != second_change:
            read_type = 1
        else:
            read_type = 0

        return read_type