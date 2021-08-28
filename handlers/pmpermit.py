from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hi there, This is a music assistant service .\n\n Contact Master :@callme_pro \n❗️ Rules:\n   - No chatting allowed\n   - No spam allowed \n\n 👉 **SEND YOUR GROUP INVITE LINK OR USERNAME HERE @Animeloverz1234  IF USERBOT CAN'T JOIN YOUR GROUP.**\n\n ⚠️ Disclamer: If you need any help then join support group :- @Animeloverz1234\n    - Don't add this user to secret groups.\n   - Don't Share private info here\n\n")
  return                        
