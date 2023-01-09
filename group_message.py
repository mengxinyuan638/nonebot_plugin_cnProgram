from nonebot import on_regex
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message

class Msg:
    def __init__(self):
        self.msg = 0
        self.key = 0
    def get_msg(self,msg):
        self.msg = msg

    def get_key(self,key):
        self.key = key
msg = Msg()
message = on_regex(pattern = r''+msg.get_key()+'^$')

@message.handle()
async def send(bot: Bot, event: GroupMessageEvent, state: T_State):
    await message.send(Message(msg.get_msg()))