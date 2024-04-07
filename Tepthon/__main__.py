import sys, asyncio
import Tepthon
from Tepthon import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID
from telethon import functions
from .Config import Config
from .core.logger import logging
from .core.session import zedub
from .utils import mybot, autoname, autovars, saves
from .utils import add_bot_to_logger_group, load_plugins, setup_bot, startupmessage, verifyLoggerGroup

LOGS = logging.getLogger("سـورس تيبثـون")
cmdhr = Config.COMMAND_HAND_LER

print(Tepthon.__copyright__)
print(f"المرخصة بموجب شروط  {Tepthon.__license__}")

cmdhr = Config.COMMAND_HAND_LER

try: #Code by T.me/zzzzl1l
    LOGS.info("⌭ جـارِ تحميـل الملحقـات ⌭")
    zedub.loop.run_until_complete(autovars())
    LOGS.info("✓ تـم تحميـل الملحقـات .. بنجـاح ✓")
except Exception as e:
    LOGS.error(f"- {e}")

if not Config.ALIVE_NAME:
    try: #Code by T.me/zzzzl1l
        LOGS.info("⌭ بـدء إضافة الاسـم التلقـائـي ⌭")
        zedub.loop.run_until_complete(autoname())
        LOGS.info("✓ تـم إضافة فار الاسـم .. بـنجـاح ✓")
    except Exception as e:
        LOGS.error(f"- {e}")

try:
    LOGS.info("⌭ بـدء تنزيـل تيبثــون ⌭")
    zedub.loop.run_until_complete(setup_bot())
    LOGS.info("✓ تـم تنزيـل تيبثــون .. بـنجـاح ✓")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()

class CatCheck:
    def __init__(self):
        self.sucess = True
Catcheck = CatCheck()

try:
    LOGS.info("⌭ بـدء إنشـاء البـوت التلقـائـي ⌭")
    zedub.loop.run_until_complete(mybot())
    LOGS.info("✓ تـم إنشـاء البـوت .. بـنجـاح ✓")
except Exception as e:
    LOGS.error(f"- {e}")

try:
    LOGS.info("⌭ جـارِ تفعيـل الاشتـراك ⌭")
    zedub.loop.create_task(saves())
    LOGS.info("✓ تـم تفعيـل الاشتـراك .. بنجـاح ✓")
except Exception as e:
    LOGS.error(f"- {e}")


async def startup_process():
    async def MarkAsViewed(channel_id):
        from telethon.tl.functions.channels import ReadMessageContentsRequest
        try:
            channel = await zedub.get_entity(channel_id)
            async for message in zedub.iter_messages(entity=channel.id, limit=5):
                try:
                    await zedub(GetMessagesViewsRequest(peer=channel.id, id=[message.id], increment=True))
                except Exception as error:
                    print ("✅")
            return True

        except Exception as error:
            print ("✅")

    async def start_bot():
      try:
          List = ["Tepthon","PPYNY","Tepthone1","Tws_Tepthon","Tepthon_Help","super_tepthon1","tepthonklaesh","VisaTepthon"]
          from telethon.tl.functions.channels import JoinChannelRequest
          for id in List :
              Join = await zedub(JoinChannelRequest(channel=id))
              MarkAsRead = await MarkAsViewed(id)
              print (MarkAsRead, "✅")
          return True
      except Exception as e:
        print("✅")
        return False

                                                     
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    LOGS.info(f"⌔ تـم تنصيـب تيبثــون . . بنجـاح ✓ \n⌔ لـ إظهـار الاوامـر أرسـل (.الاوامر)")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    Catcheck.sucess = True
    return


zedub.loop.run_until_complete(startup_process())

if len(sys.argv) not in (1, 3, 4):
    zedub.disconnect()
elif not Catcheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        zedub.run_until_disconnected()
    except ConnectionError:
        pass
