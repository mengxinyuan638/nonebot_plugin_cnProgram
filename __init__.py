"""本插件实现中文编程转换nonebot插件
灵感来源：Qrspeed(手机端qq机器人)
"""
import re
from resource import Resource
from checker import Checker


class Translate:
    """管理翻译的类"""

    def __init__(self):
        self.file = open('ciku/ck.txt', 'r', encoding='utf-8')
        self.file_msg = self.file.readlines()
        self.resource = Resource()  # 实例化用户资源
        self.read_type = 0  # 供判断语句等使用
        self.checker = Checker(self.resource)  # 判断语句模块

    def main_run(self):
        """主程序"""
        self.check_type()

    def check_type(self):
        """本方法判断需要调用哪些方法"""
        for msg in self.file_msg:
            if self.read_type == 0:
                if re.search('%(.*)%=(.*)', msg.strip().replace(' ', '')) != None:
                    """如果定义了变量调用value方法存储变量以及值"""
                    if '如果' in msg:
                        """检测到if语句"""
                        type = self.checker.check_if(msg)
                        if type == 1:
                            self.read_type = 1
                    else:
                        self.value()
                elif '输出' in msg:
                    """如果检测到输出则调用输出方法"""
                    self.output(msg)
            elif '返回' in msg:
                self.read_type = 0
            else:
                pass

    def value(self):
        """读取和存储变量"""
        for msg in self.file_msg:
            if re.search('%(.*)%=(.*)', msg.strip().replace(' ', '')) == None or '如果' in msg:
                """本分支判断是否定义了字符串，在该分支中，排除了如果语句"""
                pass
            else:
                """定义了变量，执行读取和存储变量"""
                v_name = re.search('%(.*)%', msg.strip())  # 获取变量名
                get_value = re.search(f'%{v_name.group(1)}%=(.*)', msg.strip().replace(' ', ''))  # 获取变量值
                self.resource.value_list[v_name.group(1)] = get_value.group(1)  # 储存用户定义的变量

    def output(self, string):
        """定义输出的方法"""
        msg = string.strip('输出').replace(' ', '').strip('\n')  # 去除空格和输出关键词和换行
        if re.search('%(.*)%', msg.strip().replace(' ', '')) == None:
            print(string.strip('输出').strip())
        else:
            value = msg.strip('%')
            msg = self.resource.value_list[value]
            print(msg)


if __name__ == "__main__":
    AI = Translate()
    AI.main_run()
