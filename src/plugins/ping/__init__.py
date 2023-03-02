from nonebot.plugin.on import on_regex,on_command
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import (
    Bot,
    MessageEvent,
    GroupMessageEvent,
    PrivateMessageEvent,
    MessageSegment,
    Message
    )
from nonebot.log import logger
hello = on_command("在不在", aliases = {"在不",}, rule = to_me(), priority = 50, block = True)

@hello.handle()
async def handle_first_receive(bot: Bot, event: MessageEvent):
    # print(bot)
    # print(event)
    # f"你说了：{event.get_message()}"
    msg = "嗯。"
    await  hello.finish(msg)

print(f"plugin loaded: {__name__}")