

import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from BRANDEDKING import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from BRANDEDKING import app
from random import  choice, randint

#▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒⩹━⊷⌯𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒



@app.on_message(
    command(["مميزات","مميزات هانتر"])
 )
async def mmmezat(client, message):
        await message.reply_text(f"""**مرحبآ بك عزيزي » {message.from_user.mention}**في قسم مميزات سورس هانتر ميوزك\n
⩹━𓍹𓋹𓍻⊷⌯⌞ ⩹━⊷⌯𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺

𓍹𓋹𓍻قايمه مميزات سورس هانتر 

𓍹𓋹𓍻ميزه ⦂ المطور بيجيب المطور البوت 
𓍹𓋹𓍻ميزه ⦂ تبيه بفتح+قفل المكالمه
𓍹𓋹𓍻ميزه ⦂ ترحيب دخول و خروج الاعضاء 
𓍹𓋹𓍻ميزه ⦂ جروب بيجيب الجروب+الرابط+ايدي
𓍹𓋹𓍻ميزه ⦂ قول البوت بيقول بالكلمه اللي بتقولها 
𓍹𓋹𓍻ميزه ⦂ الالعاب +كت+تويت+العاب متطوره
𓍹𓋹𓍻ميزه ⦂ تلغراف ميديا بردعالصوره
𓍹𓋹𓍻ميزه ⦂ ايدي بالرد بالصوره
𓍹𓋹𓍻ميزه ⦂ صورتي يرد بالصوره ونسبه
𓍹𓋹𓍻ميزه ⦂ اذاعه خاص+بالتثبيت+بالمساعد+عام
𓍹𓋹𓍻ميزه ⦂ الصوتيه..ف المكالمه
𓍹𓋹𓍻ميزه ⦂ نزول تلقائي للمساعد لعدم وجود حد فالمكالمه
𓍹𓋹𓍻ميزه ⦂ بث مباشر للقنوات 
𓍹𓋹𓍻ميزه ⦂ اسمي بيجب الاسم
𓍹𓋹𓍻ميزه ⦂ سورس بيجب السورس
𓍹𓋹𓍻ميزه ⦂ حظر+كتم ميوزك
𓍹𓋹𓍻ميزه ⦂ كشف
𓍹𓋹𓍻ميزه ⦂ منشن لكل الاعضاء
𓍹𓋹𓍻ميزه ⦂ انا من
𓍹𓋹𓍻ميزه ⦂ رتبتي
𓍹𓋹𓍻ميزه ⦂ مبرمج
𓍹𓋹𓍻ميزه ⦂ المنشئ+المالك
𓍹𓋹𓍻ميزه ⦂ الاحصائيات
𓍹𓋹𓍻ميزه ⦂ كيب المطور من خلاله تتحكم في الحساب المساعد
𓍹𓋹𓍻ميزه ⦂ الاذكار
𓍹𓋹𓍻ميزه ⦂ تبيه بوقت صلاه
𓍹𓋹𓍻ميزه ⦂ دعوه في مكالمه
𓍹𓋹𓍻ميزه ⦂  دعوه فالخاص متاع البوت
𓍹𓋹𓍻ميزه ⦂ تنبيه..بانضمام بوت في الجروبات
𓍹𓋹𓍻ميزه ⦂ غنيلي 
𓍹𓋹𓍻ميزه ⦂ بايو
𓍹𓋹𓍻ميزه ⦂ خروج المساعد من جروبات لعدم تقطيع صوت..البوت
𓍹𓋹𓍻ميزه ⦂ اسال/اصراحه
𓍹𓋹𓍻ميزه ⦂ نكت
𓍹𓋹𓍻ميزه ⦂ ذكاء اصتناعي 
𓍹𓋹𓍻ميزه ⦂ مميزات. بيجبلك مميزات موجوده فسورس 
𓍹𓋹𓍻ميزه ⦂ رفع و تنزيل مطور 
𓍹𓋹𓍻ميزه ⦂ افلام
𓍹𓋹𓍻ميزه ⦂ مكالمات النشطه+مجموعات البوت شغال فيها
𓍹𓋹𓍻ميزه ⦂ اساله دينيه
𓍹𓋹𓍻ميزه ⦂ من في المكالمه+تعرف من فالمكالمه و عددهم
𓍹𓋹𓍻ميزه ⦂ انا وين+بتجلك جروب
𓍹𓋹𓍻ميزه ⦂ الرابط+رابط مجموعه
𓍹𓋹𓍻ميزه ⦂ فنان+اكتب اسم فنان و هتجبلك اغانيه
𓍹𓋹𓍻ميزه ⦂ اصدار+حول
⌞ ⩹━⊷⌯𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐⌝⌯⊶𓍹𓋹𓍻━⩺

""",


        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓍹𓋹𓍻⌞ ⩹━⊷⌯𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑼𝑵𝑻𝑬𝑹 𖤐⌝⚡", url=f"https://t.me/huntersource"),                        
                 ],[
                InlineKeyboardButton(
                        "close", callback_data="close"),
               ],
          ]
        ),
    )

