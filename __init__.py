"""本插件实现中文编程转换nonebot插件
灵感来源：Qrspeed(手机端qq机器人)
"""
import re
from resource import Resource


class Translate:
    """管理翻译的类"""
    def __init__(self):
        self.file = open('./ck.txt', 'r', encoding = 'utf-8')
        self.file_msg = self.file.readlines()
        self.resource = Resource() #实例化用户资源

    def main_run(self):
        for msg in self.file_msg:
            if re.search('%(.*)%=(.*)',msg.strip().replace(' ','')) != None:
                """如果定义了变量调用value方法存储变量以及值"""
                self.value()
            elif '输出' in msg:
                """如果检测到输出则调用输出方法"""
                self.output(msg)


    def value(self):
        """读取和存储变量"""
        for msg in self.file_msg:
            if re.search('%(.*)%=(.*)',msg.strip().replace(' ','')) == None or '如果' in msg:
                """本分支判断是否定义了字符串，在该分支中，排除了如果语句"""
                pass
            else:
                """定义了变量，执行读取和存储变量"""
                v_name = re.search('%(.*)%',msg.strip()) #获取变量名
                get_value = re.search(f'%{v_name.group(1)}%=(.*)',msg.strip().replace(' ','')) #获取变量值
                self.resource.value_list[v_name.group(1)] = get_value.group(1) #储存用户定义的变量

    def output(self, string):
        """定义输出的方法"""
        msg = string.strip('输出').replace(' ','') #去除空格和输出关键词
        if re.search('%(.*)%',msg.strip().replace(' ','')) == None:
            print(msg)
        else:
            value = msg.strip('%')
            msg = self.resource.value_list[value]
            print(msg)

if __name__ == "__main__":
    AI = Translate()
    AI.main_run()