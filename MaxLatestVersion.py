print (""" 
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┃ ✯͜͡❂➣ PC Windows + IOS IPAD + CHOME OS + WIN10
┃ ✯͜͡❂➣ เครดิตการแก้ ( ห้ามเปลี่ยนส่วนนี้ )
┃ ✯͜͡❂➣ ไลน์ไอดี :: http://line.me/ti/p/%40jnx0914l
┃ ✯͜͡❂➣ ลิขสิทธิ์ :: http://github.com/teambotmax
┃ ✯͜͡❂➣ ประเทศ :: ไทย ( Thailand )
┃ ✯͜͡❂➣ ผู้สร้าง :: แม็กซ์ บินแหลก ( TEAM BOT MAX )
┃ ✯͜͡❂➣ เวอร์ชั่น :: 10.0.0.0
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
from MaxLatestVersion import *
from TEAM_BOT_MAX.ttypes import *
from TEAM_BOT_MAX.ttypes import IdentityProvider, LoginResultType, LoginRequest, LoginType
from TEAM_BOT_MAX.ttypes import TalkException
from TEAM_BOT_MAX.ttypes import ContentType as Type
from TEAM_BOT_MAX.ttypes import ChatRoomAnnouncementContents
from TEAM_BOT_MAX.ttypes import Location
from TEAM_BOT_MAX.ttypes import ChatRoomAnnouncement
from thrift.protocol import TCompactProtocol,TMultiplexedProtocol,TProtocol
from thrift.transport import TTransport,TSocket,THttpClient,TTransport,TZlibTransport
from thrift import transport, protocol, server
from thrift.Thrift import *
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from multiprocessing import Pool, Process
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from bs4 import BeautifulSoup
from bs4.element import Tag
import requests as uReq
from time import sleep
from gtts import gTTS
from Naked.toolshed.shell import execute_js
import ast, codecs, json, os, pytz, re, LineService, random, sys, time, urllib.parse, subprocess, threading, pyqrcode, pafy, humanize, os.path, traceback
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,youtube_dl,pafy,timeit,atexit,traceback,ffmpy,humanize
from datetime import datetime, timedelta
from subprocess import Popen, PIPE
from googletrans import Translator
from zalgo_text import zalgo
from humanfriendly import format_timespan, format_size, format_number, format_length
from threading import Thread,Event
#import requests,uvloop
from random import randint
import html5lib,shutil
import wikipedia,goslate
from youtube_dl import YoutubeDL
import requests, json
from newqr import NewQRLogin
_session = requests.session()
requests.packages.urllib3.disable_warnings()
newqr = NewQRLogin()
token, cert = newqr.loginWithQrCode("ios_ipad")
maxbots = TEAMBOTMAXv2(token)
print ('++ Auth Token : %s' % maxbots.authToken)
maxbotsMid = maxbots.profile.mid
maxbotsStart = time.time()
maxbotsProfile = maxbots.getProfile()
maxbotsPoll = OEPoll(maxbots)
botStart = time.time()
creator = ["uc14c3d87a1123df7c8ffa9d7402e59a2"]
owner = [maxbotsMid,"uc14c3d87a1123df7c8ffa9d7402e59a2"]
MAX = [maxbots]
admin = [maxbotsMid,"uc14c3d87a1123df7c8ffa9d7402e59a2","udcb20768bca5986eaa4a1c35d0b10ef9"]
Bots = [maxbotsMid]
MAXs = "uc14c3d87a1123df7c8ffa9d7402e59a2"
#maxbots.findAndAddContactsByMid(MAXs)
maxbots.sendMessage(MAXs,"เข้าสู่ระบบเรียบร้อย")
#======================================================================================================================
languageOpen = codecs.open("language.json","r","utf-8")
mentioOpen = codecs.open("tagme.json","r","utf-8")
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("setting.json","r","utf-8")
settingssOpen = codecs.open("save.json","r","utf-8")
unsendOpen = codecs.open("unsend.json","r","utf-8")
stickerOpen = codecs.open("sticker.json","r","utf-8")
stickertOpen = codecs.open("stickertemplate.json","r","utf-8")
textaddOpen = codecs.open("text.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
waitOpen = codecs.open("wait.json","r","utf-8")
answeOpen = codecs.open("autoanswer.json","r","utf-8")
premiumOpen = codecs.open("user.json","r","utf-8")
#======================================================================================================================
language = json.load(languageOpen)
tagme = json.load(mentioOpen)
read = json.load(readOpen)
settings = json.load(settingsOpen)
settingss = json.load(settingssOpen)
unsend = json.load(unsendOpen)
stickers = json.load(stickerOpen)
stickerstemplate = json.load(stickertOpen)
textsadd = json.load(textaddOpen)
images = json.load(imagesOpen)
wait = json.load(waitOpen)
autoanswer = json.load(answeOpen)
premium = json.load(premiumOpen)
#======================================================================================================================
pendings = []
protectname = []
protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
welcome = []
wellcome = []
offbot = []
temp_flood = {}
msg_dict = {}
msg_dict1 = {}  
unsendchat = {}
msg_image={}
msg_video={}
msg_sticker={}
msg_waktu={}
ssnd = []
stickerss = []
zxcv = []

chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}

rynk = {
    "myProfile": {
        "displayName": "",
    }
}

RfuCctv={
    "Point1":{},
    "Point2":{},
    "Point3":{}
}
kasar = "kontol","memek","kntl","ajg","anjing","asw","anju","gblk","goblok","bgsd","bangsad","bangsat"

wait = {
    "cekpc": "Pm ku gosong semm??",
}

read={
    "readPoint":{},
    "readMember":{},
    "ROM":{}
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

def restartBot():
    print('####==== PROGRAM RESTARTED ====####')
    python = sys.executable
    os.execl(python, python, *sys.argv)

def autoRestart():
    if settings["autoRestart"] == True:
        if time.time() - botStart > int(settings["timeRestart"]):
            backupData()
            restartBot()
         
def sendTemplateMax(to, data):
    xyzz = LiffContext(chat=LiffChatContext(to))
    view = LiffViewRequest('1647207293-rNJ7MlJm', context = xyzz)
    token = maxbots.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Line/8.14.0',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return _session.post(url=url, data=json.dumps(data), headers=headers)

def bcTemplate(gr, data):
    teambotmax1 = LiffChatContext(gr)
    teambotmax2 = LiffContext(chat=teambotmax1)
    teambotmax3 = LiffViewRequest("1602687308-GXq4Vvk9", teambotmax2)
    token = maxbots.liff.issueLiffView(teambotmax3)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def logError(text):
    maxbots.log("ERROR 404 !\n" + str(text))
    tz = pytz.timezone("Asia/Makassar")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("errorLog.txt","a") as error:
        error.write("\n{} {}".format(str(time), text))

def waktu(self,secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def sendMentionFooter(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@MAX"
        slen = str(len(text))
        elen = str(len(text) + len(mention))
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        nama = "{}".format(maxbots.getContact(maxbotsMid).displayName)
        img = "http://dl.profile.line-cdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus)
        ticket = "https://line.me/ti/p/{}".format(maxbots.getUserTicket().id)
        maxbots.sendMessage(to, text, {'AGENT_LINK': ticket, 'AGENT_ICON': img, 'AGENT_NAME': nama, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        maxbots.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def timeChange(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d เดือน" % (months)
    if weeks != 0: text += " %02d อาทิตย์" % (weeks)
    if days != 0: text += " %02d วัน" % (days)
    if hours !=  0: text +=  " %02d ชั่วโมง" % (hours)
    if mins != 0: text += " %02d นาที" % (mins)
    if secs != 0: text += " %02d วินาที" % (secs)
    if text[0] == " ":
        text = text[1:]
    return text

def searchRecentMessages(to,id):
    for a in maxbots.talk.getRecentMessagesV2(to,101):
        if a.id == id:
            return a
    return None
    
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))

def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
    
def delete_log1():
    ndt = datetime.now()
    for data in msg_dict1:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict1[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict1[msg_id]

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.01)        
            page = page[end_content:]
    return items

def maxSticker(to, image, text):
    data = {"messages":[{"type":"template","altText":maxbotsProfile.displayName+" ส่งสติกเกอร์","template":{"type":"image_carousel","columns":[{"imageUrl":image,"action":{"type":"uri","uri":text}}]}}]}
    sendTemplateMax(to, data)

def maxTemplateZ(to,c):
 data={"type":"flex","altText":"ƬΣΛM BӨƬ MΛX","contents":c}
 sendTemplateMax(to,data)

def teambotmaxText(to, textnya):
        data = {
            "messages": [
                {
                "type": 'text',
                "text": textnya,
                "sentBy": {
                    "label": "ƬΣΛM BӨƬ MΛX",
                    "iconUrl":  'https://os.line.naver.jp/os/p/uc14c3d87a1123df7c8ffa9d7402e59a2', 
                    "linkUrl": "line://oaMessage/@jnx0914l/?สวัสดี%20❤️"
                  
                }
            }
            ]
        }
        sendTemplateMax(to, data)

def sendTextMax(to, text):
    warna1 = ("#0008FF","#000000","#058700","#DE00D4","#05092A","#310206","#5300FC")
    warnanya1 = random.choice(warna1)
    data = {
            "type": "flex",
            "altText": "ƬΣΛM BӨƬ MΛX",
            "contents": {
                                 "styles": {
                                   "body": {
                                     "backgroundColor": warnanya1
                                   },
                                   "footer": {
                                     "backgroundColor": "#FF0000"
                                   }
                                 },
                                 "type": "bubble",
#                                 "size": "giga",
                                 "body": {
                                   "contents": [
                                     {
                                       "contents": [
                                         {
                                           "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus),
                                           "type": "image",
                                           "size": "full"
                                         }
                                       ],
                                       "type": "box",
                                       "spacing": "md",
                                       "layout": "horizontal"
                                     },
                                     {
                                       "type": "separator",
                                       "color": "#FF0000"
                                     },
                                     {
                                       "contents": [
                                         {
                                           "contents": [
                                             {
                                               "text": text,
                                               "size": "xs",
                                               "margin": "none",
                                               "color": "#FFFFFF",
                                               "wrap": True,
                                               "weight": "regular",
                                               "type": "text"
                                             }
                                           ],
                                           "type": "box",
                                           "layout": "baseline"
                                         }
                                       ],
                                       "type": "box",
                                       "layout": "vertical"
                                     }
                                   ],
                                   "type": "box",
                                   "spacing": "md",
                                   "layout": "vertical"
                                 },
                                 "footer": {
                                   "contents": [
                                     {
                                       "contents": [
                                         {
                                           "contents": [
                                             {
                                               "text": "✦ กดเพิ่มเพื่อนเพื่อติดต่อสอบถามแอดมิน ✦",
                                               "size": "md",
                                               "weight": "bold",
                                               "action": {
                                                 "uri": "http://line.me/ti/p/%40jnx0914l",
                                                 "type": "uri",
                                                 "label": "Audio"
                                                },
                                               "margin": "sm",
                                               "align": "center",
                                               "color": "#000000",
                                               "weight": "bold",
                                               "type": "text"
                                             }
                                           ],
                                           "type": "box",
                                           "layout": "baseline"
                                         }
                                       ],
                                       "type": "box",
                                       "layout": "horizontal"
                                     }
                                   ],
                                   "type": "box",
                                  "layout": "vertical"
                                 }
                               }
                               }
    maxbots.postTemplate(to, data)

def sendTextMax1(to, text):
    data = {
            "type": "flex",
            "altText": "ƬΣΛM BӨƬ MΛX",
            "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000",
      "separator":True,
      "separatorColor":"#FF0000"
    },
    "footer": {
      "backgroundColor": "#000000",
      "separator":True,
      "separatorColor":"#FF0000"
    }
  },
  "type": "bubble",
#  "size": "giga",
  "body": {
    "contents": [
      {
        "contents": [          
          {
            "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus),
            "type": "image",
            "size": "full",
            "action": {
              "uri": "http://line.me/ti/p/%40jnx0914l",
              "type": "uri"
            },
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FF0000"
       },
       {
        "contents": [
          {
            "contents": [
              {
                "text": text,
                "size": "sm",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "flex": 2,
          "contents": [{
              "type": "button",
              "style": "secondary",
              "color": "#FF0000",
              "height": "md",
              "action": {
                  "type": "uri",
                  "label": "✦ กดที่นี่เพื่อติดต่อสอบถามแอดมิน ✦",
                  "uri": "http://line.me/ti/p/%40jnx0914l"
              }
          }]
      }]
  }
}
}
    maxbots.postTemplate(to, data)

def sendTextMax2(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} send Message".format(maxbots.getProfile().displayName),
                                "contents": {
  "type": "bubble",
  "size": "giga",
  "direction": "ltr",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#FFFFFF",
            "align": "center"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#000000"
    },
    "header": {
      "backgroundColor": "#FF0000"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "1:1",
    "aspectMode": "cover",
    "url": "https://sv1.picz.in.th/images/2019/08/09/Zd7F7y.jpg",
    "size": "full",
    "margin": "xl"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#006400",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ＡＤＭＩＮ",
                  "uri": "http://line.me/ti/p/~max.self"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#800000",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ＣＲＥＡＴＯＲ",
                  "uri": "http://line.me/ti/p/%40jnx0914l"
              }
          }]
      }]
  }
}
}
    maxbots.postTemplate(to, data)

def sendTextMax3(to, text):
    warna1 = ("#0008FF","#FF0000","#058700","#DE00D4","#05092A","#310206","#5300FC")
    warnanya1 = random.choice(warna1)
    data = {
            "type": "flex",
            "altText": "ƬΣΛM BӨƬ MΛX",
            "contents": {
  "styles": {
    "body": {
      "backgroundColor": warnanya1
    }
  },
  "type": "bubble",
  "size": "giga",
  "direction": "ltr",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": text,
                "size": "md",
                "margin": "none",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  }
}
}
    maxbots.postTemplate(to, data)

def sendTextMax4(to, text):
    data = {
            "type": "flex",
            "altText": "ƬΣΛM BӨƬ MΛX",
            "contents": {
  "type": "bubble",
  "size": "giga",
  "direction": "ltr",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "sm",
            "weight": "bold",
            "wrap": True,
            "color": "#F0F8FF"
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ＳＥＬＦＢＯＴＢＹＭＡＸ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "🎶SOUNDCLOUD🎶",
        "size": "md",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "align": "center"
      }
    ]
  }
}
}
    maxbots.postTemplate(to, data)

def sendTextMax5(to, text):
    data = {
                "type": "template",
                "altText": "ƬΣΛM BӨƬ MΛX",
                "contents": {
                    "type": "bubble",
                    "size": "giga",
                    "direction": "ltr",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                               "text": text,
                               "size": "sm",
                               "margin": "none",
                               "color": "#8B008B",
                               "wrap": True,
                               "weight": "regular",
                               "type": "text"
                            }
                        ]
                    }
                }
            }
    maxbots.postTemplate(to, data)

def sendTextMax6(to, text):
    data = {
            "type": "flex",
            "altText": "ƬΣΛM BӨƬ MΛX",
            "contents": {
                                 "type": "bubble",
                                 "size": "giga",
                                 "direction": "ltr",
                                 "styles":{
                                 "header":{
                                 "backgroundColor":"#000000"
                                },
                                "body":{
                                 "backgroundColor":"#000000",
                                 "separator":True,
                                 "separatorColor":"#FF0500"
                                },
                                "footer":{
                                 "backgroundColor":"#000000",
                                 "separator":True,
                                 "separatorColor":"#FF0500"
                                }
                              },
                              "header":{
                                "type":"box",
                                "layout":"horizontal",
                                "contents":[
                                  {
                                    "type":"text",
                                    "align":"center",
                                    "text":"ＳＥＬＦＢＯＴＢＹＭＡＸ",
                                    "weight":"bold",
                                    "color":"#FF0000",
                                    "size":"lg",
                                    "action":{
                                      "type": "uri",
                                      "uri": "http://line.me/ti/p/%40jnx0914l"
                                      }
                                  }
                                ] 
                              },
                              "body":{
                                "type":"box",
                                "layout":"vertical",
                                "contents":[
                                  {
                                    "type": "box",
                                    "layout":"vertical",
                                    "margin":"lg",
                                    "spacing":"sm",
                                    "contents":[
                                      {
                                        "type":"box",
                                        "layout":"baseline",
                                        "spacing":"sm",
                                        "contents":[
                                          {
                                            "text": text,
                                            "size": "sm",
                                            "margin": "none",
                                            "color":"#FF9B0A",
                                            "wrap": True,
                                            "weight": "regular",
                                            "type": "text"
                                          }
                                        ]
                                      }
                                    ]
                                  }
                                ]
                              },
                              "footer":{
                                "type":"box",
                                "layout":"vertical",
                                "spacing":"sm",
                                "contents":[
                                  {
                                    "type":"text",
                                    "align":"center",
                                    "text":"ＣＲＥＡＴＯＲ",
                                    "color":"#FF0000",
                                    "wrap":True,
                                    "size": "xl",
                                  },
                                  {
                                    "type":"spacer",
                                    "size":"sm"
                                   }
                                ],
                                "flex": 0,
                              }
                          }
                      }
    maxbots.postTemplate(to, data)

def sendTextMax7(to, text):
    data={
            "type": "flex",
            "altText": "ƬΣΛM BӨƬ MΛX",
            "contents": {
            "type": "carousel",
            "contents": [
            {
            "type": "bubble",
            "size": "nano",
            "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
            "type": "text",
            "text": "TEAM BOT MAX",
            "color": "#ffffff",
            "align": "center",
            "size": "xxs",
            "gravity": "center"
            },
            {
            "type": "text",
            "text": "FLEX 2019",
            "color": "#ffffff",
            "align": "center",
            "size": "xxs",
            "gravity": "center",
            "margin": "lg"
            },
            {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
            "type": "filler",
            "flex": 0
            }
            ],
            "width": "100%",
            "backgroundColor": "#000000",
            "height": "6px",
            "margin": "none"
            }
            ],
            "backgroundColor": "#000000",
            "height": "6px",
            "margin": "none"
            }
            ],
            "backgroundColor": "#000000",
            "paddingTop": "19px",
            "paddingAll": "12px",
            "paddingBottom": "16px"
            },
            "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
            "type": "text",
            "text": text,
            "color": "#8C8C8C",
            "align": "center",
            "wrap": True,
            "size": "xxs"
            }
            ],
            "flex": 1,
            "spacing": "none"
            },
            {
            "type": "image",
            "url": "https://www.img.live/images/2019/10/22/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg",
            "margin": "none"
            }
            ],
            "spacing": "md",
            "paddingAll": "12px"
            },
            "styles": {
            "footer": {
            "separator": True,
            }
            }
            }
            ]
            }
            }
    maxbots.postTemplate(to,data)

def sendTextMax8(to, text):
    teambotmaxZ = {
            "type": "flex",
            "altText": "ƬΣΛM BӨƬ MΛX",
            "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "giga",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "1:1",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": text,
                    "size": "lg",
                    "color": "#ffffff",
                    "weight": "bold",
                    "align": "center",
                    "gravity": "center",
                    "wrap": True
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "icon",
                        "url": "https://www.img.live/images/2019/10/22/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                      },
                      {
                        "type": "text",
                        "text": "กดเพื่อเพิ่มเพื่อนแอดมิน",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px",
                        "action": {
                           "type": "uri",
                           "uri": "http://line.me/ti/p/%40jnx0914l"
                        }
                      },
                      {
                        "type": "icon",
                        "url": "https://www.img.live/images/2019/10/22/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "2px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#000000",
                "margin": "xxl",
                "height": "40px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#03303Acc",
            "paddingAll": "20px",
            "paddingTop": "18px",
            "borderColor": "#000000",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "NEW",
                "color": "#ffffff",
                "align": "center",
                "size": "xs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "18px",
            "backgroundColor": "#ff334b",
            "offsetStart": "18px",
            "height": "25px",
            "width": "53px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "2px",
        "borderColor": "#000000"
      }
    }
  ]
}
}
    maxbots.postTemplate(to, teambotmaxZ)

def sendStickerTemplate(to, text):
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
    to = op.param1
    data = {
                          "type": "template",
                          "altText": "{} sent a sticker".format(maxbots.getProfile().displayName),
                          "template": {
                             "type": "image_carousel",
                             "columns": [
                              {
                                  "imageUrl": text,
                                  "size": "full", 
                                  "action": {
                                      "type": "uri",
                                      "uri": "http://line.me/ti/p/%40jnx0914l"
           }                                                
 }
]
                          }
                      }
    maxbots.postTemplate(to, data)

def sendTextMax9(to, text):
    teambotmaxZ = {
            "type": "flex",
            "altText": "ƬΣΛM BӨƬ MΛX",
            "contents": {
  "type": "bubble",
  "size": "giga",
  "body": {
    "type": "box",
    "layout": "baseline",
    "contents": [
      {
        "type": "icon",
        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
      },
      {
        "type": "text",
        "text": text,
        "size": "sm",
        "align": "center",
        "color": "#000000",
        "wrap": True
      },
      {
        "type": "icon",
        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
      }
    ],
    "backgroundColor": "#ffea12",
    "borderWidth": "3px",
    "borderColor": "#ff0022"
  }
}
}
    maxbots.postTemplate(to, teambotmaxZ)

def sendTextMax10(to, text):
    warna1 = ("#0008FF","#000000","#058700","#DE00D4","#05092A","#310206","#5300FC")
    warnanya1 = random.choice(warna1)
    maxbots.reissueUserTicket()
    teambotmaxZ = {
            "type": "flex",
            "altText": "ƬΣΛM BӨƬ MΛX",
            "contents": {
  "type": "bubble",
#  "size": "giga",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "1:1",
            "gravity": "center",
            "flex": 1
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "NEW",
                "size": "xs",
                "color": "#ffffff",
                "align": "center",
                "gravity": "center"
              }
            ],
            "backgroundColor": "#EC3D44",
            "paddingAll": "2px",
            "paddingStart": "4px",
            "paddingEnd": "4px",
            "flex": 0,
            "position": "absolute",
            "offsetStart": "18px",
            "offsetTop": "18px",
            "cornerRadius": "100px",
            "width": "48px",
            "height": "25px"
          }
        ]
      }
    ],
    "paddingAll": "0px"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "contents": [],
                "size": "xl",
                "wrap": True,
                "text": "✦ รายการคำสั่งบอท ✦",
                "color": "#ffffff",
                "weight": "bold",
                "align": "center"
              },
              {
                "type": "text",
                "text": "「 พิมพ์ตามข้อความด้านล่าง 」",
                "color": "#EBFF00",
                "size": "sm",
                "wrap": True,
                "align": "center",
                "weight": "bold"
              }
            ],
            "spacing": "sm"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "contents": [],
                "size": "md",
                "wrap": True,
                "margin": "lg",
                "text": text,
                "color": "#ffffff"
              }
            ],
            "paddingAll": "13px",
            "margin": "xl"
          }
        ]
      }
    ],
    "paddingAll": "20px",
    "backgroundColor": warnanya1
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "✦ กดที่นี่เพิ่อติดต่อแอดมิน ✦",
            "color": "#000000",
            "size": "md",
            "weight": "bold",
            "align": "center",
            "wrap": True
          }
        ],
        "spacing": "sm"
      }
    ],
    "backgroundColor": "#ff0e00",
    "action": {
      "type": "uri",
      "label": "action",
      "uri": "http://line.me/ti/p/%40jnx0914l"
    }
  },
  "styles": {
    "body": {
      "separatorColor": "#000000",
      "separator": True
    },
    "footer": {
      "separatorColor": "#000000",
      "separator": True
    }
  }
}
}
    maxbots.postTemplate(to, teambotmaxZ)

def sendTextMax11(to, text):
    warna1 = ("#ffb800","#ff0009","#ff0099","#ffffff")
    warnanya1 = random.choice(warna1)
    teambotmaxZ = {
            "type": "flex",
            "altText": "ƬΣΛM BӨƬ MΛX",
            "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus),
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "cornerRadius": "100px",
            "width": "75px",
            "height": "75px",
            "borderWidth": "2px",
            "borderColor": "#000000"
          }
        ],
        "spacing": "xl",
        "paddingAll": "20px",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "http://line.me/ti/p/%40jnx0914l"
        }
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text",
        "text": "TEAM BOT MAX",
        "weight": "bold",
        "size": "lg",
        "margin": "md",
        "color": "#000033"
      },
      {
        "type": "text",
        "text": "Self bot protect 3D bot template",
        "size": "xs",
        "color": "#000000",
        "wrap": True
      },
      {
        "type": "separator",
        "margin": "xxl",
        "color": "#000000"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "xxl",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": text,
                "size": "md",
                "color": "#000000",
                "wrap": True,
                "weight": "regular"
              }
            ]
          }
        ]
      },
      {
        "type": "separator",
        "margin": "xxl",
        "color": "#000000"
      }
    ],
    "cornerRadius": "17px",
    "borderColor": "#000000",
    "borderWidth": "3px",
    "backgroundColor": warnanya1
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}
}
    maxbots.postTemplate(to, teambotmaxZ)

def teambotmaxLike(to, sender):
    timeNow = time.time()
    runtime = timeNow - botStart
    runtime = format_timespan(runtime)
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    teambotmax1 = maxbots.getContact(maxbotsMid)
    teambotmax2 = maxbots.getProfileCoverURL(maxbotsMid)
    teambotmaxZ = {
        "messages": [
            {
                "type": "flex",
                "altText": "ƬΣΛM BӨƬ MΛX",
                "contents": {
  "type": "bubble",
  "size": "giga",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "image",
            "url": teambotmax2,
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "20:13",
            "gravity": "center",
            "flex": 1
          }
        ],
        "borderWidth": "2px",
        "borderColor": "#000000"
      },
      {
        "type": "separator",
        "color": "#ffffff"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus),
                "aspectMode": "cover",
                "size": "full",
                "action": {
                  "uri": "http://line.me/ti/p/%40jnx0914l",
                  "type": "uri",
                }
              }
            ],
            "cornerRadius": "100px",
            "width": "72px",
            "height": "72px",
            "borderWidth": "2px",
            "borderColor": "#000000"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "icon",
                    "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                  },
                  {
                    "type": "text",
                    "text": "✦ ขื่อ :",
                    "weight": "bold",
                    "margin": "sm",
                    "flex": 0
                  },
                  {
                    "type": "text",
                    "text": "{}".format(teambotmax1.displayName),
                    "size": "md",
                    "align": "end",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "icon",
                    "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                  },
                  {
                    "type": "text",
                    "text": "✦ สถานะ :",
                    "weight": "bold",
                    "margin": "sm",
                    "flex": 0
                  },
                  {
                    "type": "text",
                    "text": "ออโต้ไลค์อัตโนมัติ",
                    "size": "md",
                    "align": "end",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "icon",
                    "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                  },
                  {
                    "type": "text",
                    "text": "✦ วันที่ :",
                    "weight": "bold",
                    "margin": "sm",
                    "flex": 0
                  },
                  {
                    "type": "text",
                    "text": "" + datetime.strftime(timeNow,'%Y-%m-%d'),
                    "size": "md",
                    "align": "end",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "icon",
                    "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                  },
                  {
                    "type": "text",
                    "text": "✦ เวลา :",
                    "weight": "bold",
                    "margin": "sm",
                    "flex": 0
                  },
                  {
                    "type": "text",
                    "text": "" + datetime.strftime(timeNow,'%H:%M:%S') + " นาที",
                    "size": "md",
                    "align": "end",
                    "weight": "regular"
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "xl",
        "paddingAll": "20px",
        "borderColor": "#000000",
        "borderWidth": "2px",
        "backgroundColor": "#FFAC00"
      }
    ],
    "paddingAll": "0px"
  }
}
}
]
}
    maxbots.postTemplate(to, teambotmaxZ)

def sendMessageWithFooter(to, text, name, url, iconlink):
        contentMetadata = {
            'AGENT_NAME': name,
            'AGENT_LINK': url,
            'AGENT_ICON': iconlink
        }
        return maxbots.sendMessage(to, text, contentMetadata, 0)
    
def sendMessageWithFooter(to, text):
 maxbots.reissueUserTicket()
 dap = maxbots.getProfile()
 ticket = "http://line.me/ti/p/"+maxbots.getUserTicket().id
 pict = "http://dl.profile.line-cdn.net/"+maxbots.pictureStatus
 name = dap.displayName
 dapi = {"AGENT_ICON": pict,
     "AGENT_NAME": name,
     "AGENT_LINK": ticket
 }
 maxbots.sendMessage(to, text, contentMetadata=maxbots)
 
 def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def convertYoutubeMp4(url):
    import pafy
    video = pafy.new(url, basic=False)
    result = video.streams[-1]
    return result.url

def youtubeMp4(to, link):
    subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
    try:
        maxbots.sendVideo(to, "TeamAnuBot.mp4")
        time.sleep(2)
        os.remove('TeamAnuBot.mp4')
    except Exception as e:
        teambotmaxText(to, ' 「 ERROR 」\nMungkin Link Nya Salah GaN~', contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+maxbots.getContact(maxbotsMid).pictureStatus, 'AGENT_NAME': '「 ERROR 」', 'AGENT_LINK': 'https://line.me/ti/p/~teambotmax'})

def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@MAX\n "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        maxbots.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        maxbots.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMentionWithFooter(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@MAX"
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    maxbots.sendMessage(to, textx, {'AGENT_NAME':'Dont Click!', 'AGENT_LINK': 'http://line.me/ti/p/~teambotmax', 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + maxbots.getProfile().picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = maxbots.getGroup(to)
            mention = "@MAX\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += "welcome"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(maxbots.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
      #  teambotmaxText(to, textx)
    except Exception as error:
        teambotmaxText(to)
        
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = maxbots.getGroup(to)
            mention = "@MAX\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += "babay"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(maxbots.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        #teambotmaxText(to, textx)
    except Exception as error:
        teambotmaxText(to)

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@MAX\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(maxbots.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        teambotmaxText(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        teambotmaxText(to, "[ INFO ] Error :\n" + str(error))

def rynSplitText(text,lp=''):
    separate = text.split(" ")
    if lp == '':
        adalah = text.replace(separate[0]+" ","")
    elif lp == 's':
        adalah = text.replace(separate[0]+" "+separate[1]+" ","")
    else:
        adalah = text.replace(separate[0]+" "+separate[1]+" "+separate[2]+" ","")
    return adalah

def Pertambahan(a,b):
    jum = a+b
    print(a, "+",b," = ",jum)
def Pengurangan(a,b):
    jum = a-b
    print(a, "-",b," = ",jum)
def Perkalian(a,b):
    jum = a*b
    print(a, "x",b," = ",jum)
def Pembagian(a,b):
    jum = a/b
    print(a, ":",b," = ",jum)
def Perpangkatan(a,b):
    jum = a**b
    print(a,"Pangkat ",b," = ",jum )

def sendSticker(to, version, packageId, stickerId):
    contentMetadata = {
        'STKVER': version,
        'STKPKGID': packageId,
        'STKID': stickerId
    }
    maxbots.sendMessage(to, '', contentMetadata, 7)

def urlEncode(url):
  import base64
  return base64.b64encode(url.encode()).decode('utf-8')

def urlDecode(url):
  import base64
  return base64.b64decode(url.encode()).decode('utf-8')

def removeCmdv(text, key=""):
    setKey = key
    text_ = text[len(setKey):]
    sep = text_.split(" ")
    return text_.replace(sep[0] + " ", "")

def removeCmd(teambotmax, text):
    key = settings["keyCommand"]
    if settings["setKey"] == False: key = ''
    rmv = len(key + teambotmax) + 1
    return text[rmv:]

def multiCommand(teambotmax, list_teambotmax=[]):
    if True in [teambotmax.startswith(c) for c in list_teambotmax]:
        return True
    else:
        return False

def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            teambotmax = pesan.replace(settings["keyCommand"],"")
        else:
            teambotmax = "Undefined command"
    else:
        teambotmax = text.lower()
    return teambotmax
    
def commander(text):
    pesan = text.lower()
    if settings["setKey"] == False:
        if pesan.startswith(settings["keyCommand"]):
            teambotmax = pesan.replace(settings["keyCommand"],"")
        else:
            teambotmax = "Undefined command"
    else:
        teambotmax = text.lower()
    return teambotmax

def backupData():
    try:
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = settings
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = settingss
        f = codecs.open('save.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = unsend
        f = codecs.open('unsend.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        bekep = tagme
        f = codecs.open('tagme.json','w','utf-8')
        json.dump(bekep, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False

def generateLink(to, ryn, rynurl=None):
    path = maxbots.downloadFileURL('https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+ryn, 'path','ryngenerate.jpg')
    data = {'register':'submit'}
    files = {"file": open(path,'rb')}
    url = 'https://fahminogameno.life/uploadimage/action.php'
    r = requests.post(url, data=data, files=files)
    teambotmaxText(to, '%s\n%s' % (r.status_code,r.text))
    teambotmaxText(to, '{}{}'.format(rynurl,urlEncode('https://fahminogameno.life/uploadimage/images/ryngenerate.png')))

def uploadFile(ryn):
    url = 'https://fahminogameno.life/uploadimage/action.php'
    path = maxbots.downloadFileURL('https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+ryn, 'path','ryngenerate.png')
    data = {'register':'submit'}
    files = {"file": open(path,'rb')}
    r = requests.post(url, data=data, files=files)
    if r.status_code == 200:
        return path

def cloneProfile(mid):
    contact = maxbots.getContact(mid)
    if contact.videoProfile == None:
        maxbots.cloneContactProfile(mid)
    else:
        profile = maxbots.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        maxbots.updateProfile(profile)
        pict = maxbots.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = maxbots.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = maxbots.getProfileDetail(mid)['result']['objectId']
    maxbots.updateProfileCoverById(coverId)

def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = maxbots.genOBSParams({'oid': maxbotsMid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = maxbots.server.postContent('{}/talk/vp/upload.nhn'.format(str(maxbots.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        maxbots.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
        os.remove("FadhilvanHalen.mp4")

def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        sujar = "✯͜͡❂ ƬΣΛM BӨƬ MΛX"
                        teambotmaxText(tmp, sujar)        
                    except Exception as error:
                        logError(error)

def delExpirev2():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        sujar = "「Assalamualaikum」"
                        teambotmaxText(tmp, sujar)        
                    except Exception as error:
                        logError(error)
#=====================================================================
def teambotmax(op):
    try:
        timeis = time.localtime()
        a = time.strftime('%H:%M:%S', timeis)
        if op.type == 0:
            return
        print ('++ Operation : ( %i ) %s' % (op.type, OpType._VALUES_TO_NAMES[op.type].replace('_', ' ')))
        if op.type == 5:
            if settings["autoAdd"] == True:
                maxbots.findAndAddContactsByMid(op.param1)
            maxbots.sendMention(op.param1, settings["autoAddMessage"], [op.param1])
            print("AUTO ADD CONTACT")
#=====================================================================
        if op.type == 5:
            if settings["autoBlock"] == True:
                maxbots.blockContact(op.param1)
            maxbots.sendMention(MAXs, settings["autoBlockMessage"], [op.param1])
            maxbots.sendMessage(MAXs, None, contentMetadata={'mid': op.param1}, contentType=13)           
            print("AUTO BLOCK CONTACT")
#=====================================================================
        if op.type == 13:
           teambotmaxZ = maxbots.getGroup(op.param1)
           if settings["maxReject"] == False:
              if settings["memberCancel"]["on"] == True:
                  if len(teambotmaxZ.members) <= settings["memberCancel"]["members"]:
                      time.sleep(random.uniform(0.75,1.5))
                      maxbots.rejectGroupInvitation(op.param1)
                      print("✦ เทพแม็กแดกห้องรัน ✦")
                  else:
                      pass
#=====================================================================
        if op.type == 13:
            if maxbotsMid in op.param3:
                if settings["autoLeave"] == True:
                    maxbots.acceptGroupInvitation(op.param1)
                    group = maxbots.getGroup(op.param1)
                    maxbots.updateGroup(group)
                    maxbots.leaveGroup(op.param1)
                    time.sleep(2)
#=====================================================================        			
        if op.type == 11:
            if op.param1 in protectqr:
                if op.param2 in Bots:
                    pass
                else:
                    settings["blackList"][op.param2] = True
                    print ("PROTECT BERTINDAK DI GRUP "+maxbots.getGroup(op.param1).name)
                    try:
                        M = maxbots.getGroup(op.param1)
                        M.preventedJoinByTicket = True
                        maxbots.updateGroup(M)
                        maxbots.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        M = maxbots.getGroup(op.param1)
                        M.preventedJoinByTicket = True
                        maxbots.updateGroup(M)
                        maxbots.kickoutFromGroup(op.param1,[op.param2])
#=====================================================================
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in protectname:
                    try:
                        settings["blackList"][op.param2] = True
                        G = maxbots.getGroup(op.param1)
                    except:
                        try:
                            G = maxbots.getGroup(op.param1)
                        except:
                            try:
                                G = maxbots.getGroup(op.param1)
                            except:
                                pass
                    G.name = settings['lock_name'][op.param1]
                    try:
                        maxbots.updateGroup(G)
                    except:
                        try:
                            maxbots.updateGroup(G)
                        except:
                            try:
                                maxbots.updateGroup(G)
                            except:
                                pass
                    if op.param2 in Bots:
                        pass
                    elif op.param2 not in Bots:
                        pass
                    else:
                        try:
                            maxbots.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                maxbots.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass
#=====================================================================
        if op.type == 13:
          if op.param2 and op.param3 in settings["blackList"]:
            if op.param2 not in Bots and op.param2 not in admin:
                maxbots.cancelGroupInvitation(op.param1,[op.param3])
                maxbots.kickoutFromGroup(op.param1,[op.param2])
                maxbots.kickoutFromGroup(op.param1,[op.param3])
                G = maxbots.getGroup(op.param1)
                G.preventedJoinByTicket = True
                maxbots.updateGroup(G)
                maxbots.sendMessage(op.param1, "✯͜͡❂ 13 ผู้ใช้อยู่ในบัญชีดำ โปรดล้างบัญชีดำก่อน")
#=====================================================================
        if op.type == 13:
            if maxbotsMid in op.param3:
                G = maxbots.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["memberCancel"]["on"] == True:
                        if len(G.members) <= settings["memberCancel"]["members"]:
                            maxbots.acceptGroupInvitation(op.param1)
                            time.sleep(random.uniform(0.75,1.5))
                        else:
                            maxbots.leaveGroup(op.param1)
                    else:
                        maxbots.acceptGroupInvitation(op.param1)
                        time.sleep(1)
                elif settings["memberCancel"]["on"] == True:
                    if len(G.members) <= settings["memberCancel"]["members"]:
                        maxbots.acceptGroupInvitation(op.param1)
                        time.sleep(random.uniform(0.75,1.5))
                        maxbots.leaveGroup(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blackList"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    maxbots.acceptGroupInvitation(op.param1, matched_list)
                    time.sleep(random.uniform(0.75,1.5))
                    maxbots.leaveGroup(op.param1, matched_list)
                    print ("LEAVE GROUP")
#=====================================================================
        if op.type == 13:
            if op.param2 in Bots:
            	pass
            else:
              try:
                 if op.param1 in protectinvite:
                     settings["blackList"][op.param2] = True
                     G = maxbots.getGroup(op.param1)
                     maxbots.cancelGroupInvitation(op.param1,[op.param3])
                     maxbots.kickoutFromGroup(op.param1,[op.param2])
                 else:
                     pass
              except:
                try:
                    G = maxbots.getGroup(op.param1)
                    maxbots.cancelGroupInvitation(op.param1,[op.param3])
                    maxbots.kickoutFromGroup(op.param1,[op.param2])
                    settings["blackList"][op.param2] = True
                except:
                    try:
                        G = maxbots.getGroup(op.param1)
                        maxbots.cancelGroupInvitation(op.param1,[op.param3])
                        maxbots.kickoutFromGroup(op.param1,[op.param2])
                        settings["blackList"][op.param2] = True
                    except:
                        pass
#=====================================================================   
        if op.type == 17:
          if op.param2 not in Bots and op.param2 not in admin:
            if op.param2 in settings["blackList"]:
                maxbots.kickoutFromGroup(op.param1,[op.param2])
                G = maxbots.getGroup(op.param1)
                G.preventedJoinByTicket = True
                maxbots.updateGroup(G)
                settings["blackList"][op.param2] = True
                maxbots.sendMessage(op.param1, "✯͜͡❂ 17 ผู้ใช้อยู่ในบัญชีดำ โปรดล้างบัญชีดำก่อน")
#=====================================================================
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in admin:
                    settings["blackList"][op.param2] = True
                    try:
                        if op.param3 not in settings["blackList"]:
                        	maxbots.kickoutFromGroup(op.param1,[op.param2])
                    except:                        
                    	pass
                return
#=====================================================================
        if op.type == 17 and settings["sapa"]==True:
            maxbots.acceptGroupInvitation(op.param1)
            contact = maxbots.getContact(op.param2)
            teambotmaxZ = {
                "type": "template",
                "altText": "{} มีคนเข้ากลุ่ม".format(str(maxbots.getContact(maxbotsMid).displayName)),
                "baseSize": {
                    "height": 1040,
                    "width": 1040
                },
                "template": {
                    "type": "image_carousel",
                    "columns": [{
                        "imageUrl": "https://obs.line-scdn.net/{}".format(maxbots.getContact(op.param2).pictureStatus),
                        "action": {
                            "type": "uri",
                            "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                            "area": {
                                "x": 520,
                                "y": 0,
                                "width": 520,
                                "height": 1040
                            }
                        }
                    }]
                }
            }
            maxbots.sendFlex(op.param1,teambotmaxZ)
            msgSticker = settings["messageSticker"]["listSticker"]["welcomeSticker"]
            if msgSticker != None:
                sid = msgSticker["STKID"]
                spkg = msgSticker["STKPKGID"]
                sver = msgSticker["STKVER"]
                sendSticker(op.param1, sver, spkg, sid)
#=====================================================================
        if op.type == 15 and settings["sapa"]==True or op.type == 19 and settings["sapa"]==True:
            maxbots.acceptGroupInvitation(op.param1)
            contact = maxbots.getContact(op.param2)
            teambotmaxZ = {
                "type": "template",
                "altText": "{} มีคนออกกลุ่ม".format(str(maxbots.getContact(maxbotsMid).displayName)),
                "baseSize": {
                    "height": 1040,
                    "width": 1040
                },
                "template": {
                    "type": "image_carousel",
                    "columns": [{
                        "imageUrl": "https://obs.line-scdn.net/{}".format(maxbots.getContact(op.param2).pictureStatus),
                        "action": {
                            "type": "uri",
                            "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                            "area": {
                                "x": 520,
                                "y": 0,
                                "width": 520,
                                "height": 1040
                            }
                        }
                    }]
                }
            }
            maxbots.sendFlex(op.param1,teambotmaxZ)
            msgSticker = settings["messageSticker"]["listSticker"]["leaveSticker"]
            if msgSticker != None:
                sid = msgSticker["STKID"]
                spkg = msgSticker["STKPKGID"]
                sver = msgSticker["STKVER"]
                sendSticker(op.param1, sver, spkg, sid)
#=====================================================================
        if op.type == 15 and settings["newWelcome"]==True:
            teambotmax1 = maxbots.getContact(op.param2)
            teambotmax2 = maxbots.getContact(op.param2)                   
            teambotmax3 = maxbots.getProfileCoverURL(op.param2)
            teambotmaxZ = {
                    "type": "flex",
                    "altText": "ƬΣΛM BӨƬ MΛX",
                    "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(op.param2).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top",
            "action": {
              "uri": "http://line.me/ti/p/%40jnx0914l",
              "type": "uri",
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "✦ ข้อความคนออกกลุ่ม ✦",
                    "size": "xl",
                    "color": "#ffffff",
                    "weight": "bold",
                    "action": {
                      "uri": "http://line.me/ti/p/%40jnx0914l",
                      "type": "uri",
                    }
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "ลาก่อน",
                    "color": "#ebebeb",
                    "size": "sm",
                    "flex": 0
                  },
                  {
                    "type": "text",
                    "text": "{}".format(str(teambotmax1.displayName)),
                    "color": "#ffffffcc",
                    "decoration": "line-through",
                    "gravity": "bottom",
                    "flex": 0,
                    "size": "sm"
                  }
                ],
                "spacing": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "icon",
                        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                      },
                      {
                        "type": "text",
                        "text": "สนใจเช่าบอทกดตรงนี้",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px",
                        "action": {
                          "uri": "http://line.me/ti/p/%40jnx0914l",
                          "type": "uri",
                        }
                      },
                      {
                        "type": "icon",
                        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#03303Acc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Profile",
                "color": "#ffffff",
                "align": "center",
                "size": "xs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "18px",
            "backgroundColor": "#ff334b",
            "offsetStart": "18px",
            "height": "25px",
            "width": "53px"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": teambotmax3,
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top",
            "action": {
              "uri": "http://line.me/ti/p/%40jnx0914l",
              "type": "uri",
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "✦ ข้อความคนออกกลุ่ม ✦",
                    "size": "xl",
                    "color": "#ffffff",
                    "weight": "bold",
                    "action": {
                      "uri": "http://line.me/ti/p/%40jnx0914l",
                      "type": "uri",
                    }
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "ลาก่อน",
                    "color": "#ebebeb",
                    "size": "sm",
                    "flex": 0
                  },
                  {
                    "type": "text",
                    "text": "{}".format(str(teambotmax1.displayName)),
                    "color": "#ffffffcc",
                    "decoration": "line-through",
                    "gravity": "bottom",
                    "flex": 0,
                    "size": "sm"
                  }
                ],
                "spacing": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "icon",
                        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                      },
                      {
                        "type": "text",
                        "text": "สนใจเช่าบอทกดตรงนี้",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px",
                        "action": {
                          "uri": "http://line.me/ti/p/%40jnx0914l",
                          "type": "uri",
                        }
                      },
                      {
                        "type": "icon",
                        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#9C8E7Ecc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Cover",
                "color": "#ffffff",
                "align": "center",
                "size": "xs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "18px",
            "backgroundColor": "#ff334b",
            "offsetStart": "18px",
            "height": "25px",
            "width": "53px"
          }
        ],
        "paddingAll": "0px"
      }
    }
  ]
}
}
            maxbots.postTemplate(op.param1, teambotmaxZ)
            print("GROUP LEAVE")
#=====================================================================
        if op.type == 17 and settings["newWelcome"]==True:
            teambotmax1 = maxbots.getContact(op.param2)
            teambotmax2 = maxbots.getContact(op.param2)                   
            teambotmax3 = maxbots.getProfileCoverURL(op.param2)
            teambotmaxZ = {
                    "type": "flex",
                    "altText": "ƬΣΛM BӨƬ MΛX",
                    "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(op.param2).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top",
            "action": {
              "uri": "http://line.me/ti/p/%40jnx0914l",
              "type": "uri",
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "✦ ข้อความคนเข้ากลุ่ม ✦",
                    "size": "xl",
                    "color": "#ffffff",
                    "weight": "bold",
                    "action": {
                      "uri": "http://line.me/ti/p/%40jnx0914l",
                      "type": "uri",
                    }
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "สวัสดีครับ",
                    "color": "#ebebeb",
                    "size": "sm",
                    "flex": 0
                  },
                  {
                    "type": "text",
                    "text": "{}".format(str(teambotmax1.displayName)),
                    "color": "#ffffffcc",
                    "decoration": "line-through",
                    "gravity": "bottom",
                    "flex": 0,
                    "size": "sm"
                  }
                ],
                "spacing": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "icon",
                        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                      },
                      {
                        "type": "text",
                        "text": "สนใจเช่าบอทกดตรงนี้",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px",
                        "action": {
                          "uri": "http://line.me/ti/p/%40jnx0914l",
                          "type": "uri",
                        }
                      },
                      {
                        "type": "icon",
                        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#03303Acc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Profile",
                "color": "#ffffff",
                "align": "center",
                "size": "xs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "18px",
            "backgroundColor": "#ff334b",
            "offsetStart": "18px",
            "height": "25px",
            "width": "53px"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": teambotmax3,
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top",
            "action": {
              "uri": "http://line.me/ti/p/%40jnx0914l",
              "type": "uri",
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "✦ ข้อความคนเข้ากลุ่ม ✦",
                    "size": "xl",
                    "color": "#ffffff",
                    "weight": "bold",
                    "action": {
                      "uri": "http://line.me/ti/p/%40jnx0914l",
                      "type": "uri",
                    }
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "สวัสดีครับ",
                    "color": "#ebebeb",
                    "size": "sm",
                    "flex": 0
                  },
                  {
                    "type": "text",
                    "text": "{}".format(str(teambotmax1.displayName)),
                    "color": "#ffffffcc",
                    "decoration": "line-through",
                    "gravity": "bottom",
                    "flex": 0,
                    "size": "sm"
                  }
                ],
                "spacing": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "icon",
                        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                      },
                      {
                        "type": "text",
                        "text": "สนใจเช่าบอทกดตรงนี้",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px",
                        "action": {
                          "uri": "http://line.me/ti/p/%40jnx0914l",
                          "type": "uri",
                        }
                      },
                      {
                        "type": "icon",
                        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#9C8E7Ecc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Cover",
                "color": "#ffffff",
                "align": "center",
                "size": "xs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "18px",
            "backgroundColor": "#ff334b",
            "offsetStart": "18px",
            "height": "25px",
            "width": "53px"
          }
        ],
        "paddingAll": "0px"
      }
    }
  ]
}
}
            maxbots.postTemplate(op.param1, teambotmaxZ)
            print("GROUP WELCOME")
#=====================================================================
        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = maxbots.getGroup(op.param1)
                contact = maxbots.getContact(op.param2)
                leaveMembers(op.param1, [op.param2])
                warna1 = ("#0011FF","#00FF00","#AC42FF","#C80066","#1C2513","#31C2FF","#09395E")
                warnanya1 = random.choice(warna1)
                teambotmaxZ = {
                        "type": "flex",
                        "altText": "ƬΣΛM BӨƬ MΛX",
                        "contents": {
                                              "styles": {
                                              "body": {
                                              "backgroundColor": warnanya1
                                           },
                                           "footer": {
                                             "backgroundColor": "#000000"
                                             }
                                           },
                                           "type": "bubble",
                                           "size": "giga",
                                             "body": {
                                             "contents": [
                                               {
                                                 "contents": [
                                                   {
                                                      "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(op.param2).pictureStatus),
                                                      "size": "full",
                                                      "type": "image"
                                                    },
                                                 ],
                                                 "type": "box",
                                                 "spacing": "sm",
                                                 "layout": "vertical"
                                               },
                                               {
                                                 "type": "separator",
                                                 "color": "#FF0000"
                                               },
                                               {
                                                 "contents": [
                                                    {
                                                      "text": "{}".format(maxbots.getContact(op.param2).displayName),
                                                      "size": "md",
                                                      "align": "center",
                                                      "color": "#FF0000",
                                                      "wrap": True,
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                 ],
                                                 "type": "box",
                                                 "spacing": "sm",
                                                 "layout": "vertical"
                                               },
                                               {
                                                 "type": "separator",
                                                 "color": "#FF0000"
                                               },
                                               {
                                                 "contents": [
                                                    {
                                                      "contents": [
                                                        {
                                                          "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg",
                                                          "type": "icon",
                                                          "size": "md"
                                                        },
                                                        {
                                                          "text": "╰➣ {}".format(settings["leave"]),
                                                          "size": "md",
                                                          "margin": "none",
                                                          "color": "#FFFFFF",
                                                          "wrap": True,
                                                          "weight": "regular",
                                                          "type": "text"
                                                        }
                                                      ],
                                                      "type": "box",
                                                      "layout": "baseline"
                                                    }
                                                 ],          
                                                 "type": "box",
                                                 "layout": "vertical"
                                               }
                                             ],
                                             "type": "box",
                                             "spacing": "md",
                                             "layout": "vertical"
                                           },
                                           "footer": {
                                             "contents": [
                                                {
                                                  "contents": [
                                                     {
                                                       "contents": [
                                                          {
                                                            "text": "✦ สนใจบอทสวยสวยเพิ่มเพื่อนมาเลย ✦",
                                                            "size": "sm",
                                                            "action": {
                                                              "uri": "http://line.me/ti/p/%40jnx0914l",
                                                              "type": "uri",
                                                              "label": "ADD ME"
                                                            },
                                                            "margin": "md",
                                                            "align": "center",
                                                            "color": "#FF1300",
                                                            "weight": "bold",
                                                            "type": "text"
                                                          }
                                                       ],
                                                       "type": "box",
                                                       "layout": "baseline"
                                                     }
                                                  ],
                                                  "type": "box",
                                                  "layout": "horizontal"
                                                }
                                             ],
                                             "type": "box",
                                             "layout": "vertical"
                                             }
                                           }
                                           }
                maxbots.postTemplate(op.param1, teambotmaxZ)
                msgSticker = settings["messageSticker"]["listSticker"]["leaveSticker"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    sendSticker(op.param1, sver, spkg, sid)
#=====================================================================
        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = maxbots.getGroup(op.param1)
                contact = maxbots.getContact(op.param2)
                welcomeMembers(op.param1, [op.param2])
                warna1 = ("#0011FF","#00FF00","#AC42FF","#C80066","#1C2513","#31C2FF","#09395E")
                warnanya1 = random.choice(warna1)
                teambotmaxZ = {
                        "type": "flex",
                        "altText": "ƬΣΛM BӨƬ MΛX",
                        "contents": {
                                              "styles": {
                                              "body": {
                                              "backgroundColor": warnanya1
                                           },
                                           "footer": {
                                             "backgroundColor": "#000000"
                                             }
                                           },
                                           "type": "bubble",
                                           "size": "giga",
                                             "body": {
                                             "contents": [
                                               {
                                                 "contents": [
                                                   {
                                                      "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(op.param2).pictureStatus),
                                                      "size": "full",
                                                      "type": "image"
                                                    },
                                                 ],
                                                 "type": "box",
                                                 "spacing": "sm",
                                                 "layout": "vertical"
                                               },
                                               {
                                                 "type": "separator",
                                                 "color": "#FF0000"
                                               },
                                               {
                                                 "contents": [
                                                    {
                                                      "text": "{}".format(maxbots.getContact(op.param2).displayName),
                                                      "size": "md",
                                                      "align": "center",
                                                      "color": "#FF0000",
                                                      "wrap": True,
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                 ],
                                                 "type": "box",
                                                 "spacing": "sm",
                                                 "layout": "vertical"
                                               },
                                               {
                                                 "type": "separator",
                                                 "color": "#FF0000"
                                               },
                                               {
                                                 "contents": [
                                                    {
                                                      "contents": [
                                                        {
                                                          "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg",
                                                          "type": "icon",
                                                          "size": "md"
                                                        },
                                                        {
                                                          "text": "╰➣ {}".format(settings["welcome"]),
                                                          "size": "md",
                                                          "margin": "none",
                                                          "color": "#FFFFFF",
                                                          "wrap": True,
                                                          "weight": "regular",
                                                          "type": "text"
                                                        }
                                                      ],
                                                      "type": "box",
                                                      "layout": "baseline"
                                                    }
                                                 ],          
                                                 "type": "box",
                                                 "layout": "vertical"
                                               }
                                             ],
                                             "type": "box",
                                             "spacing": "md",
                                             "layout": "vertical"
                                           },
                                           "footer": {
                                             "contents": [
                                                {
                                                  "contents": [
                                                     {
                                                       "contents": [
                                                          {
                                                            "text": "✦ สนใจบอทสวยสวยเพิ่มเพื่อนมาเลย ✦",
                                                            "size": "sm",
                                                            "action": {
                                                              "uri": "http://line.me/ti/p/%40jnx0914l",
                                                              "type": "uri",
                                                              "label": "ADD ME"
                                                            },
                                                            "margin": "md",
                                                            "align": "center",
                                                            "color": "#FF1300",
                                                            "weight": "bold",
                                                            "type": "text"
                                                          }
                                                       ],
                                                       "type": "box",
                                                       "layout": "baseline"
                                                     }
                                                  ],
                                                  "type": "box",
                                                  "layout": "horizontal"
                                                }
                                             ],
                                             "type": "box",
                                             "layout": "vertical"
                                             }
                                           }
                                           }
                maxbots.postTemplate(op.param1, teambotmaxZ)
                msgSticker = settings["messageSticker"]["listSticker"]["welcomeSticker"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    sendSticker(op.param1, sver, spkg, sid)
#=====================================================================
        if op.type == 19:
            if maxbotsMid in op.param3:
                settings["blackList"][op.param2] = True
#=====================================================================   
        if op.type == 19:
          if op.param2 not in Bots and op.param2 not in admin:
            if op.param2 in settings["blackList"]:
                maxbots.kickoutFromGroup(op.param1,[op.param2])
                G = maxbots.getGroup(op.param1)
                G.preventedJoinByTicket = True
                maxbots.updateGroup(G)
                settings["blackList"][op.param2] = True
                maxbots.sendMessage(op.param1, "✯͜͡❂ 19 ผู้ใช้อยู่ในบัญชีดำ โปรดล้างบัญชีดำก่อน")
#=====================================================================   
        if op.type == 19:
            if op.param2 in Bots:
            	pass
            else:
              try:
                 if op.param1 in protectkick:
                     settings["blackList"][op.param2] = True
                     G = maxbots.getGroup(op.param1)
                     maxbots.kickoutFromGroup(op.param1,[op.param2])
                     maxbots.findAndAddContactsByMid(op.param3)
                     maxbots.inviteIntoGroup(op.param1,[op.param3])
                 else:
                   pass
              except:
                try:
                    G = maxbots.getGroup(op.param1)
                    maxbots.kickoutFromGroup(op.param1,[op.param2])
                    maxbots.findAndAddContactsByMid(op.param3)
                    maxbots.inviteIntoGroup(op.param1,[op.param3])
                    settings["blackList"][op.param2] = True
                except:
                    pass
#=====================================================================
        if op.type == 22:
            if settings["leaveRoom"] == True:
                maxbots.leaveRoom(op.param1)
#=====================================================================
        if op.type == 24:
            if settings["leaveRoom"] == True:
                maxbots.leaveRoom(op.param1)
#=====================================================================
        if op.type == 26:
            msg = op.message
            if msg.text is None:
               return
            elif "สแปม" in msg.text:
               maxbots.blockContact(msg._from)
#=====================================================================
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in admin:
                    settings["blackList"][op.param2] = True
                    try:
                        if op.param3 not in settings["blackList"]:
                            maxbots.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
#=====================================================================                        
        if op.type == 55:
            if op.param1 in read["readPoint"]:
                if op.param2 not in read["readMember"][op.param1]:
                    read["readMember"][op.param1].append(op.param2)
#=====================================================================
        if op.type == 55:
          if op.param2 not in Bots and op.param2 not in admin:
            if op.param2 in settings["blackList"]:
                maxbots.kickoutFromGroup(op.param1,[op.param2])
                G = maxbots.getGroup(op.param1)
                G.preventedJoinByTicket = True
                maxbots.updateGroup(G)
                settings["blackList"][op.param2] = True
                maxbots.sendMessage(op.param1, "✯͜͡❂ 55 ผู้ใช้อยู่ในบัญชีดำ โปรดล้างบัญชีดำก่อน")
#=====================================================================
        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = maxbots.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n• " + Name
                        contact = maxbots.getContact(op.param2)
                        warna1 = ("#0011FF","#000000","#AC42FF","#C80066","#1C2513","#31C2FF","#09395E")
                        warnanya1 = random.choice(warna1)
                        teambotmaxZ = {
                               "type": "flex",
                               "altText": "ƬΣΛM BӨƬ MΛX",
                               "contents": {
                                                    "styles": {
                                                      "body": {
                                                        "backgroundColor": warnanya1
                                                      },
                                                      "footer": {
                                                        "backgroundColor": "#FF1E00"
                                                      }
                                                    },
                                                    "type": "bubble",
                                                    "size": "giga",
                                                    "body": {
                                                      "contents": [
                                                        {
                                                          "contents": [
                                                            {
                                                              "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(op.param2).pictureStatus),
                                                              "type": "image",
                                                              "size": "full"
                                                            },
                                                            {
                                                              "type": "separator",
                                                              "color": "#FFFFFF"
                                                            },
                                                            {
                                                              "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg",
                                                              "type": "image",
                                                              "size": "full"
                                                            }
                                                          ],
                                                          "type": "box",
                                                          "spacing": "md",
                                                          "layout": "horizontal"
                                                        },
                                                        {
                                                          "type": "separator",
                                                          "color": "#FFFFFF"
                                                        },
                                                        {
                                                          "contents": [
                                                            {
                                                              "text": "☬ NamaSider ☬",
                                                              "size": "md",
                                                              "margin": "none",
                                                              "color": "#81FF00",
                                                              "align": "center",
                                                              "wrap": True,
                                                              "weight": "regular",
                                                              "type": "text"
                                                            },
                                                            {                                                             
                                                              "text": "{}".format(maxbots.getContact(op.param2).displayName),
                                                              "size": "md",
                                                              "margin": "none",
                                                              "color": "#FFFFFF",
                                                              "align": "center",
                                                              "wrap": True,
                                                              "weight": "regular",
                                                              "type": "text"
                                                            }
                                                          ],
                                                          "type": "box",
                                                          "spacing": "md",
                                                          "layout": "vertical"
                                                        },
                                                        {
                                                          "type": "separator",
                                                          "color": "#FFFFFF"
                                                        },
                                                        {
                                                          "contents": [
                                                            {
                                                              "text": "☣ AutoResponSider ☣",
                                                              "size": "md",
                                                              "margin": "none",
                                                              "color": "#81FF00",
                                                              "align": "center",
                                                              "wrap": True,
                                                              "weight": "regular",
                                                              "type": "text"
                                                            },
                                                            {
                                                              "text": "{}".format(settings["mention"]),
                                                              "size": "md",
                                                              "margin": "none",
                                                              "align": "center",
                                                              "color": "#FFFFFF",
                                                              "wrap": True,
                                                              "weight": "regular",
                                                              "type": "text"
                                                            }
                                                          ],
                                                          "type": "box",
                                                          "layout": "vertical"
                                                        }
                                                      ],
                                                      "type": "box",
                                                      "spacing": "md",
                                                      "layout": "vertical"
                                                    },
                                                    "footer": {
                                                      "contents": [
                                                        {
                                                          "contents": [
                                                            {
                                                              "contents": [
                                                                {
                                                                  "text": "✦ สนใจบอทสวยสวยเพิ่มเพื่อนมาเลย ✦",
                                                                  "size": "md",
                                                                  "weight": "bold",
                                                                  "action": {
                                                                    "uri": "http://line.me/ti/p/%40jnx0914l",
                                                                    "type": "uri",
                                                                    "label": "Audio"
                                                                   },
                                                                  "margin": "sm",
                                                                  "align": "center",
                                                                  "color": "#000000",
                                                                  "weight": "bold",
                                                                  "type": "text"
                                                                }
                                                              ],
                                                              "type": "box",
                                                              "layout": "baseline"
                                                            }
                                                          ],
                                                          "type": "box",
                                                          "layout": "horizontal"
                                                        }
                                                      ],
                                                      "type": "box",
                                                      "layout": "vertical"
                                                     }
                                                   }
                                                   }
                        maxbots.postTemplate(op.param1, teambotmaxZ)
                        msgSticker = settings["messageSticker"]["listSticker"]["readerSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(op.param1, sver, spkg, sid)
#=====================================================================
        if op.type == 26:
           msg = op.message
           if msg._from not in Bots:
               if msg._from in settings["blackList"]:
                  try:
                      maxbots.kickoutFromGroup(msg.to, [msg._from])
                  except:
                      try:
                          maxbots.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          maxbots.kickoutFromGroup(msg.to, [msg._from])
#=======================================================================================================
        if op.type == 26:
            msg = op.message
            sender = msg._from
            to = msg.to
            if msg.contentType == 6:
                    if settings["spamCall"] == True and sender != maxbotsMid:
                        contact = maxbots.getContact(sender)
                        if msg.toType == 0:
                            if msg.contentMetadata["GC_EVT_TYPE"] == "I":
                                maxbots.sendMention(to, sender, "@!")
                                arg = " • รัวคอล"
                                arg += "\n • ชื่อผู้ใช้ : {}".format(str(contact.displayName))
                                print (arg)
                        elif msg.toType == 2:
                            group = maxbots.getGroup(to)
                            if msg.contentMetadata["GC_EVT_TYPE"] == "S":
                                arg = " • รัวคอล"
                                arg += "\n • กลุ่ม : {}".format(str(group.name))
                                arg += "\n • ชื่อผู้ใช้ : {}".format(str(contact.displayName))
                                print (arg)
                                maxbots.sendMention(to, sender, "@!")
                            elif msg.contentMetadata["GC_EVT_TYPE"] == "E":
                                maxbots.sendMention(to, sender, "@!")
                                arg = " • สิ้นสุดการคอล"
                                arg += "\n • กลุ่ม : {}".format(str(group.name))
                                arg += "\n • ชื่อผู้ใช้ : {}".format(str(contact.displayName))
                                print (arg)
#=======================================================================================================
        if op.type == 25 or op.type == 26:
            msg = op.message 
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 1:
                    path = maxbots.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}

            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n├ ⌬ Sticker ID : {}".format(stk_id)
                   ret_ += "\n├ ⌬ Sticker Version : {}".format(stk_ver)
                   ret_ += "\n├ ⌬ Sticker Package : {}".format(pkg_id)
                   ret_ += "\n├ ⌬ Sticker Url : line://shop/detail/{}".format(pkg_id)
                   ret_ += "\n╰─「 ＳＥＬＦＢＯＴＢＹＭＡＸ 」"
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = maxbots.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}         

            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver

               if msg.contentType == 13:
                if msg._from in admin:
                  if settings["groupInvite"] == True:
                    msg.contentType = 0
                    contact = maxbots.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = maxbots.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in settings["blackList"]:
                            maxbots.sendMessage(msg.to, "โปรดล้างบัญชีดำก่อน จึงจะเชิญได้")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                             try:
                                  maxbots.findAndAddContactsByMid(target)
                                  maxbots.inviteIntoGroup(msg.to,[target])
                                  ryan = maxbots.getContact(target)
                                  zx = ""
                                  zxc = ""
                                  zx2 = []
                                  xpesan =  "• ชื่อ : "
                                  ret_ = "• ทำการเชิญเข้ากลุ่มสำเร็จ"
                                  ry = str(ryan.displayName)
                                  pesan = ''
                                  pesan2 = pesan+"@MAX\n"
                                  xlen = str(len(zxc)+len(xpesan))
                                  xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                  zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                  zx2.append(zx)
                                  zxc += pesan2
                                  text = xpesan + zxc + ret_ + ""
                                  maxbots.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  settings["groupInvite"] = False
                                  break
                             except:
                                  maxbots.sendText(msg.to,"• คุณมีขีด จำกัด ในการเชิญเพื่อน")
                                  settings["groupInvite"] = False
                                  break

        if op.type == 25 or op.type == 26:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                teambotmax = command(text)
                ryyn = "uc14c3d87a1123df7c8ffa9d7402e59a2"
                setKey = settings["keyCommand"].title()
                if settings["setKey"] == False:
                    setKey = ''
                if settings["TrapCode"] == True:
                    if msg.contentType == 22:
                       teambotmaxText(msg.to, str(msg))
                       print(msg)
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.contentType == 16:
                        if settings["autolike"] == True:
                            if msg.toType in (2, 1, 0):
                                try:
                                    purl = (
                                        msg.contentMetadata["postEndUrl"]
                                        .split("userMid=")[1]
                                        .split("&postId=")
                                    )
                                    maxbots.likePost(purl[0], purl[1], 1003)
                                    settingss["liked"] += 1
                                    backupData()
                                    maxbots.createComment(
                                        purl[0], purl[1], settings["commentPost"]
                                    )
                                    teambotmaxLike(to, settings["commentPost"])
                                except:
                                    pass

                    if sender not in maxbotsMid:
                        if msg.toType != 0 and msg.toType == 2:
                          if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            contact = maxbots.getContact(sender)
                            status = maxbots.getContact(sender)
                            for mention in mentionees:
                              if maxbotsMid in mention["M"]:
                                if settings["responMentionnya"] == True:
                                  contact = maxbots.getProfile()
                                  mids = [contact.mid]
                                  teambotmax1 = maxbots.getContact(sender)
                                  teambotmaxZ = {
                                          "type": "flex",
                                          "altText": "ƬΣΛM BӨƬ MΛX",
                                          "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "giga",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top",
            "action": {
              "uri": "http://line.me/ti/p/%40jnx0914l",
              "type": "uri",
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "✦ ข้อความตอบกลับอัตโนมัติ ✦",
                    "size": "xl",
                    "color": "#ffffff",
                    "weight": "bold",
                    "align": "center",
                    "action": {
                      "uri": "http://line.me/ti/p/%40jnx0914l",
                      "type": "uri",
                    }
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "╰➣ มีอะไร",
                    "color": "#ebebeb",
                    "size": "sm",
                    "flex": 0
                  },
                  {
                    "type": "text",
                    "text": "{}".format(str(teambotmax1.displayName)),
                    "color": "#ffffffcc",
                    "decoration": "line-through",
                    "gravity": "bottom",
                    "flex": 0,
                    "size": "sm"
                  }
                ],
                "spacing": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "icon",
                        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                      },
                      {
                        "type": "text",
                        "text": "กดตรงนี้เพื่อเพิ่มเพื่อนฉัน",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px",
                        "action": {
                          "uri": "https://line.me/ti/p/"+maxbots.getUserTicket().id,
                          "type": "uri",
                        }
                      },
                      {
                        "type": "icon",
                        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px",
                "position": "relative",
                "flex": 0
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#03303Acc",
            "paddingAll": "20px",
            "paddingTop": "18px",
            "spacing": "none",
            "margin": "none"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "NEW",
                "color": "#ffffff",
                "align": "center",
                "size": "xs",
                "offsetTop": "4px",
                "flex": 0,
                "margin": "none",
                "weight": "regular",
                "style": "normal",
                "decoration": "none",
                "position": "relative",
                "gravity": "top",
                "wrap": True
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "18px",
            "backgroundColor": "#ff334b",
            "offsetStart": "18px",
            "height": "25px",
            "width": "53px"
          }
        ],
        "paddingAll": "0px"
      },
      "action": {
        "type": "uri",
        "label": "action",
        "uri": "http://line.me/ti/p/%40jnx0914l"
      }
    }
  ]
}
}
                                  maxbots.postTemplate(receiver, teambotmaxZ)

                    if sender not in maxbotsMid:
                        if msg.toType != 0 and msg.toType == 2:
                          if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            contact = maxbots.getContact(sender)
                            status = maxbots.getContact(sender)
                            for mention in mentionees:
                              if maxbotsMid in mention["M"]:
                                if settings["responMaxNewVersion"] == True:
                                  contact = maxbots.getProfile()
                                  mids = [contact.mid]
                                  timeNow = time.time()
                                  runtime = timeNow - botStart
                                  runtime = format_timespan(runtime)
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  teambotmax1 = maxbots.getContact(sender)
                                  teambotmaxZ = {
                                          "type": "flex",
                                          "altText": "ƬΣΛM BӨƬ MΛX",
                                          "contents": {
  "type": "bubble",
  "size": "giga",
  "hero": {
    "type": "image",
    "url": "https://www.img.live/images/2019/11/23/1565537279814.jpg",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://line.me/ti/p/%40jnx0914l"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "✦ ข้อความตอบกลับอัตโนมัติ ✦",
        "weight": "bold",
        "size": "xl",
        "color": "#000000",
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "box",
        "layout": "baseline",
        "margin": "md",
        "contents": [
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "text",
            "text": "5.0",
            "size": "sm",
            "color": "#999999",
            "margin": "md",
            "flex": 0
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "• วันที่",
                "color": "#003EFF",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "" + datetime.strftime(timeNow,'%Y-%m-%d'),
                "wrap": True,
                "color": "#ff0000",
                "size": "sm",
                "flex": 5
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "• เวลา",
                "color": "#FF9E00",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "" + datetime.strftime(timeNow,'%H:%M:%S') + " นาที",
                "wrap": True,
                "color": "#00B50F",
                "size": "sm",
                "flex": 5
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(sender).pictureStatus),
            "aspectMode": "cover",
            "size": "full"
          }
        ],
        "cornerRadius": "100px",
        "width": "80px",
        "height": "80px",
        "borderColor": "#FF4900",
        "borderWidth": "2px",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "https://line.me/ti/p/"+maxbots.getUserTicket().id
        }
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(teambotmax1.displayName),
                "color": "#FF00D7",
                "wrap": True,
                "size": "sm"
              }
            ],
            "spacing": "sm",
            "margin": "md"
          },
          {
            "type": "separator",
            "color": "#000000"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(str(settings["autoResponMessage"])),
                "color": "#ff0e09",
                "wrap": True,
                "size": "sm"
              }
            ],
            "spacing": "sm",
            "margin": "md"
          }
        ]
      }
    ],
    "spacing": "xl",
    "paddingAll": "20px",
    "borderColor": "#0011FF"
  },
  "styles": {
    "body": {
      "separatorColor": "#000000",
      "separator": True
    },
    "footer": {
      "separatorColor": "#000000",
      "separator": True
    }
  }
}
}
                                  maxbots.postTemplate(receiver, teambotmaxZ)
                                  msgSticker = settings["messageSticker"]["listSticker"]["responSticker"]
                                  if msgSticker != None:
                                      sid = msgSticker["STKID"]
                                      spkg = msgSticker["STKPKGID"]
                                      sver = msgSticker["STKVER"]
                                      sendSticker(msg.to, sver, spkg, sid)
                                  break

                    if sender not in maxbotsMid:
                        if msg.toType != 0 and msg.toType == 2:
                          if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            contact = maxbots.getContact(sender)
                            status = maxbots.getContact(sender)
                            for mention in mentionees:
                              if maxbotsMid in mention["M"]:
                                if settings["responMaxNewVersion2"] == True:
                                  contact = maxbots.getProfile()
                                  mids = [contact.mid]
                                  teambotmax1 = maxbots.getContact(sender)
                                  teambotmaxZ = {
                                          "type": "flex",
                                          "altText": "ƬΣΛM BӨƬ MΛX",
                                          "contents": {
  "type": "bubble",
  "size": "mega",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(sender).pictureStatus),
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "cornerRadius": "100px",
            "width": "72px",
            "height": "72px",
            "borderWidth": "2px",
            "borderColor": "#FF0E00",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://line.me/ti/p/%40jnx0914l"
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(maxbots.getContact(sender).displayName),
                "size": "xs",
                "wrap": True,
                "color": "#FF4E00",
                "weight": "regular",
                "align": "center"
              },
              {
                "type": "separator"
              },
              {
                "type": "text",
                "text": "{}".format(str(settings["autoResponMessage"])),
                "wrap": True,
                "size": "xs",
                "color": "#ffffff",
                "weight": "bold",
                "align": "center"
              },
              {
                "type": "separator"
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "✦ ติดต่อ ✦",
                    "size": "sm",
                    "color": "#FFF200",
                    "align": "center",
                    "weight": "bold",
                    "style": "normal",
                    "decoration": "line-through"
                  }
                ],
                "spacing": "sm",
                "margin": "md",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/%40jnx0914l"
                }
              }
            ]
          }
        ],
        "spacing": "xl",
        "paddingAll": "20px"
      }
    ],
    "paddingAll": "0px",
    "borderColor": "#FF0E00",
    "cornerRadius": "17px",
    "borderWidth": "2px",
    "backgroundColor": "#000000"
  }
}
}
                                  maxbots.postTemplate(receiver, teambotmaxZ)
                                  msgSticker = settings["messageSticker"]["listSticker"]["responSticker"]
                                  if msgSticker != None:
                                      sid = msgSticker["STKID"]
                                      spkg = msgSticker["STKPKGID"]
                                      sver = msgSticker["STKVER"]
                                      sendSticker(msg.to, sver, spkg, sid)
                                  break
#===============================================================================================================================================
                    if msg.toType == 0:
                        if sender != maxbots.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if teambotmax == "off":
                              if msg._from in admin:
                                if to not in offbot:
                                  maxbots.sendMessageWithFooter(to, "❂➣ Mode Mute Active Di Group ini")
                                  offbot.append(to)
                                  print(to)                                  
                                else:
                                  maxbots.sendMessageWithFooter(to, "❂➣ Sukses Menonaktifkan Mute di Room ini")

                        if teambotmax == "on":
                              if msg._from in admin:
                                if to in offbot:
                                  offbot.remove(to)
                                  maxbots.sendMessageWithFooter(to, "❂➣ Mode Mute Aktif")
                                  print(to)                                  
                                else:
                                  maxbots.sendMessageWithFooter(to, "❂➣ Sukses Mengaktifkan Mute Di Room ini")

                        if teambotmax == "sticker on":
                          if msg._from in admin or msg._from in owner:
                            settings["sticker"] = True
                            maxbots.sendMessage(msg.to, 'On !!')

                        if teambotmax == "sticker off":
                          if msg._from in admin or msg._from in owner:
                            settings["sticker"] = False
                            maxbots.sendMessage(msg.to, 'Off !!')

                        elif teambotmax == "เช็คบอท":
                               maxbots.sendMessage(to,"M A X")

                        elif teambotmax == "ดึง":
                          if msg._from in admin or msg._from in owner:
                            if settings["groupInvite"] == True:
                                teambotmaxText(to, "• ส่ง คท ลงมา")
                            else:
                                settings["groupInvite"] = True
                                teambotmaxText(to, "• ส่ง คท ลงมา")

                        elif teambotmax.startswith("/spam "):
                          if msg._from in admin or msg._from in owner:
                            try:
                                bctxt = msg.text.replace("/spam ", "")
                                match = re.search(r'\d+', bctxt)
                                txt = re.search(r'\D+', bctxt)
                                print(txt.group(0))
                                print(match.group(0))
                                n = int(match.group(0))
                                for _ in range(n):
                                    maxbots.sendMessage(msg.to, (txt.group(0)))
                            except:
                                maxbots.sendMessage(msg.to,"error")

                        elif teambotmax.startswith("ออก: "):
                          if msg._from in admin or msg._from in owner:
                            proses = text.split(" ")
                            ng = text.replace(proses[0] + " ","")
                            gid = maxbots.getGroupIdsJoined()
                            for i in gid:
                                h = maxbots.getGroup(i).name
                                if h == ng:
                                    maxbots.leaveGroup(i)

                        elif teambotmax.startswith("นับ "):
                          if msg._from in admin or msg._from in owner:
                           number = removeCmd("นับ", text)
                           if len(number) > 0:
                               if number.isdigit():
                                   number = int(number)
                                   if number > 50000:                                             
                                       maxbots.sendMessage(to,"Done")
                                   else:
                                       for i in range(0,number):
                                           maxbots.sendMessage(to,str(i+1))
                                           i += 1+1
                                           time.sleep(0.009)
                               else:
                                  maxbots.sendMessage(to,"Please specify a valid number.")

                        elif teambotmax.startswith("kick4 "):
                          if msg._from in admin or msg._from in owner:
                            Max0 = text.replace("kick4 ","")
                            Max1 = Max0.rstrip()
                            Max2 = Max1.replace("@","")
                            Max3 = Max2.rstrip()
                            _name = Max3
                            gs = maxbots.getGroup(msg.to)
                            targets = []
                            for s in gs.members:
                                if _name in s.displayName:
                                    targets.append(s.mid)
                            if targets == []:
                                pass
                            else:
                                for target in targets:
                                    if target in admin:
                                        pass
                                    else:
                                        try:
                                            maxbots.kickoutFromGroup(to,[target])
                                        except:
                                            pass

                        elif teambotmax.startswith("kick3 "):
                          if msg._from in admin or msg._from in owner:
                            Max0 = text.replace("kick3 ","")
                            Max1 = Max0.rstrip()
                            Max2 = Max1.replace("@","")
                            Max3 = Max2.rstrip()
                            _name = Max3
                            gs = maxbots.getGroup(msg.to)
                            targets = []
                            for s in gs.members:
                                if _name in s.displayName:
                                    targets.append(s.mid)
                            if targets == []:
                                pass
                            else:
                                for target in targets:
                                    if target in admin:
                                        pass
                                    else:
                                        try:
                                            maxbots.kickoutFromGroup(to,[target])
                                            maxbots.findAndAddContactsByMid(target)
                                            maxbots.inviteIntoGroup(to,[target])
                                        except:
                                            pass

                        elif teambotmax.startswith("kick2 "):
                          if msg._from in admin or msg._from in owner:
                            vkick0 = msg.text.replace("kick2 ","")
                            vkick1 = vkick0.rstrip()
                            vkick2 = vkick1.replace("@","")
                            vkick3 = vkick2.rstrip()
                            _name = vkick3
                            gs = maxbots.getGroup(msg.to)
                            targets = []
                            for s in gs.members:
                                if _name in s.displayName:
                                    targets.append(s.mid)
                            if targets == []:
                                pass
                            else:
                                for target in targets:
                                    try:
                                        maxbots.kickoutFromGroup(msg.to,[target])
                                        maxbots.findAndAddContactsByMid(target)
                                        maxbots.inviteIntoGroup(msg.to,[target])
                                        maxbots.cancelGroupInvitation(msg.to,[target])
                                    except:
                                        pass

                        elif teambotmax == "memberpict":
                          if msg._from in admin or msg._from in owner:
                            kontak = maxbots.getGroup(to)
                            group = kontak.members
                            picall = []
                            for ids in group:
                              if len(picall) >= 400:
                                pass
                              else:
                                picall.append({
                                 "imageUrl": "https://os.line.naver.jp/os/p/{}".format(ids.mid),
                                 "action": {
                                    "type": "uri",
                                    "uri": "https://line.me/ti/p/UeFNMxETvC"
                                    }
                                  }
                                )
                            k = len(picall)//10
                            for aa in range(k+1):
                              data = {
                                "messages": [
                                   {
                                     "type": "template",
                                     "altText": "warga",
                                     "template": {
                                       "type": "image_carousel",
                                       "columns": picall[aa*10 : (aa+1)*10]
                                     }
                                   }
                                 ]
                               }
                              sendTemplateMax(to, data)

                        elif teambotmax.startswith("spam "):
                            if msg._from in admin or msg._from in owner:
                                txt = teambotmax.split(" ")
                                jmlh = int(txt[2])
                                teks = teambotmax.replace("spam "+str(txt[1])+" "+str(jmlh)+" ","")
                                tulisan = jmlh * (teks+"\n")
                                if txt[1] == "on":
                                    if jmlh <= 5000:
                                       for x in range(jmlh):
                                           maxbots.sendText(to, teks)
                                    else:
                                       maxbots.sendText(to, "Maksimal 5000 SpamTeks!")
                                elif txt[1] == "off":
                                    if jmlh <= 5000:
                                        maxbots.sendText(to, tulisan)
                                    else:
                                        maxbots.sendText(to, "Maksimal 5000 SpamTeks!")

                        elif teambotmax == "#ขายบอท1":
                          if msg._from in admin or msg._from in owner:
                            saya = maxbots.getGroupIdsJoined()
                            for gr in saya:
                                teambotmaxZ={
                                        "type": "flex",
                                        "altText": "ƬΣΛM BӨƬ MΛX",
                                        "contents": {
  "type": "bubble",
  "size": "giga",
  "hero": {
    "type": "image",
    "url": "https://www.img.live/images/2019/10/22/744475356953244e707a0f36a7657c607ca0cc87bf8809fff038c1cc1f42afab1570086316050.0.jpg",
    "size": "full",
    "aspectRatio": "1:1",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://line.me/ti/p/~maxxxxxxxxxxxxxxxx"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "contents": [
      {
        "type": "text",
        "text": "ขออนุญาตขายบอทนะครับ",
        "wrap": True,
        "weight": "bold",
        "gravity": "center",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "baseline",
        "margin": "md",
        "contents": [
          {
            "type": "icon",
            "size": "sm",
            "url": "https://www.img.live/images/2019/10/22/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
          },
          {
            "type": "text",
            "text": "• ชำระเงินได้หลายช่องทาง",
            "size": "sm",
            "color": "#999999",
            "margin": "md",
            "flex": 0
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "• 1.",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "ปล่อยให้เช่าเชลบอท 1 เดือน 100 บาท ไม่เก็บเพิ่ม.",
                "wrap": True,
                "size": "sm",
                "color": "#666666",
                "flex": 4
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "• 2.",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "ขายไฟล์บอททุกชนิด & สอนแก้สคริปบอท & ไฟล์บอท",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 4
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "• 3.",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "รับโปรโมท & ฝากร้านขายสติกเกอร์ ฯลฯ",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 4
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "• 4.",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "รับลบรันทั้งหมด มีล้านก็ลบได้ ราคาเบาๆ 50 บาท",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 4
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "• 5.",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "หารายได้จากบอทได้สบาย โปรโมทขายของก็ได้",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 4
              }
            ]
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact("uc14c3d87a1123df7c8ffa9d7402e59a2").pictureStatus),
                "aspectMode": "cover",
                "size": "full",
                "action": {
                  "type": "uri",
                  "uri": "http://line.me/ti/p/~maxxxxxxxxxxxxxxxx"
                }
              }
            ],
            "cornerRadius": "100px",
            "width": "72px",
            "height": "72px"
          },
          {
            "type": "text",
            "text": "• แตะที่รูปเพื่อติดต่อ\n• มีฟังก์ชั่นหลายแบบ\n• มีประกาศหลายแบบ\n• มีบอทล็อกอินใช้งานได้ 24 ชม.",
            "color": "#aaaaaa",
            "wrap": True,
            "margin": "xxl",
            "size": "xs"
          }
        ]
      }
    ]
  }
}
}
                                maxbots.postTemplate(gr, teambotmaxZ)
                                time.sleep(1)
                                print ("ประกาศกลุ่มเรียบร้อย")

                        elif teambotmax == "#ขายบอท2":
                          if msg._from in admin or msg._from in owner:
                            saya = maxbots.getGroupIdsJoined()
                            for gr in saya:
                                teambotmaxZ={
                                        "type": "flex",
                                        "altText": "ƬΣΛM BӨƬ MΛX",
                                        "contents": {
  "type": "bubble",
  "size": "giga",
  "hero": {
    "type": "image",
    "url": "https://www.img.live/images/2019/10/22/1565537279814.jpg",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://line.me/ti/p/%40jnx0914l"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "ซื้อบอทราคาถูกต้องซื้อที่นี่",
        "weight": "bold",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "baseline",
        "margin": "md",
        "contents": [
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "text",
            "text": "5.0",
            "size": "sm",
            "color": "#999999",
            "margin": "md",
            "flex": 0
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "HOT",
                "color": "#000000",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "เชลบอท 1 เดือนแค่ 100 บาท เท่านั้น",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "HOT",
                "color": "#000000",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "คิกเกอร์ 11 ตัว 1 เดือนแค่ 200 บาท เท่านั้น",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "HOT",
                "color": "#000000",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "รับแก้ไฟล์บอททุกชนิด คุยราคาได้ตลอด",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "HOT",
                "color": "#000000",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "ขายไฟล์บอททุกชนิดที่มี ถูก คุ้ม เครดิตแน่น",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "✦ เพิ่มเพื่อนคนขาย ✦",
          "uri": "http://line.me/ti/p/~maxxxxxxxxxxxxxxxx"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "✦ เพิ่มเพื่อนแอดมิน ✦",
          "uri": "http://line.me/ti/p/%40jnx0914l"
        }
      },
      {
        "type": "spacer",
        "size": "sm"
      }
    ],
    "flex": 0
  }
}
}
                                maxbots.postTemplate(gr, teambotmaxZ)
                                time.sleep(1)
                                print ("ประกาศกลุ่มเรียบร้อย")

                        elif teambotmax.startswith("mp3"):
                          if msg._from in admin or msg._from in owner:
                            try:
                                teambotmaxText(to,"Wait...")
                                proses = text.split(" ")
                                urutan = text.replace(proses[0] + " ","")
                                r = requests.get("http://api.zicor.ooo/joox.php?song={}".format(str(urllib.parse.quote(urutan))))
                                data = r.text
                                data = json.loads(data)
                                b = data
                                c = str(b["title"])
                                d = str(b["singer"])
                                e = str(b["url"])
                                g = str(b["image"])
                                ret_ = "╭────────「 Music 」"
                                ret_ += "\n├ Penyanyi: "+str(d)
                                ret_ += "\n├ Judul : "+str(c) 
                                ret_ += "\n╰────────「 Finish 」"
                                dataa= {
                                        "type": "flex",
                                        "altText": "lagi dengerin lagu",
                                        "contents":{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": g,
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": g
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xs",
    "contents": [
      {
        "type": "text", 
        "text": ret_,
        "color": "#FF0000",
        "wrap": True,
        "weight": "bold",
        "gravity": "center",
        "size": "xs",
        "action": {
          "type": "uri",
          "uri":  "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2"
        }
      }
    ]
  },
  "styles": {"body": {"backgroundColor": "#0000FF"},
   }
 }
}
                                maxbots.postTemplate(to,dataa)
                                maxbots.sendAudioWithURL(to,e)
                            except Exception as error:
                                teambotmaxText(to, "error\n" + str(error))
                                logError(error)

                        elif teambotmax.startswith("music "):
                            if msg._from in admin or msg._from in owner:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.fckveza.com/jooxmusic={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╭──「 Result Music 」"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n├ {}. {}".format(str(num), str(music["judul"]))
                                    ret_ += "\n╰──「 Total {} Music 」".format(str(len(music)))
                                    ret_ += "\n\nUntuk Melihat Details Music, silahkan gunakan command {}Music {}|「number」".format(str(setKey), str(search))
                                    teambotmaxText(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.fckveza.com/musicid={}".format(str(music["songid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data != []:
                                            ret_ = "╭──「 Music 」"
                                            ret_ += "\n├ Singer : {}".format(str(data["result"][0]["artis"]))
                                            ret_ += "\n├ Title : {}".format(str(data["result"][0]["judul"]))
                                            ret_ += "\n├ Album : {}".format(str(data["result"][0]["single"]))
                                            ret_ += "\n╰──「 Finish 」"
                                            dataa= {
                                                    "type": "flex",
                                                    "altText": "lagi dengerin lagu",
                                                    "contents":{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "{}".format(str(data["result"][0]["imgUrl"])),
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "{}".format(str(data["result"][0]["imgUrl"]))
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xs",
    "contents": [
      {
        "type": "text", 
        "text": "{}".format(str(ret_)),
        "color": "#FF0000",
        "wrap": True,
        "weight": "bold",
        "gravity": "center",
        "size": "xs",
        "action": {
          "type": "uri",
          "uri":  "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2"
        }
      }
    ]
  },
  "styles": {"body": {"backgroundColor": "#00FFFF"},
   }
 }
}
                                            maxbots.postTemplate(to,dataa)
                                            maxbots.sendAudioWithURL(to, str(data["result"][0]["mp3Url"]))

                        elif teambotmax.startswith("musik "):
                          if msg._from in admin or msg._from in owner:
                            try:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                r = requests.get("http://ryns-api.herokuapp.com/joox?q={}".format(query))
                                data = r.text
                                data = json.loads(data)
                                data = data["result"]
                                jmlh = len(data)
                                datalagu = []
                                if jmlh > 10 :
                                    jmlh = 10
                                else:
                                    pass
                                    for x in range(0,jmlh):
                                        item= {
  "type": "bubble",
    "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
        {
        "type": "text",
        "text":  "ＳＥＬＦＢＯＴＢＹＭＡＸ",
        "size": "md",
        "wrap": True,
        "weight": "bold",
        "align": "center",
        "color": "#1900FF"
      }
    ]
  },
  "hero": {
    "type": "image",
    "url": "{}".format(data[x]["img"]),
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "{}".format(data[x]["img"])
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xs",
    "contents": [
      {
        "type": "text",
        "text": "Artist :",
        "color": "#FF0000",
        "size": "md",
        "flex": 1
      },
      {
        "type": "text",
        "text": "{}".format(data[x]["title"]),
        "wrap": True,
        "weight": "bold",
        "color": "#FF0000",
        "gravity": "center",
        "size": "md",
        "flex": 2
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "xs",
        "spacing": "xs",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "xs",
            "contents": [
              {
                "type": "text",
                "text": "Artist :",
                "color": "#FF0000",
                "size": "md",
                "flex": 3
              },
              {
                "type": "text",
                "text": "{}".format(data[x]["artis"]),
                "wrap": True,
                "color": "#FF0000",
                "size": "md",
                "flex": 4
              }
            ]
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "xs",
        "contents": [
          {
            "type": "spacer"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "Download",
              "uri": "{}".format(data[x]["url"]),
            },
            "style": "primary",
            "color": "#0000ff"
          }
        ]
      }
    ]
   },
      "type": "bubble",
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "url": "https://i.ibb.co/sb3KcWs/click-here-button-gif-c200.gif",
                    "type": "icon",
                    "size": "xl"
                    },
                    {
                    "text": "Creator Caem",
                    "size": "md",
                    "action": {
                      "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                      "type": "uri",
                      "label": "Add Creator"
                    },
                    "margin": "xl",
                    "align": "center",
                    "color": "#001CFF",
                    "weight": "bold",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "layout": "horizontal"
          }
        ]
      },
      "styles": {
        "header": {
            "backgroundColor": "#7FFF00"
        },
        "body": {
          "backgroundColor": "#00FFFF","separator": True,"separatorColor": "#FF0000"
        },
        "footer": {
          "backgroundColor": "#7FFF00","separator": True,"separatorColor": "#FF0000"
        }
      }
    }
                                        datalagu.append(item)
                                    data1 = {  
                                        "type": "flex",
                                        "altText": "#Joox music results for {}".format(str(query)),
                                        "contents": {
                                                      "type": "carousel",
                                                      "contents":datalagu }}
                                    maxbots.postTemplate(to,data1)
                            except Exception as error:
                                        logError(error)
                                        maxbots.sendReplyMessage(msg.id, to, str(error))

                        elif teambotmax == 'order' or teambotmax == 'ขาย':
                          if msg._from in admin or msg._from in owner:
                            teambotmaxZ = {
                                    "type": "flex",
                                    "altText": "ƬΣΛM BӨƬ MΛX",
                                    "contents": {
  "type": "bubble",
  "size": "giga",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "image",
            "url": "https://www.img.live/images/2019/11/23/1565537279814.jpg",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~maxxxxxxxxxxxxxxxx"
            }
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "NEW",
                "size": "xs",
                "color": "#ffffff",
                "align": "center",
                "gravity": "center"
              }
            ],
            "backgroundColor": "#EC3D44",
            "paddingAll": "2px",
            "paddingStart": "4px",
            "paddingEnd": "4px",
            "flex": 0,
            "position": "absolute",
            "offsetStart": "18px",
            "offsetTop": "18px",
            "cornerRadius": "100px",
            "width": "48px",
            "height": "25px"
          }
        ]
      }
    ],
    "paddingAll": "0px"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "✦ ขายไฟล์บอท & ปล่อยเช่าบอท ✦",
        "weight": "bold",
        "size": "lg",
        "align": "center",
        "wrap": True
      },
      {
        "type": "box",
        "layout": "baseline",
        "margin": "md",
        "contents": [
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "text",
            "text": "5.0",
            "size": "sm",
            "color": "#999999",
            "margin": "md",
            "flex": 0
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "• ขาย",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "บอทเฟ็ก & บอทป้องกัน & บอทบิน",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "• เช่า",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "บอทเฟ็ก & ป้องกัน & รับแก้ไฟล์",
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "secondary",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "✦ ติดต่อคนขาย ✦",
          "uri": "http://line.me/ti/p/~maxxxxxxxxxxxxxxxx"
        },
        "color": "#32C510"
      },
      {
        "type": "button",
        "style": "secondary",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "✦ ติดต่อแอดมิน ✦",
          "uri": "http://line.me/ti/p/%40jnx0914l"
        },
        "color": "#32C510"
      }
    ],
    "flex": 0
  },
  "styles": {
    "body": {
      "separatorColor": "#000000",
      "separator": True
    },
    "footer": {
      "separatorColor": "#000000",
      "separator": True
    }
  }
}
}
                            maxbots.postTemplate(to,teambotmaxZ)

                        elif teambotmax == "grouppicture":
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = maxbots.getGroup(to)
                                data = {
                                            "type": "flex",
                                            "altText": "ƬΣΛM BӨƬ MΛX",
                                            "contents": {
  "type": "bubble",
  "size": "giga",
  "direction": "ltr",
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#0000FF"
    },
    "header": {
      "backgroundColor": "#0000FF"
    }
  },  
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#FF0000",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ᴄʀᴇᴀᴛᴏʀ",
                  "uri": "http://line.me/ti/p/%40jnx0914l"
              }
          }]
      }]
  },
  "hero": {
    "aspectMode": "cover",
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(maxbots.getGroup(to).pictureStatus),
    "size": "full",
    "align": "center",
  },
  "header": {
    "type": "box",   
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "ʄσtσ ℘гσʄıɭε ɢгσน℘",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
        "align": "center"
      }
    ]
  }
}
}
                                maxbots.postTemplate(to, data)
                                time.sleep(1)

                        elif teambotmax == "ขออนุญาตขายของครับ":
                          if msg._from in admin or msg._from in owner:
                            Nama = maxbots.getContact(to)
                            cover = maxbots.getProfileCoverURL(to)
                            maxbots.reissueUserTicket()
                            data = {"type": "flex","altText": "{} มาขายของครับ".format(str(Nama.displayName)),"contents": {"type": "bubble","styles": {"header": {"backgroundColor": "#FFFFFF",},"body": {"backgroundColor": "#FFFFFF","separator": True,"separatorColor": "#FFFFFF"},"footer": {"backgroundColor": "#FFFFFF","separator": True}},"hero": {"type": "image","url": "https://os.line.naver.jp/os/p/{}".format(to),"size": "full","aspectRatio": "1:1","aspectMode": "cover","action": {"type": "uri","uri": "http://line.me/ti/p/%40jnx0914l"}},"body": {"type": "box","layout": "vertical","spacing": "md","action": {"type": "uri","uri": "http://line.me/ti/p/%40jnx0914l"},"contents": [{"type": "text","text": "♥️ มาขายของครับ ♥️","size": "md","color": "#000000"},{"type": "box","layout": "vertical","spacing": "sm","contents": [{"type": "box","layout": "baseline","contents": [{"type": "icon","url": "https://os.line.naver.jp/os/p/{}".format(to),"size": "5xl"},{"type": "text","text": "  ❣️ ชื่อ : ","weight": "bold","color": "#000000","margin": "sm","flex": 0},{"type": "text","text": Nama.displayName,"size": "sm","align": "end","color": "#000000"}]}]},{"type": "text","text": "_________________________________________________\n❣️ ขายไฟล์ Template\n❣️ ขายไฟล์ Kicker\n❣️ ขายไฟล์ JS","wrap": True,"color": "#000000","size": "xxs"}]},"footer": {"type": "box","layout": "vertical","contents": [{"type": "spacer","size": "sm"},{"type": "button","style": "primary","color": "#000000","action": {"type": "uri","label": "༺ ติดต่อคนขาย ༻","uri": "https://line.me/ti/p/"+maxbots.getUserTicket().id}}]}}}
                            maxbots.sendFlex(to, data)

                        elif teambotmax == "แทค":
                          if msg._from in admin or msg._from in owner:
                            try:group = maxbots.getGroup(to);midMembers = [contact.mid for contact in group.members]
                            except:group = maxbots.getRoom(to);midMembers = [contact.mid for contact in group.contacts]
                            midSelect = len(midMembers)//20
                            for mentionMembers in range(midSelect+1):
                                no = 0
                                ret_ = "╭───「 รายชื่อสมาชิก 」"
                                dataMid = []
                                if msg.toType == 2:
                                    for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                        dataMid.append(dataMention.mid)
                                        no += 1
                                        ret_ += "\n"+"├ • {}. @!".format(str(no))
                                    ret_ += "\n╰───「 ทั้งหมด {} สมาชิก 」".format(str(len(dataMid)))
                                    maxbots.sendReplyMention(msg_id, to, ret_, dataMid)
                                else:
                                    for dataMention in group.contacts[mentionMembers*20 : (mentionMembers+1)*20]:
                                        dataMid.append(dataMention.mid)
                                        no += 1
                                        ret_ += "\n"+"├ • {}. @!".format(str(no))
                                    ret_ += "\n╰───「 รวม {} สมาชิก 」".format(str(len(dataMid)))
                                    maxbots.sendReplyMention(msg_id, to, ret_, dataMid)

                        elif teambotmax == 'runtime' or teambotmax == 'ออน':
                          if msg._from in admin:
                            timeNow = time.time() - botStart
                            runtime = timeChange(timeNow)
                            run = ""
                            run += runtime
                            teambotmax1 = maxbots.getContact(maxbotsMid)
                            teambotmaxZ = {
                                    "type": "flex",
                                    "altText": "ƬΣΛM BӨƬ MΛX",
                                    "contents": {
  "type": "bubble",
  "size": "giga",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus),
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "5:7",
        "gravity": "top"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "✦ เวลาทำงานของบอท ✦",
                "size": "xl",
                "weight": "bold",
                "color": "#ffffff",
                "align": "center",
                "wrap": True
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(str(run)),
                "size": "md",
                "color": "#ffffff",
                "weight": "bold",
                "align": "center"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "filler"
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "icon",
                    "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                  },
                  {
                    "type": "text",
                    "text": "กดตรงนี้เพื่อเพิ่มเพื่อน",
                    "color": "#ffffff",
                    "flex": 0,
                    "offsetTop": "-2px"
                  },
                  {
                    "type": "icon",
                    "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "spacing": "sm"
              },
              {
                "type": "filler"
              }
            ],
            "borderWidth": "1px",
            "cornerRadius": "4px",
            "spacing": "sm",
            "borderColor": "#ffffff",
            "margin": "xxl",
            "height": "40px",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://line.me/ti/p/~" + maxbots.profile.userid
            }
          }
        ],
        "position": "absolute",
        "offsetBottom": "0px",
        "offsetStart": "0px",
        "offsetEnd": "0px",
        "backgroundColor": "#03303Acc",
        "paddingAll": "20px",
        "paddingTop": "18px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "NEW",
            "color": "#ffffff",
            "align": "center",
            "size": "xs",
            "offsetTop": "3px"
          }
        ],
        "position": "absolute",
        "cornerRadius": "20px",
        "offsetTop": "18px",
        "backgroundColor": "#ff334b",
        "offsetStart": "18px",
        "height": "25px",
        "width": "53px"
      }
    ],
    "paddingAll": "0px",
    "borderColor": "#000000",
    "borderWidth": "4px"
  }
}
}
                            maxbots.postTemplate(to, teambotmaxZ)

                        elif teambotmax == 'runtime2' or teambotmax == 'ออน2':
                          if msg._from in admin or msg._from in owner:
                            teambotmaxTm = time.time()
                            teambotmax_time = teambotmaxTm - botStart
                            teambotmax_time = format_timespan(teambotmax_time)
                            data={
                                 "type": "flex",
                                 "altText": "ƬΣΛM BӨƬ MΛX",
                                         "contents": { 
                               "type": "bubble",  
                               "size": "giga",
                               "direction": "ltr",   
                               "header": {
                                                    "type": "box",
                                                    "layout": "baseline",
                                                    "contents": [
                                                            {
                                                            "type": "text",
                                                            "text": "༺ ƬΣΛM BӨƬ MΛX ༻",
                                                              "align" : "center",
                                                            "weight": "bold",
                                                            "color": "#000000",
                                                            "size": "md"
                                                        }
                                                    ]
                                                },
                               "hero": {
                                 "type": "image",
                                 "url": "https://sv1.picz.in.th/images/2019/08/09/Zd7F7y.jpg",
                                 "size": "full",
                                   "aspectRatio": "1:1",
                                    "aspectMode": "cover",
                                    "action": {
                                         "type":"uri","uri":"http://line.me/ti/p/%40jnx0914l"
                                 }
                               },
                               "body": {
                               "type": "box",
                               "layout": "vertical",
                                 "contents": [
                                    {
                                    "type": "text",
                                    "text": "• Bot telah aktif selama",
                                    "weight": "bold",
                                    "align": "center",
                                    "size": "md",
                                    "color": "#000000",
                                    'flex': 1,
                                    },
                                    {
                                     "type": "text",
                                     "text": "\n{}".format(str(teambotmax_time)),
                                     "size": "md",
                                     "weight": "bold",
                                      "align": "center",
                                      "color": "#000000",
                                     "wrap": True,
                                     "flex": 1
                                   }
                                 ]
                               },
                               "footer": {
                                  "type": "box",
                                  "layout": "vertical",
                                  "contents": [
                                    {
                                      "type": "text",
                                      "text": "• Waktu " +datetime.today().strftime('%H:%M:%S')+ "™",
                                      "color": "#000000",
                                      "weight": "bold",
                                      "size": "md",
                                      "align": "center"
                                    }
                                  ]
                                },
                                "styles": {
                                  "header": {
                                    "backgroundColor": "#808080"
                                    },
                                    "hero": {
                                      "separator": True,
                                      "separatorColor": "#000000",
                                      "backgroundColor": "#808080"
                                    },
                                    "footer": {
                                      "backgroundColor": "#808080",
                                      "separator": True,
                                      "separatorColor": "#000000"
                                    },
                                    "body": {
                                     "backgroundColor": "#808080",
                                    }
                                  }
                                }
                              }
                            maxbots.postTemplate(to, data)

                        elif teambotmax == "runtime3" or teambotmax == 'ออน3':
                          if msg._from in admin:
                            try:
                                arr = []
                                bagas = "uc14c3d87a1123df7c8ffa9d7402e59a2"
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = timeChange(runtime)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                ret_ = "「 Bot Working Time 」"
                                ret_ += "\n• User : @!"
                                ret_ += "\n• Runtime : {}".format(str(runtime))
                                ret_ += "\n• Day : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                ret_ += "\n• Time : " + datetime.strftime(timeNow,'%H:%M:%S') + " Minutes"
                                ret_ += "\n• Creator : @!"
                                maxbots.sendReplyMention(msg_id, to, ret_, [maxbotsMid, bagas])
                            except Exception as error:
                                	maxbots.sendMessage(to, str(error))

                        elif teambotmax == "about":
                            if msg._from in admin or msg._from in owner:
                                groups = maxbots.getGroupIdsJoined()
                                contacts = maxbots.getAllContactIds()
                                blockeds = maxbots.getBlockedContactIds()
                                crt = "uc14c3d87a1123df7c8ffa9d7402e59a2"
                                supp = "uc14c3d87a1123df7c8ffa9d7402e59a2"
                                suplist = []
                                lists = []
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                timeNoww = time.time()
                                runtime = timeNoww - maxbotsStart
                                runtime = timeChange(runtime)
                                for i in range(len(day)):
                                   if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                   if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n│ Jam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                data = {
                                        "type": "flex",
                                        "altText": "ƬΣΛM BӨƬ MΛX",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#FF0000"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus),
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#F8F8FF"
          },
          {
            "url": "https://sv1.picz.in.th/images/2019/08/09/Zd7F7y.jpg",
           "type": "image"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#F8F8FF"
      },
      {
        "contents": [
          {
            "text": "「About Profile」",
            "size": "md",
            "align": "center",
            "color": "#F8F8FF",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#F8F8FF"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "url": "https://sv1.picz.in.th/images/2019/08/09/Zd7F7y.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": " • USER: {}".format(maxbots.getProfile().displayName),
                "size": "xs",
                "margin": "none",
                "color": "#F8F8FF",
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "type": "separator",
            "color": "#F8F8FF"
          },
          {
            "contents": [
              {
                "url": "https://sv1.picz.in.th/images/2019/08/09/Zd7F7y.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": " • RUNTIME : {}".format(str(runtime)),
                "size": "xs",
                "margin": "none",
                "color": "#F8F8FF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://sv1.picz.in.th/images/2019/08/09/Zd7F7y.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": " • GROUP: {}".format(str(len(groups))),
                "size": "xs",
                "margin": "none",
                "color": "#F8F8FF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://sv1.picz.in.th/images/2019/08/09/Zd7F7y.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": " • TEMAN : {}".format(str(len(contacts))),
                "size": "xs",
                "margin": "none",
                "color": "#F8F8FF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://sv1.picz.in.th/images/2019/08/09/Zd7F7y.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": " • TERBLOCK: {}".format(str(len(blockeds))),
                "size": "xs",
                "margin": "none",
                "color": "#F8F8FF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://sv1.picz.in.th/images/2019/08/09/Zd7F7y.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": " • VERSION : SB ONLY 2019",
                "size": "xs",
                "margin": "none",
                "color": "#F8F8FF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://sv1.picz.in.th/images/2019/08/09/Zd7F7y.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": " • TEAM : ＳＥＬＦＢＯＴＢＹＭＡＸ",
                "size": "xs",
                "margin": "none",
                "color": "#F8F8FF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": "「CHAT CREATOR」",
                "size": "sm",
                "action": {
                  "uri": "http://line.me/ti/p/%40jnx0914l",
                  "type": "uri",
                  "label": "ADD CREATOR"
                },
                "margin": "xl",
                "align": "center",
                "color": "#FFFFFF",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": "「ORDER PERSON」",
                "size": "sm",
                "action": {
                  "uri": "line://app/1623679774-k9nBDB6b?type=text&text=order",
                  "type": "uri",
                  "label": " 「CONTACT ORDER」"
                },
                "margin": "xl",
                "align": "center",
                "color": "#F5F5DC",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "layout": "vertical"
  }
}
}
                                maxbots.postTemplate(to, data)
   
                        elif teambotmax.startswith("แปรงคท "):
                          if msg._from in admin or msg._from in owner:
                              delcmd = msg.text.split(" ")
                              teambotmaxZ = msg.text.replace(delcmd[0] + " ","")
                              maxbots.sendContact(msg.to,str(teambotmaxZ))

                        elif text.lower() == 'เทส':
                          if msg._from in admin or msg._from in owner:
                            teambotmaxZ = {
                                    "type": "flex",
                                    "altText": "ƬΣΛM BӨƬ MΛX",
                                    "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "TEAM BOT MAX",
            "color": "#ffffff",
            "align": "center",
            "size": "xs",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "10%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "10%",
                "backgroundColor": "#000000",
                "height": "6px"
              }
            ],
            "backgroundColor": "#FAD2A76E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": "#FF9E00",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "10",
                "color": "#000000",
                "wrap": True,
                "size": "4xl",
                "align": "center"
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": False
        }
      }
    },
    {
      "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "TEAM BOT MAX",
            "color": "#ffffff",
            "align": "center",
            "size": "sm",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "20%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "20%",
                "backgroundColor": "#000000",
                "height": "6px"
              }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": "#006CFF",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "20",
                "color": "#000000",
                "wrap": True,
                "size": "4xl",
                "align": "center"
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": False
        }
      }
    },
    {
      "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "TEAM BOT MAX",
            "color": "#ffffff",
            "align": "center",
            "size": "sm",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "30%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "30%",
                "backgroundColor": "#000000",
                "height": "6px"
              }
            ],
            "backgroundColor": "#FAD2A76E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": "#FF6B6E",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "30",
                "color": "#000000",
                "wrap": True,
                "size": "4xl",
                "align": "center"
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": False
        }
      }
    },
    {
      "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "TEAM BOT MAX",
            "color": "#ffffff",
            "align": "center",
            "size": "sm",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "40%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "40%",
                "backgroundColor": "#000000",
                "height": "6px"
              }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": "#00A3FF",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "40",
                "color": "#000000",
                "wrap": True,
                "size": "4xl",
                "align": "center"
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": False
        }
      }
    },
    {
      "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "TEAM BOT MAX",
            "color": "#ffffff",
            "align": "center",
            "size": "sm",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "50%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "50%",
                "backgroundColor": "#000000",
                "height": "6px"
              }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": "#D662FF",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "50",
                "color": "#000000",
                "wrap": True,
                "size": "4xl",
                "align": "center"
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": False
        }
      }
    },
    {
      "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "TEAM BOT MAX",
            "color": "#ffffff",
            "align": "center",
            "size": "sm",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "60%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "60%",
                "backgroundColor": "#000000",
                "height": "6px"
              }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": "#6266FF",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "60",
                "color": "#000000",
                "wrap": True,
                "size": "4xl",
                "align": "center"
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": False
        }
      }
    },
    {
      "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "TEAM BOT MAX",
            "color": "#ffffff",
            "align": "center",
            "size": "sm",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "70%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "70%",
                "backgroundColor": "#000000",
                "height": "6px"
              }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": "#27ACB2",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "70",
                "color": "#000000",
                "wrap": True,
                "size": "4xl",
                "align": "center"
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": False
        }
      }
    },
    {
      "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "TEAM BOT MAX",
            "color": "#ffffff",
            "align": "center",
            "size": "sm",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "80%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "80%",
                "backgroundColor": "#000000",
                "height": "6px"
              }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": "#FF628E",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "80",
                "color": "#000000",
                "wrap": True,
                "size": "4xl",
                "align": "center"
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": False
        }
      }
    },
    {
      "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "TEAM BOT MAX",
            "color": "#ffffff",
            "align": "center",
            "size": "sm",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "90%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "90%",
                "backgroundColor": "#000000",
                "height": "6px"
              }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": "#AE44FF",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "90",
                "color": "#000000",
                "wrap": True,
                "size": "4xl",
                "align": "center"
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": False
        }
      }
    },
    {
      "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "TEAM BOT MAX",
            "color": "#ffffff",
            "align": "center",
            "size": "sm",
            "gravity": "center"
          },
          {
            "type": "text",
            "text": "100%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "width": "100%",
                "backgroundColor": "#000000",
                "height": "6px"
              }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
          }
        ],
        "backgroundColor": "#E70050",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "100",
                "color": "#000000",
                "wrap": True,
                "size": "4xl",
                "align": "center"
              }
            ],
            "flex": 1
          }
        ],
        "spacing": "md",
        "paddingAll": "12px"
      },
      "styles": {
        "footer": {
          "separator": False
        }
      }
    }
  ]
}
}
                            maxbots.postTemplate(to, teambotmaxZ)

                        elif teambotmax.startswith("unsend "):
                          if msg._from in admin or msg._from in owner:
                            args = teambotmax.replace("unsend ","")
                            mes = 0
                            try:
                                mes = int(args[1])
                            except:
                                mes = 1
                            M = maxbots.getRecentMessagesV2(to, 101)
                            MId = []
                            for ind,i in enumerate(M):
                                if ind == 0:
                                    pass
                                else:
                                    if i._from == maxbots.profile.mid:
                                        MId.append(i.id)
                                        if len(MId) == mes:
                                            break
                            def unsMes(id):
                                maxbots.unsendMessage(id)
                            for i in MId:
                                thread1 = threading.Thread(target=unsMes, args=(i,))
                                thread1.start()
                                thread1.join()
                            maxbots.unsendMessage(msg_id)

                        elif teambotmax == "log out":
                          if msg._from in admin or msg._from in owner:
                            maxbots.generateReplyMessage(msg.id)
                            maxbots.sendReplyMessage(msg.id, to, "ออกจากระบบแล้ว ♪")
                            sys.exit("#============= BOT SHUTDOWN =============")

                        elif teambotmax.startswith("fbc: "):
                          if msg._from in admin or msg._from in owner:
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            contacts = maxbots.getAllContactIds()
                            for contact in contacts:
                                maxbots.sendMessage(contact, "{}".format(str(txt)))
                            maxbots.sendMessage(to, "Bₑᵣₕₐₛᵢₗ bᵣₒₐdcₐₛₜ ₖₑ {} ₜₑₘₐₙ".format(str(len(contacts))))

                        elif teambotmax.startswith("gbc: "):
                          if msg._from in admin or msg._from in owner:
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            groups = maxbots.getGroupIdsJoined()
                            for group in groups:
                                maxbots.sendMessage(group, "{}".format(str(txt)))
                            maxbots.sendMessage(to, "Bₑᵣₕₐₛᵢₗ bᵣₒₐdcₐₛₜ ₖₑ {} gᵣₒᵤₚ".format(str(len(groups))))

                        elif teambotmax == "บอท":
                          if msg._from in admin or msg._from in owner:
                            teambotmaxZ = {
                                    "type": "flex",
                                    "altText": "ƬΣΛM BӨƬ MΛX",
                                    "contents": {
  "type": "bubble",
  "size": "giga",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://os.line.naver.jp/os/p/{}".format("uc14c3d87a1123df7c8ffa9d7402e59a2"),
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:1",
        "gravity": "top"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "NEW",
            "color": "#ffffff",
            "align": "center",
            "size": "xs",
            "offsetTop": "3px"
          }
        ],
        "position": "absolute",
        "cornerRadius": "20px",
        "offsetTop": "18px",
        "backgroundColor": "#ff334b",
        "offsetStart": "18px",
        "height": "25px",
        "width": "53px"
      }
    ],
    "paddingAll": "0px",
    "borderColor": "#000000",
    "borderWidth": "4px",
    "cornerRadius": "4px"
  }
}
}
                            maxbots.postTemplate(to, teambotmaxZ)

                        elif teambotmax.startswith(".ประกาศทั้งหมด"):
                          if msg._from in admin:
                            tod = text.split(" ")
                            hey = text.replace(tod[0] + " ", "")
                            text = "{}".format(hey)
                            groups = maxbots.getGroupIdsJoined()
                            friends = maxbots.getAllContactIds()
                            for gr in groups:
                                data = {
                                    "type": "text",
                                    "text": "{}".format(text),
                                    "sentBy": {
                                        "label": "ƬΣΛM BӨƬ MΛX",
                                        "iconUrl": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus),
                                        "linkUrl": "https://line.me/ti/p/~" + maxbots.profile.userid
                                    }
                                }
                                bcTemplate(gr, data)
                                time.sleep(1)
                            maxbots.sendMessage(to, "• ส่งข้อความถึงกลุ่ม {} กลุ่ม ".format(str(len(groups))))
                            for gr in friends:
                                data = {
                                    "type": "text",
                                    "text": "{}".format(text),
                                    "sentBy": {
                                        "label": "ƬΣΛM BӨƬ MΛX",
                                        "iconUrl": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus),
                                        "linkUrl": "https://line.me/ti/p/~" + maxbots.profile.userid
                                    }
                                }
                                bcTemplate(gr, data)
                                time.sleep(1)
                            maxbots.sendMessage(to, "• ส่งข้อความถึงเพื่อน {} คน ".format(str(len(friends))))

                        elif teambotmax.startswith(".ประกาศกลุ่ม "):
                          if msg._from in admin or msg._from in owner:
                            teambotmax69 = text.split(" ")
                            teambotmaxZ = text.replace(teambotmax69[0] + " ", "")
                            maxZ = "{}".format(teambotmaxZ)
                            groups = maxbots.getGroupIdsJoined()
                            teambotmaxX = maxbots.getContact(maxbotsMid)
                            sender_profile = maxbots.getContact(sender)
                            teambotmax69 = maxbots.getProfileCoverURL(maxbots.profile.mid)
                            maxbots.reissueUserTicket()
                            warna1 = ("#FFFFFF","#FFFF00")
                            warnanya1 = random.choice(warna1)
                            for gr in groups:
                                teambotmaxZ = {
                                        "type": "flex",
                                        "altText": "ƬΣΛM BӨƬ MΛX",
                                        "contents": {
                              "styles": {
                                "body": {
                                  "backgroundColor": "#000000",
                                  "separator":True,
                                  "separatorColor":"#FF0000"
                                },
                                "footer": {
                                  "backgroundColor": "#000000",
                                  "separator":True,
                                  "separatorColor":"#FF0000"
                                }
                              },
                              "type": "bubble",
                              "body": {
                                "contents": [
                                  {
                                    "contents": [          
                                      {
                                        "type": "image",            
                                        "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus),
                                        "size": "full",
                                        "action": {
                                          "uri": "http://line.me/ti/p/%40jnx0914l",
                                          "type": "uri"
                                         },
                                      }
                                    ],
                                    "type": "box",
                                    "spacing": "md",
                                    "layout": "horizontal"
                                  },
                                  {
                                    "type": "separator",
                                    "color": "#FF0000"
                                   },
                                   {
                                    "contents": [
                                      {
                                        "contents": [
                                          {
                                            "text": "{}".format(str(maxZ)),
                                            "size": "sm",
                                            "margin": "none",
                                            "color": warnanya1,
                                            "wrap": True,
                                            "weight": "regular",
                                            "type": "text"
                                          }
                                        ],
                                        "type": "box",
                                        "layout": "baseline"
                                      }
                                    ],
                                    "type": "box",
                                    "layout": "vertical"
                                  }
                                ],
                                "type": "box",
                                "spacing": "md",
                                "layout": "vertical"
                              },
                              "footer": {
                                  "type": "box",
                                  "layout": "vertical",
                                  "contents": [{
                                      "type": "box",
                                      "layout": "horizontal",
                                      "flex": 2,
                                      "contents": [{
                                          "type": "button",
                                          "style": "secondary",
                                          "color": "#FF0000",
                                          "height": "sm",
                                          "action": {
                                            "uri": "https://line.me/ti/p/~" + maxbots.profile.userid,                                            
                                            "label": "✦ กดเพิ่มเพื่อนติดต่อ ✦",
                                            "type": "uri",
                                          }
                                      }]
                                  }]
                              }
                            }
                            }
                                bcTemplate(gr, teambotmaxZ)
                                time.sleep(1)
                                print ("ประกาศกลุ่มเรียบร้อย")

                        elif teambotmax.startswith("ประกาศกลุ่ม1 "):
                          if msg._from in admin or msg._from in owner:
                            teambotmax69 = text.split(" ")
                            teambotmaxZ = text.replace(teambotmax69[0] + " ", "")
                            maxZ = "{}".format(teambotmaxZ)
                            groups = maxbots.getGroupIdsJoined()
                            teambotmaxX = maxbots.getContact(maxbotsMid)
                            sender_profile = maxbots.getContact(sender)
                            teambotmax69 = maxbots.getProfileCoverURL(maxbots.profile.mid)
                            maxbots.reissueUserTicket()
                            for gr in groups:
                                teambotmaxZ={
                         "type": "flex",
                         "altText": "ƬΣΛM BӨƬ MΛX",
                                 "contents": { 
                       "type": "bubble",     
                       "header": {
                         "type": "box",
                         "layout": "vertical",   
                         "contents": [
                           {     
                             "type": "text",
                             "text": "༺ ข้อความประกาศกลุ่ม ༻",
                             "color": "#000000",
                             "align": "center"
                           }
                         ]
                       },
                       "hero": {
                         "type": "image",
                         "url": "https://os.line.naver.jp/os/p/{}".format(maxbotsMid),
                         "size": "full",
                         "aspectRatio": "1:1",
                         "action": {
                                 "type":"uri","uri":"https://line.me/ti/p/~" + maxbots.profile.userid
                         },
                       },
                       "body": {
                         "type": "box",
                         "layout": "vertical",
                         "contents": [
                           {
                             "type": "text",
                             "text": "{}".format(maxZ),
                              "align": "center",
                             "size": "lg",
                             "color": "#000000",
                             "wrap": True,
                             "flex": 1
                           }
                         ]
                       },
                       "footer": {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "text",
                              "text": "༺ ติดต่อคนประกาศ ༻",
                              "color": "#000000",
                              "size": "xs",
                              "align": "center"
                            }
                          ]
                        },
                        "styles": {
                          "header": {
                            "backgroundColor": "#808080",
                            "separator": True,
                            "separatorColor": "#000000"
                            },
                            "hero": {
                              "separator": True,
                              "separatorColor": "#000000",
                            },
                            "footer": {
                              "backgroundColor": "#808080",
                              "separator": True,
                              "separatorColor": "#000000"
                            },
                            "body": {
                             "backgroundColor": "#808080",
                            }
                          }
                        }
                      }
                                bcTemplate(gr, teambotmaxZ)
                                time.sleep(1)
                                print ("ประกาศกลุ่มเรียบร้อย")

                        elif teambotmax.startswith("ประกาศกลุ่ม2 "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               groups = maxbots.getGroupIdsJoined()
                               maxbots.reissueUserTicket()
                               for group in groups:
                                   teambotmaxZ = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(sender).pictureStatus),
        "action": {
          "uri": "https://line.me/ti/p/~" + maxbots.profile.userid,
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#808080"
        },
        "footer": {
          "backgroundColor": "#808080"
        },
        "header": {
          "backgroundColor": "#808080"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": pesan,
                    "color": "#000000",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "size": "lg",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "༺ สนใจกดตรงนี้ ༻",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#000000",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~" + maxbots.profile.userid
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "༺ ข้อความประกาศกลุ่ม ༻",
            "size": "lg",
            "wrap": True,
            "weight": "bold",
            "color": "#000000",
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                   maxbots.postFlex(group, teambotmaxZ)
                                   time.sleep(1)
                                   print ("ประกาศกลุ่มเรียบร้อย")

                        elif teambotmax.startswith("ประกาศกลุ่ม3 "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = maxbots.getGroupIdsJoined()
                               for group in saya:
                                   teambotmaxZ = {
  "contents": [
    {
      "hero": {
       "aspectMode": "cover",
       "aspectRatio": "6:9",
       "type": "image",
       "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(sender).pictureStatus),
       "size": "full",
       "align": "center",
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": pesan,
                    "size": "xs",
                    "margin": "none",
                    "color": "#FFFFFF",
                    "wrap": True,
                    "weight": "regular",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [          
          {
            "text": "{}".format(maxbots.getProfile().displayName),
            "size": "md",
            "margin": "none",
            "color": "#FF0000",
            "weight": "bold",
            "type": "text"           
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                   maxbots.postFlex(group, teambotmaxZ)
                                   time.sleep(1)
                                   print ("ประกาศกลุ่มเรียบร้อย")
    
                        elif teambotmax.startswith("ประกาศกลุ่ม4 "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = maxbots.getGroupIdsJoined()
                               for group in saya:
                                   teambotmaxZ = {
  "contents": [
    {
      "hero": {
       "aspectMode": "cover",
       "aspectRatio": "3:1",
       "type": "image",
       "url": "https://i.imgur.com/NBb34Zp.jpg",
       "size": "full",
       "align": "center",
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": pesan,
                    "size": "xs",
                    "margin": "none",
                    "color": "#FFFFFF",
                    "wrap": True,
                    "weight": "regular",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [          
          {
            "text": "{}".format(maxbots.getProfile().displayName),
            "size": "md",
            "margin": "none",
            "color": "#FF0000",
            "weight": "bold",
            "type": "text"           
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                   maxbots.postFlex(group, teambotmaxZ)
                                   time.sleep(1)
                                   print ("ประกาศกลุ่มเรียบร้อย")
    
                        elif teambotmax.startswith("ประกาศกลุ่ม5 "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = maxbots.getGroupIdsJoined()
                               for group in saya:
                                   teambotmaxZ = {
  "contents": [
    {
      "hero": {
       "aspectMode": "cover",
       "aspectRatio": "3:1",
       "type": "image",
       "url": "https://media.giphy.com/media/YlXt2dP9tYOXbRho3s/giphy.gif",
       "size": "full",
       "align": "center",
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": pesan,
                    "size": "xs",
                    "margin": "none",
                    "color": "#FFFFFF",
                    "wrap": True,
                    "weight": "regular",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [          
          {
            "text": "{}".format(maxbots.getProfile().displayName),
            "size": "md",
            "margin": "none",
            "color": "#FF0000",
            "weight": "bold",
            "type": "text"           
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                   maxbots.postFlex(group, teambotmaxZ)
                                   time.sleep(1)
                                   print ("ประกาศกลุ่มเรียบร้อย")

                        elif teambotmax.startswith("ประกาศกลุ่ม6 "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = maxbots.getGroupIdsJoined()
                               maxbots.reissueUserTicket()
                               for group in saya:
                                teambotmaxZ = {
    "contents": [
    {
     "hero": {
       "type": "image",
    "aspectRatio": "1:1",
    "aspectMode": "cover",
    "url": "https://os.line.naver.jp/os/p/{}".format(maxbotsMid),
    "size": "full",
    "margin": "xs"
      },
      "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#000000"
      },
      "header": {
       "backgroundColor": "#000000"
    }
  },  
  "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                  "type": "text",
                    "text": pesan,
                    "size": "xs",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
            },
          {
            "type": "separator",
            "color": "#ffffff"
          },
          {
            "contents": [
               {
                "contents": [
                  {
                  "type": "text",
                    "text": "ᴊᴀᴍ: {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))),
                    "size": "xs",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#000000"
          },
          {
            "contents": [
            {
           "type": "image",
            "url": "https://4.bp.blogspot.com/-E7DFmEtCcO0/Vx3frfw4zII/AAAAAAAAAEU/V4oUfhvK7_soc1dPxg60TQH9QmAed9m6gCLcB/s1600/line.png", #https://shop.hiushoes.com/wp-content/uploads/2017/07/logo-Line.png", #https://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/%40jnx0914l",
            },         
            "flex": 1
          },
          {
            "type": "separator",
            "color": "#ff0000"
          },
          {
          "type": "image",
            "url": "https://jualsaladbuahenakdisurabaya.files.wordpress.com/2017/06/icon-wa.jpg", #https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRG8U5UNSW8lOIhkY4AfRisxxpQKlMC1WrgIKSQYCxY6cXiVAJw", #https://s18955.pcdn.co/wp-content/uploads/2017/05/WhatsApp.png", #watshap
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://wa.me/",   
           }, 
            "flex": 1
           },
          {
            "type": "separator",
            "color": "#ff0000"
          },
          {
            "type": "image",
            "url": "https://2.bp.blogspot.com/-1GRWlQBGf9I/WIRQXiXVelI/AAAAAAAAAIM/cp2h8QQYXKQOFv9hNkwC5eOogcYPxezrwCLcB/s320/sms-icon.png", #https://images-eu.ssl-images-amazon.com/images/I/41iKHNX1WbL.png", #chat
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/chat"
          },
            "flex": 1
            },
          {
            "type": "separator",
            "color": "#ff0000"
          },
          {
          "type": "image",
            "url": "https://cdn2.iconfinder.com/data/icons/contact-flat-buttons/512/dial-512.png", #https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcReFldAe2KbdzYP-InVc5OzA22dW2Bi2J6cffUYdBNAy92SPWSB", #https://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
              "uri": "line://call/contacts"            
            },
            "flex": 1
           },
          {
            "type": "separator",
            "color": "#ff0000"
            },
            {
           "type": "image",
            "url": "https://is1-ssl.mzstatic.com/image/thumb/Purple118/v4/b2/5a/72/b25a72fe-2ff6-015b-436a-eff66a6d0161/AppIcon-CCCP-1x_U007emarketing-85-220-9.png/1200x630bb.jpg",
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },
            "flex": 1
         }
            ],
         "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"#0000"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
        }, #batas
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
           "type": "text",
            "text": "✴️ʙʀᴏᴀᴅᴄʜᴀsᴛ✴️",
            "size": "md",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"        
          }
        ]
      }
    }
  ],
  "type": "carousel"
} 
                                maxbots.postFlex(group, teambotmaxZ)
                                time.sleep(1)
                                print ("ประกาศกลุ่มเรียบร้อย")

                        elif teambotmax.startswith("ประกาศกลุ่ม7 "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               groups = maxbots.getGroupIdsJoined()
                               maxbots.reissueUserTicket()
                               for group in groups:
                                   warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                                   warnanya1 = random.choice(warna1)
                                   teambotmaxZ = {
                                "type": "flex",
                                "altText": "คุณส่งวิดีโอ",
                                "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000080"
    },
    "footer": {
      "backgroundColor": "#000080"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "text": "• ɴᴀᴍᴀ : {}".format(maxbotsProfile.displayName)+"\n• ᴄʀᴇᴀᴛᴏʀ : _\n• ᴍᴇᴍʙᴇʀ : _\n• ᴊᴜᴍʟᴀʜ : _",
            "size": "sm",
            "color": "#FF3366",
            "wrap": True,
            "type": "text",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus),
            "type": "image",
            "size": "full"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },
      {
        "contents": [
          {
            "contents": [            
              {
                "size": "xxl",
                "type": "icon",
                "url": "https://sv1.picz.in.th/images/2019/08/09/Zd7F7y.jpg",
              },
              {
                "text": str(pesan),
                "size": "sm",
                "margin": "none",
                "color": "#00FF00",
                "wrap": True,
                "weight": "regular",
                "type": "text",
                "align": "center"            
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "flex": 2,
          "contents": [{
              "type": "button",
              "style": "secondary",
              "color": "#00FF00",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "༺ สนใจติดต่อ ༻",
                  "uri": "https://line.me/ti/p/~" + maxbots.profile.userid
              }
          }]
      }]
  }
}
}
                                   maxbots.sendFlex(group, teambotmaxZ)
                                   time.sleep(1)
                                   print ("ประกาศกลุ่มเรียบร้อย")

                        elif teambotmax.startswith("ประกาศกลุ่ม8 "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               txt = text.replace(sep[0] + " ","")
                               groups = maxbots.getGroupIdsJoined()
                               for group in groups:
                                   warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                                   warnanya1 = random.choice(warna1)
                                   teambotmaxZ = {
            "type": "flex",
            "altText": "{} Menghapus anda dari grup ".format(maxbotsProfile.displayName),
            "contents": {
             "type": "bubble",
             "styles": {
               "header": {
                 "backgroundColor": "#000000",
               },
               "body": {
                 "backgroundColor": "#000000",
                 "separator": True,
                 "separatorColor": "#ffffff"
               },
               "footer": {
                 "backgroundColor": "#000000",
                 "separator": True
               }
             },
             "header": {
               "type": "box",
               "layout": "horizontal",
               "contents": [
                 {
                   "type": "text",
                   "text": "ＳＥＬＦＢＯＴＢＹＭＡＸ",
                   "weight": "bold",
                   "color": warnanya1,
                   "size": "md"
                 }
               ]
             },
             "hero": {
               "type": "image",
               "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus),
               "size": "full",
               "aspectRatio": "1:1",
               "aspectMode": "cover",
               "action": {
                 "type": "uri",
                 "uri": "http://line.me/ti/p/%40jnx0914l"
                 }
               },
                   "type": "bubble",
                   "body": {
                       "type": "box",
                       "layout": "horizontal",
                       "contents": [
                           {
                               "type": "text",
                               "text": str(txt),
                               "wrap": True,
                               "color": warnanya1,
                               "align": "center"
                           }
                       ]
                   },
                   "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [{
                        "type": "button",
                        "style": "primary",
                        "color": warnanya1,
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "ADD MY LINE",
                            "uri": "https://line.me/ti/p/~" + maxbots.profile.userid
                            }													
                        },
                    {
                        "type": "spacer",
                        "size": "sm",
                    }],
                    "flex": 0
                }
            }
        }
                                   maxbots.sendFlex(group, teambotmaxZ)
                                   time.sleep(1)
                                   print ("ประกาศกลุ่มเรียบร้อย")

                        elif teambotmax.startswith("ประกาศกลุ่ม9 "):
                          if msg._from in admin or msg._from in owner:
                            teambotmax69 = text.split(" ")
                            teambotmaxZ = text.replace(teambotmax69[0] + " ", "")
                            maxZ = "{}".format(teambotmaxZ)
                            groups = maxbots.getGroupIdsJoined()
                            teambotmaxX = maxbots.getContact(maxbotsMid)
                            sender_profile = maxbots.getContact(sender)
                            teambotmax69 = maxbots.getProfileCoverURL(maxbots.profile.mid)
                            maxbots.reissueUserTicket()
                            for gr in groups:
                                teambotmaxZ = {
                                                            "type": "flex",
                                                            "altText": "คุณส่งวิดีโอ",
                                                            "contents": {
                              "type": "bubble",
                              "body": {
                                "type": "box",
                                "layout": "horizontal",
                                "spacing": "md",
                                "contents": [
                                  {
                                    "type": "box",
                                    "layout": "vertical",
                                    "flex": 2,
                                    "contents": [
                                      {
                                        "type": "text",
                                        "text": maxZ,
                                        "size": "md",
                                        "weight": "bold",
                                        "wrap": True,
                                        "color": "#FFFFFF",
                                        "align": "center"
                                      },
                                    ]
                                  }
                                ]
                              },
                              "styles": {
                                "body": {
                                  "backgroundColor": "#000000"
                                },
                                "footer": {
                                  "backgroundColor": "#000000"
                                },
                                "header": {
                                  "backgroundColor": "#FF0000"
                                }
                              },  
                              "hero": {
                                "type": "image",
                                "aspectRatio": "1:1",
                                "aspectMode": "cover",
                                "url": "https://os.line.naver.jp/os/p/{}".format(maxbotsMid),
                                "size": "full",
                                "margin": "xl"
                              },
                              "footer": {
                                  "type": "box",
                                  "layout": "vertical",
                                  "contents": [{
                                      "type": "box",
                                      "layout": "horizontal",
                                      "contents": [{
                                          "type": "button",
                                          "flex": 2,
                                          "style": "primary",
                                          "color": "#006400",
                                          "height": "sm",
                                          "action": {
                                              "type": "uri",
                                              "label": "ติดต่อ",
                                              "uri": "https://line.me/ti/p/~" + maxbots.profile.userid
                                          }
                                      }, {
                                          "flex": 3,
                                          "type": "button",
                                          "style": "primary",
                                          "color": "#800000",
                                          "margin": "sm",
                                          "height": "sm",
                                          "action": {
                                              "type": "uri",
                                              "label": "แอดมิน",
                                              "uri": "http://line.me/ti/p/%40jnx0914l"
                                          }
                                      }]
                                  }]
                              }
                            }
                            }
                                bcTemplate(gr, teambotmaxZ)
                                time.sleep(1)
                                print ("ประกาศกลุ่มเรียบร้อย")

                        elif teambotmax.startswith("ประกาศกลุ่ม10 "):
                          if msg._from in admin or msg._from in owner:
                            txt = removeCmd("ประกาศ", text)
                            groups = maxbots.getGroupIdsJoined()
                            url = 'https://nekos.life/api/v2/img/ngif'
                            text1 = requests.get(url).text
                            image = json.loads(text1)['url']
                            for group in groups:
                                sa = "{}".format(str(txt))
                                teambotmaxZ = {
"type":"flex",
"altText":"คุณส่งวิดีโอ",
"contents":{
"type": "carousel",
"contents": [
{
"type": "bubble",
"styles": {
"header": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FF0000"},
"body": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FF0000"},
"footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FF0000"}
},
"header": {
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": "༺ ข้อความประกาศกลุ่ม ༻",
"align": "center",
"size": "lg",
"weight": "bold",
"color": "#FFFFFF",
"wrap": True
}
]
},
"type": "bubble",
"body": {
"contents": [
{
"contents": [
{
"url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus),
"type": "image"
},
{
"type": "separator",
"color": "#FF0000"
},
{
"url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus),
"type": "image"
}
],
"type": "box",
"spacing": "md",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#FF0000"
},
{
"contents": [
{
"text": sa,
"size": "md",
"align": "center",
"color": "#FFFFFF",
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
{
"type": "separator",
"color": "#FF0000"
},
{
"contents": [
{
"contents": [
{
"type": "text",
"text": sa,
"align": "center",
"size": "xs",
"weight": "bold",
"color": "#FFFFFF",
"wrap": True
}
],
"type": "box",
"layout": "baseline"
},
{
"contents": [
{
"url": "https://sv1.picz.in.th/images/2019/08/09/Zd7F7y.jpg",
"type": "icon",
"size": "md"
},
{
"text": "  • ติดต่อได้ที่คนประกาศ\n  • {}".format(maxbots.getProfile().displayName),
"size": "xs",
"margin": "none",
"color": "#FFFFFF",
"wrap": True,
"weight": "regular",
"type": "text"
}
],
"type": "box",
"layout": "baseline"
}
],
"type": "box",
"layout": "vertical"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
"footer": {
"type": "box",
"layout": "horizontal",
"spacing": "sm",
"contents": [
{
"type": "button",
"flex": 2,
"style": "primary",
"color": "#006400",
"height": "sm",
"action": {
"type": "uri",
"label": "ติดต่อ",
"uri": "https://line.me/ti/p/~" + maxbots.profile.userid,
}
},
{
"flex": 3,
"type": "button",
"style": "primary",
"color": "#800000",
"margin": "sm",
"height": "sm",
"action": {
"type": "uri",
"label": "แอดมิน",
"uri": "http://line.me/ti/p/%40jnx0914l",
}
}
]
}
}
]
}
}
                                bcTemplate(group, teambotmaxZ)
                                time.sleep(1)
                                print ("ประกาศกลุ่มเรียบร้อย")

                        elif teambotmax.startswith("ประกาศกลุ่ม11 "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = maxbots.getGroupIdsJoined()
                               for group in saya:
                                   data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg",
        "action": {
          "uri": "http://line.me/ti/p/%40jnx0914l",
          "type": "uri"
        },
        "type": "image",
        "aspectRatio": "1:1",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#0000FF"
        },
        "header": {
          "backgroundColor": "#0000FF"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": pesan,
                    "color": "#FF0000",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "size": "lg",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [{
              "type": "box",
              "layout": "horizontal",
              "contents": [{
                  "type": "button",
                  "flex": 2,
                  "style": "primary",
                  "color": "#FF0000",
                  "height": "sm",
                  "action": {
                      "type": "uri",
                      "label": "ᴏʀᴅᴇʀᴀɴ",
                      "uri": "line://app/1603968955-ORWb9RdY/?type=text&text=order"
                  }
              }, {
                  "flex": 3,
                  "type": "button",
                  "style": "primary",
                  "color": "#800080",
                  "margin": "sm",
                  "height": "sm",
                  "action": {
                      "type": "uri",
                      "label": "ᴄʀᴇᴀᴛᴏʀ",
                      "uri": "http://line.me/ti/p/%40jnx0914l"
                  }
              }]
          }]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "🎉ʙʀᴏᴀᴅᴄᴀsʜ🎉",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                   maxbots.postFlex(group, data)
                                   time.sleep(1)
                                   print ("ประกาศกลุ่มเรียบร้อย")

                        elif teambotmax.startswith("ประกาศกลุ่ม12 "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = maxbots.getGroupIdsJoined()
                               for group in saya:
                                   data = {
                                           "type": "flex",
                                           "altText": "BROADCASH EAGLE DARURAT",
                                           "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": pesan,
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#7FFFD4",
            "align": "center"            
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#0000FF"
    },
    "header": {
      "backgroundColor": "#0000FF"
    }
  },  
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#FF0000",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ᴏʀᴅᴇʀᴀɴ",
                  "uri": "line://app/1603968955-ORWb9RdY/?type=text&text=order"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#800080",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ᴄʀᴇᴀᴛᴏʀ",
                  "uri": "http://line.me/ti/p/%40jnx0914l"
              }
          }]
      }]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "🎉ʙʀᴏᴀᴅᴄᴀsʜ🎉",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFFFFF",
        "align": "center"            
      }
    ]
  }
}
}
                                   maxbots.postTemplate(group, data)
                                   time.sleep(1)
                                   print ("ประกาศกลุ่มเรียบร้อย")

                        elif teambotmax.startswith("ประกาศกลุ่ม13 "):
                            if msg._from in admin:
                               saya = maxbots.getGroupIdsJoined()
                               for group in saya:
                                   data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg",
        "action": {
          "uri": "http://line.me/ti/p/%40jnx0914l",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#0000FF"
        },
        "header": {
          "backgroundColor": "#0000FF"
        }
      },
      "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [{
              "type": "box",
              "layout": "horizontal",
              "contents": [{
                  "type": "button",
                  "flex": 2,
                  "style": "primary",
                  "color": "#FF0000",
                  "height": "sm",
                  "action": {
                      "type": "uri",
                      "label": "ᴏʀᴅᴇʀᴀɴ",
                      "uri": "line://app/1603968955-ORWb9RdY/?type=text&text=order"
                  }
              }, {
                  "flex": 3,
                  "type": "button",
                  "style": "primary",
                  "color": "#800080",
                  "margin": "sm",
                  "height": "sm",
                  "action": {
                      "type": "uri",
                      "label": "ᴄʀᴇᴀᴛᴏʀ",
                      "uri": "http://line.me/ti/p/%40jnx0914l"
                  }
              }]
          }]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "🎉ʙʀᴏᴀᴅᴄᴀsʜ🎉",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                   maxbots.postFlex(group, data)
                                   time.sleep(1)
                                   print ("ประกาศกลุ่มเรียบร้อย")

                        elif teambotmax == "super menu":
                          if msg._from in admin:
                                data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg",
        "action": {
          "uri": "http://line.me/ti/p/%40jnx0914l",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#0000FF"
        },
        "header": {
          "backgroundColor": "#0000FF"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#00FF00",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Musik Joox",
                   "uri": "line://app/1623679774-z6dOvOV9"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg",
        "action": {
          "uri": "http://line.me/ti/p/%40jnx0914l",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#0000FF"
        },
        "header": {
          "backgroundColor": "#0000FF"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#00FF00",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Sound Clouds",
                   "uri": "line://app/1623679774-lGOq9q3G"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg",
        "action": {
          "uri": "http://line.me/ti/p/%40jnx0914l",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#0000FF"
        },
        "header": {
          "backgroundColor": "#0000FF"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#00FF00",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Smulle ID",
                   "uri": "line://app/1623679774-qmmXPXJ5"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg",
        "action": {
          "uri": "http://line.me/ti/p/%40jnx0914l",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#0000FF"
        },
        "header": {
          "backgroundColor": "#0000FF"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#00FF00",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Google",
                   "uri": "line://app/1623679774-3vDKkKaP"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg",
        "action": {
          "uri": "http://line.me/ti/p/%40jnx0914l",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#0000FF"
        },
        "header": {
          "backgroundColor": "#0000FF"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#00FF00",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Google Play Store",
                   "uri": "line://app/1623679774-qmmXPXJ5"
                 }
               }
            ]
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                maxbots.postFlex(to, data)
                                data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg",
        "action": {
          "uri": "http://line.me/ti/p/%40jnx0914l",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#0000FF"
        },
        "header": {
          "backgroundColor": "#0000FF"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#00FF00",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Game Online",
                   "uri": "line://app/1609524990-ODaJ0Va0"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg",
        "action": {
          "uri": "http://line.me/ti/p/%40jnx0914l",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#0000FF"
        },
        "header": {
          "backgroundColor": "#0000FF"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#00FF00",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Main Game",
                   "uri": "line://app/1623679774-j4rZkZ51"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg",
        "action": {
          "uri": "http://line.me/ti/p/%40jnx0914l",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#0000FF"
        },
        "header": {
          "backgroundColor": "#0000FF"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#00FF00",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Photo Editor",
                   "uri": "line://app/1623679774-1pKn8ngr"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg",
        "action": {
          "uri": "http://line.me/ti/p/%40jnx0914l",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#0000FF"
        },
        "header": {
          "backgroundColor": "#0000FF"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#00FF00",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Text Neon Editor",
                   "uri": "line://app/1609524990-pdlOGglG"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg",
        "action": {
          "uri": "http://line.me/ti/p/%40jnx0914l",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#0000FF"
        },
        "header": {
          "backgroundColor": "#0000FF"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#00FF00",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "TV Online",
                   "uri": "line://app/1623679774-WVajRjDn"
                 }
               }
            ]
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                maxbots.postFlex(to, data)
                                data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/1qzvnLR/images-1.jpg",
        "action": {
          "uri": "http://line.me/ti/p/%40jnx0914l",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#0000FF"
        },
        "header": {
          "backgroundColor": "#0000FF"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#00FF00",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Notepad",
                   "uri": "line://app/1623679774-pXJyQy1D"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg",
        "action": {
          "uri": "http://line.me/ti/p/%40jnx0914l",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#0000FF"
        },
        "header": {
          "backgroundColor": "#0000FF"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#00FF00",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Get Channel",
                   "uri": "line://app/1623679774-9GWpqpGw"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/61SWtyx/images-4.jpg",
        "action": {
          "uri": "http://line.me/ti/p/%40jnx0914l",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#0000FF"
        },
        "header": {
          "backgroundColor": "#0000FF"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#00FF00",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Facebook",
                   "uri": "line://app/1609524990-mpvZ5xv5"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg",
        "action": {
          "uri": "http://line.me/ti/p/%40jnx0914l",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#0000FF"
        },
        "header": {
          "backgroundColor": "#0000FF"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#00FF00",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Twitter",
                   "uri": "https://mobile.twitter.com"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/mhh8f8T/images-5.jpg",
        "action": {
          "uri": "http://line.me/ti/p/%40jnx0914l",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#0000FF"
        },
        "header": {
          "backgroundColor": "#0000FF"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#00FF00",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Instagram",
                   "uri": "https://www.instagram.com/"
                 }
               }
            ]
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                maxbots.postFlex(to, data)

                        elif teambotmax == "bc" or teambotmax == 'คท ดำ':
                            if msg._from in admin:
                              if settings["blackList"] == {}:
                                    teambotmaxText(to,"✯͜͡❂ ไม่มีบัญชีดำ")
                              else:
                                    ma = ""
                                    for i in settings["blackList"]:
                                        ma = maxbots.getContact(i)
                                        maxbots.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif teambotmax == 'ไวรัส':
                          if msg._from in admin or msg._from in owner:
                              maxbots.unsendMessage(msg_id)
                              maxbots.sendMessage(msg.to, "M.A.X.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.M.A.X")
                              maxbots.sendMessage(msg.to, "M.A.X.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.M.A.X.")
                              maxbots.sendMessage(msg.to, "M.A.X.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.M.A.X.")
                              maxbots.sendMessage(msg.to, "M.A.X.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.M.A.X.")

                        elif teambotmax == "เช็คดำ" or teambotmax == "banlist":
                            if msg._from in admin:
                                if len(settings["blackList"]) > 0:
                                    h = [a for a in settings["blackList"]]
                                    k = len(h)//20
                                    for aa in range(k+1):
                                        if aa == 0:dd = '╭──「 รายชื่อบัญชีดำ 」';no=aa
                                        else:dd = '';no=aa*20
                                        msgas = dd
                                        for a in h[aa*20:(aa+1)*20]:
                                            no+=1
                                            if no == len(h):msgas+='\n│ {}. @!'.format(no)
                                            else:msgas += '\n│ {}. @!'.format(no)
                                        maxbots.sendMention(to, msgas, h[aa*20:(aa+1)*20])
                                else:
                                    teambotmaxText(to, "• ไม่มีผู้ใช้บัญชีดำ")

                        elif teambotmax == "cb" or teambotmax == 'ล้างดำ':
                            if msg._from in admin:
                              teambotmaxText(to,"✯͜͡❂ ล้างบัญชีดำ「 {} 」บัญชีดำ".format(str(len(settings["blackList"]))))
                              settings["blackList"] = {}

                        elif teambotmax == "เตะดำ" or teambotmax == "ล่า" or teambotmax == "killban":
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = maxbots.getGroup(to)
                                gMembMids = [contact.mid for contact in group.members]
                                matched_list = []
                            for tag in settings["blackList"]:
                                matched_list+=filter(lambda str: str == tag, gMembMids)
                            if matched_list == []:
                                teambotmaxText(to,"✯͜͡❂ ไม่มีผู้ใช้บัญชีดำ")
                                return
                            for tbm in matched_list:
                                maxbots.kickoutFromGroup(msg.to,[tbm])
                            teambotmaxText(to,"✯͜͡❂ ลบบัญชีดำเรียบร้อย")

                        elif teambotmax == "bancontact on":
                          if sender in admin:
                            settings["contactBan"] = True
                            teambotmaxText(to, "✯͜͡❂ แบนผู้ติดต่อ\n✯͜͡❂ ส่งที่อยู่ติดต่อ")

                        elif teambotmax == "bancontact off":
                          if sender in admin:
                            if settings["contactBan"] == False:
                                teambotmaxText(to, "✯͜͡❂ แบนผู้ติดต่อถูกปิดใช้งาน")
                            else:
                                settings["contactBan"] = False
                                teambotmaxText(to, "✯͜͡❂ แบนผู้ติดต่อถูกปิดใช้งาน")

                        elif teambotmax == "unbancontact on":
                          if sender in admin:
                            settings["unbanContact"] = True
                            teambotmaxText(to, "✯͜͡❂ ล้างดำ\n✯͜͡❂ ส่งผู้ติดต่อ")

                        elif teambotmax == "unbancontact off":
                          if sender in admin:
                            if settings["unbanContact"] == False:
                                teambotmaxText(to, "✯͜͡❂ ยกเลิกการล้างดำแล้ว")
                            else:
                                settings["unbanContact"] = False
                                teambotmaxText(to, "✯͜͡❂ ยกเลิกการล้างดำแล้ว")

                        elif teambotmax.startswith("ban "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for list in lists:
                                    try:
                                        settings["blackList"][list] = True
                                        f=codecs.open('settings.json','w','utf-8')
                                        json.dump(settings, f, sort_keys=True, indent=4,ensure_ascii=False)
                                        teambotmaxText(msg.to,"✯͜͡❂ เพิ่มบัญชีดำสำเร็จแล้ว")
                                    except:
                                        pass
                            else:
                                teambotmaxText(to, "✯͜͡❂ เพิ่มใน บัญชีดำ สำเร็จแล้ว")

                        elif teambotmax.startswith("unban "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for list in lists:
                                    try:
                                        del settings["blackList"][list]
                                        f=codecs.open('settings.json','w','utf-8')
                                        json.dump(settings, f, sort_keys=True, indent=4,ensure_ascii=False)
                                        teambotmaxText(to,"✯͜͡❂ ลบบัญชีดำสำเร็จแล้ว")
                                    except:
                                        pass
                            else:
                                teambotmaxText(to, "✯͜͡❂ สำเร็จในการลบบัญชีดำ")

                        elif teambotmax.startswith("cvp "):
                          if msg._from in admin or msg._from in owner:
                            link = removeCmd("cvp", text)
                            contact = maxbots.getContact(sender)
                            teambotmaxText(to, "✯͜͡❂ กำลังดาวน์โหลดกรุณารอสักครู่...")
                            print("เปลี่ยนรูปภาพวิดีโอ")
                            pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
                            pict = maxbots.downloadFileURL(pic)
                            vids = "TeamAnuBot.mp4"
                            changeVideoAndPictureProfile(pict, vids)
                            teambotmaxText(to, "✯͜͡❂ สำเร็จในการเปลี่ยนวิดีโอโปรไฟล์")
                            os.remove("TeamAnuBot.mp4")

                        elif teambotmax.startswith("github "):
                          if msg._from in admin or msg._from in owner:
                            maxX = teambotmax.replace('github ',"")
                            teambotmaxText(to,"✯͜͡❂ กำลังค้นหารอสักครู่...")
                            teambotmaxText(to,"✯͜͡❂ ผลจากการค้นหา : "+maxX+"\n✯͜͡❂ จาก : GitHub\n✯͜͡❂ ลิ้ง : https://github.com/search?q=" + maxX)

                        elif teambotmax.startswith("facebook "):
                          if msg._from in admin or msg._from in owner:
                            maxX = teambotmax.replace('facebook ',"")
                            teambotmaxText(to,"✯͜͡❂ กำลังค้นหารอสักครู่...")
                            teambotmaxText(to,"✯͜͡❂ ผลจากการค้นหา : "+maxX+"\n✯͜͡❂ จาก : Facebook\n✯͜͡❂ ลิ้ง : https://m.facebook.com/search/top/?q=" + maxX)

                        elif teambotmax.startswith("ประกาศแชท "):
                          if msg._from in admin or msg._from in owner:
                            teambotmax69 = text.split(" ")
                            teambotmaxZ = text.replace(teambotmax69[0] + " ", "")
                            maxZ = "{}".format(teambotmaxZ)
                            contacts = maxbots.getAllContactIds()
                            teambotmaxX = maxbots.getContact(maxbotsMid)
                            sender_profile = maxbots.getContact(sender)
                            teambotmax69 = maxbots.getProfileCoverURL(maxbots.profile.mid)
                            maxbots.reissueUserTicket()
                            warna1 = ("#FFFFFF","#FFFF00")
                            warnanya1 = random.choice(warna1)
                            for contact in contacts:
                                teambotmaxZ = {
                                        "type": "flex",
                                        "altText": "ƬΣΛM BӨƬ MΛX",
                                        "contents": {
                              "styles": {
                                "body": {
                                  "backgroundColor": "#000000",
                                  "separator":True,
                                  "separatorColor":"#FF0000"
                                },
                                "footer": {
                                  "backgroundColor": "#000000",
                                  "separator":True,
                                  "separatorColor":"#FF0000"
                                }
                              },
                              "type": "bubble",
                              "body": {
                                "contents": [
                                  {
                                    "contents": [          
                                      {
                                        "type": "image",            
                                        "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus),
                                        "size": "full",
                                        "action": {
                                          "uri": "http://line.me/ti/p/%40jnx0914l",
                                          "type": "uri"
                                         },
                                      }
                                    ],
                                    "type": "box",
                                    "spacing": "md",
                                    "layout": "horizontal"
                                  },
                                  {
                                    "type": "separator",
                                    "color": "#FF0000"
                                   },
                                   {
                                    "contents": [
                                      {
                                        "contents": [
                                          {
                                            "text": "{}".format(maxZ),
                                            "size": "sm",
                                            "margin": "none",
                                            "color": warnanya1,
                                            "wrap": True,
                                            "weight": "regular",
                                            "type": "text"
                                          }
                                        ],
                                        "type": "box",
                                        "layout": "baseline"
                                      }
                                    ],
                                    "type": "box",
                                    "layout": "vertical"
                                  }
                                ],
                                "type": "box",
                                "spacing": "md",
                                "layout": "vertical"
                              },
                              "footer": {
                                  "type": "box",
                                  "layout": "vertical",
                                  "contents": [{
                                      "type": "box",
                                      "layout": "horizontal",
                                      "flex": 2,
                                      "contents": [{
                                          "type": "button",
                                          "style": "secondary",
                                          "color": "#FF0000",
                                          "height": "sm",
                                          "action": {
                                            "uri": "https://line.me/ti/p/~" + maxbots.profile.userid,                                            
                                            "label": "✦ กดเพิ่มเพื่อนติดต่อ ✦",
                                            "type": "uri",
                                          }
                                      }]
                                  }]
                              }
                            }
                            }
                                bcTemplate(contact, teambotmaxZ)
                                time.sleep(1)
                                print ("ประกาศกลุ่มเรียบร้อย")

                        elif teambotmax.startswith("รูป "):
                            if msg._from in admin:
                                query = removeCmd("รูป", text)
                                cond = query.split(" ")
                                search = str(cond[0])
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/{}".format(str(search)))
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    ret_ = []                                	
                                    for food in data:
                                        if 'http://' in food["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(food["url"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "ส่งรูปภาพ",
                                                        "uri": "line://app/1623679774-k9nBDB6b?type=image&img={}".format(str(food["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                          "messages": [
                                            {
                                              "type": "template",
                                              "altText": "image",
                                              "template": {
                                                  "type": "image_carousel",
                                                  "columns": ret_[aa*10 : (aa+1)*10]
                                              }
                                            }
                                          ]
                                        }
                                        sendTemplateMax(to, data)

                        elif teambotmax.startswith("ภาพ "):
                          if msg._from in admin or msg._from in owner:
                            teambotmax69 = text.split(" ")
                            max = text.replace(teambotmax69[0] + " ","")
                            url = requests.get("https://rest.farzain.com/api/gambarg.php?id={}&apikey=VBbUElsjMS84rXUO7wRlIwjFm".format(max))
                            data = url.json()
                            selfbotbymax = {
                                  "type": "template",
                                  "altText": "ƬΣΛM BӨƬ MΛX",
                                  "template": {
                                     "type": "image_carousel",
                                     "columns": [
                                     {
                                          "imageUrl": "{}".format(str(data["url"])),
                                          "size": "xxxl",
                                          "aspectRatio": "1:1",
                                          "action": {
                                            "type": "uri",
                                            "uri": "line://app/1623679774-k9nBDB6b?type=image&img={}".format(str(data["url"]))
                                         }
                                        }
                                       ]
                                     }
                                   }
                            maxbots.sendFlex(to, selfbotbymax)
                            print ("Sender Foto Showed")

                        elif teambotmax.startswith("foto "):
                          if msg._from in admin or msg._from in owner:
                            teambotmax69 = text.split(" ")
                            max = text.replace(teambotmax69[0] + " ","")
                            url = requests.get("https://rest.farzain.com/api/gambarg.php?id={}&apikey=VBbUElsjMS84rXUO7wRlIwjFm".format(max))
                            data = url.json()
                            selfbotbymax = {
                                  "type": "template",
                                  "altText": "ƬΣΛM BӨƬ MΛX",
                                  "template": {
                                     "type": "image_carousel",
                                     "columns": [
                                     {
                                          "imageUrl": "{}".format(str(data["url"])),
                                          "size": "xxxl",
                                          "aspectRatio": "1:1",
                                          "action": {
                                            "type": "uri",
                                            "uri": "line://app/1623679774-k9nBDB6b?type=image&img={}".format(str(data["url"]))
                                         }
                                        }
                                       ]
                                     }
                                   }
                            maxbots.sendFlex(to, selfbotbymax)
                            print ("Sender Foto Showed")

                        elif teambotmax == 'mid':
                          if msg._from in admin or msg._from in owner:
                            memyid = maxbots.getContact(sender).mid
                            pesannya = {
                                    "type": "flex",
                                    "altText": "{} Menampilkan".format(str(maxbots.getContact(maxbotsMid).displayName)),
                                    "contents": {
                                        "type": "bubble",
                                        "body": {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2"
                                            },
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "MID : {}".format(str(memyid)),
                                                    "color": "#000000",
                                                    "align": "center",
                                                    "weight":"bold",
                                                    "wrap": True
                                                }
                                            ]
                                        },
                                        "styles": {
                                            "body": {
                                                "backgroundColor": "#ffda6b"
                                            }
                                        }
                                    }
                                }
                            maxbots.sendFlex(msg.to,pesannya)
                            print ("Sender MID Showed")

                        elif teambotmax.startswith("ประกาศกลุ่ม: "):
                            if msg._from in admin or msg._from in owner:
                                bc = msg.text.replace("ประกาศกลุ่ม: ","")
                                gid = maxbots.getGroupIdsJoined()
                                owner = "uc14c3d87a1123df7c8ffa9d7402e59a2"
                                for i in gid:
                                    maxbots.mentionWithRFU(i,owner,"" + str("「 "+bc+" 」"))
                                    time.sleep(1)
                                    print ("ประกาศกลุ่มเรียบร้อย")

                        elif teambotmax.startswith("ประกาศเพื่อน: "):
                            if msg._from in admin or msg._from in owner:
                                bc = msg.text.replace("ประกาศเพื่อน: ","")
                                gid = maxbots.getAllContactIds()
                                owner = "uc14c3d87a1123df7c8ffa9d7402e59a2"
                                for i in gid:
                                    maxbots.mentionWithRFU(i,owner,"༺ ข้อความประกาศเพื่อน ༻\n ","\n\n" + str("「 "+bc+" 」"))
                                    time.sleep(1)
                                    print ("ประกาศเพื่อนเรียบร้อย")

                        elif teambotmax == "me":
                            if msg._from in admin or msg._from in owner:
                                teambotmax1 = maxbots.getContact(maxbotsMid)
                                teambotmax2 = maxbots.getContact(sender)                   
                                teambotmax3 = maxbots.getProfileCoverURL(sender)
                                teambotmaxZ = {
                                        "type": "flex",
                                        "altText": "ƬΣΛM BӨƬ MΛX",
                                        "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
#      "size": "giga",
#      "direction": "ltr",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "℘ɧσtσ ℘гσʄıɭε",
                    "size": "xl",
                    "color": "#ffffff",
                    "weight": "bold",
                    "align": "center",
                    "action": {
                      "uri": "http://line.me/ti/p/%40jnx0914l",
                      "type": "uri",
                    }
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "• ชื่อ",
                    "color": "#ebebeb",
                    "size": "sm",
                    "flex": 0
                  },
                  {
                    "type": "text",
                    "text": "{}".format(str(teambotmax1.displayName)),
                    "color": "#ffffffcc",
                    "decoration": "line-through",
                    "gravity": "bottom",
                    "flex": 0,
                    "size": "sm",
                    "action": {
                      "uri": "http://line.me/ti/p/%40jnx0914l",
                      "type": "uri",
                    }
                  }
                ],
                "spacing": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "icon",
                        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                      },
                      {
                        "type": "text",
                        "text": "กดตรงนี้เพื่อเพิ่มเพื่อนฉัน",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px",
                        "action": {
                          "uri": "https://line.me/ti/p/"+maxbots.getUserTicket().id,
                          "type": "uri",
                        }
                      },
                      {
                        "type": "icon",
                        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#03303Acc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "NEW",
                "color": "#ffffff",
                "align": "center",
                "size": "xs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "18px",
            "backgroundColor": "#ff334b",
            "offsetStart": "18px",
            "height": "25px",
            "width": "53px"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
#      "size": "giga",
#      "direction": "ltr",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": teambotmax3,
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "℘ɧσtσ ɕσvεг",
                    "size": "xl",
                    "color": "#ffffff",
                    "weight": "bold",
                    "align": "center",
                    "action": {
                      "uri": "http://line.me/ti/p/%40jnx0914l",
                      "type": "uri",
                    }
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "• ชื่อ",
                    "color": "#ebebeb",
                    "size": "sm",
                    "flex": 0
                  },
                  {
                    "type": "text",
                    "text": "{}".format(str(teambotmax1.displayName)),
                    "color": "#ffffffcc",
                    "decoration": "line-through",
                    "gravity": "bottom",
                    "flex": 0,
                    "size": "sm",
                    "action": {
                      "uri": "http://line.me/ti/p/%40jnx0914l",
                      "type": "uri",
                    }
                  }
                ],
                "spacing": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "icon",
                        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                      },
                      {
                        "type": "text",
                        "text": "กดตรงนี้เพื่อเพิ่มเพื่อนฉัน",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px",
                        "action": {
                          "uri": "https://line.me/ti/p/"+maxbots.getUserTicket().id,
                          "type": "uri",
                        }
                      },
                      {
                        "type": "icon",
                        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#9C8E7Ecc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "NEW",
                "color": "#ffffff",
                "align": "center",
                "size": "xs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "18px",
            "backgroundColor": "#ff334b",
            "offsetStart": "18px",
            "height": "25px",
            "width": "53px"
          }
        ],
        "paddingAll": "0px"
      }
    }
  ]
}
}
                                maxbots.postTemplate(to, teambotmaxZ)

                        elif teambotmax == "me1":
                            if msg._from in admin or msg._from in owner:
                                contact = maxbots.getProfile()
                                mids = [contact.mid]
                                teambotmax1 = maxbots.getContact(maxbotsMid)
                                teambotmax2 = maxbots.getContact(sender) 
                                data = {
                                        "type": "flex",
                                        "altText": "ƬΣΛM BӨƬ MΛX",
                                        "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": "✦ ƬΣΛM BӨƬ MΛX ✦",
            "size": "md",
            "weight": "bold",
            "align": "center",
            "wrap": True,
            "color": "#ffffff"
          },
          {
            "type": "text",
            "text": "{}".format(teambotmax2.displayName),
            "align": "center",
            "size": "sm",
            "weight": "bold",
            "align": "center",
            "color": "#FF00FF",
            "wrap": True
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "0A3800"
    },
    "footer": {
      "backgroundColor": "#000000"
    },
    "header": {
      "backgroundColor": "#000000"
    }
  },  
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "✦ กดตรงนี้เพื่อเพิ่มเพื่อนฉัน ✦",
        "size": "md",
        "wrap": True,
        "weight": "bold",
        "color": "#ffffff",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/%40jnx0914l"
        },
        "align": "center"
      }
    ]
  },
  "hero": {
    "aspectMode": "cover",
    "aspectRatio": "1:1",
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(sender).pictureStatus),
    "size": "full",
    "align": "center",
  },
  "header": {
    "type": "box",   
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "{}".format(teambotmax1.displayName),
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#ffffff",
        "align": "center"
      }
    ]
  }
}
}
                                maxbots.postTemplate(to, data)

                        elif teambotmax == "me2":
                            if msg._from in admin or msg._from in owner:
                                contact = maxbots.getProfile()
                                mids = [contact.mid]
                                status = maxbots.getContact(sender)                   
                                cover = maxbots.getProfileCoverURL(sender)
                                data = {
                                        "type": "flex",
                                        "altText": "ƬΣΛM BӨƬ MΛX",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000" #999999"
    },
    "footer": {
      "backgroundColor": "#ff0000" #0000" #cc9999"
    }
  },
  "type": "bubble",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#FFFFFF"            
      },
      {
        "type": "separator",
        "color": "#FFFFFF"      
      },
      {        
        "contents": [
          {            
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
          "text": "✴️ᴘʀᴏғɪʟᴇ✴️",
           "size": "xs",
           "align": "center",
           "color": "#FFFF00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
            },
           {     
            "type": "separator",
            "color": "#000000"
            },
          {
            "type": "separator",
            "color": "#000000"
            },
            {
           "text": "✴️ʙᴇʀᴀɴᴅᴀ✴️",
           "size": "xs",
           "align": "center",
           "color": "#FFFF00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
            }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"      
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
      },
      {
        "contents": [
         {
         "type": "image",
           "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(sender).pictureStatus),
            "size": "xl",                   
           },
           {     
            "type": "separator",
            "color": "#FFFFFF"#ff0000"
            },
          {
            "type": "separator",
            "color": "#FFFFFF"
            },
            {
           "type": "image",
           "url": cover, 
            "size": "xl",
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
            "color": "#FFFFFF"
            },
          {
        "contents": [
            {          
            "text": "{}".format(maxbots.getContact(sender).displayName),
            "size": "xs",
            "align": "center",
            "color": "#FF0099",
            "wrap": True,
            "weight": "bold",
            "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
          },
          {
            "contents": [  
           {          
            "text": "✴️ᴘᴇsᴀɴ sᴛᴀᴛᴜs✴️",
            "size": "xs",
            "align": "center",
            "color": "#FFFF00", #ffff00",
            "wrap": True,
            "weight": "bold",
            "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
          },
          {
            "contents": [
           {            
            "type": "separator",
            "color": "#FFFFFF"#ff0000"
          },
          {
            "text": "{}".format(status.statusMessage),
            "size": "xs",
            "align": "center",
            "color": "#FF6600",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"      
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
      },
      {
        "contents": [           
           {
           "type": "image",
            "url": "https://4.bp.blogspot.com/-E7DFmEtCcO0/Vx3frfw4zII/AAAAAAAAAEU/V4oUfhvK7_soc1dPxg60TQH9QmAed9m6gCLcB/s1600/line.png", #https://shop.hiushoes.com/wp-content/uploads/2017/07/logo-Line.png", #https://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/%40jnx0914l",
            },         
            "flex": 1
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
          "type": "image",
            "url": "https://jualsaladbuahenakdisurabaya.files.wordpress.com/2017/06/icon-wa.jpg", #https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRG8U5UNSW8lOIhkY4AfRisxxpQKlMC1WrgIKSQYCxY6cXiVAJw", #https://s18955.pcdn.co/wp-content/uploads/2017/05/WhatsApp.png", #watshap
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://wa.me/",   
           }, 
            "flex": 1
           },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "type": "image",
            "url": "https://2.bp.blogspot.com/-1GRWlQBGf9I/WIRQXiXVelI/AAAAAAAAAIM/cp2h8QQYXKQOFv9hNkwC5eOogcYPxezrwCLcB/s320/sms-icon.png", #https://images-eu.ssl-images-amazon.com/images/I/41iKHNX1WbL.png", #chat
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/chat"
          },
            "flex": 1
            },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
          "type": "image",
            "url": "https://cdn2.iconfinder.com/data/icons/contact-flat-buttons/512/dial-512.png", #https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcReFldAe2KbdzYP-InVc5OzA22dW2Bi2J6cffUYdBNAy92SPWSB", #https://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
              "uri": "line://call/contacts"            
            },
            "flex": 1
           },
          {
            "type": "separator",
            "color": "#FFFFFF"
            },
            {
           "type": "image",
            "url": "https://is1-ssl.mzstatic.com/image/thumb/Purple118/v4/b2/5a/72/b25a72fe-2ff6-015b-436a-eff66a6d0161/AppIcon-CCCP-1x_U007emarketing-85-220-9.png/1200x630bb.jpg",
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },
            "flex": 1 
         }
            ], 
            "type": "box",
            "layout": "horizontal"   
            },
      {
        "type": "separator",
        "color": "#FFFFFF"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
                                maxbots.postTemplate(to, data)

                        elif teambotmax == "me3":
                            if msg._from in admin or msg._from in owner:
                                contact = maxbots.getProfile()
                                mids = [contact.mid]
                                status = maxbots.getContact(sender)
                                cover = maxbots.getProfileCoverURL(sender)
                                data = {
                                        "type": "flex",
                                        "altText": "ƬΣΛM BӨƬ MΛX",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#FFFFFF"
    }
  },
  "type": "bubble",
      "body": {
    "contents": [
      {
        "contents": [
          {
            "type": "image",
        "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(sender).pictureStatus),
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "type": "image",
        "url": cover,
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
           "type": "image",
       "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(sender).pictureStatus),     
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "image",
        "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(sender).pictureStatus),
        "aspectRatio": "1:1",
        "aspectMode": "cover",
        "size": "full",
      },     
      {
        "contents": [
          {        
            "contents": [
              {              
                "type": "text",
            "text": "{}".format(status.displayName),
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#7FFF00",
            "align": "center"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#000000",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ADMIN",
                  "uri": "http://line.me/ti/p/%40jnx0914l"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#000000",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "CREATOR",
                  "uri": "http://line.me/ti/p/~teambotmax"
              }
          }]
      }]
  }
}
}
                                maxbots.postTemplate(to, data)

                        elif teambotmax == "me4":
                            if msg._from in admin or msg._from in owner:
                                h = maxbots.getContact(msg._from)
                                maxbots.reissueUserTicket()
                                data = {
                                 "type": "flex",
                                 "altText": "{} cangkemu".format(str(h.displayName)),
                                 "contents": {
                                  "type": "bubble",
                                  "styles": {
                                    "header": {
                                      "backgroundColor": "#000000",
                                    },
                                    "body": {
                                      "backgroundColor": "#000000",
                                      "separator": True,
                                      "separatorColor": "#FFFFFF"
                                    },
                                    "footer": {
                                      "backgroundColor": "#000000",
                                      "separator": True
                                    }
                                  },
                                  "header": {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                      {
                                        "type": "text",
                                        "text": "        ＳＥＬＦＢＯＴＢＹＭＡＸ",
                                        "weight": "bold",
                                        "color": "#FFFFFF",
                                        "size": "md"
                                      }
                                    ]
                                  },
                                  "hero": {
                                    "type": "image",
                                    "url": "https://os.line.naver.jp/os/p/{}".format(msg._from),
                                    "size": "full",
                                    "aspectRatio": "1:1",
                                    "aspectMode": "cover",
                                    "action": {
                                      "type": "uri",
                                      "uri": "http://line.me/ti/p/%40jnx0914l"
                                    }
                                  },
                                  "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "spacing": "md",
                                    "action": {
                                      "type": "uri",
                                      "uri": "http://line.me/ti/p/%40jnx0914l"
                                    },
                                    "contents": [
                                      {
                                        "type": "text",
                                        "text": "        ＳＥＬＦＢＯＴＢＹＭＡＸ",
                                        "size": "md",
                                        "color": "#FFFFFF"
                                      },
                                      {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                          {
                                            "type": "box",
                                            "layout": "baseline",
                                            "contents": [
                                              {
                                                "type": "icon",
                                                "url": "https://os.line.naver.jp/os/p/{}".format(msg._from),
                                                "size": "5xl"
                                              },
                                              {
                                                "type": "text",
                                                "text": "• ชื่อผู้ใช้ :",
                                                "weight": "bold",
                                                "color": "#FFFFFF",
                                                "margin": "sm",
                                                "flex": 0
                                              },
                                              {
                                                "type": "text",
                                                "text": h.displayName,
                                                "size": "sm",
                                                "align": "end",
                                                "color": "#FF0000"
                                              }
                                            ]
                                          },
                                          {
                                            "type": "box",
                                            "layout": "baseline",
                                            "contents": [
                                              {
                                                "type": "icon",
                                                "url": "https://media.giphy.com/media/ggF6OBD1wAERqZYh7K/giphy.gif",
                                                "size": "5xl"
                                              },
                                              {
                                                "type": "text",
                                                "text": "• แอดมิน :",
                                                "weight": "bold",
                                                "color": "#FFFFFF",
                                                "margin": "sm",
                                                "flex": 0
                                              },
                                              {
                                                "type": "text",
                                                "text": "𝐌𝐚𝐱",
                                                "size": "sm",
                                                "align": "end",
                                                "color": "#FF0000"
                                              }
                                            ]
                                          },
                                          {
                                            "type": "box",
                                            "layout": "baseline",
                                            "contents": [
                                              {
                                                "type": "icon",
                                                "url": "https://media.giphy.com/media/JSjyKthOO1v6NsoiEs/giphy.gif",
                                                "size": "5xl"
                                              },
                                              {
                                                "type": "text",
                                                "text": "• ผู้สร้าง :",
                                                "margin": "sm",
                                                "color": "#FFFFFF",
                                                "weight": "bold",
                                                "flex": 0
                                              },
                                              {
                                                "type": "text",
                                                "text": "𝐌𝐚𝐱",
                                                "size": "sm",
                                                "align": "end",
                                                "color": "#FF0000"
                                              }
                                            ]
                                          }
                                        ]
                                      },
                                      {
                                        "type": "text",
                                        "text": "━━━━━━━━━━━━━━━━━━\n• เบอร์ติดต่อ : ??𝟗??𝟓𝟑𝟖𝟐??𝟒𝟎",
                                        "wrap": True,
                                        "color": "#FFFFFF",
                                        "size": "xxs"
                                      }
                                    ]
                                  },
                                  "footer": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                      {
                                        "type": "spacer",
                                        "size": "sm"
                                      },
                                      {
                                        "type": "button",
                                        "style": "primary",
                                        "color": "#000000",
                                        "action": {
                                          "type": "uri",
                                          "label": "༺ ติดต่อแอดมิน ༻",
                                          "uri": "https://line.me/ti/p/"+maxbots.getUserTicket().id
                                        }
                                      }
                                    ]
                                  }
                                 }
                                }
                                maxbots.postTemplate(to, data)

                        elif teambotmax == "me5":
                            if msg._from in admin or msg._from in owner:
                                contact = maxbots.getProfile()
                                mids = [contact.mid]
                                status = maxbots.getContact(sender)                   
                                cover = maxbots.getProfileCoverURL(sender)
                                data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(sender).pictureStatus),
        "action": {
          "uri": "http://line.me/ti/p/%40jnx0914l",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#666666",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "𝐀𝐃𝐃 𝐌𝐄",
                  "uri": "http://line.me/ti/p/%40jnx0914l"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#666666",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "𝐎𝐑𝐃𝐄𝐑",
                  "uri": "line://app/1623679774-k9nBDB6b?type=text&text=order"
              }
          }]
      }]
  },
  "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "𝐏𝐈𝐂𝐓𝐔𝐑𝐄",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": cover,
        "action": {
          "uri": "http://line.me/ti/p/%40jnx0914l",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#666666",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "𝐀𝐃𝐃 𝐌𝐄",
                  "uri": "http://line.me/ti/p/%40jnx0914l"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#666666",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "𝐎𝐑𝐃𝐄𝐑",
                  "uri": "line://app/1623679774-k9nBDB6b?type=text&text=order"
              }
          }]
      }]
  },
  "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "𝐂𝐎𝐕𝐄??",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    },
    {
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(status.displayName),
                    "size": "xl",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#00EE00",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#666666"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "ＳＥＬＦＢＯＴＢＹＭＡＸ",
                    "size": "md",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#FF0000",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#666666"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(status.statusMessage),
                    "size": "xs",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#FF7F00",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#666666",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "𝐀𝐃𝐃 𝐌𝐄",
                  "uri": "http://line.me/ti/p/%40jnx0914l"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#666666",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "𝐎𝐑𝐃𝐄𝐑",
                  "uri": "line://app/1623679774-k9nBDB6b?type=text&text=order"
              }
          }]
      }]
  },
  "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "𝐌𝐘𝐁𝐈𝐎",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                maxbots.postFlex(to, data)

                        elif teambotmax == "me6":
                            if msg._from in admin or msg._from in owner:
                                contact = maxbots.getProfile()
                                mids = [contact.mid]
                                status = maxbots.getContact(sender)
                                data = {
                                        "type": "flex",
                                        "altText": "ＳＥＬＦＢＯＴＢＹＭＡＸ",
                                        "contents": {
  "type": "bubble",
  "size": "giga",
  "direction": "ltr",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": "• ชื่อ :",
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#FF00FF"
          },
          {
            "type": "text",
            "flex": 2,
            "text": "{}".format(status.displayName),
            "size": "md",
            "wrap": True,
            "weight": "bold",
            "gravity": "center",
            "color": "#FF0000"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "type": "text",
            "text": "• สถานะ :",
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#FF00FF"
          },
          {
            "type": "text",
            "text": "{}".format(status.statusMessage),
            "size": "md",
            "color": "#00FF00",
            "wrap": True
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#666666"
    }
  },
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(sender).pictureStatus),
    "size": "full",
    "margin": "xl"
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "𝐀𝐃𝐃 𝐌𝐄",
        "size": "md",
        "wrap": True,
        "weight": "bold",
        "color": "#FFFFFF",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/%40jnx0914l"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
      },
      {
        "type": "text",
        "text": "𝐎𝐑𝐃𝐄𝐑",
        "size": "md",
        "wrap": True,
        "weight": "bold",
        "color": "#FFFFFF",
        "action": {
          "type": "uri",
          "uri": "line://app/1623679774-k9nBDB6b?type=text&text=order"
        },
        "align": "center"
      }
    ]
  }
}
}
                                maxbots.postTemplate(to, data)

                        elif teambotmax == "me7":
                            if msg._from in admin or msg._from in owner:
                                h = maxbots.getContact(msg._from)
                                maxbots.reissueUserTicket()
                                data = {
                                        "type":"flex",
                                        "altText": "ＳＥＬＦＢＯＴＢＹＭＡＸ",
                                        "contents":{
                                        "type":"bubble",
                                        "footer":{
                                        "type":"box",
                                        "layout":"horizontal",
                                        "contents":[
                                        {
                                        "color": "#000000",
                                        "size":"xs",
                                        "wrap":True,
                                        "action":{
                                        "type":"uri",
                                        "uri":"line://app/1623679774-k9nBDB6b?type=profile"
                                        },
                                        "type":"text",
                                        "text":"𝐏𝐫𝐨𝐟𝐢𝐥𝐞",
                                        "align":"center",
                                        "weight":"bold"
                                        },
                                        {
                                        "type":"separator",
                                        "color":"#FF0000"
                                        },
                                        {
                                        "color":"#000000",
                                        "size":"xs",
                                        "wrap":True,
                                        "action":{
                                        "type":"uri",
                                        "uri":"http://line.me/ti/p/" + maxbots.getUserTicket().id
                                        },
                                        "type":"text",
                                        "text":"𝐀𝐃𝐃 𝐌𝐄",
                                        "align":"center","weight":"bold"
                                        }
                                        ]
                                        },
                                        "styles":{
                                        "footer":{
                                        "backgroundColor":"#FF0000"
                                        },
                                        "body":{
                                        "backgroundColor":"#666666"
                                        }
                                        },
                                        "body":{
                                        "type":"box",
                                        "contents":[
                                        {
                                        "type":"box",
                                        "contents":[
                                        {
                                        "type":"separator",
                                        "color":"#000000"
                                        },
                                        {
                                        "aspectMode":"cover",
                                        "gravity":"bottom",
                                        "aspectRatio":"1:1",
                                        "size":"sm",
                                        "type":"image",
                                         "url": "https://os.line.naver.jp/os/p/{}".format(msg._from),
                                         "action": {
                                         "type":"uri","uri": "line://app/1623679774-k9nBDB6b?type=profile"
                                         }
                                        },
                                        {
                                        "type":"separator",
                                        "color":"#000000"
                                        },
                                        {
                                        "type":"image",
                                        "aspectMode":"cover",
                                        "aspectRatio":"1:1",
                                        "size":"sm",
                                        "url":"https://media.giphy.com/media/gfHcXDuuclchrQVt2z/giphy.gif",
                                         "action": {
                                         "type":"uri","uri":"line://app/1623679774-k9nBDB6b?type=profile"
                                         }
                                        },
                                        {
                                        "type":"separator",
                                        "color":"#000000"
                                        }
                                        ],
                                        "layout":"vertical",
                                        "spacing":"none","flex":1
                                        },
                                        {
                                        "type":"separator",
                                        "color":"#000000"
                                        },
                                        {
                                        "type":"box",
                                        "contents":[
                                        {
                                        "type":"separator",
                                        "color":"#000000"
                                        },
                                        {
                                        "color":"#FF9B0A",
                                        "size":"md",
                                        "wrap":True,
                                        "type":"text",
                                        "text":"ＢＹＭＡＸ",
                                        "weight":"bold"
                                        },
                                        {
                                        "type":"separator",
                                        "color":"#000000"
                                        },
                                        {
                                        "color":"#FF0000",
                                        "size":"md",
                                        "wrap":True,
                                        "type":"text",
                                        "text":"{}".format(h.displayName),
                                        "weight":"bold"
                                        },
                                        {
                                        "type":"separator",
                                        "color":"#FF0000"
                                        },
                                        {
                                        "color":"#000000",
                                        "size":"xs",
                                        "wrap":True,
                                        "type":"text",
                                        "text":"Status Profile:",
                                        "weight":"bold"
                                        },
                                        {
                                        "type":"text",
                                        "text":"{}".format(h.statusMessage),
                                        "size":"xxs",
                                        "wrap":True,
                                        "color":"#FF9B0A"
                                        }
                                        ],
                                        "layout":"vertical",
                                        "flex":2
                                        }
                                        ],
                                        "layout":"horizontal",
                                        "spacing":"md"
                                        },
                                        "hero":{
                                        "aspectMode":"cover",
                                        "margin":"xxl",
                                        "aspectRatio":"1:1",
                                        "size":"full",
                                        "type":"image",
                                        "url":"https://obs.line-scdn.net/{}".format(h.pictureStatus),
                                        "action": {
                                         "type":"uri","uri": "line://app/1623679774-k9nBDB6b?type=profile"
                                          }
                                        }
                                    }
                                }
                                maxbots.postTemplate(to, data)

                        elif teambotmax == "me8":
                            if msg._from in admin or msg._from in owner:
                                contact = maxbots.getProfile()
                                mids = [contact.mid]
                                status = maxbots.getContact(sender)                   
                                cover = maxbots.getProfileCoverURL(sender)
                                data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(sender).pictureStatus),
        "action": {
          "uri": "http://line.me/ti/p/%40jnx0914l",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "CREATOR",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/%40jnx0914l"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "PROFIL",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": cover,
        "action": {
          "uri": "http://line.me/ti/p/%40jnx0914l",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(status.displayName),
                    "size": "xl",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#7FFF00",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "STATUS",
                    "size": "md",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(status.statusMessage),
                    "size": "xs",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#F0FFFF",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "CREATOR",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/%40jnx0914l"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "BERANDA",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                maxbots.postFlex(to, data)
    
                        elif teambotmax == "me9":
                            if msg._from in admin or msg._from in owner:
                                contact = maxbots.getProfile()
                                mids = [contact.mid]
                                status = maxbots.getContact(sender)                   
                                cover = maxbots.getProfileCoverURL(sender)
                                data = {
    "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(sender).pictureStatus),
        "action": {
          "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#000000"
      },
      "header": {
       "backgroundColor": "#000000"
    }
  },
  "type": "bubble",
      "body": {
  "contents": [
      {
        "contents": [                   
           {
           "type": "separator",
                  "color": "#000000"                 
                  },
                  {
                    "text": "♦️ᴀᴘʟɪᴋᴀsɪ ᴍᴇ♦️",
                "size": "sm",
                "align": "center",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "bold",
                "type": "text"
             }
            ],
            "type": "box",
            "spacing": "md",
            "layout": "horizontal"        
          },
          {
          "type": "separator",
            "color": "#ff0000"
          },
          {
          "contents": [
            {
           "type": "image",
            "url": "https://4.bp.blogspot.com/-E7DFmEtCcO0/Vx3frfw4zII/AAAAAAAAAEU/V4oUfhvK7_soc1dPxg60TQH9QmAed9m6gCLcB/s1600/line.png", #https://shop.hiushoes.com/wp-content/uploads/2017/07/logo-Line.png", #https://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
            },         
            "flex": 1
          },
          {
            "type": "separator",
            "color": "#ff0000"
          },
          {
          "type": "image",
            "url": "https://jualsaladbuahenakdisurabaya.files.wordpress.com/2017/06/icon-wa.jpg", #https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRG8U5UNSW8lOIhkY4AfRisxxpQKlMC1WrgIKSQYCxY6cXiVAJw", #https://s18955.pcdn.co/wp-content/uploads/2017/05/WhatsApp.png", #watshap
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://app/1602290395-78kGJWZp",   
           }, 
            "flex": 1
           },
          {
            "type": "separator",
            "color": "#ff0000"
          },
          {
            "type": "image",
            "url": "https://2.bp.blogspot.com/-1GRWlQBGf9I/WIRQXiXVelI/AAAAAAAAAIM/cp2h8QQYXKQOFv9hNkwC5eOogcYPxezrwCLcB/s320/sms-icon.png", #https://images-eu.ssl-images-amazon.com/images/I/41iKHNX1WbL.png", #chat
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/chat"
          },
            "flex": 1
            },
          {
            "type": "separator",
            "color": "#ff0000"
          },
          {
          "type": "image",
            "url": "https://cdn2.iconfinder.com/data/icons/contact-flat-buttons/512/dial-512.png", #https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcReFldAe2KbdzYP-InVc5OzA22dW2Bi2J6cffUYdBNAy92SPWSB", #https://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
              "uri": "line://call/contacts"            
            },
            "flex": 1
           },
          {
            "type": "separator",
            "color": "#ff0000"
            },
            {
           "type": "image",
            "url": "https://is1-ssl.mzstatic.com/image/thumb/Purple118/v4/b2/5a/72/b25a72fe-2ff6-015b-436a-eff66a6d0161/AppIcon-CCCP-1x_U007emarketing-85-220-9.png/1200x630bb.jpg",
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__TRSC_OLALA__",
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FF0000"   
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "♦️ᴘʀᴏғɪʟᴇ♦️",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center" 
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": cover,
        "action": {
          "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
    "contents": [
      {
        "contents": [
          {
                  "type": "separator",
                  "color": "#000000"                 
                  },
                  {
                    "text": "♦️ᴀᴘʟɪᴋᴀsɪ ᴍᴇ♦️",
                "size": "sm",
                "align": "center",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "bold",
                "type": "text"
             }
            ],
            "type": "box",
            "spacing": "md",
            "layout": "horizontal"        
          },
          {
          "type": "separator",
            "color": "#ff0000"
          },
          {
          "contents": [
             {
              "type": "image",
            "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQTPm07mRMipbYi0abivFuIYfuQen2uotWyGdpJGwMm3q9tYU0v", #https://i.ibb.co/qBks5dv/20190414-220412.png", #camerahttps://s18955.pcdn.co/wp-content/uploads/2017/05/WhatsApp.png", #watshap
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera",
            },
            "flex": 1
          },
          {
            "type": "separator",
            "color": "#ff0000"
          },
          {
           "type": "image",
            "url": "https://2.bp.blogspot.com/-f8v0v2EiGbI/WDUMAHjUEsI/AAAAAAAABGI/65Mef7tDue067QVDMXzFln5BldDlrslSgCLcB/s1600/obeng%2Btang.jpg", #setting
            "size": "xs",
            "action": {
               "type": "uri",
               "uri": "line://nv/settings",
               },
            "flex": 1
            },
          {
            "type": "separator",
            "color": "#ff0000"
            },
            {
           "type": "image",
            "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRPjjbM1r_8t3Sy_XGQq9z02ZwVRNvfqlPLbJQeUerGqFYmY2Eq", #yutub
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com/"
              },
               "flex": 1
          },
          {
            "type": "separator",
            "color": "#ff0000"
          },
          {
          "type": "image",
            "url": "https://previews.123rf.com/images/dxinerz/dxinerz1508/dxinerz150800464/43410998-galer%C3%ADa-foto-icono-imagen-vectorial-tambi%C3%A9n-se-puede-utilizar-para-aplicaciones-m%C3%B3viles-barra-de-pesta%C3%B1as-de-t.jpg",
            "size": "xs",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi",         
           },
           "flex": 1
          },
          {
            "type": "separator",
            "color": "#ff0000"
          },
          {
            "type": "image",
            "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSYtthIuklAOYGGBZxletmiAa6TEwvcwx3scdZho1UhNjoEvS_7", #https://gotongroyong.online/Uploads/user-photo-profile/default/user-icon.png", #galery
            "size": "xs",
            "action": {
            "type": "uri",
              "uri": "line://nv/profile",
            },
             "flex": 1             
          }
        ],
         "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
          },
          {
        "type": "separator",
        "color": "#ff0000"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },      
       "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "♦️ʙᴇʀᴀɴᴅᴀ♦️",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center" 
          }
        ]
      }
    },
    {
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#FF0000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(status.displayName),
                    "size": "xl",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#ffFF00",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#ff0000"
          },
          {
            "contents": [
              {
                "contents": [
                {
                  "type": "text",
                    "text": "☣️☣️☣️☣️☣️☣️☣️☣️",
                    "size": "md",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#00FF00",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#000000"
          },
          {
            "contents": [
              {
                "contents": [
                  {                  
                    "type": "text",
                    "text": "{}".format(status.statusMessage),
                    "size": "xs",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#00FF00",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
                },
                  {
                "type": "separator",
                  "color": "#ff0000"                 
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      }, #batas
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
        "text": "ᴄʀᴇᴀᴛᴏʀ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/%40jnx0914l",
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#FFffff"#0000"
      },
      {
        "type": "text",
        "text": "ᴏʀᴅᴇʀᴀɴ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/%40jnx0914l"
        },
        "align": "center"
      },
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "♦️sᴛᴀᴛᴜs♦️",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"        
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                maxbots.postFlex(to, data)

                        elif teambotmax == "me10":
                            if msg._from in admin or msg._from in owner:
                                contact = maxbots.getProfile()
                                mids = [contact.mid]
                                status = maxbots.getContact(sender)                             	
                                data = {
  "contents": [
    {
      "hero": {
       "aspectMode": "cover",
       "aspectRatio": "6:9",
       "type": "image",
       "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(sender).pictureStatus),
       "size": "full",
       "align": "center",
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#000000"
        },
        "header": {
          "backgroundColor": "#000000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(status.displayName),
                    "size": "xl",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#0000FF",
                    "align": "center"               
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },      
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [          
          {
            "type": "text",
            "text": "ＳＥＬＦＢＯＴＢＹＭＡＸ",
            "size": "lg",
            "wrap": True,
            "weight": "bold",
            "color": "#FF0000",
            "align": "center"           
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                maxbots.postFlex(to, data)

                        elif teambotmax == "me11":
                            if msg._from in admin or msg._from in owner:
                                contact = maxbots.getProfile()
                                mids = [contact.mid]
                                status = maxbots.getContact(sender)
                                warna1 = ("#81FF00","#00F2FF","#FFCC00","#FF0019","#FF00E5","#2D00FF","#FA0143","#00FF8C","#000000")
                                warnanya1 = random.choice(warna1)
                                data = {
                                        "type": "flex",
                                        "altText": "ＳＥＬＦＢＯＴＢＹＭＡＸ",
                                        "contents": {
                                                             "type": "bubble",
                                                             "header": {
                                                             "type": "box",
                                                             "layout": "vertical",
                                                             "spacing": "xs",
                                                             "contents": [
                                                               {
                                                                 "type": "text",
                                                                 "text": "ＳＥＬＦＢＯＴＢＹＭＡＸ",
                                                                 "wrap" : True,
                                                                 "weight": "bold",
                                                                 "color": warnanya1,
                                                                 "align": "center",
                                                                 "size":"md"
                                                               }
                                                             ]
                                                            },
                                                            "hero": {
                                                              "type": "image",
                                                              "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(sender).pictureStatus),
                                                              "size": "full",
                                                              "margin": "xxl"
                                                            },
                                                            "body": {
                                                              "type": "box",
                                                              "layout": "vertical",
                                                              "spacing": "md",
                                                              "contents": [
                                                                 {
                                                                   "type": "box",
                                                                   "layout": "horizontal",
                                                                   "spacing": "md",
                                                                   "contents": [
                                                                      {
                                                                        "url": "https://obs-sg.line-apps.com/myhome/c/download.nhn?userid=u308a4e0976ace6e2e2c234a09ef9f581&oid=1559471452",
                                                                        "type": "image",
                                                                        "size": "sm"
                                                                      },
                                                                      {
                                                                        "type": "separator",
                                                                       },
                                                                       {
                                                                         "type": "text",
                                                                         "text": "✯͜͡❂ ชื่อผู้ใช้ :\n{}".format(status.displayName),
                                                                         "wrap": True,
                                                                         "size": "md",
                                                                       }
                                                                   ]
                                                                 },
                                                                 {
                                                                   "type": "separator",
                                                                 },
                                                                 {
                                                                   "type": "box",
                                                                   "layout": "horizontal",
                                                                   "spacing": "md",
                                                                   "contents": [
                                                                      {
                                                                        "url": "https://obs-sg.line-apps.com/myhome/c/download.nhn?userid=u308a4e0976ace6e2e2c234a09ef9f581&oid=1559616082",
                                                                        "type": "image",
                                                                        "size": "sm"
                                                                      },
                                                                      {
                                                                        "type": "separator",
                                                                      },
                                                                      {
                                                                        "type": "text",
                                                                        "text": "✯͜͡❂ สถานะโปรไฟล์ :\n{}".format(status.statusMessage),
                                                                        "wrap": True,
                                                                        "size": "xs"
                                                                      }
                                                                   ]
                                                                 }
                                                              ]
                                                            },
                                                            "footer": {
                                                              "type": "box",
                                                              "layout": "vertical",
                                                              "contents": [
                                                                 {
                                                                   "type": "spacer",
                                                                   "size": "md"
                                                                 },
                                                                 {
                                                                   "type": "button",
                                                                   "action": {
                                                                     "type": "uri",
                                                                     "label": "༺ ติดต่อแอดมิน ༻",
                                                                     "uri": "http://line.me/ti/p/%40jnx0914l",
                                                                 },
                                                                  "style":"primary",
                                                                  "color": warnanya1
                                                              }
                                                        ]
                                                    }
                                                }
                                            }
                                maxbots.postTemplate(to, data)

                        elif teambotmax == "me12":
                          if msg._from in admin or msg._from in owner:
                            contact = maxbots.getContact(maxbotsMid)
                            data = {
"type":"bubble",
"styles":{
"body":{
"backgroundColor":"#696969"
},
"footer":{
"backgroundColor":"#FF0000"
}
},
"hero":{
"type":"image",
"url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus),
"aspectMode":"cover",
"aspectRatio":"1:1",
"size":"full",
"margin":"xxl"
},
"body":{
"type":"box",
"layout":"vertical",
"spacing":"md",
"contents":[{
"type":"box",
"layout":"baseline",
"contents":[{
"type":"icon",
"url":"https://os.line.naver.jp/os/p/{}".format(maxbotsMid),
"size":"xl"
},
{
"type":"text",
"text":"ƬΣΛM BӨƬ MΛX",
"weight":"bold",
"size":"md",
"align":"center",
"color":"#FF1493",
"action":{
"type":"uri",
"uri":"http://line.me/ti/p/%40jnx0914l"
}
}
]
},
{
"type":"separator",
"color":"#ffffff"
},
{
"type":"box",
"layout":"vertical",
"spacing":"xs",
"flex":2,
"contents":[{
"type":"separator",
"color":"#ffffff"
},
{
"type":"text",
"text":"ƬΣΛM BӨƬ MΛX",
"wrap":True,
"weight":"bold",
"align":"center",
"color":"#FFA500",
"size":"md"
},
{
"type":"separator",
"color":"#ffffff"
},
{
"type":"text",
"text":"MY STATUS PROFILE",
"wrap":True,
"weight":"bold",
"align":"center",
"color":"#ADFF2F",
"size":"xs"
},
{
"type":"text",
"text":"เช่าบอทกันรันถูกๆได้ที่นี่ครับ",
"wrap":True,
"align":"center",
"size":"xxs",
"color":"#FFFFE0"
}
]
},
{
"type":"separator",
"color":"#ffffff"
},
{
"type":"text",
"text":"กดไอคอนได้เลยครับ",
"wrap":True,
"size":"xs",
"margin":"md",
"weight":"bold",
"align":"center",
"color":"#FFFFE0",
"flex":0
},
{
"type":"box",
"layout":"horizontal",
"spacing":"xs",
"flex":2,
"contents":[{
"type":"image",
"url":"https://cdn.icon-icons.com/icons2/374/PNG/512/iPhone-WE-icon_37271.png",
"aspectMode":"cover",
"aspectRatio":"1:1",
"size":"xxs",
"action":{
"type":"uri",
"uri":"line://nv/camera/"
}
},
{
"type":"image",
"url":"https://cdn4.iconfinder.com/data/icons/social-media-pro-icons/1080/Whatsapp-01-512.png",
"aspectMode":"cover",
"aspectRatio":"1:1",
"size":"xxs",
"action":{
"type":"uri",
"uri":"https://wa.me/"
}
},
{
"type":"image",
"url":"https://cdn.iconscout.com/icon/free/png-256/settings-409-461608.png",
"aspectMode":"cover",
"aspectRatio":"1:1",
"size":"xxs",
"action":{
"type":"uri",
"uri":"line://nv/settings"
}
},
{
"type":"image",
"url":"https://i.downloadatoz.com/upload/android/icon/1/5/1/ef36baf8fac387f619c77fbaf613e735.jpg",
"aspectMode":"cover",
"aspectRatio":"1:1",
"size":"xxs",
"action":{
"type":"uri",
"uri":"line://nv/cameraRoll/multi"
}
},
{
"type":"image",
"url":"https://support.apple.com/content/dam/edam/applecare/images/en_US/icloud/featured-content-messages-icon_2x.png",
"aspectMode":"cover",
"aspectRatio":"1:1",
"size":"xxs",
"action":{
"type":"uri",
"uri":"http://line.me/ti/p/%40jnx0914l"
}
}
]
}
]
},
"footer":{
"type":"box",
"layout":"horizontal",
"contents":[{
"type":"text",
"text":"OWNER",
"wrap":True,
"align":"center",
"weight":"bold",
"color":"#000000",
"size":"xs",
"action":{
"type":"uri",
"uri":"http://line.me/ti/p/%40jnx0914l"
}
},
{
"type":"separator",
"color":"#000000"
},
{
"type":"text",
"text":"ADMIN",
"wrap":True,
"align":"center",
"weight":"bold",
"color":"#000000",
"size":"xs",
"action":{
"type":"uri",
"uri":"http://line.me/ti/p/%40jnx0914l"
}
}
]
}
}
                            data = {'type': 'flex','altText': 'ƬΣΛM BӨƬ MΛX','contents': data}
                            maxbots.postTemplate(to, data)

                        elif teambotmax == "me13":
                        	contact = maxbots.getContact(maxbotsMid)
                        	Max0 = random.choice(["#000000"])
                        	Max1 = random.choice(["#FFFFFF"])
                        	maxbots.reissueUserTicket()
                        	data = {
                                    "type":"flex",
                                    "altText": "ƬΣΛM BӨƬ MΛX",
                                    "contents":
                                    {
                                    "type":"bubble",
                                    "footer":
                                    {
                                        "type":"box",
                                        "layout":"horizontal",
                                        "contents":
                                        [
                                    {
                                        "color":Max1,
                                        "size":"xs",
                                        "wrap":True,
                                        "action":
                                            {
                                                "type":"uri",
                                                "uri":"line://app/1602687308-GXq4Vvk9?type=profile"
                                            },
                                                "type":"text",
                                                "text":"Me",
                                                "align":"center",
                                                "weight":"bold"
                                            },
                                        {
                                            "type":"separator",
                                            "color":Max1
                                            },
                                        {
                                            "color":Max1,
                                            "size":"xs",
                                            "wrap":True,
                                            "action":
                                                {
                                                    "type":"uri",
                                                    "uri":"http://line.me/ti/p/" + maxbots.getUserTicket().id
                                                },
                                                    "type":"text",
                                                    "text":"KEPO ME",
                                                    "align":"center",
                                                    "weight":"bold"
                                                }
                                            ]
                                        },
                                            "styles":
                                            {
                                            "footer":
                                            {
                                            "backgroundColor":Max0
                                            },
                                            "body":
                                            {
                                            "backgroundColor":"#683D65"
                                            }
                                        },
                                            "body":
                                            {
                                                "type":"box",
                                                "contents":
                                                [
                                            {
                                                "type":"box",
                                                "contents":
                                            [
                                        {
                                            "type":"separator",
                                            "color":Max0
                                        },
                                        {
                                            "aspectMode":"cover",
                                            "gravity":"bottom",
                                            "aspectRatio":"1:1",
                                            "size":"sm",
                                            "type":"image",
                                            "url":"https://obs-sg.line-apps.com/myhome/c/download.nhn?userid=u308a4e0976ace6e2e2c234a09ef9f581&oid=1559471452"
                                        },
                                        {
                                            "type":"separator",
                                            "color":Max0
                                        },
                                        {
                                            "type":"image",
                                            "aspectMode":"cover",
                                            "aspectRatio":"1:1",
                                            "size":"sm",
                                            "url":"https://obs-sg.line-apps.com/myhome/c/download.nhn?userid=u308a4e0976ace6e2e2c234a09ef9f581&oid=1559471452"
                                            },
                                            {
                                                "type":"separator",
                                                "color":Max0
                                            },
                                            {
                                                "type":"image",
                                                "aspectMode":"cover",
                                                "aspectRatio":"1:1",
                                                "size":"sm",
                                                "url":"https://obs-sg.line-apps.com/myhome/c/download.nhn?userid=u308a4e0976ace6e2e2c234a09ef9f581&oid=1559471452"
                                            },
                                            {
                                                "type":"separator",
                                                "color":Max0
                                            },
                                            {
                                                "type":"image",
                                                "aspectMode":"cover",
                                                "aspectRatio":"1:1",
                                                "size":"sm",
                                                "url":"https://obs-sg.line-apps.com/myhome/c/download.nhn?userid=u308a4e0976ace6e2e2c234a09ef9f581&oid=1559471452"
                                            },
                                            {
                                                "type":"separator",
                                                "color":Max0
                                            }
                                            ],
                                                "layout":"vertical",
                                                "spacing":"none",
                                                "flex":1
                                            },
                                            {
                                                "type":"separator",
                                                "color":Max0
                                            },
                                            {
                                                "type":"box",
                                                "contents":
                                            [
                                        {
                                            "type":"separator",
                                            "color":Max0
                                            },
                                        {
                                            "color":"#FC8AF3",
                                            "size":"md",
                                            "wrap":True,
                                            "type":"text",
                                            "text":"Uching Bots",
                                            "weight":"bold"
                                            },
                                        {
                                            "type":"separator",
                                            "color":Max0
                                            },
                                        {
                                            "color":"#413877",
                                            "size":"md",
                                            "wrap":True,
                                            "type":"text",
                                            "text":"{}".format(contact.displayName),
                                            "weight":"bold"
                                            },
                                        {
                                            "type":"separator",
                                            "color":Max0
                                            },
                                        {
                                            "color":Max0,
                                            "size":"xs",
                                            "wrap":True,
                                            "type":"text",
                                            "text":"Status Profile:",
                                            "weight":"bold"
                                            },
                                        {
                                            "type":"text",
                                            "text":"{}".format(contact.statusMessage),                                          
                                            "size":"xxs",
                                            "wrap":True,
                                            "color":"#e00f0f"
                                        }
                                    ],
                                        "layout":"vertical",
                                        "flex":2
                                        }
                                    ],
                                        "layout":"horizontal",
                                        "spacing":"md"
                                    },
                                        "hero":
                                    {
                                        "aspectMode":"cover",
                                        "margin":"xxl",
                                        "aspectRatio":"20:13",
                                        "size":"full",
                                        "type":"image",
                                        "url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                                    }
                                 }
                            }
                        	maxbots.postTemplate(to, data)

                        elif teambotmax == "me14":
                          if msg._from in admin or msg._from in owner:
                            contact = maxbots.getContact(maxbotsMid)
                            cu = maxbots.getProfileCoverURL(maxbotsMid)
                            image = str(cu)
                            data = {
                                    "type": "flex",
                                    "altText": "ƬΣΛM BӨƬ MΛX",
                                        "contents": {
                                        "styles": {
                                        "body": {
                                        "backgroundColor": "#F5CD30"
                                        },
                                        "footer": {
                                          "backgroundColor": "#000000"
                                        }
                                        },
                                            "type": "bubble",
                                                "hero": {
                                                    "type": "image",
                                                    "url": image,
                                                    "size": "full",
                                                    "aspectRatio": "1:1",
                                                    "aspectMode": "cover",
                                                },
                                            "body": {
                                            "contents": [
                                              {
                                                "contents": [
                                                  {
                                                    "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus),
                                                    "type": "image"
                                                  },
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                              },
                                              {
                                                "type": "separator",
                                                "color": "#DC143C"
                                              },
                                              {
                                                "contents": [
                                                  {
                                                    "text": "• ชื่อ : {}".format(contact.displayName),
                                                    "size": "xl",
                                                    "align": "center",
                                                    "color": "#FF0000",
                                                    "wrap": True,
                                                    "weight": "bold",
                                                    "type": "text"
                                                  }
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                              },
                                              {
                                                "type": "separator",
                                                "color": "#DC143C"
                                              },
                                              {
                                                "contents": [
                                                  {
                                                    "contents": [
                                                      {
                                                        "url": "https://media1.tenor.com/images/835dd1190b09afad8211ee59de37a339/tenor.gif",
                                                        "type": "icon",
                                                        "size": "md"
                                                      },
                                                      {
                                                        "text":"{}".format(contact.statusMessage),              
                                                        "size": "sm",
                                                        "margin": "none",
                                                        "color": "#6F4E37",
                                                        "wrap": True,
                                                        "weight": "regular",
                                                        "type": "text"
                                                      }
                                                    ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                                  }
                                                ],          
                                                "type": "box",
                                                "layout": "vertical"
                                              }
                                            ],
                                            "type": "box",
                                            "spacing": "md",
                                            "layout": "vertical"
                                        },
                                        "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "style": "link",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "༺ กดเพื่อเพิ่มเพื่อน ༻",
                                                    "uri": "https://line.me/ti/p/~" + maxbots.profile.userid
                                                }
                                        },
                                        {
                                            "type": "spacer",
                                            "size": "sm",
                                        }
                                    ],
                                    "flex": 0
                                    }
                                }
                            }
                            maxbots.postTemplate(to, data)

                        elif teambotmax == "me15":
                            if msg._from in admin:
                               contact = maxbots.getContact(msg._from)
                               cover = maxbots.getProfileCoverURL(msg._from)
                               LINKFOTO = "https://os.line.naver.jp/os/p/" + maxbotsMid
                               LINKVIDEO = "https://os.line.naver.jp/os/p/" + maxbotsMid + "/vp"
                               maxA = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785")
                               maxB = random.choice(maxA)
                               maxC= {
                                 "messages": [
                                    {
                                      "type": "flex",
                                      "altText": "ƬΣΛM BӨƬ MΛX",
                                      "contents":{
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://obs.line-scdn.net/{}".format(contact.picturePath),
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "uri": "https://obs.line-scdn.net/{}".format(contact.picturePath),
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "xs",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(contact.displayName),
            "wrap": True,
            "weight": "bold",
            "color": "#FF0000",
            "align": "center",
            "size": "md",
            "flex": 2
          },
          {
            "type": "separator",
            "color": "#000000"
          },
          {
            "type": "text", 
            "text": "{}".format(contact.statusMessage),
            "color": "#FF0000",
            "wrap": True,
            "weight": "bold",
            "align": "center",
            "size": "xs",
            "action": {
              "type": "uri",
              "uri": "line://app/1643963120-oYbGLGry?type=video&ocu={}&piu={}".format(LINKVIDEO,LINKFOTO)
            }
          }
        ]
      },
      "styles": {"body": {"backgroundColor": maxB},
       }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": cover,
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "uri": cover,
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "xs",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(contact.displayName),
            "wrap": True,
            "weight": "bold",
            "color": "#FF0000",
            "align": "center",
            "size": "md",
            "flex": 2
          },
          {
            "type": "separator",
            "color": "#000000"
          },
          {
            "type": "text", 
            "text": "༺ กดเพื่อเพิ่มเพื่อน ༻",
            "color": "#FF0000",
            "wrap": True,
            "weight": "bold",
            "align": "center",
            "size": "xs",
            "action": {
              "type": "uri",
              "uri": "line://app/1623679774-k9nBDB6b?type=video&ocu={}&piu={}".format(LINKVIDEO,LINKFOTO)
            }
          }
        ]
      },
      "styles": {"body": {"backgroundColor": maxB},
       }
    }
  ],
  "type": "carousel"
}
}
]
}
                               sendTemplateMax(to, maxC)

                        elif teambotmax == "me16":
                            if msg._from in admin:
                               contact = maxbots.getContact(msg._from)
                               LINKFOTO = "https://os.line.naver.jp/os/p/" + maxbotsMid
                               LINKVIDEO = "https://os.line.naver.jp/os/p/" + maxbotsMid + "/vp"
                               maxA = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785")
                               maxB = random.choice(maxA)
                               maxC = {
                                 "messages": [
                                    {
                                      "type": "flex",
                                      "altText": "ƬΣΛM BӨƬ MΛX",
                                      "contents":{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(contact.picturePath),
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://obs.line-scdn.net/{}".format(contact.picturePath),
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xs",
    "contents": [
      {
        "type": "text",
        "text": "{}".format(contact.displayName),
        "wrap": True,
        "weight": "bold",
        "color": "#FF0000",
        "align": "center",
        "size": "md",
        "flex": 2
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text", 
        "text": "{}".format(contact.statusMessage),
        "color": "#FF0000",
        "wrap": True,
        "weight": "bold",
        "align": "center",
        "size": "xs",
        "action": {
          "type": "uri",
          "uri": "line://app/1623679774-k9nBDB6b?type=video&ocu={}&piu={}".format(LINKVIDEO,LINKFOTO)
        }
      }
    ]
  },
  "styles": {"body": {"backgroundColor": maxB},
   }
}
}
]
}
                               sendTemplateMax(to, maxC)

                        elif teambotmax == "me17":
                            if msg._from in admin:
                                contact = maxbots.getProfile()
                                mids = [contact.mid]
                                status = maxbots.getContact(sender)
                                data = {
                                   "messages": [
                                      {
                                        "type": "flex",
                                        "altText": "ƬΣΛM BӨƬ MΛX",
                                        "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "flex": 2,
            "text": "{}".format(status.displayName),
            "size": "md",
            "wrap": True,
            "weight": "bold",
            "gravity": "center",
            "color": "#657383"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "type": "text",
            "text": "Status Profile:",
            "size": "xs",
            "weight": "bold",
            "wrap": True,
            "color": "#657383"
          },
          {
            "type": "text",
            "text": "{}".format(status.statusMessage),
            "size": "xs",
            "color": "#657383",
            "wrap": True
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#00BFFF"
    },
    "footer": {
      "backgroundColor": "#00BFFF"
    }
  },
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(sender).pictureStatus),
    "size": "full",
    "margin": "xxl"
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "Me",
        "size": "xs",
        "wrap": True,
        "weight": "bold",
        "color": "#E5E4E2",
        "action": {
          "type": "uri",
          "uri": "line://app/1643963120-oYbGLGry?type=profile"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      }
    ]
  }
}
}
]
}
                                sendTemplateMax(to, data)

                        elif teambotmax == "me18":
                            if msg._from in admin:
                                contact = maxbots.getProfile()
                                mids = [contact.mid]
                                status = maxbots.getContact(sender)                   
                                cover = maxbots.getProfileCoverURL(sender)
                                data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(sender).pictureStatus),
        "action": {
          "uri": "https://line.me/ti/p/~" + maxbots.profile.userid,
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#0000FF"
        },
        "header": {
          "backgroundColor": "#0000FF"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "℘ɧσtσ ℘гσʄıɭε",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#00FF00",
            "align": "center"            
          }
        ]
      },
      "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [{
              "type": "box",
              "layout": "horizontal",
              "contents": [{
                  "type": "button",
                  "flex": 2,
                  "style": "primary",
                  "color": "#FF0000",
                  "height": "sm",
                  "action": {
                      "type": "uri",
                      "label": "༺ กดเพื่อเพิ่มเพื่อน ༻",
                      "uri": "https://line.me/ti/p/~" + maxbots.profile.userid
                  }
              }]
          }]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "༺ ƬΣΛM BӨƬ MΛX ༻",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": cover,
        "action": {
          "uri": "https://line.me/ti/p/~" + maxbots.profile.userid,
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#0000FF"
        },
        "header": {
          "backgroundColor": "#0000FF"
        }
      },
      "type": "bubble",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "℘ɧσtσ ɕσvεг",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#00FF00",
            "align": "center"            
          }
        ]
      },
      "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [{
              "type": "box",
              "layout": "horizontal",
              "contents": [{
                  "type": "button",
                  "flex": 2,
                  "style": "primary",
                  "color": "#FF0000",
                  "height": "sm",
                  "action": {
                      "type": "uri",
                      "label": "༺ กดเพื่อเพิ่มเพื่อน ༻",
                      "uri": "https://line.me/ti/p/~" + maxbots.profile.userid
                  }
              }]
          }]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "༺ ƬΣΛM BӨƬ MΛX ༻",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    },
    {
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#0000FF"
        },
        "header": {
          "backgroundColor": "#0000FF"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(status.displayName),
                    "size": "xl",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#7FFF00",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "รtศtนร ℘rσʄıɭε :",
                    "size": "md",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#FFFF00",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(status.statusMessage),
                    "size": "xs",
                    "wrap": True,
                    "weight": "bold",
                    "color": "#F0FFFF",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [{
              "type": "box",
              "layout": "horizontal",
              "contents": [{
                  "type": "button",
                  "flex": 2,
                  "style": "primary",
                  "color": "#FF0000",
                  "height": "sm",
                  "action": {
                      "type": "uri",
                      "label": "༺ กดเพื่อเพิ่มเพื่อน ༻",
                      "uri": "https://line.me/ti/p/~" + maxbots.profile.userid
                  }
              }]
          }]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "༺ ƬΣΛM BӨƬ MΛX ༻",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                maxbots.postFlex(to, data)

                        elif teambotmax == "me19":
                            if msg._from in admin or msg._from in owner:
                                contact = maxbots.getProfile()
                                mids = [contact.mid]
                                status = maxbots.getContact(sender)                      	
                                data = {
                                        "type": "flex",
                                        "altText": "ƬΣΛM BӨƬ MΛX",
                                        "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": "รtศtนร ℘гσʄıɭε :",
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#7FFF00"
          },
          {
            "type": "text",
            "text": "{}".format(status.statusMessage),
            "align": "center",
            "size": "sm",
            "weight": "bold",
            "color": "#FF00FF",
            "wrap": True
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#0000FF"
    },
    "header": {
      "backgroundColor": "#0000FF"
    }
  },  
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#FF0000",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "༺ กดเพื่อเพิ่มเพื่อน ༻",
                  "uri": "https://line.me/ti/p/~" + maxbots.profile.userid
              }
          }]
      }]
  },
  "hero": {
    "aspectMode": "cover",
    "aspectRatio": "20:13",
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(sender).pictureStatus),
    "size": "full",
    "align": "center",
  },
  "header": {
    "type": "box",   
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "{}".format(status.displayName),
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#7FFF00",
        "align": "center"
      }
    ]
  }
}
}
                                maxbots.postTemplate(to, data)

                        elif teambotmax == 'me20':
                          if msg._from in admin or msg._from in owner:
                            kontaknyo = maxbots.getContact(maxbotsMid)
                            teambotmaxZ = {
                                "type": "flex",
                                "altText": "ƬΣΛM BӨƬ MΛX",
                                "contents": {
                                    "type": "bubble",
                                    "header": {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}".format(str(kontaknyo.displayName)),
                                                "color": "#000000",
                                                "align":"center",
                                                "weight": "bold",
                                                "size": "xl"
                                            }
                                        ]
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "https://os.line.naver.jp/os/p/{}".format(maxbotsMid),
                                        "size": "full",
                                        "aspectRatio": "1:1",
                                        "aspectMode": "cover",
                                        "action": {
                                            "type": "uri",
                                            "uri": "https://os.line.naver.jp/os/p/{}".format(maxbotsMid)
                                        }
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}".format(str(kontaknyo.statusMessage)),
                                                "color": "#000000",
                                                "align":"center",
                                                "wrap": True
                                            }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "spacer",
                                                "size": "sm"
                                            },
                                            {
                                                "type": "button",
                                                "style": "primary",
                                                "color": "#604800",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "ADD FRIEND",
                                                    "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2"
                                                }
                                            }
                                        ]
                                    },
                                    "styles": {
                                        "header": {
                                            "backgroundColor": "#f9bb00"
                                        },
                                        "hero": {
                                            "backgroundColor": "#ffda6b"
                                        },
                                        "body": {
                                            "backgroundColor": "#ffda6b"
                                        },
                                        "footer": {
                                            "backgroundColor": "#f9bb00"
                                        }
                                    }
                                }
                            }
                            maxbots.sendFlex(msg.to,teambotmaxZ)

                        elif teambotmax == "ตองสิบ":
                          if msg._from in admin or msg._from in owner:
                            maxbots.reissueUserTicket()
                            maxZ = {
                                   "type": "template",
                                   "altText": "ƬΣΛM BӨƬ MΛX",
                                   "template": {
                                      "type": "image_carousel",
                                      "columns": [
                                      {          
                                           "imageUrl": "https://www.img.live/images/2019/08/19/FB_IMG_1564112382658.jpg",
                                           "size": "xxxl",
                                           "aspectRatio": "1:2",
                                           "action": {
                                             "type": "uri",
                                             "uri": "https://line.me/ti/p/~" + maxbots.profile.userid,
                                             }
                                        },
                                        {
                                              "imageUrl":  "https://www.img.live/images/2019/08/19/received_397003854276519.jpg",
                                           "size": "xxxl",
                                           "aspectRatio": "1:2",
                                           "action": {
                                             "type": "uri",
                                             "uri": "https://line.me/ti/p/~" + maxbots.profile.userid,
                                             }
                                          },
                                          {
                                              "imageUrl": "https://www.img.live/images/2019/08/19/1564714852764.jpg",
                                           "size": "xxxl",
                                           "aspectRatio": "1:2",
                                           "action": {
                                             "type": "uri",
                                             "uri": "https://line.me/ti/p/~" + maxbots.profile.userid,
                                             }
                                          },
                                          {
                                              "imageUrl": "https://www.img.live/images/2019/08/19/1564891537501.jpg",
                                           "size": "xxxl",
                                           "aspectRatio": "1:2",
                                           "action": {
                                             "type": "uri",
                                             "uri": "https://line.me/ti/p/~" + maxbots.profile.userid,
                                             }
                                          },
                                          {
                                              "imageUrl": "https://www.img.live/images/2019/08/19/1565524859268.jpg",
                                           "size": "xxxl",
                                           "aspectRatio": "1:2",
                                           "action": {
                                             "type": "uri",
                                             "uri": "https://line.me/ti/p/~" + maxbots.profile.userid,
                                             }
                                          },
                                          {
                                              "imageUrl": "https://www.img.live/images/2019/08/19/1565525431599.jpg",
                                           "size": "xxxl",
                                           "aspectRatio": "1:2",
                                           "action": {
                                             "type": "uri",
                                             "uri": "https://line.me/ti/p/~" + maxbots.profile.userid,
                                             }
                                          },
                                          {
                                              "imageUrl": "https://www.img.live/images/2019/08/19/received_1073879236153945.jpg",
                                           "size": "xxxl",
                                           "aspectRatio": "1:2",
                                           "action": {
                                             "type": "uri",
                                             "uri": "https://line.me/ti/p/~" + maxbots.profile.userid,
                                             }
                                          },
                                          {
                                              "imageUrl": "https://www.img.live/images/2019/08/19/1564682589786.jpg",
                                           "size": "xxxl",
                                           "aspectRatio": "1:2",
                                           "action": {
                                             "type": "uri",
                                             "uri": "https://line.me/ti/p/~" + maxbots.profile.userid,
                                             }
                                          },
                                          {
                                              "imageUrl": "https://www.img.live/images/2019/08/19/1565525429969.jpg",
                                           "size": "xxxl",
                                           "aspectRatio": "1:2",
                                           "action": {
                                             "type": "uri",
                                             "uri": "https://line.me/ti/p/~" + maxbots.profile.userid,
                                             }
                                          },
                                          {
                                               "imageUrl": "https://www.img.live/images/2019/08/19/received_1840456406099679.jpg",
                                           "size": "xxxl",
                                           "aspectRatio": "1:2",
                                           "action": {
                                             "type": "uri",
                                             "uri": "https://line.me/ti/p/~" + maxbots.profile.userid,
                                            }
                                          }
                                        ]
                                      }
                                    }
                            maxbots.postTemplate(to, maxZ)
#===================================================================
                        elif teambotmax == "ฮ่าๆ":
                          if msg._from in maxbotsMid:
                            pesannya = {
                                "type": "template",
                                "altText": "{} ส่งสติกเกอร์".format(str(maxbots.getContact(maxbotsMid).displayName)),
                                "baseSize": {
                                    "height": 1040,
                                    "width": 1040
                                },
                                "template": {
                                "type": "image_carousel",
                                "columns": [{
                                    "imageUrl": "https://i.ibb.co/9Yp3hNN/AW1238395-00.gif",
                                    "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                            "x": 520,
                                            "y": 0,
                                            "width": 520,
                                            "height": 1040
                                        }
                                    }
                                }]
                                }
                            }
                            maxbots.sendFlex(msg.to,pesannya)
                            maxbots.unsendMessage(msg_id)
                            print ("Sticker Showed")    

                        elif teambotmax == "ของขวัญ":
                          if msg._from in maxbotsMid:
                            pesannya = {
                                "type": "template",
                                "altText": "{} ส่งสติกเกอร์".format(str(maxbots.getContact(maxbotsMid).displayName)),
                                "baseSize": {
                                    "height": 1040,
                                    "width": 1040
                                },
                                "template": {
                                "type": "image_carousel",
                                "columns": [{
                                    "imageUrl": "https://media.giphy.com/media/d7ShmJHWybIydmxZXP/giphy.gif",
                                    "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                            "x": 520,
                                            "y": 0,
                                            "width": 520,
                                            "height": 1040
                                        }
                                    }
                                }]
                                }
                            }
                            maxbots.sendFlex(msg.to,pesannya)
                            maxbots.unsendMessage(msg_id)
                            print ("Sticker Showed")    

                        elif teambotmax == "ฟัคยู":
                          if msg._from in maxbotsMid:
                            pesannya = {
                                "type": "template",
                                "altText": "{} ส่งสติกเกอร์".format(str(maxbots.getContact(maxbotsMid).displayName)),
                                "baseSize": {
                                    "height": 1040,
                                    "width": 1040
                                },
                                "template": {
                                "type": "image_carousel",
                                "columns": [{
                                    "imageUrl": "https://media.giphy.com/media/hs0pZaEWmx86uxUtKJ/giphy.gif",
                                    "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                            "x": 520,
                                            "y": 0,
                                            "width": 520,
                                            "height": 1040
                                        }
                                    }
                                }]
                                }
                            }
                            maxbots.sendFlex(msg.to,pesannya)
                            maxbots.unsendMessage(msg_id)
                            print ("Sticker Showed")    

                        elif teambotmax == "555555555555":
                          if msg._from in maxbotsMid:
                            pesannya = {
                                "type": "template",
                                "altText": "{} ส่งสติกเกอร์".format(str(maxbots.getContact(maxbotsMid).displayName)),
                                "baseSize": {
                                    "height": 1040,
                                    "width": 1040
                                },
                                "template": {
                                "type": "image_carousel",
                                "columns": [{
                                    "imageUrl": "https://media.giphy.com/media/gHohwrHIWhU8UboBsl/giphy.gif",
                                    "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                            "x": 520,
                                            "y": 0,
                                            "width": 520,
                                            "height": 1040
                                        }
                                    }
                                }]
                                }
                            }
                            maxbots.sendFlex(msg.to,pesannya)
                            maxbots.unsendMessage(msg_id)
                            print ("Sticker Showed")    

                        elif teambotmax == "ใช่":
                          if msg._from in maxbotsMid:
                            pesannya = {
                                "type": "template",
                                "altText": "{} ส่งสติกเกอร์".format(str(maxbots.getContact(maxbotsMid).displayName)),
                                "baseSize": {
                                    "height": 1040,
                                    "width": 1040
                                },
                                "template": {
                                "type": "image_carousel",
                                "columns": [{
                                    "imageUrl": "https://media.giphy.com/media/Q5FEcpCJPOVAigoHqZ/giphy.gif",
                                    "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                            "x": 520,
                                            "y": 0,
                                            "width": 520,
                                            "height": 1040
                                        }
                                    }
                                }]
                                }
                            }
                            maxbots.sendFlex(msg.to,pesannya)
                            maxbots.unsendMessage(msg_id)
                            print ("Sticker Showed")    

                        elif teambotmax == "เคร":
                          if msg._from in maxbotsMid:
                            pesannya = {
                                "type": "template",
                                "altText": "{} ส่งสติกเกอร์".format(str(maxbots.getContact(maxbotsMid).displayName)),
                                "baseSize": {
                                    "height": 1040,
                                    "width": 1040
                                },
                                "template": {
                                "type": "image_carousel",
                                "columns": [{
                                    "imageUrl": "https://media.giphy.com/media/Q93nnpN6qu2xdl08A3/giphy.gif",
                                    "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                            "x": 520,
                                            "y": 0,
                                            "width": 520,
                                            "height": 1040
                                        }
                                    }
                                }]
                                }
                            }
                            maxbots.sendFlex(msg.to,pesannya)
                            maxbots.unsendMessage(msg_id)
                            print ("Sticker Showed")    

                        elif teambotmax == "อิอิ":
                          if msg._from in maxbotsMid:
                            pesannya = {
                                "type": "template",
                                "altText": "{} ส่งสติกเกอร์".format(str(maxbots.getContact(maxbotsMid).displayName)),
                                "baseSize": {
                                    "height": 1040,
                                    "width": 1040
                                },
                                "template": {
                                "type": "image_carousel",
                                "columns": [{
                                    "imageUrl": "https://media.giphy.com/media/MAWeODSGxRQT4iiRDg/giphy.gif",
                                    "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                            "x": 520,
                                            "y": 0,
                                            "width": 520,
                                            "height": 1040
                                        }
                                    }
                                }]
                                }
                            }
                            maxbots.sendFlex(msg.to,pesannya)
                            maxbots.unsendMessage(msg_id)
                            print ("Sticker Showed")    

                        elif teambotmax == "ฝันดี":
                          if msg._from in maxbotsMid:
                            pesannya = {
                                "type": "template",
                                "altText": "{} ส่งสติกเกอร์".format(str(maxbots.getContact(maxbotsMid).displayName)),
                                "baseSize": {
                                    "height": 1040,
                                    "width": 1040
                                },
                                "template": {
                                "type": "image_carousel",
                                "columns": [{
                                    "imageUrl": "https://media.giphy.com/media/hVyS1bq5HBV12g5bkZ/giphy.gif",
                                    "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                            "x": 520,
                                            "y": 0,
                                            "width": 520,
                                            "height": 1040
                                        }
                                    }
                                }]
                                }
                            }
                            maxbots.sendFlex(msg.to,pesannya)
                            maxbots.unsendMessage(msg_id)
                            print ("Sticker Showed")    

                        elif teambotmax == "มอนิ่ง":
                          if msg._from in maxbotsMid:
                            pesannya = {
                                "type": "template",
                                "altText": "{} ส่งสติกเกอร์".format(str(maxbots.getContact(maxbotsMid).displayName)),
                                "baseSize": {
                                    "height": 1040,
                                    "width": 1040
                                },
                                "template": {
                                "type": "image_carousel",
                                "columns": [{
                                    "imageUrl": "https://media.giphy.com/media/gHhI4WekeTSX3kQhcs/giphy.gif",
                                    "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                            "x": 520,
                                            "y": 0,
                                            "width": 520,
                                            "height": 1040
                                        }
                                    }
                                }]
                                }
                            }
                            maxbots.sendFlex(msg.to,pesannya)
                            maxbots.unsendMessage(msg_id)
                            print ("Sticker Showed")    

                        elif teambotmax == "ขอบคุณ":
                          if msg._from in maxbotsMid:
                            pesannya = {
                                "type": "template",
                                "altText": "{} ส่งสติกเกอร์".format(str(maxbots.getContact(maxbotsMid).displayName)),
                                "baseSize": {
                                    "height": 1040,
                                    "width": 1040
                                },
                                "template": {
                                "type": "image_carousel",
                                "columns": [{
                                    "imageUrl": "https://media.giphy.com/media/L4fYPdyw8DbazciATY/giphy.gif",
                                    "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                            "x": 520,
                                            "y": 0,
                                            "width": 520,
                                            "height": 1040
                                        }
                                    }
                                }]
                                }
                            }
                            maxbots.sendFlex(msg.to,pesannya)
                            maxbots.unsendMessage(msg_id)
                            print ("Sticker Showed")    

                        elif teambotmax == "อะไรๆ":
                          if msg._from in maxbotsMid:
                            pesannya = {
                                "type": "template",
                                "altText": "{} ส่งสติกเกอร์".format(str(maxbots.getContact(maxbotsMid).displayName)),
                                "baseSize": {
                                    "height": 1040,
                                    "width": 1040
                                },
                                "template": {
                                "type": "image_carousel",
                                "columns": [{
                                    "imageUrl": "https://media.giphy.com/media/Tg1X4fl6TAUw8D3ytK/giphy.gif",
                                    "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                            "x": 520,
                                            "y": 0,
                                            "width": 520,
                                            "height": 1040
                                        }
                                    }
                                }]
                                }
                            }
                            maxbots.sendFlex(msg.to,pesannya)
                            maxbots.unsendMessage(msg_id)
                            print ("Sticker Showed")    

                        elif teambotmax == "ขำ":
                          if msg._from in maxbotsMid:
                            pesannya = {
                                "type": "template",
                                "altText": "{} ส่งสติกเกอร์".format(str(maxbots.getContact(maxbotsMid).displayName)),
                                "baseSize": {
                                    "height": 1040,
                                    "width": 1040
                                },
                                "template": {
                                "type": "image_carousel",
                                "columns": [{
                                    "imageUrl": "https://media.giphy.com/media/SU7xfoYuAb4xnslrc4/giphy.gif",
                                    "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                            "x": 520,
                                            "y": 0,
                                            "width": 520,
                                            "height": 1040
                                        }
                                    }
                                }]
                                }
                            }
                            maxbots.sendFlex(msg.to,pesannya)
                            maxbots.unsendMessage(msg_id)
                            print ("Sticker Showed")    

                        elif teambotmax == "ร้อน":
                          if msg._from in maxbotsMid:
                            pesannya = {
                                "type": "template",
                                "altText": "{} ส่งสติกเกอร์".format(str(maxbots.getContact(maxbotsMid).displayName)),
                                "baseSize": {
                                    "height": 1040,
                                    "width": 1040
                                },
                                "template": {
                                "type": "image_carousel",
                                "columns": [{
                                    "imageUrl": "https://media.giphy.com/media/U1gaxWVTyeqp8lSfdI/giphy.gif",
                                    "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                            "x": 520,
                                            "y": 0,
                                            "width": 520,
                                            "height": 1040
                                        }
                                    }
                                }]
                                }
                            }
                            maxbots.sendFlex(msg.to,pesannya)
                            maxbots.unsendMessage(msg_id)
                            print ("Sticker Showed")    

                        elif teambotmax == "รัก":
                          if msg._from in maxbotsMid:
                            pesannya = {
                                "type": "template",
                                "altText": "{} ส่งสติกเกอร์".format(str(maxbots.getContact(maxbotsMid).displayName)),
                                "baseSize": {
                                    "height": 1040,
                                    "width": 1040
                                },
                                "template": {
                                "type": "image_carousel",
                                "columns": [{
                                    "imageUrl": "https://media.giphy.com/media/WQZpY0ZAVKWvnIzrJC/giphy.gif",
                                    "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                            "x": 520,
                                            "y": 0,
                                            "width": 520,
                                            "height": 1040
                                        }
                                    }
                                }]
                                }
                            }
                            maxbots.sendFlex(msg.to,pesannya)
                            maxbots.unsendMessage(msg_id)
                            print ("Sticker Showed")    

                        elif teambotmax == "ไม่":
                          if msg._from in maxbotsMid:
                            pesannya = {
                                "type": "template",
                                "altText": "{} ส่งสติกเกอร์".format(str(maxbots.getContact(maxbotsMid).displayName)),
                                "baseSize": {
                                    "height": 1040,
                                    "width": 1040
                                },
                                "template": {
                                "type": "image_carousel",
                                "columns": [{
                                    "imageUrl": "https://media.giphy.com/media/gK5gdtHhz2dMu3Fnmy/giphy.gif",
                                    "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                            "x": 520,
                                            "y": 0,
                                            "width": 520,
                                            "height": 1040
                                        }
                                    }
                                }]
                                }
                            }
                            maxbots.sendFlex(msg.to,pesannya)
                            maxbots.unsendMessage(msg_id)
                            print ("Sticker Showed")    

                        elif teambotmax == "help js":
                          if msg._from in admin:
                            teambotmaxText(to, "Help Message :\n\n1. #kickall\n2. #kick < ชื่อ >\n3. #bypass")

                        elif teambotmax == "#kickall":
                          if msg._from in admin:
                            xyz = maxbots.getGroup(to)
                            mem = [c.mid for c in xyz.members]
                            targets = []
                            for x in mem:
                              if x not in ["uc14c3d87a1123df7c8ffa9d7402e59a2","udcb20768bca5986eaa4a1c35d0b10ef9",maxbots.profile.mid]:targets.append(x)
                            if targets:
                              imnoob = 'simple.js gid={} token={} app={}'.format(to, maxbots.authToken, "IOSIPAD\t9.19.1\tiPhone X\t11.2.5")
                              for target in targets:
                                imnoob += ' uid={}'.format(target)
                              success = execute_js(imnoob)
                              if success:maxbots.sendMessage(to, "Success kick %i members." % len(targets))
                              else:maxbots.sendMessage(to, "Failed kick %i members." % len(targets))
                            else:maxbots.sendMessage(to, "Target not found.")

                        elif teambotmax == "#bypass":
                          if msg._from in admin:
                            xyz = maxbots.getGroup(to)
                            if xyz.invitee == None:pends = []
                            else:pends = [c.mid for c in xyz.invitee]
                            targp = []
                            for x in pends:
                              if x not in ["uc14c3d87a1123df7c8ffa9d7402e59a2","udcb20768bca5986eaa4a1c35d0b10ef9",maxbots.profile.mid]:targp.append(x)
                            mems = [c.mid for c in xyz.members]
                            targk = []
                            for x in mems:
                              if x not in ["uc14c3d87a1123df7c8ffa9d7402e59a2","udcb20768bca5986eaa4a1c35d0b10ef9",maxbots.profile.mid]:targk.append(x)
                            imnoob = 'dual.js gid={} token={}'.format(to, maxbots.authToken)
                            for x in targp:imnoob += ' uid={}'.format(x)
                            for x in targk:imnoob += ' uik={}'.format(x)
                            execute_js(imnoob)

                        elif teambotmax.startswith("#kick "):
                          if msg._from in admin:
                             sep = text.split(" ")
                             midn = text.replace(sep[0] + " ","")
                             hmm = text.lower()
                             G = maxbots.getGroup(msg.to)
                             members = [G.mid for G in G.members]
                             targets = []
                             imnoob = 'simple.js gid={} token={} app={}'.format(to, maxbots.authToken, "IOSIPAD\t9.19.1\tiPhone X\t11.2.5")
                             for x in members:
                                 contact = maxbots.getContact(x)
                                 msg = op.message
                                 testt = contact.displayName.lower()
                                 if midn in testt:targets.append(contact.mid)
                             if targets == []:return maxbots.sendMessage(to,"• ไม่พบชื่อ "+midn)
                             for target in targets:
                               imnoob += ' uid={}'.format(target)
                             success = execute_js(imnoob)

                        elif teambotmax.startswith('#แทค '):
                          if msg._from in admin:
                            msg.text = maxbots.mycmd(msg.text,wait)
                            if msg.toType == 0:
                                maxbots.datamention(to,'Spam',[to]*int(teambotmax.split(" ")[1]))
                            elif msg.toType == 2:
                                gs = maxbots.getGroup(to)
                                nama = [contact.mid for contact in gs.members]
                                try:
                                    if 'MENTION' in msg.contentMetadata.keys()!=None:maxbots.datamention(to,'Spam',[eval(msg.contentMetadata["MENTION"])["MENTIONEES"][0]["M"]]*int(cmd.split(" ")[1]))
                                    else:texst = maxbots.adityasplittext(cmd)
                                    gs = maxbots.getGroup(to)
                                    nama = [contact.mid for contact in gs.members];nama.remove(maxbots.getProfile().mid)
                                    c = ['{}:-:{}'.format(a.displayName,a.mid) for a in gs.members]
                                    c.sort()
                                    b = []
                                    for s in c:
                                        if len(texst) == 1:dd = s[len(texst)-1].lower()
                                        else:dd = s[:len(texst)].lower()
                                        if texst in dd:b.append(s.split(':-:')[1])
                                    maxbots.datamention(to,'Mention By Abjad',b)
                                except:maxbots.adityaarchi(wait,'Mention','',to,maxbots.adityasplittext(msg.text),msg,'\n├Group: '+gs.name[:20],nama=nama)
#=====================================================================================================================
                        if "/ti/g/" in msg.text.lower():
                            if settings["autoJoinTicket"] == True:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(text)
                                n_links = []
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    group = maxbots.findGroupByTicket(ticket_id)
                                    maxbots.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    teambotmaxText(group.id, "• ประสบความสำเร็จในการเข้าร่วม %s" % str(group.name))
                                    break
#=====================================================================================================================
                        if msg.toType != 0 and msg.toType == 2:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    if ryyn in mention["M"]:
                                        if ryyn in mention["M"]:
                                            if to not in tagme['ROM']:
                                                tagme['ROM'][to] = {}
                                            if sender not in tagme['ROM'][to]:
                                                tagme['ROM'][to][sender] = {}
                                            if 'msg.id' not in tagme['ROM'][to][sender]:
                                                tagme['ROM'][to][sender]['msg.id'] = []
                                            if 'waktu' not in tagme['ROM'][to][sender]:
                                                tagme['ROM'][to][sender]['waktu'] = []
                                            tagme['ROM'][to][sender]['msg.id'].append(msg.id)
                                            tagme['ROM'][to][sender]['waktu'].append(msg.createdTime)

                            elif receiver in temp_flood:
                                if temp_flood[receiver]["expire"] == True:
                                    if teambotmax == "open":
                                        temp_flood[receiver]["expire"] = False
                                        temp_flood[receiver]["time"] = time.time()
                                        teambotmaxText(to, "✯͜͡❂ ƬΣΛM BӨƬ MΛX")
                                    return
                                elif time.time() - temp_flood[receiver]["time"] <= 5:
                                    temp_flood[receiver]["flood"] += 1
                                    if temp_flood[receiver]["flood"] >= 20:
                                        temp_flood[receiver]["flood"] = 0
                                        temp_flood[receiver]["expire"] = True
                                        ret_ = "Spam terdetect DI Ruangan"
                                        contact = maxbots.getContact(sender)
                                        warna1 = ("#000080","#0000CD","#00FA9A","#FFA500","#98FB98","#00FF7F","#D8BFD8","000000","#40E0D0")
                                        warnanya1 = random.choice(warna1)
                                        data = {
                                                "messages": [
                                                          {
                                                            "type": "flex",
                                                            "altText": "ＳＥＬＦＢＯＴＢＹＭＡＸ",
                                                            "contents":{
"contents":[
{
  "type": "bubble",
  "size": "giga",
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
    "size": "full",
    "aspectRatio": "1:1",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xs",
    "contents": [ 
      {
        "type": "text",
        "text":  "{}".format(contact.displayName),
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "align": "center",
        "size": "md",
        "flex": 2
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text", 
        "text": "{}".format(str(ret_)),
        "color": "#000000",
        "wrap": True,
        "weight": "bold",
        "align": "center",
        "size": "xs",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/%40jnx0914l",
        }
      }
    ]
  },
  "styles": {"body": {"backgroundColor": warnanya1},
   }
}
],
"type": "carousel"
}
}
]
}
                                        sendTemplateMax(to, data)
                                else:
                                    temp_flood[receiver]["flood"] = 0
                                temp_flood[receiver]["time"] = time.time()
                            else:
                                temp_flood[receiver] = {
                                 "time": time.time(),
                                 "flood": 0,
                                 "expire": False
                                }
            except Exception as error:
                logError(error)
#=======================================================================================================
        if op.type == 26:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                teambotmax = command(text)
                for teambotmax in teambotmax.split(" & "):
                    setKey = settings["keyCommand"].title()
                    if settings["setKey"] == False:
                        setKey = ''
                    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                        if msg.toType == 0:
                            if sender != maxbots.profile.mid:
                                to = sender
                            else:
                                to = receiver
                        elif msg.toType == 1:
                            to = receiver
                        elif msg.toType == 2:
                            to = receiver
                        if msg.contentType == 0:
                            if to in offbot:
                                return
                        elif msg.contentType == 16:
                            if settings["checkPost"] == True:
                                try:
                                    ret_ = "╭───「 Details Post 」"
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        contact = maxbots.getContact(sender)
                                        auth = "\n│ • Penulis : {}".format(str(contact.displayName))
                                    else:
                                        auth = "\n│ • Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                    purl = "\n│ • URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                    ret_ += auth
                                    ret_ += purl
                                    if "mediaOid" in msg.contentMetadata:
                                        object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                        if msg.contentMetadata["mediaType"] == "V":
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\n│ • Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                                murl = "\n│ • Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\n│ • Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                                murl = "\n│ • Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                            ret_ += murl
                                        else:
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\n│ • Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\n│ • Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        ret_ += ourl
                                    if "stickerId" in msg.contentMetadata:
                                        stck = "\n│ • Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                        ret_ += stck
                                    if "text" in msg.contentMetadata:
                                        text = "\n│ • Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                        ret_ += text
                                    ret_ += "\n╰───「 Finish 」"
                                    teambotmaxText(to, str(ret_))
                                except:
                                    teambotmaxText(to, "Post tidak valid")
            except Exception as error:
                logError(error)
#==========================================================================================================
        if op.type == 25:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                teambotmax = command(text)
                for teambotmax in teambotmax.split(" & "):
                    setKey = settings["keyCommand"].title()
                    if settings["setKey"] == False:
                        setKey = ''
                    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                        if msg.toType == 0:
                            if sender != maxbots.profile.mid:
                                to = sender
                            else:
                                to = receiver
                        elif msg.toType == 1:
                            to = receiver
                        elif msg.toType == 2:
                            to = receiver
                        if msg.contentType == 0:
                            if to in offbot:
                                return
                            if teambotmax == "logout":
                                maxbots.generateReplyMessage(msg.id)
                                maxbots.sendReplyMessage(msg.id, to, "• เชลบอทของคุณออกจากระบบแล้ว ♪")
                                sys.exit("[ INFO ] BOT SHUTDOWN")

                            elif teambotmax == "reset":
                                restart = "Restarting Sukses"
                                contact = maxbots.getContact(sender)
                                teambotmaxText(to, restart)
                                restartBot()

                            elif teambotmax == "speed" or teambotmax == "สปีด":
                            	get_profile_time_start = time.time()
                            	get_profile = maxbots.getProfile()
                            	get_profile_time = time.time() - get_profile_time_start
                            	speed = " {} detik".format(str(get_profile_time))
                            	teambotmaxText(to, speed)
        
                            elif teambotmax == "sp":
                                start = time.time()                              
                                elapsed_time = time.time() - start
                                took = time.time() - start
                                teambotmaxText(to,"「 Speed 」\n - Took : %.3fms\n - Taken: %.10f" % (took,elapsed_time/10))

                            elif teambotmax == "sp1":
                                 start = time.time()                               
                                 maxbots.sendReplyMessage(msg.id, to, "Checking the speed of the bots...")                               
                                 elapsed_time = time.time() - start
                                 maxbots.sendReplyMessage(msg.id, to, "Speed {} detik".format(str(elapsed_time/100)))

                            elif teambotmax == "gid":
                                gid = maxbots.getGroupIdsJoined()
                                h = ""
                                for i in gid:
                                    h += "✯͜͡❂ %s:\n%s\n\n" % (maxbots.getGroup(i).name,i)
                                maxbots.sendReplyMessage(msg_id, to,"List Group\n\n"+h)

                            elif teambotmax == "namagroup":
                                gid = maxbots.getGroup(to)
                                sendTextMax3(to, "🔹 Display Name🔹\n✯͜͡❂  {}".format(gid.displayName))

                            elif teambotmax == "fotogroup":
                                gid = maxbots.getGroup(to)
                                maxbots.sendReplyImageWithURL(msg.id, to,"http://dl.profile.line-cdn.net/{}".format(gid.pictureStatus))

                            elif teambotmax == "reject":
                                  ginvited = maxbots.getGroupIdsInvited()
                                  if ginvited != [] and ginvited != None:
                                      for gid in ginvited:
                                          maxbots.rejectGroupInvitation(gid)
                                          time.sleep(2)
                                      teambotmaxText(to, "❂➣ ʙᴇʀʜᴀsɪʟ ᴛᴏʟᴀᴋ sᴇʙᴀɴʏᴀᴋ {} ᴜɴᴅᴀɴɢᴀɴ ɢʀᴏᴜᴘ".format(str(len(ginvited))))
                                  else:
                                      teambotmaxText(to, "❂➣ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴜɴᴅᴀɴɢᴀɴ ʏᴀɴɢ ᴛᴇʀᴛᴜɴᴅᴀ")

                            elif teambotmax == ".ลบรัน":
                                gid = maxbots.getGroupIdsInvited()
                                start = time.time()
                                for i in gid:
                                    maxbots.rejectGroupInvitation(i)
                                    time.sleep(2)
                                elapsed_time = time.time() - start
                                teambotmaxText(to, "Time spent %s second" % (elapsed_time))

                            elif teambotmax == "ลบรัน":
                                gid = maxbots.getGroupIdsInvited()
                                for i in gid:
                                    maxbots.acceptGroupInvitation(i)
                                    maxbots.leaveGroup(i)
                                    time.sleep(2)
                                    print(i)
                                teambotmaxText(to,"✯͜͡❂ ลบรันเรียบร้อย")

                            elif teambotmax == "@clear":
                                gids = maxbots.getGroupIdsInvited()
                                xyzs = []
                                for x in gids:xyzs.append(x)
                                for x in gids:
                                  maxbots.acceptGroupInvitation(x)
                                for x in xyzs:
                                  maxbots.leaveGroup(x)
                                  time.sleep(2)
                                teambotmaxText(to, "ʙᴇʀʜᴀsɪʟ ᴛᴏʟᴀᴋ sᴇʙᴀɴʏᴀᴋ %i ᴜɴᴅᴀɴɢᴀɴ ɢʀᴏᴜᴘ." % len(xyzs))

                            elif teambotmax == "clear spam":
                                ginvited = maxbots.getGroupIdsInvited()
                                if ginvited != [] and ginvited != None:
                                    for gid in ginvited:
                                        maxbots.acceptGroupInvitation(gid)
                                        maxbots.leaveGroup(gid)
                                        time.sleep(2)
                                    teambotmaxText(to, "• ʙᴇʀʜᴀsɪʟ ᴛᴏʟᴀᴋ sᴇʙᴀɴʏᴀᴋ {} ᴜɴᴅᴀɴɢᴀɴ ɢʀᴏᴜᴘ".format(str(len(ginvited))))
                                else:
                                    teambotmaxText(to, "• ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴜɴᴅᴀɴɢᴀɴ ʏᴀɴɢ ᴛᴇʀᴛᴜɴᴅᴀ")

                            elif teambotmax == "reset error":
                                    with open('errorLog.txt', 'w') as er:
                                        error = er.write("")
                                    maxbots.sendMessageWithFooter(to, str(error))

                            elif teambotmax.startswith("setkey: "):
                                sep = text.split(" ")
                                key = text.replace(sep[0] + " ","")
                                settings["keyCommand"] = str(key).lower()
                                teambotmaxText(to, "Setkey dirubah menjadi : 「{}」".format(str(key).lower()))

                            elif teambotmax == "help" or teambotmax == "คำสั่ง":
                                teambotmaxZ = {
                                        "type": "flex",
                                        "altText": "ƬΣΛM BӨƬ MΛX",
                                        "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://www.img.live/images/2019/12/24/1577201181725.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "HELP - MESSAGE",
                    "size": "xxl",
                    "color": "#ffffff",
                    "weight": "bold",
                    "align": "center"
                  }
                ]
              },
              {
                "type": "separator"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Help menu",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Help media",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Help sticker",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Help set",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Help setting",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Help group",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Help protect",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Help profile",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Help spam",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Help friend",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Help special",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Help kicker",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Help js",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "text",
                        "text": "⚡ กดตรงนี้เพื่อเพิ่มเพื่อน ⚡",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/~maxxxxxxxxxxxxxxxx"
                }
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
#            "backgroundColor": "#03303Acc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          }
        ],
        "paddingAll": "0px",
        "cornerRadius": "17px",
        "borderColor": "#000000",
        "borderWidth": "3px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://www.img.live/images/2019/12/24/1577201181725.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "HELP - MESSAGE",
                    "size": "xxl",
                    "color": "#ffffff",
                    "weight": "bold",
                    "align": "center"
                  }
                ]
              },
              {
                "type": "separator"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Ban 「 @ 」",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Unban 「 @ 」",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Banlist",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Bc",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Cb",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Killban",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Status",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Runtime",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "About",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Speed",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Tag",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Remove",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Groupinfo",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "text",
                        "text": "⚡ กดตรงนี้เพื่อเพิ่มเพื่อน ⚡",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/~maxxxxxxxxxxxxxxxx"
                }
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
#            "backgroundColor": "#03303Acc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          }
        ],
        "paddingAll": "0px",
        "cornerRadius": "17px",
        "borderColor": "#000000",
        "borderWidth": "3px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://www.img.live/images/2019/12/24/1577201181725.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "HELP - MESSAGE",
                    "size": "xxl",
                    "color": "#ffffff",
                    "weight": "bold",
                    "align": "center"
                  }
                ]
              },
              {
                "type": "separator"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Grouplist",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Memberlist",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Memberpict",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Pendinglist",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Open",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Close",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Url",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Myprofile",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Mymid",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Mybio",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Myname",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Mycover",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Mypict",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "text",
                        "text": "⚡ กดตรงนี้เพื่อเพิ่มเพื่อน ⚡",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/~maxxxxxxxxxxxxxxxx"
                }
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
#            "backgroundColor": "#03303Acc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          }
        ],
        "paddingAll": "0px",
        "cornerRadius": "17px",
        "borderColor": "#000000",
        "borderWidth": "3px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://www.img.live/images/2019/12/24/1577201181725.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "HELP - MESSAGE",
                    "size": "xxl",
                    "color": "#ffffff",
                    "weight": "bold",
                    "align": "center"
                  }
                ]
              },
              {
                "type": "separator"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "YouTube 「 ค้นหา 」",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "YouTube2 「 ค้นหา 」",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "YouTube3 「 ค้นหา 」",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Foto 「 ค้นหา 」",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Cvp 「 ลิ้งยูทูป 」",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Tiktok 「 ไอดี 」",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Mp3 「 ชื่อเพลง 」",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Music 「 ชื่อเพลง 」",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Musik 「 ชื่อเพลง 」",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Getcover 「 @ 」",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Getbio 「 @ 」",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Getname 「 @ 」",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Getmid 「 @ 」",
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "regular"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "text",
                        "text": "⚡ กดตรงนี้เพื่อเพิ่มเพื่อน ⚡",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/~maxxxxxxxxxxxxxxxx"
                }
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
#            "backgroundColor": "#03303Acc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          }
        ],
        "paddingAll": "0px",
        "cornerRadius": "17px",
        "borderColor": "#000000",
        "borderWidth": "3px"
      }
    }
  ]
}
}
                                maxbots.postTemplate(to, teambotmaxZ) 

                            elif teambotmax == "help1":
                                data = {
                                            "type": "template",
                                            "altText": "ＳＥＬＦＢＯＴＢＹＭＡＸ",
                                            "template": {
                                                "type": "carousel",
                                                "columns": [
                                                    {
                                                        "thumbnailImageUrl": "https://obs-sg.line-apps.com/myhome/c/download.nhn?userid=u308a4e0976ace6e2e2c234a09ef9f581&oid=1559471452",
                                                        "title": "MENU",
                                                        "text": "To Use This command just menu help",
                                                        "defaultAction": {
                                                            "type": "uri",
                                                            "uri": "line://app/1623679774-k9nBDB6b?type=text&text=menu"
                                                        },
                                                        "actions": [
                                                            {
                                                                "type": "uri",
                                                                "label": "ƬΣΛM BӨƬ MΛX",
                                                                "uri": "http://line.me/ti/p/%40jnx0914l"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "thumbnailImageUrl": "https://obs-sg.line-apps.com/myhome/c/download.nhn?userid=u308a4e0976ace6e2e2c234a09ef9f581&oid=1559471452",
                                                        "title": "SETTING",
                                                        "text": "To Use This command just Setting help",
                                                        "defaultAction": {
                                                            "type": "uri",
                                                            "uri": "line://app/1623679774-k9nBDB6b?type=text&text=setting"
                                                        },
                                                        "actions": [
                                                            {
                                                                "type": "uri",
                                                                "label": "ƬΣΛM BӨƬ MΛX",
                                                                "uri": "http://line.me/ti/p/%40jnx0914l"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "thumbnailImageUrl": "https://obs-sg.line-apps.com/myhome/c/download.nhn?userid=u308a4e0976ace6e2e2c234a09ef9f581&oid=1559471452",
                                                        "title": "SET",
                                                        "text": "To Use This command just Set help",
                                                        "defaultAction": {
                                                            "type": "uri",
                                                            "uri": "line://app/1623679774-k9nBDB6b?type=text&text=set"
                                                        },
                                                        "actions": [
                                                            {
                                                                "type": "uri",
                                                                "label": "ƬΣΛM BӨƬ MΛX",
                                                                "uri": "http://line.me/ti/p/%40jnx0914l"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "thumbnailImageUrl": "https://obs-sg.line-apps.com/myhome/c/download.nhn?userid=u308a4e0976ace6e2e2c234a09ef9f581&oid=1559471452",
                                                        "title": "GROUP",
                                                        "text": "To Use This command just Group help",
                                                        "defaultAction": {
                                                            "type": "uri",
                                                            "uri": "line://app/1623679774-k9nBDB6b?type=text&text=group"
                                                        },
                                                        "actions": [
                                                            {
                                                                "type": "uri",
                                                                "label": "ƬΣΛM BӨƬ MΛX",
                                                                "uri": "http://line.me/ti/p/%40jnx0914l"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "thumbnailImageUrl": "https://obs-sg.line-apps.com/myhome/c/download.nhn?userid=u308a4e0976ace6e2e2c234a09ef9f581&oid=1559471452",
                                                        "title": "PROTECT",
                                                        "text": "To Use This command just protect help",
                                                        "defaultAction": {
                                                            "type": "uri",
                                                            "uri": "line://app/1623679774-k9nBDB6b?type=text&text=protect"
                                                        },
                                                        "actions": [
                                                            {
                                                                "type": "uri",
                                                                "label": "ƬΣΛM BӨƬ MΛX",
                                                                "uri": "http://line.me/ti/p/%40jnx0914l"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "thumbnailImageUrl": "https://obs-sg.line-apps.com/myhome/c/download.nhn?userid=u308a4e0976ace6e2e2c234a09ef9f581&oid=1559471452",
                                                        "title": "FRIEND",
                                                        "text": "To Use This command just Friend help",
                                                        "defaultAction": {
                                                            "type": "uri",
                                                            "uri": "line://app/1623679774-k9nBDB6b?type=text&text=friend"
                                                        },
                                                        "actions": [
                                                            {
                                                                "type": "uri",
                                                                "label": "ƬΣΛM BӨƬ MΛX",
                                                                "uri": "http://line.me/ti/p/%40jnx0914l"
                                                            }
                                                        ]
                                                    } 
                                                ],
                                                "imageAspectRatio": "square",
                                                "imageSize": "contain"
                                            }
                                       }
                                maxbots.postTemplate(to, data) 

                            elif teambotmax == "help2":
                                data = {
                                            "type": "template",
                                            "altText": "ＳＥＬＦＢＯＴＢＹＭＡＸ",
                                            "template": {
                                                "type": "carousel",
                                                "columns": [
                                                    {
                                                        "thumbnailImageUrl": "https://obs-sg.line-apps.com/myhome/c/download.nhn?userid=u308a4e0976ace6e2e2c234a09ef9f581&oid=1559471452",
                                                        "title": "MEDIA",
                                                        "text": "To Use This command just Media help",
                                                        "defaultAction": {
                                                            "type": "uri",
                                                            "uri": "line://app/1623679774-k9nBDB6b?type=text&text=media"
                                                        },
                                                        "actions": [
                                                            {
                                                                "type": "uri",
                                                                "label": "ƬΣΛM BӨƬ MΛX",
                                                                "uri": "http://line.me/ti/p/%40jnx0914l"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "thumbnailImageUrl": "https://obs-sg.line-apps.com/myhome/c/download.nhn?userid=u308a4e0976ace6e2e2c234a09ef9f581&oid=1559471452",
                                                        "title": "SPECIAL ORDER",
                                                        "text": "To Use This command just Special help",
                                                        "defaultAction": {
                                                            "type": "uri",
                                                            "uri": "line://app/1623679774-k9nBDB6b?type=text&text=special"
                                                        },
                                                        "actions": [
                                                            {
                                                                "type": "uri",
                                                                "label": "ƬΣΛM BӨƬ MΛX",
                                                                "uri": "http://line.me/ti/p/%40jnx0914l"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "thumbnailImageUrl": "https://obs-sg.line-apps.com/myhome/c/download.nhn?userid=u308a4e0976ace6e2e2c234a09ef9f581&oid=1559471452",
                                                        "title": "STICKER",
                                                        "text": "To Use This command just Sticker help",
                                                        "defaultAction": {
                                                            "type": "uri",
                                                            "uri": "line://app/1623679774-k9nBDB6b?type=text&text=sticker"
                                                        },
                                                        "actions": [
                                                            {
                                                                "type": "uri",
                                                                "label": "ƬΣΛM BӨƬ MΛX",
                                                                "uri": "http://line.me/ti/p/%40jnx0914l"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "thumbnailImageUrl": "https://obs-sg.line-apps.com/myhome/c/download.nhn?userid=u308a4e0976ace6e2e2c234a09ef9f581&oid=1559471452",
                                                        "title": "PROFILE",
                                                        "text": "To Use This command just Profile help",
                                                        "defaultAction": {
                                                            "type": "uri",
                                                            "uri": "line://app/1623679774-k9nBDB6b?type=text&text=profile"
                                                        },
                                                        "actions": [
                                                            {
                                                                "type": "uri",
                                                                "label": "ƬΣΛM BӨƬ MΛX",
                                                                "uri": "http://line.me/ti/p/%40jnx0914l"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "thumbnailImageUrl": "https://obs-sg.line-apps.com/myhome/c/download.nhn?userid=u308a4e0976ace6e2e2c234a09ef9f581&oid=1559471452",
                                                        "title": "SPAM",
                                                        "text": "To Use This command just Spam help",
                                                        "defaultAction": {
                                                            "type": "uri",
                                                            "uri": "line://app/1623679774-k9nBDB6b?type=text&text=spam"
                                                        },
                                                        "actions": [
                                                            {
                                                                "type": "uri",
                                                                "label": "ƬΣΛM BӨƬ MΛX",
                                                                "uri": "http://line.me/ti/p/%40jnx0914l"
                                                            }
                                                        ]
                                                    } 
                                                ],
                                                "imageAspectRatio": "square",
                                                "imageSize": "contain"
                                            }
                                       }
                                maxbots.postTemplate(to, data) 

                            elif teambotmax == "help3":
                                 data = {
      "contents": [
        {
          "hero": {
            "aspectMode": "cover",
            "url": "https://www.img.live/images/2019/10/02/USER_SCOPED_TEMP_DATA_orca-image-2065117818.jpg",
            "action": {
              "uri": "http://line.me/ti/p/%40jnx0914l",
              "type": "uri"
            },
            "type": "image",
            "size": "full"
          },
          "styles": {
            "body": {
              "backgroundColor": "#000000"
            },
            "footer": {
              "backgroundColor": "#FF0000"
            },
            "header": {
              "backgroundColor": "#FF0000"
            }
          },
          "type": "bubble",
          "size": "giga",
          "body": {
            "contents": [
              {
                "text": "꧁༺ คำสั่ง ༻꧂ ",
                "color": "#FF0000",
                "wrap": True,
                "weight": "bold",
                "type": "text",
                "size": "lg",
                "align": "center"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "1.Me *โปรไฟล์เรา\n2.Me2-10 *โปรไฟล์เรา\n3.Help *รายการคำสั่ง\n4.Help1-3 *รายการคำสั่ง",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "5.Mymid *เอ็มไอดีของเรา\n6.Tag *แทคสมาชิกทั้งกลุ่ม\n7.Status *เช็คการตั้งค่า\n8.Reset *รีสตาร์ทบอท",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "9.Url grup *ลิ้งกลุ่ม\n10.Open *เปิดลิ้ง\n11.Close *ปิดลิ้ง\n12.Grouplist *กลุ่มทั้งหมดของเรา",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "13.FriendInfo「@」*ข้อมูลคนอื่น\n14.Getpict「@」*รูปคนอื่น\n15.Getbio「@」*สเตตัสคนอื่น\n16.Getcover「@」รูปปกคนอื่น",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          "type": "bubble",
          "size": "giga",
          "footer": {
            "type": "box",   
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "✦ ติดต่อผู้สร้าง ✦ ",
                "size": "xl",
                "wrap": True,
                "weight": "bold",
                "color": "#000000",
                "action": {
                  "type": "uri",
                  "uri": "http://line.me/ti/p/%40jnx0914l"
                },
                "align": "center"            
              }
            ]
          },
          "type": "bubble",
          "size": "giga",
          "header": {
            "type": "box",   
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",    
                "text": "✦ รายการคำสั่งที่ 1 ✦",
                "size": "lg",
                "wrap": True,
                "weight": "bold",
                "color": "#000000",
                "action": {
                  "type": "uri",
                  "uri": "http://line.me/ti/p/%40jnx0914l"
                },
                "align": "center"            
              }
            ]
          }
        },
        {
          "hero": {
            "aspectMode": "cover",
            "url": "https://www.img.live/images/2019/10/02/USER_SCOPED_TEMP_DATA_orca-image-728076021.jpg",
            "action": {
              "uri": "http://line.me/ti/p/%40jnx0914l",
              "type": "uri"
            },
            "type": "image",
            "size": "full"
          },
          "styles": {
            "body": {
              "backgroundColor": "#000000"
            },
            "footer": {
              "backgroundColor": "#FF0000"
            },
            "header": {
              "backgroundColor": "#FF0000"
            }
          },
          "type": "bubble",
          "size": "giga",
          "body": {
            "contents": [
              {
                "text": "꧁༺ คำสั่ง ༻꧂ ",
                "color": "#FF0000",
                "wrap": True,
                "weight": "bold",
                "type": "text",
                "size": "lg",
                "align": "center"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "1.Respon on|off *ตอบกลับอัตโนมัติ\n2.Sider on|off *ดูคนแอบ\n3.Welcome on|off *ต้อนรับคนเข้าออก\n4.Sticker on|off *สติกเกอร์ใหญ่",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "5.Autojoin on|off *เข้ากลุ่มอัตโนมัติ\n6.Autoread on|off *อ่านอัตโนมัติ\n7.Autoblock on|off *บล็อกอัตโนมัติ\n8.Autoadd on|off *เพิ่มเพื่อนอัตโนมัติ",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "9.Groupbc:「Text」*ประกาศกลุ่ม\n10.Friendbc:「Text」*ประกาศเพื่อน\n11.Broadcast:「Text」*ประกาศ\n12.Mp3:「Text」*เพลง",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "13.Setrespon:「Text」*ตั้งคนแทค\n14.Setautoadd:「Text」*ตั้งรับเพื่อน\n15.Setautoblock:「Text」*ตั้งบล็อก\n16.Setwelcome:「Text」*ตั้งคนเข้าออก",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          "type": "bubble",
          "size": "giga",
          "footer": {
            "type": "box",   
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "✦ ติดต่อผู้สร้าง ✦",
                "size": "xl",
                "wrap": True,
                "weight": "bold",
                "color": "#000000",
                "action": {
                  "type": "uri",
                  "uri": "http://line.me/ti/p/%40jnx0914l"
                },
                "align": "center"            
              }
            ]
          },
          "type": "bubble",
          "size": "giga",
          "header": {
            "type": "box",   
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "✦ รายการคำสั่งที่ 2 ✦",
                "size": "lg",
                "wrap": True,
                "weight": "bold",
                "color": "#000000",
                "action": {
                  "type": "uri",
                  "uri": "http://line.me/ti/p/%40jnx0914l"
                },
                "align": "center"            
              }
            ]
          }
        },
        {
          "body": {
            "type": "cover",
            "backgroundColor": "#00FFFF"
          },
          "hero": {
            "aspectMode": "cover",
            "url": "https://www.img.live/images/2019/10/02/USER_SCOPED_TEMP_DATA_orca-image--1988088485.jpg",
            "action": {
              "uri": "http://line.me/ti/p/%40jnx0914l",
              "type": "uri"
            },
            "type": "image",
            "size": "full"
          },
          "styles": {
            "body": {
              "backgroundColor": "#000000"
            },
            "footer": {
              "backgroundColor": "#FF0000"
            },
            "header": {
              "backgroundColor": "#FF0000"
            }
          },
          "type": "bubble",
          "size": "giga",
          "body": {
            "contents": [
              {
                "text": "꧁༺ คำสั่ง ༻꧂ ", 
                "color": "#FF0000",
                "wrap": True,
                "weight": "bold",
                "type": "text",
                "size": "lg",
                "align": "center"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "1.Bc *คท คนติดดำ\n2.Cb *ล้างดำ\n3.Ban「@」\n4.Unban「@」",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "5.Menu *เมนู\n6.Setting *ตั้งค่า\n7.Set *ตั้งข้อความ\n8.Sticker *สติกเกอร์",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "9.Youtube「Text」*ยูทูป\n10.Youtube2「Text」*ยูทูป\n11.Music:「Text」*เพลง\n12.About *ข้อมูล",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "13.Unsend「number」*ยกเลิกข้อความ\n14.Myurl *ลิ้งค์ไลน์ของเรา\n15.Friendlist *เพื่อนทั้งหมด\n16.All mid *เอ็มไอดีทุกคนในกลุ่ม",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          "type": "bubble",
          "size": "giga",
          "footer": {
            "type": "box",   
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "✦ ติดต่อผู้สร้าง ✦",
                "size": "xl",
                "wrap": True,
                "weight": "bold",
                "color": "#000000",
                "action": {
                  "type": "uri",
                  "uri": "http://line.me/ti/p/%40jnx0914l"
                },
                "align": "center"            
              }
            ]
          },
          "type": "bubble",
          "size": "giga",
          "header": {
            "type": "box",   
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "✦ รายการคำสั่งที่ 3 ✦",
                "size": "lg",
                "wrap": True,
                "weight": "bold",
                "color": "#000000",  
                "action": {
                  "type": "uri",
                  "uri": "http://line.me/ti/p/%40jnx0914l"
                },
                "align": "center"            
              }
            ]
          }
        },
        {
          "hero": {
            "aspectMode": "cover",
            "url": "https://www.img.live/images/2019/10/02/USER_SCOPED_TEMP_DATA_orca-image-370782930.jpg",
            "action": {
              "uri": "http://line.me/ti/p/%40jnx0914l",
              "type": "uri"
            },
            "type": "image",
            "size": "full"
          },
          "styles": {
            "body": {
              "backgroundColor": "#000000"
            },
            "footer": {
              "backgroundColor": "#FF0000"
            },
            "header": {
              "backgroundColor": "#FF0000"
            }
          },
          "type": "bubble",
          "size": "giga",
          "body": {
            "contents": [
              {
                "text": "꧁༺ คำสั่ง ༻꧂ ",
                "color": "#FF0000",
                "wrap": True,
                "weight": "bold",
                "type": "text",
                "size": "lg",
                "align": "center"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "1.Unsend on|off *ตรวจยกเลิกข้อความ\n2.Checkcontact on|off *เช็คคอนแท็ค\n3.Checkpost on|off *เช็คโพส\n4.Checksticker on|off *เช็คสติกเกอร์",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "5.ประกาศกลุ่ม「Text」*ประกาศ\n6.ประกาศกลุ่ม1「Text」*ประกาศ\n7.ประกาศกลุ่ม2「Text」*ประกาศ\n8.ประกาศกลุ่ม3「Text」*ประกาศ",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "9.Changename:「Text」*เปลี่ยนชื่อ\n10.Changebio:「Text」เปลี่ยนสเตตัส*\n11.Changepict *เปลี่ยนรูปโปรไฟล์\n12.Changecover *เปลี่ยนรูปปก",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              },
              {
                "contents": [
                  {
                    "contents": [
                      {
                        "text": "13.Kickban *ลบคนติดดำ\n14.Kick「@」*ลบสมาชิกบางคน\n15.@clear *ลบรัน\n16.Remove *ลบแชท",
                        "size": "xs",
                        "margin": "none",
                        "color": "#FFFFFF",
                        "wrap": True,
                        "weight": "regular",
                        "type": "text"
                      }
                    ],
                    "type": "box",
                    "layout": "baseline"
                  }
                ],
                "type": "box",
                "spacing": "xs",
                "layout": "vertical"
              },
              {
                "type": "separator",
                "color": "#FFFFFF"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          "type": "bubble",
          "size": "giga",
          "footer": {
            "type": "box",   
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "✦ ติดต่อผู้สร้าง ✦",
                "size": "xl",
                "wrap": True,
                "weight": "bold",
                "color": "#000000",
                "action": {
                  "type": "uri",
                  "uri": "http://line.me/ti/p/%40jnx0914l"
                },
                "align": "center"            
              }
            ]
          },
          "type": "bubble",
          "size": "giga",
          "header": {
            "type": "box",   
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "✦ รายการคำสั่งที่ 4 ✦",
                "size": "lg",
                "wrap": True,
                "weight": "bold",
                "color": "#000000",
                "action": {
                  "type": "uri",
                  "uri": "http://line.me/ti/p/%40jnx0914l"
                },
                "align": "center"            
              }
            ]
          }
        }
      ],
      "type": "carousel"
    }
                                 maxbots.postFlex(to, data)          

                            elif teambotmax == "help4":
                                teambotmaxS = maxbots.getContact(maxbotsMid)
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                teambotmaxZ = {
                                        "type": "flex",
                                        "altText": "ƬΣΛM BӨƬ MΛX",
                                        "contents": {
  "type": "bubble",
  "size": "giga",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "✦ ƬΣΛM BӨƬ MΛX ✦",
        "weight": "bold",
        "color": "#1DB446",
        "size": "xl",
        "align": "center",
        "wrap": True,
        "margin": "none"
      },
      {
        "type": "separator",
        "margin": "xxl",
        "color": "#000000"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "1:1",
            "gravity": "top",
            "position": "relative",
            "margin": "xxl",
            "align": "center",
            "backgroundColor": "#ff0000"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "NEW",
                "color": "#ffffff",
                "align": "center",
                "size": "xs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "18px",
            "backgroundColor": "#ff334b",
            "offsetStart": "18px",
            "height": "25px",
            "width": "53px"
          }
        ],
        "paddingAll": "0px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "✦ รายการคำสั่งบอท ✦",
            "weight": "bold",
            "size": "xxl",
            "margin": "md",
            "align": "center",
            "gravity": "top",
            "wrap": True,
            "position": "relative",
            "decoration": "none",
            "style": "normal"
          },
          {
            "type": "text",
            "text": "หากไม่เข้าใจกรุณากดที่ข้อความเพื่อความสะดวก",
            "size": "xs",
            "color": "#aaaaaa",
            "wrap": True,
            "align": "center",
            "gravity": "top",
            "weight": "bold"
          },
          {
            "type": "separator",
            "margin": "xxl",
            "color": "#000000"
          },
          {
            "type": "box",
            "layout": "vertical",
            "margin": "xxl",
            "spacing": "sm",
            "contents": [
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": "Help「คำสั่ง」",
                    "size": "sm",
                    "color": "#111111",
                    "align": "start",
                    "weight": "bold",
                    "gravity": "bottom",
                    "wrap": True,
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "line://app/1623679774-k9nBDB6b?type=text&text=help"
                    }
                  },
                  {
                    "type": "text",
                    "text": "Help1「คำสั่งหนึ่ง」",
                    "size": "sm",
                    "color": "#111111",
                    "align": "end",
                    "weight": "bold",
                    "gravity": "bottom",
                    "wrap": True,
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "line://app/1623679774-k9nBDB6b?type=text&text=help1"
                    }
                  }
                ]
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": "Help2「คำสั่งสอง」",
                    "size": "sm",
                    "color": "#111111",
                    "align": "start",
                    "weight": "bold",
                    "gravity": "bottom",
                    "wrap": True,
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "line://app/1623679774-k9nBDB6b?type=text&text=help2"
                    }
                  },
                  {
                    "type": "text",
                    "text": "Help3「คำสั่งสาม」",
                    "size": "sm",
                    "color": "#111111",
                    "align": "end",
                    "weight": "bold",
                    "gravity": "bottom",
                    "wrap": True,
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "line://app/1623679774-k9nBDB6b?type=text&text=help3"
                    }
                  }
                ]
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": "Menu「คำสั่งเมนู」",
                    "size": "sm",
                    "color": "#111111",
                    "align": "start",
                    "weight": "bold",
                    "gravity": "bottom",
                    "wrap": True,
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "line://app/1623679774-k9nBDB6b?type=text&text=menu"
                    }
                  },
                  {
                    "type": "text",
                    "text": "Group「คำสั่งกลุ่ม」",
                    "size": "sm",
                    "color": "#111111",
                    "align": "end",
                    "weight": "bold",
                    "gravity": "bottom",
                    "wrap": True,
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "line://app/1623679774-k9nBDB6b?type=text&text=group"
                    }
                  }
                ]
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": "Special「คำสั่งสเปเชียล」",
                    "size": "sm",
                    "color": "#111111",
                    "align": "start",
                    "weight": "bold",
                    "gravity": "bottom",
                    "wrap": True,
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "line://app/1623679774-k9nBDB6b?type=text&text=special"
                    }
                  },
                  {
                    "type": "text",
                    "text": "Sticker「คำสั่งสติกเกอร์」",
                    "size": "sm",
                    "color": "#111111",
                    "align": "end",
                    "weight": "bold",
                    "gravity": "bottom",
                    "wrap": True,
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "line://app/1623679774-k9nBDB6b?type=text&text=sticker"
                    }
                  }
                ]
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": "Setting「คำสั่งตั้งค่า」",
                    "size": "sm",
                    "color": "#111111",
                    "align": "start",
                    "weight": "bold",
                    "gravity": "bottom",
                    "wrap": True,
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "line://app/1623679774-k9nBDB6b?type=text&text=setting"
                    }
                  },
                  {
                    "type": "text",
                    "text": "Set「คำสั่งตั้งข้อความ」",
                    "size": "sm",
                    "color": "#111111",
                    "align": "end",
                    "weight": "bold",
                    "gravity": "bottom",
                    "wrap": True,
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "line://app/1623679774-k9nBDB6b?type=text&text=set"
                    }
                  }
                ]
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": "Protect「คำสั่งป้องกัน」",
                    "size": "sm",
                    "color": "#111111",
                    "align": "start",
                    "weight": "bold",
                    "gravity": "bottom",
                    "wrap": True,
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "line://app/1623679774-k9nBDB6b?type=text&text=protect"
                    }
                  },
                  {
                    "type": "text",
                    "text": "Friend「คำสั่งเพื่อน」",
                    "size": "sm",
                    "color": "#111111",
                    "align": "end",
                    "weight": "bold",
                    "gravity": "bottom",
                    "wrap": True,
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "http://linecorp.com/"
                    }
                  }
                ]
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": "Profile「คำสั่งโปรไฟล์」",
                    "size": "sm",
                    "color": "#111111",
                    "align": "start",
                    "weight": "bold",
                    "gravity": "bottom",
                    "wrap": True,
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "line://app/1623679774-k9nBDB6b?type=text&text=profile"
                    }
                  },
                  {
                    "type": "text",
                    "text": "Spam「คำสั่งแสปม」",
                    "size": "sm",
                    "color": "#111111",
                    "align": "end",
                    "weight": "bold",
                    "gravity": "bottom",
                    "wrap": True,
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "line://app/1623679774-k9nBDB6b?type=text&text=spam"
                    }
                  }
                ]
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": "Media「มีเดียร์」",
                    "size": "sm",
                    "color": "#111111",
                    "align": "start",
                    "weight": "bold",
                    "gravity": "bottom",
                    "wrap": True,
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "line://app/1623679774-k9nBDB6b?type=text&text=media"
                    }
                  },
                  {
                    "type": "text",
                    "text": "Status「เช็คตั้งค่า」",
                    "size": "sm",
                    "color": "#111111",
                    "align": "end",
                    "weight": "bold",
                    "gravity": "bottom",
                    "wrap": True,
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "line://app/1623679774-k9nBDB6b?type=text&text=status"
                    }
                  }
                ]
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": "About「ข้อมูล」",
                    "size": "sm",
                    "color": "#111111",
                    "align": "start",
                    "weight": "bold",
                    "gravity": "bottom",
                    "wrap": True,
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "line://app/1623679774-k9nBDB6b?type=text&text=about"
                    }
                  },
                  {
                    "type": "text",
                    "text": "Runtime「เวลาทำงาน」",
                    "size": "sm",
                    "color": "#111111",
                    "align": "end",
                    "weight": "bold",
                    "gravity": "bottom",
                    "wrap": True,
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "line://app/1623679774-k9nBDB6b?type=text&text=runtime"
                    }
                  }
                ]
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": "Banlist「เช็คบัญชีดำ」",
                    "size": "sm",
                    "color": "#111111",
                    "align": "start",
                    "weight": "bold",
                    "gravity": "bottom",
                    "wrap": True,
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "line://app/1623679774-k9nBDB6b?type=text&text=banlist"
                    }
                  },
                  {
                    "type": "text",
                    "text": "Killban 「ลบบัญชีดำ」",
                    "size": "sm",
                    "color": "#111111",
                    "align": "end",
                    "weight": "bold",
                    "gravity": "bottom",
                    "wrap": True,
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "line://app/1623679774-k9nBDB6b?type=text&text=killban"
                    }
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "margin": "xxl",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "separator",
                    "margin": "xl",
                    "color": "#000000"
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "xxl",
                    "contents": [
                      {
                        "type": "text",
                        "text": "• เวลา :",
                        "size": "sm",
                        "color": "#555555"
                      },
                      {
                        "type": "text",
                        "text": "" + datetime.strftime(timeNow,'%H:%M:%S') + " นาที",
                        "size": "sm",
                        "color": "#111111",
                        "align": "end"
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "text",
                        "text": "• วันที่ :",
                        "size": "sm",
                        "color": "#555555"
                      },
                      {
                        "type": "text",
                        "text": "" + datetime.strftime(timeNow,'%Y-%m-%d'), 
                        "size": "sm",
                        "color": "#111111",
                        "align": "end"
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "text",
                        "text": "• ชื่อ :",
                        "size": "sm",
                        "color": "#555555"
                      },
                      {
                        "type": "text",
                        "text": "{}".format(str(teambotmaxS.displayName)),
                        "size": "sm",
                        "color": "#111111",
                        "align": "end"
                      }
                    ]
                  }
                ]
              }
            ]
          },
          {
            "type": "separator",
            "margin": "xxl",
            "color": "#000000"
          },
          {
            "type": "text",
            "text": "✦ มีปัญหากับบอทกรุณาสอบถามแอดมิน ✦",
            "align": "center",
            "margin": "md",
            "weight": "bold",
            "wrap": True,
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://line.me/ti/p/%40jnx0914l"
            }
          }
        ]
      }
    ],
    "margin": "xxl",
    "backgroundColor": "#ffffff"
  }
}
}
                                maxbots.postTemplate(to, teambotmaxZ)

                            elif teambotmax == "help5" or teambotmax == "คำสั่ง5":
                                teambotmaxS = maxbots.getContact(maxbotsMid)
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                maxbots.reissueUserTicket()
                                teambotmaxZ = {
                                        "type": "flex",
                                        "altText": "ƬΣΛM BӨƬ MΛX",
                                        "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "giga",
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "✦ คำสั่งเชลบอท ✦",
            "wrap": True,
            "weight": "bold",
            "size": "xl",
            "align": "center"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": " BY : TEAM BOT MAX",
                "weight": "bold",
                "align": "center"
              }
            ]
          }
        ],
        "borderColor": "#000000",
        "borderWidth": "2px",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "http://line.me/ti/p/%40jnx0914l"
        }
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "✦ ติดต่อคนสร้างบอท  ✦",
              "uri": "http://line.me/ti/p/%40jnx0914l"
            },
            "style": "primary",
            "color": "#000000"
          },
          {
            "type": "separator",
            "margin": "sm",
            "color": "#000000"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "กดที่นี่เพื่อดูคำสั่งเมนู",
              "uri": "line://app/1623679774-k9nBDB6b?type=text&text=Menu"
            },
            "style": "primary",
            "color": "#ff0000"
          },
          {
            "type": "separator",
            "margin": "sm",
            "color": "#000000"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "กดที่นี่เพื่อดูคำสั่งตั้งค่า",
              "uri": "line://app/1623679774-k9nBDB6b?type=text&text=Setting"
            },
            "style": "primary",
            "color": "#ff0000"
          },
          {
            "type": "separator",
            "margin": "sm",
            "color": "#000000"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "กดที่นี่เพื่อดูคำสั่งเพื่อน",
              "uri": "line://app/1623679774-k9nBDB6b?type=text&text=Friend"
            },
            "style": "primary",
            "color": "#ff0000"
          },
          {
            "type": "separator",
            "margin": "sm",
            "color": "#000000"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "กดที่นี่เพื่อดูคำสั่งกลุ่ม",
              "uri": "line://app/1623679774-k9nBDB6b?type=text&text=Group"
            },
            "style": "primary",
            "color": "#ff0000"
          },
          {
            "type": "separator",
            "margin": "sm",
            "color": "#000000"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "กดที่นี่เพื่อดูคำสั่งมีเดีย",
              "uri": "line://app/1623679774-k9nBDB6b?type=text&text=Media"
            },
            "style": "primary",
            "color": "#ff0000"
          },
          {
            "type": "separator",
            "margin": "sm",
            "color": "#000000"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "กดที่นี่เพื่อดูคำสั่งป้องกัน",
              "uri": "line://app/1623679774-k9nBDB6b?type=text&text=Protect"
            },
            "style": "primary",
            "color": "#ff0000"
          },
          {
            "type": "separator",
            "margin": "sm",
            "color": "#000000"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "กดที่นี่เพื่อดูคำสั่งแสปม",
              "uri": "line://app/1623679774-k9nBDB6b?type=text&text=Spam"
            },
            "style": "primary",
            "color": "#ff0000"
          },
          {
            "type": "separator",
            "margin": "sm",
            "color": "#000000"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "กดที่นี่เพื่อดูคำสั่งสติกเกอร์",
              "uri": "line://app/1623679774-k9nBDB6b?type=text&text=Special"
            },
            "style": "primary",
            "color": "#ff0000"
          },
          {
            "type": "separator",
            "margin": "sm",
            "color": "#000000"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "✦ ติดต่อคนใช้บอท ✦",
              "uri": "http://line.me/ti/p/%40jnx0914l"
            },
            "style": "primary",
            "color": "#000000"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus),
                    "aspectMode": "cover",
                    "size": "full",
                    "align": "center"
                  }
                ],
                "cornerRadius": "100px",
                "width": "72px",
                "height": "72px",
                "borderColor": "#000000",
                "borderWidth": "2px",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/" + maxbots.getUserTicket().id
                }
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "• ชื่อ : {}".format(str(teambotmaxS.displayName)),
                    "size": "lg",
                    "gravity": "top"
                  },
                  {
                    "type": "text",
                    "text": "• วันที : " + datetime.strftime(timeNow,'%Y-%m-%d'), 
                    "size": "lg",
                    "gravity": "top"
                  },
                  {
                    "type": "text",
                    "text": "• เวลา : " + datetime.strftime(timeNow,'%H:%M:%S') + " นาที",
                    "size": "lg",
                    "gravity": "top"
                  }
                ]
              }
            ],
            "spacing": "xl",
            "paddingAll": "20px",
            "cornerRadius": "100px",
            "borderColor": "#000000",
            "borderWidth": "2px",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://line.me/ti/p/" + maxbots.getUserTicket().id
            }
          }
        ],
        "borderColor": "#000000",
        "position": "relative",
        "borderWidth": "2px"
      },
      "styles": {
        "body": {
          "separator": True
        },
        "footer": {
          "separator": True
        }
      }
    }
  ]
}
}
                                maxbots.postTemplate(to, teambotmaxZ)

                            elif teambotmax == "menu" or teambotmax == "help menu":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╭───────────────────"
                                md+="\n│         🍎 Menu Message 🍎"
                                md+="\n├───────────────────"
                                md+="\n│ ✯͜͡❂➣ Me 1 - 20"
                                md+="\n│ ✯͜͡❂➣ Help 1 - 3"
                                md+="\n│ ✯͜͡❂➣ Help special"
                                md+="\n│ ✯͜͡❂➣ Help sticker"
                                md+="\n│ ✯͜͡❂➣ Help setting"
                                md+="\n│ ✯͜͡❂➣ Help set"
                                md+="\n│ ✯͜͡❂➣ Help group"
                                md+="\n│ ✯͜͡❂➣ Help protect"
                                md+="\n│ ✯͜͡❂➣ Help friend"
                                md+="\n│ ✯͜͡❂➣ Help profile"
                                md+="\n│ ✯͜͡❂➣ Help spam"
                                md+="\n│ ✯͜͡❂➣ Help media"
                                md+="\n│ ✯͜͡❂➣ ประกาศกลุ่ม 「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ ประกาศแชท 「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ Kickname「ชื่อ」"
                                md+="\n│ ✯͜͡❂➣ Kickbio「ชื่อ」"
                                md+="\n│ ✯͜͡❂➣ Banlist"
                                md+="\n│ ✯͜͡❂➣ Ban「@」"
                                md+="\n│ ✯͜͡❂➣ Unban「@」"
                                md+="\n│ ✯͜͡❂➣ Bc"
                                md+="\n│ ✯͜͡❂➣ Cb"
                                md+="\n│ ✯͜͡❂➣ Killban"
                                md+="\n│ ✯͜͡❂➣ Speed"
                                md+="\n│ ✯͜͡❂➣ Runtime"
                                md+="\n│ ✯͜͡❂➣ Reset"
                                md+="\n│ ✯͜͡❂➣ Remove"
                                md+="\n│ ✯͜͡❂➣ About"
                                md+="\n│ ✯͜͡❂➣ Status"
                                md+="\n│ ✯͜͡❂➣ ประกาศกลุ่ม1 - 10「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ Groupbc:「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ Friendbc:「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ Clear spam"
                                md+="\n│ ✯͜͡❂➣ Key"
                                md+="\n│ ✯͜͡❂➣ Changekey"
                                md+="\n│ ✯͜͡❂➣ Setkey:「ข้อความ」"
                                md+="\n├───────────────────"
                                md+="\n│ • ผู้ใช้งาน : {}".format(maxbots.getProfile().displayName)
                                md+="\n│ • วันที่ : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                md+="\n│ • เวลา : " + datetime.strftime(timeNow,'%H:%M:%S') + " นาที"
                                md+="\n╰───────────────────"
                                sendTextMax11(to, md) 

                            elif teambotmax == "help special" or teambotmax == "special":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╭───────────────────"
                                md+="\n│       🍎 Special Message 🍎"
                                md+="\n├───────────────────"
                                md+="\n│ ✯͜͡❂➣ เคร"
                                md+="\n│ ✯͜͡❂➣ อิอิ"
                                md+="\n│ ✯͜͡❂➣ บ้า"
                                md+="\n│ ✯͜͡❂➣ ฝันดี"
                                md+="\n│ ✯͜͡❂➣ อะไร"
                                md+="\n│ ✯͜͡❂➣ ของขวัญ"
                                md+="\n│ ✯͜͡❂➣ เยี่ยม"
                                md+="\n│ ✯͜͡❂➣ ใช่"
                                md+="\n│ ✯͜͡❂➣ ไม่"
                                md+="\n│ ✯͜͡❂➣ ฮีฮี"
                                md+="\n│ ✯͜͡❂➣ รัก"
                                md+="\n│ ✯͜͡❂➣ ร้อน"
                                md+="\n│ ✯͜͡❂➣ ขอบคุณ"
                                md+="\n│ ✯͜͡❂➣ ฮ่าฮ่า"
                                md+="\n│ ✯͜͡❂➣ 555"
                                md+="\n│ ✯͜͡❂➣ วนๆ"
                                md+="\n│ ✯͜͡❂➣ แงๆ"
                                md+="\n│ ✯͜͡❂➣ ไม่แคร์"
                                md+="\n│ ✯͜͡❂➣ จุ๊บ"
                                md+="\n│ ✯͜͡❂➣ ตบ"
                                md+="\n│ ✯͜͡❂➣ เออ"
                                md+="\n├───────────────────"
                                md+="\n│ • ผู้ใช้งาน : {}".format(maxbots.getProfile().displayName)
                                md+="\n│ • วันที่ : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                md+="\n│ • เวลา : " + datetime.strftime(timeNow,'%H:%M:%S') + " นาที"
                                md+="\n╰───────────────────"
                                sendTextMax11(to, md)

                            elif teambotmax == "sticker" or teambotmax == "help sticker":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╭───────────────────"
                                md+="\n│       🍎 Sticker Message 🍎"
                                md+="\n├───────────────────"
                                md+="\n│ ✯͜͡❂➣ AddSticker「ข้อความ」  "
                                md+="\n│ ✯͜͡❂➣ Addleavesticker"
                                md+="\n│ ✯͜͡❂➣ Addwelcomesticker"
                                md+="\n│ ✯͜͡❂➣ Addresponsticker"
                                md+="\n│ ✯͜͡❂➣ Addsidersticker"
                                md+="\n│ ✯͜͡❂➣ AddStp「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ Delsticker「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ Delwelcomesticker"
                                md+="\n│ ✯͜͡❂➣ Delresponsticker "
                                md+="\n│ ✯͜͡❂➣ Delsidersticker "
                                md+="\n│ ✯͜͡❂➣ Delleavesticker "
                                md+="\n│ ✯͜͡❂➣ DelStp「ข้อความ」 "
                                md+="\n│ ✯͜͡❂➣ List stp"
                                md+="\n│ ✯͜͡❂➣ List sticker"
                                md+="\n├───────────────────"
                                md+="\n│ • ผู้ใช้งาน : {}".format(maxbots.getProfile().displayName)
                                md+="\n│ • วันที่ : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                md+="\n│ • เวลา : " + datetime.strftime(timeNow,'%H:%M:%S') + " นาที"
                                md+="\n╰───────────────────"
                                sendTextMax11(to, md) 

                            elif teambotmax == "setting" or teambotmax == "help setting":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╭───────────────────"
                                md+="\n│       🍎 Setting Message 🍎"
                                md+="\n├───────────────────"
                                md+="\n│ ✯͜͡❂➣ Autoadd 「 On/Off 」 "
                                md+="\n│ ✯͜͡❂➣ Autoblock 「 On/Off 」"
                                md+="\n│ ✯͜͡❂➣ Autolike 「 On/Off 」"
                                md+="\n│ ✯͜͡❂➣ Autojoin 「 On/Off 」"
                                md+="\n│ ✯͜͡❂➣ Autoread 「 On/Off 」" 
                                md+="\n│ ✯͜͡❂➣ Autojointicket 「 On/Off 」"
                                md+="\n│ ✯͜͡❂➣ Checkcontact 「 On/Off 」"
                                md+="\n│ ✯͜͡❂➣ Checkpost 「 On/Off 」"
                                md+="\n│ ✯͜͡❂➣ Checksticker 「 On/Off 」"
                                md+="\n│ ✯͜͡❂➣ Deletefriend 「 On/Off 」 "
                                md+="\n│ ✯͜͡❂➣ Decode 「 On/Off 」"
                                md+="\n│ ✯͜͡❂➣ Drawink 「 On/Off 」"
                                md+="\n│ ✯͜͡❂➣ Leaveroom  「 On/Off 」"
                                md+="\n│ ✯͜͡❂➣ Respon 「 On/Off 」"
                                md+="\n│ ✯͜͡❂➣ Respon2 「 On/Off 」"
                                md+="\n│ ✯͜͡❂➣ Respon3 「 On/Off 」"
                                md+="\n│ ✯͜͡❂➣ Sticker 「 On/Off 」 "
                                md+="\n│ ✯͜͡❂➣ Setkey 「 On/Off 」 "
                                md+="\n│ ✯͜͡❂➣ Watercolor 「 On/Off 」"
                                md+="\n│ ✯͜͡❂➣ Welcome 「 On/Off 」"
                                md+="\n│ ✯͜͡❂➣ Welcome2 「 On/Off 」"
                                md+="\n│ ✯͜͡❂➣ Welcome3 「 On/Off 」"
                                md+="\n│ ✯͜͡❂➣ Unsend 「 On/Off 」 "
                                md+="\n│ ✯͜͡❂➣ Lurking  「 On/Off 」"
                                md+="\n│ ✯͜͡❂➣ Lurking"
                                md+="\n├───────────────────"
                                md+="\n│ • ผู้ใช้งาน : {}".format(maxbots.getProfile().displayName)
                                md+="\n│ • วันที่ : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                md+="\n│ • เวลา : " + datetime.strftime(timeNow,'%H:%M:%S') + " นาที"
                                md+="\n╰───────────────────"
                                sendTextMax11(to, md) 

                            elif teambotmax == "set" or teambotmax == "help set":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╭───────────────────"
                                md+="\n│          🍎 Set Message 🍎"
                                md+="\n├───────────────────"
                                md+="\n│ ✯͜͡❂➣ Setautoadd:「ข้อความ」  "
                                md+="\n│ ✯͜͡❂➣ Setrespon:「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ Setautojoin:「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ Setsider:「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ Setwelcome:「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ Setleave:「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ Setmember:「จำนวน」"
                                md+="\n│ ✯͜͡❂➣ Setcomment:「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ Setmention: 「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ Cek "
                                md+="\n├───────────────────"
                                md+="\n│ • ผู้ใช้งาน : {}".format(maxbots.getProfile().displayName)
                                md+="\n│ • วันที่ : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                md+="\n│ • เวลา : " + datetime.strftime(timeNow,'%H:%M:%S') + " นาที"
                                md+="\n╰───────────────────"
                                sendTextMax11(to, md) 

                            elif teambotmax == "group" or teambotmax == "help group":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╭───────────────────"
                                md+="\n│       🍎 Group Message 🍎"
                                md+="\n├───────────────────"
                                md+="\n│ ✯͜͡❂➣ ประกาศกลุ่ม 「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ ประกาศกลุ่ม: 「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ ประกาศแชท: 「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ ประกาศ - 3 「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ เขียน 「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ Groupbc: 「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ Friendbc: 「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ Gbc: 「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ Fbc: 「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ ประกาศกลุ่ม1 - 7: 「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ Namagrup"
                                md+="\n│ ✯͜͡❂➣ Potogrup"
                                md+="\n│ ✯͜͡❂➣ Open"
                                md+="\n│ ✯͜͡❂➣ Close"
                                md+="\n│ ✯͜͡❂➣ Url"
                                md+="\n│ ✯͜͡❂➣ Grouplist"
                                md+="\n│ ✯͜͡❂➣ Changegroupname:「ชื่อกลุ่ม」"
                                md+="\n│ ✯͜͡❂➣ Grouppicture"
                                md+="\n│ ✯͜͡❂➣ Pendinglist"
                                md+="\n│ ✯͜͡❂➣ Memberlist"
                                md+="\n│ ✯͜͡❂➣ Memberpict"
                                md+="\n│ ✯͜͡❂➣ Get note 「ลำดับ」"
                                md+="\n│ ✯͜͡❂➣ Groupinfo "
                                md+="\n├───────────────────"
                                md+="\n│ • ผู้ใช้งาน : {}".format(maxbots.getProfile().displayName)
                                md+="\n│ • วันที่ : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                md+="\n│ • เวลา : " + datetime.strftime(timeNow,'%H:%M:%S') + " นาที"
                                md+="\n╰───────────────────"
                                sendTextMax11(to, md) 

                            elif teambotmax == "protect" or teambotmax == "help protect":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╭───────────────────"
                                md+="\n│      🍎 Protect Message 🍎"
                                md+="\n├───────────────────"
                                md+="\n│ ✯͜͡❂➣ Allpro「On/Off」 "
                                md+="\n│ ✯͜͡❂➣ Protectname「On/Off」 "
                                md+="\n│ ✯͜͡❂➣ Protecturl 「On/Off」 "
                                md+="\n│ ✯͜͡❂➣ Protectjoin 「On/Off」 "
                                md+="\n│ ✯͜͡❂➣ Protectkick 「On/Off」 "
                                md+="\n│ ✯͜͡❂➣ Protectcancel 「On/Off」 "
                                md+="\n│ ✯͜͡❂➣ Protectinvite 「On/Off」 "
                                md+="\n├───────────────────"
                                md+="\n│       🍎 Banlist Message 🍎"
                                md+="\n├───────────────────"
                                md+="\n│ ✯͜͡❂➣ Kick 「@」 "
                                md+="\n│ ✯͜͡❂➣ Ban 「@」 "
                                md+="\n│ ✯͜͡❂➣ Unban 「@」 "
                                md+="\n│ ✯͜͡❂➣ Banlist "
                                md+="\n│ ✯͜͡❂➣ Bc "
                                md+="\n│ ✯͜͡❂➣ Cb "
                                md+="\n│ ✯͜͡❂➣ Kickban "
                                md+="\n├───────────────────"
                                md+="\n│ • ผู้ใช้งาน : {}".format(maxbots.getProfile().displayName)
                                md+="\n│ • วันที่ : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                md+="\n│ • เวลา : " + datetime.strftime(timeNow,'%H:%M:%S') + " นาที"
                                md+="\n╰───────────────────"
                                sendTextMax11(to, md) 

                            elif teambotmax == "friend" or teambotmax == "help friend":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╭───────────────────"
                                md+="\n│       🍎 Friend Message 🍎"
                                md+="\n├──────────────────"
                                md+="\n│ ✯͜͡❂➣ Friendinfo 「ลำดับ」"
                                md+="\n│ ✯͜͡❂➣ Delfriendmid 「mid」"
                                md+="\n│ ✯͜͡❂➣ Friendlist"
                                md+="\n│ ✯͜͡❂➣ Unfriendall"
                                md+="\n│ ✯͜͡❂➣ Delfriend 「@」"
                                md+="\n│ ✯͜͡❂➣ Blocklist"
                                md+="\n│ ✯͜͡❂➣ Rename 「@」"
                                md+="\n│ ✯͜͡❂➣ Add 「@」"
                                md+="\n│ ✯͜͡❂➣ Block 「@」"
                                md+="\n│ ✯͜͡❂➣ Unblock 「mid」"
                                md+="\n│ ✯͜͡❂➣ Blockinfo 「 ลำดับ 」 "
                                md+="\n├───────────────────"
                                md+="\n│ • ผู้ใช้งาน : {}".format(maxbots.getProfile().displayName)
                                md+="\n│ • วันที่ : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                md+="\n│ • เวลา : " + datetime.strftime(timeNow,'%H:%M:%S') + " นาที"
                                md+="\n╰───────────────────"
                                sendTextMax11(to, md) 

                            elif teambotmax == "profile" or teambotmax == "help profile":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╭───────────────────"
                                md+="\n│       🍎 Profile Message 🍎"
                                md+="\n├───────────────────"
                                md+="\n│ ✯͜͡❂➣ Changename: 「ชื่อ」"
                                md+="\n│ ✯͜͡❂➣ Changebio: 「ตัส」"
                                md+="\n│ ✯͜͡❂➣ Cvp「ลิ้งยูทูป」"
                                md+="\n│ ✯͜͡❂➣ Check me "
                                md+="\n│ ✯͜͡❂➣ Myprofile "
                                md+="\n│ ✯͜͡❂➣ Mymid"
                                md+="\n│ ✯͜͡❂➣ Myname"
                                md+="\n│ ✯͜͡❂➣ Mybio"
                                md+="\n│ ✯͜͡❂➣ Mypicture"
                                md+="\n│ ✯͜͡❂➣ Myvideoprofile"
                                md+="\n│ ✯͜͡❂➣ Mycover"
                                md+="\n│ ✯͜͡❂➣ Mycover url"
                                md+="\n│ ✯͜͡❂➣ Getmid 「@」"
                                md+="\n│ ✯͜͡❂➣ Getcontact 「@」"
                                md+="\n│ ✯͜͡❂➣ Getidline 「@」"
                                md+="\n│ ✯͜͡❂➣ Getname 「@」"
                                md+="\n│ ✯͜͡❂➣ Getbio 「@」"
                                md+="\n│ ✯͜͡❂➣ Getpict 「@」"
                                md+="\n│ ✯͜͡❂➣ Getvideo 「@」"
                                md+="\n│ ✯͜͡❂➣ Getcover 「@」"
                                md+="\n│ ✯͜͡❂➣ All mid"
                                md+="\n│ ✯͜͡❂➣ Changedual"
                                md+="\n│ ✯͜͡❂➣ Changepict"
                                md+="\n│ ✯͜͡❂➣ Changecover"
                                md+="\n│ ✯͜͡❂➣ Changevp"
                                md+="\n├───────────────────"
                                md+="\n│ • ผู้ใช้งาน : {}".format(maxbots.getProfile().displayName)
                                md+="\n│ • วันที่ : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                md+="\n│ • เวลา : " + datetime.strftime(timeNow,'%H:%M:%S') + " นาที"
                                md+="\n╰───────────────────"
                                sendTextMax11(to, md) 

                            elif teambotmax == "spam" or teambotmax == "help spam":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╭───────────────────"
                                md+="\n│        🍎 Spam Message 🍎"
                                md+="\n├───────────────────"
                                md+="\n│ ✯͜͡❂➣ Stag 「จำนวน + @」"
                                md+="\n│ ✯͜͡❂➣ Scall 「จำนวน + @」"
                                md+="\n│ ✯͜͡❂➣ Schat「On + จำนวน + กขค」"
                                md+="\n│ ✯͜͡❂➣ Spam「On + จำนวน + กขค」"
                                md+="\n│ ✯͜͡❂➣ Sgift 「จำนวน + mid」"
                                md+="\n│ ✯͜͡❂➣ Call 「จำนวน」"
                                md+="\n│ ✯͜͡❂➣ Clear spam"
                                md+="\n├───────────────────"
                                md+="\n│ • ผู้ใช้งาน : {}".format(maxbots.getProfile().displayName)
                                md+="\n│ • วันที่ : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                md+="\n│ • เวลา : " + datetime.strftime(timeNow,'%H:%M:%S') + " นาที"
                                md+="\n╰───────────────────"
                                sendTextMax11(to, md) 

                            elif teambotmax == "media" or teambotmax == "help media":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╭───────────────────"
                                md+="\n│       🍎 Media Message 🍎"
                                md+="\n├───────────────────"
                                md+="\n│ ✯͜͡❂➣ Musik「ชื่อเพลง」"
                                md+="\n│ ✯͜͡❂➣ Mp3「ชื่อเพลง」"
                                md+="\n│ ✯͜͡❂➣ Music 「ชื่อเพลง」"
                                md+="\n│ ✯͜͡❂➣ Al-qur'an 「ชื่อ」"
                                md+="\n│ ✯͜͡❂➣ Murrotal"
                                md+="\n│ ✯͜͡❂➣ Ayat sajadah"
                                md+="\n│ ✯͜͡❂➣ Pulsk"
                                md+="\n│ ✯͜͡❂➣ Listmeme"
                                md+="\n│ ✯͜͡❂➣ Meme"
                                md+="\n│ ✯͜͡❂➣ Fscosplay 「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ Fsv url 「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ Ss"
                                md+="\n│ ✯͜͡❂➣ Decode"
                                md+="\n│ ✯͜͡❂➣ Linedownload"
                                md+="\n│ ✯͜͡❂➣ Linepost"
                                md+="\n│ ✯͜͡❂➣ Newalbum"
                                md+="\n│ ✯͜͡❂➣ Tiktok 「ไอดี」"
                                md+="\n│ ✯͜͡❂➣ Artinama 「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ Artimimpi 「ข้อความ」"
                                md+="\n│ ✯͜͡❂➣ Ytmp3 「ชื่อเรื่อง」"
                                md+="\n│ ✯͜͡❂➣ Ytmp4 「ชื่อเรื่อง」"
                                md+="\n│ ✯͜͡❂➣ Ssweb 「ลิงค์」"
                                md+="\n│ ✯͜͡❂➣ Video 「ชื่อเรื่อง」"
                                md+="\n│ ✯͜͡❂➣ Samehadaku 「ชื่อ」"
                                md+="\n│ ✯͜͡❂➣ Zodiak 「ชื่อ」"
                                md+="\n│ ✯͜͡❂➣ Praytime 「สถานที่」"
                                md+="\n│ ✯͜͡❂➣ Acaratv 「ชื่อ」"
                                md+="\n│ ✯͜͡❂➣ Youtube 「ค้นหา」"
                                md+="\n│ ✯͜͡❂➣ Youtube2 「ค้นหา」"
                                md+="\n│ ✯͜͡❂➣ Youtube3 「ค้นหา」"
                                md+="\n│ ✯͜͡❂➣ Smulerecords 「ไอดี」"
                                md+="\n│ ✯͜͡❂➣ Image 「ค้นหา」"
                                md+="\n├───────────────────"
                                md+="\n│ • ผู้ใช้งาน : {}".format(maxbots.getProfile().displayName)
                                md+="\n│ • วันที่ : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                md+="\n│ • เวลา : " + datetime.strftime(timeNow,'%H:%M:%S') + " นาที"
                                md+="\n╰───────────────────"
                                sendTextMax11(to, md) 

                            elif teambotmax == "cek":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╭──────────────────────"
                                md+="\n│          🍎 Check Message 🍎"
                                md+="\n├──────────────────────"
                                md+="\n│ ✯͜͡❂➣ Cek Sider :\n{}\n".format(str(settings["mention"]))
                                md+="\n│ ✯͜͡❂➣ Cek Mention/Tag :\n{}\n".format(str(settings["taggal"]))
                                md+="\n│ ✯͜͡❂➣ Cek Respon Tag :\n{}\n".format(str(settings["autoResponMessage"]))
                                md+="\n│ ✯͜͡❂➣ Cek Pm Message :\n{}\n".format(str(wait["cekpc"]))
                                md+="\n│ ✯͜͡❂➣ Cek Welcome Msg : \n{}\n".format(str(settings["welcome"]))
                                md+="\n│ ✯͜͡❂➣ Cek Add Message : \n{}\n".format(str(settings["autoAddMessage"]))
                                md+="\n│ ✯͜͡❂➣ Cek Leave Message :\n{}\n".format(str(settings["leave"]))
                                md+="\n│ ✯͜͡❂➣ Cek Join Message : \n{}\n".format(str(settings["autoJoinMessage"]))
                                md+="\n│ ✯͜͡❂➣ Cek Like Message : \n{}\n".format(str(settings["commentPost"]))
                                md+="\n│ ✯͜͡❂➣ Cek Block Message : \n{}\n".format(str(settings["autoAddMessage"]))
                                md+="\n├──────────────────────"
                                md+="\n│ • ผู้ใช้งาน : {}".format(maxbots.getProfile().displayName)
                                md+="\n│ • วันที่ : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                md+="\n│ • เวลา : " + datetime.strftime(timeNow,'%H:%M:%S') + " นาที"
                                md+="\n╰──────────────────────"
                                sendTextMax1(to, md) 

                            elif teambotmax == "status":
                                try:
                                    timeNow = time.time()
                                    runtime = timeNow - botStart
                                    runtime = format_timespan(runtime)
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    ret_ = "╭────────────────────\n"
                                    ret_ += "│    🍎 STATUS MESSAGE 🍎\n"
                                    ret_ += "├────────────────────"
                                    if settings["autolike"] == True: ret_ += "\n│ ✯͜͡❂➣ Autolike : On"
                                    else: ret_ += "\n│ ✯͜͡❂➣ Autolike : Off"
                                    if settings["autoAdd"] == True: ret_ += "\n│ ✯͜͡❂➣ Autoadd : On"
                                    else: ret_ += "\n│ ✯͜͡❂➣ Autoadd : Off"
                                    if settings["autoBlock"] == True: ret_ += "\n│ ✯͜͡❂➣ Autoblock : On"
                                    else: ret_ += "\n│ ✯͜͡❂➣ Autoblock : Off"
                                    if settings["autoLeave"] == True: ret_ += "\n│ ✯͜͡❂➣ Autoleave : On"
                                    else: ret_ += "\n│ ✯͜͡❂➣ Autoleave : Off"
                                    if settings["autoJoin"] == True: ret_ += "\n│ ✯͜͡❂➣ Autojoin : On"
                                    else: ret_ += "\n│ ✯͜͡❂➣ Autojoin : Off"
                                    if settings["autoJoinTicket"] == True: ret_ += "\n│ ✯͜͡❂➣ Autojointicket : On"
                                    else: ret_ += "\n│ ✯͜͡❂➣ Autojointicket : Off"
                                    if settings["autoRead"] == True: ret_ += "\n│ ✯͜͡❂➣ Autoread : On"
                                    else: ret_ += "\n│ ✯͜͡❂➣ Autoread : Off"
                                    if settings["checkContact"] == True: ret_ += "\n│ ✯͜͡❂➣ Checkcontact : On"
                                    else: ret_ += "\n│ ✯͜͡❂➣ Checkcontact : Off"
                                    if settings["checkPost"] == True: ret_ += "\n│ ✯͜͡❂➣ Checkpost : On"
                                    else: ret_ += "\n│ ✯͜͡❂➣ Checkpost : Off"
                                    if settings["checkSticker"] == True: ret_ += "\n│ ✯͜͡❂➣ Checksticker : On"
                                    else: ret_ += "\n│ ✯͜͡❂➣ Check Sticker : OFF"
                                    if settings["leaveRoom"] == True: ret_ += "\n│ ✯͜͡❂➣ Leaveroom : On"
                                    else: ret_ += "\n│ ✯͜͡❂➣ Leaveroom : Off"
                                    if settings["autoRespon"] == True: ret_ += "\n│ ✯͜͡❂➣ Respon : On"
                                    else: ret_ += "\n│ ✯͜͡❂➣ Respon : Off"
                                    if settings["responMentionnya"] == True: ret_ += "\n│ ✯͜͡❂➣ Respon2 : On"
                                    else: ret_ += "\n│ ✯͜͡❂➣ Respon2 : Off"
                                    if settings["responMaxNewVersion"] == True: ret_ += "\n│ ✯͜͡❂➣ Respon3 : On"
                                    else: ret_ += "\n│ ✯͜͡❂➣ Respon3 : Off"
                                    if settings["setKey"] == True: ret_ += "\n│ ✯͜͡❂➣ Setkey : On"
                                    else: ret_ += "\n│ ✯͜͡❂➣ Setkey : Off"
                                    if settings["unsendMessage"] == True: ret_ += "\n│ ✯͜͡❂➣ Unsend : On"
                                    else: ret_ += "\n│ ✯͜͡❂➣ Unsend : Off"
                                    if msg.to in welcome: ret_ +="\n│ ✯͜͡❂➣ Welcome : On"
                                    else: ret_ += "\n│ ✯͜͡❂➣ Welcome : Off"
                                    if settings["newWelcome"] == True: ret_ += "\n│ ✯͜͡❂➣ Welcome2 : On"
                                    else: ret_ += "\n│ ✯͜͡❂➣ Welcome2 : Off"
                                    if msg.to in protectinvite: ret_ +="\n│ ✯͜͡❂➣ Protectinvite : On"
                                    else: ret_ += "\n│ ✯͜͡❂➣ Protectinvite : Off"
                                    if msg.to in protectqr: ret_ +="\n│ ✯͜͡❂➣ Protectqr : On"
                                    else: ret_ += "\n│ ✯͜͡❂➣ Protectqr : Off"
                                    if msg.to in protectjoin: ret_ +="\n│ ✯͜͡❂➣ Protectjoin : On"
                                    else: ret_ += "\n│ ✯͜͡❂➣ Protectjoin : Off"
                                    if msg.to in protectkick: ret_ +="\n│ ✯͜͡❂➣ Protectkick : On"
                                    else: ret_ += "\n│ ✯͜͡❂➣ Protectkick : Off"
                                    if msg.to in protectcancel: ret_ +="\n│ ✯͜͡❂➣ Protectcancel : On"
                                    else: ret_ += "\n│ ✯͜͡❂➣ Protectcancel : Off"
                                    if msg.to in protectname: ret_ +="\n│ ✯͜͡❂➣ Protectname : On"
                                    else: ret_ += "\n│ ✯͜͡❂➣ Protectname : Off"
                                    ret_ += "\n├────────────────────"
                                    ret_ += "\n│ • ผู้ใช้งาน : {}".format(maxbots.getProfile().displayName)
                                    ret_ += "\n│ • วันที่ : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n│ • เวลา : " + datetime.strftime(timeNow,'%H:%M:%S') + " นาที"
                                    ret_ += "\n╰────────────────────"
                                    sendTextMax1(to, ret_) 
                                except Exception as error:
                                    sendTextMax1(to, str(error))

                            elif teambotmax == "remove":
                              if msg._from in maxbotsMid:
                                maxbots.removeAllMessages(op.param2)
                                teambotmaxText(to, "✯͜͡❂ สำเร็จ ลบการแชททั้งหมด")

                            elif teambotmax == "open":
                              if msg._from in maxbotsMid:
                                if msg.toType == 2:
                                   X = maxbots.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   maxbots.updateGroup(X)
                                   teambotmaxText(msg.to, "✯͜͡❂ เปิดแล้ว")

                            elif teambotmax == "close":
                              if msg._from in maxbotsMid:
                                  if msg.toType == 2:
                                     X = maxbots.getGroup(msg.to)
                                     X.preventedJoinByTicket = True
                                     maxbots.updateGroup(X)
                                     teambotmaxText(msg.to, "✯͜͡❂ ปิดแล้ว")

                            elif teambotmax == "url":
                              if msg._from in maxbotsMid:
                                  if msg.toType == 2:
                                     x = maxbots.getGroup(msg.to)
                                     if x.preventedJoinByTicket == True:
                                        x.preventedJoinByTicket = False
                                        maxbots.updateGroup(x)
                                     gurl = maxbots.reissueGroupTicket(msg.to)
                                     teambotmaxText(to, "✯͜͡❂ ชื่อกลุ่ม : "+str(x.name)+ "\n✯͜͡❂ ลิ้งกลุ่ม : http://line.me/R/ti/g/"+gurl)                                                                                                                                              
                       
                            elif teambotmax.startswith("friendbc: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                contacts = maxbots.getAllContactIds()
                                for contact in contacts:
                                    maxbots.sendMessage(contact, "{}".format(str(txt)))
                                maxbots.sendMessage(to, "Bₑᵣₕₐₛᵢₗ bᵣₒₐdcₐₛₜ ₖₑ {} ₜₑₘₐₙ".format(str(len(contacts))))

                            elif teambotmax.startswith("groupbc: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                groups = maxbots.getGroupIdsJoined()
                                for group in groups:
                                    maxbots.sendMessage(group, "{}".format(str(txt)))
                                maxbots.sendMessage(to, "Bₑᵣₕₐₛᵢₗ bᵣₒₐdcₐₛₜ ₖₑ {} gᵣₒᵤₚ".format(str(len(groups))))

                            elif teambotmax == "unfriendall":
                              if msg._from in maxbotsMid:
                                try:
                                    friend = maxbots.getContacts(maxbots.getAllContactIds())
                                    teambotmaxText(to,"✯͜͡❂ คุณได้ล้างเพื่อนทั้งหมด {} คน".format(len(friend)))
                                    for unfriend in friend:
                                        maxbots.deleteContact(unfriend.mid)
                                    teambotmaxText(to,"✯͜͡❂ คุณได้ล้างเพื่อนทั้งหมด {} คน".format(len(friend)))
                                except Exception as error:
                                    teambotmaxText(to, "「 ข้อผิดพลาด 」\n" + str(error))

                            elif teambotmax == '@bye':
                                if msg.toType == 2:
                                   ge = ("uc14c3d87a1123df7c8ffa9d7402e59a2")
                                   ginfo = maxbots.getGroup(to)
                                   try:
                                       maxbots.sendReplyMessage(msg.id, to,"✯͜͡❂ ขอบคุณที่เชิญฉัน")
                                       time.sleep(1)
                                       maxbots.leaveGroup(to)
                                   except:
                                       pass                                                                                                                  
#=======================KICK OUT==============================================
                            elif teambotmax.startswith("vk "):
                                maxbots.unsendMessage(msg_id)
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        maxbots.kickoutFromGroup(to, [ls])

                            elif teambotmax.startswith("kick "):
                                maxbots.unsendMessage(msg_id)
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        try:
                                            maxbots.kickoutFromGroup(to, [ls])
                                            maxbots.findAndAddContactsByMid(ls)
                                            maxbots.inviteIntoGroup(to, [ls])
                                            maxbots.cancelGroupInvitation(to, [ls])
                                        except:
                                           teambotmaxText(to, "Limited")

                            elif teambotmax == "#ยกเชิญ":
                                if msg.toType == 2:
                                    group = maxbots.getGroup(to)
                                    if group.invitee is None or group.invitee == []:
                                        maxbots.sendMessage(to, "ไม่มีสมาชิกค้างเชิญ")
                                    else:
                                        invitee = [contact.mid for contact in group.invitee]
                                        for inv in invitee:
                                            maxbots.cancelGroupInvitation(to, [inv])
                                            time.sleep(1)
                                        maxbots.sendMessage(to, "ยกเลิกสมาชิก 「 {} 」คน".format(str(len(invitee))))

                            elif teambotmax == "@kickall":
                                maxbots.unsendMessage(msg_id)
                                if msg.toType == 2:
                                    if settings['K-lock'] == True:
                                        try:
                                            X = maxbots.getGroup(receiver)
                                            for x in X.members:
                                                maxbots.kickoutFromGroup(receiver, [str(x.mid)])
                                        except:
                                            pass
                                    else:
                                        print("\'K-lock\' is not on <true>")
                                        maxbots.sendMessage(receiver, "Sorry, this function is \"lock\" now.")

                            elif teambotmax == "fuckall":
                                maxbots.unsendMessage(msg_id)
                                gs = maxbots.getGroup(msg.to)
                                targets = []
                                for x in gs.members:
                                    targets.append(x.mid)
                                for b in Bots:
                                    if b in targets:
                                        try:
                                            targets.remove(b)
                                        except:
                                            pass
                                for target in targets:
                                    try:
                                        klist = [maxbots]
                                        kicker = random.choice(klist)
                                        kicker.kickoutFromGroup(msg.to,[target])
                                    except:
                                        pass 

                            elif ("เชิญ " in msg.text):
                                if msg.toType == 2:
                                    group = maxbots.getGroup(to)
                                    if 'MENTION' in msg.contentMetadata.keys()!=None:
                                        targets = []
                                        key = eval(msg.contentMetadata["MENTION"])
                                        key["MENTIONEES"][0]["M"]
                                        for x in key["MENTIONEES"]:
                                            targets.append(x["M"])
                                        for target in targets:
                                            try:
                                                maxbots.findAndAddContactsByMid(target)
                                                maxbots.inviteIntoGroup(group.id,[target])
                                            except:maxbots.sendMessage(msg.to,'「 MESSAGE 」\n• EROR 404, Bots was limited')
                                    else:maxbots.sendMessage(msg.to,'「 MESSAGE 」\n• Tag target oey')

                            elif ("kickname " in msg.text):
                               sep = text.split(" ")
                               midn = text.replace(sep[0] + " ","")
                               hmm = text.lower()
                               G = maxbots.getGroup(msg.to)
                               members = [G.mid for G in G.members]
                               targets = []
                               for x in members:
                                   contact = maxbots.getContact(x)
                                   msg = op.message
                                   testt = contact.displayName.lower()
                                   if midn in testt:targets.append(contact.mid)
                               if targets == []:return teambotmaxText(to,"✯͜͡❂ ไม่พบชื่อนี้ "+midn)
                               for target in targets:
                                   invsend = 0
                                   def usirNam():
                                       maxbots.kickoutFromGroup(to,[target])
                                   threadd = Thread(target=usirNam())
                                   threadd.daemon = True
                                   threadd.start()

                            elif ("Kickbio " in msg.text):
                               sep = text.split(" ")
                               midn = text.replace(sep[0] + " ","")
                               hmm = text.lower()
                               G = maxbots.getGroup(msg.to)
                               members = [G.mid for G in G.members]
                               targets = []
                               for x in members:
                                   contact = maxbots.getContact(x)
                                   msg = op.message
                                   testt = contact.statusMessage.lower()
                                   if midn in testt:targets.append(contact.mid)
                               if targets == []:return teambotmaxText(to,"✯͜͡❂ ไม่พบสถานะนี้ "+midn)
                               for target in targets:
                                   invsend = 0
                                   def usirBio():
                                       maxbots.kickoutFromGroup(to,[target])
                                   threadd = Thread(target=usirBio())
                                   threadd.daemon = True
                                   threadd.start()
#=====================================================================
                            elif teambotmax.startswith("pictlab "):
                              separate = text.split(" ")
                              teks = text.replace(separate[0] + " ","")
                              url1 = "https://memegen.link/buzz/"+teks+".jpg"
                              url2 = "https://memegen.link/joker/"+teks+".jpg"
                              url3 = "https://memegen.link/cbg/"+teks+".jpg"
                              url4 = "https://memegen.link/fry/"+teks+".jpg"
                              url5 = "https://memegen.link/yuno/"+teks+".jpg"
                              url6 = "https://memegen.link/fa/"+teks+".jpg"
                              url7 = "https://memegen.link/iw/"+teks+".jpg"
                              url8 = "https://memegen.link/blb/"+teks+".jpg"
                              url9 = "https://memegen.link/doge/"+teks+".jpg"
                              url10 = "https://memegen.link/firsttry/"+teks+".jpg"
                              data = {
                                "type": "template",
                                "altText": "ＳＥＬＦＢＯＴＢＹＭＡＸ",
                                "template": {
                                  "type": "image_carousel",
                                  "columns": [
                                    {
                                      "imageUrl": url1,
                                      "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                          "x": 447,
                                          "y": 356,
                                          "width": 1040,
                                          "height": 1040
                                        }
                                      }
                                    },
                                    {
                                      "imageUrl": url2,
                                      "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                          "x": 447,
                                          "y": 356,
                                          "width": 1040,
                                          "height": 1040
                                        }
                                      }
                                    },
                                    {
                                      "imageUrl": url3,
                                      "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                          "x": 447,
                                          "y": 356,
                                          "width": 1040,
                                          "height": 1040
                                        }
                                      }
                                    },
                                    {
                                      "imageUrl": url4,
                                      "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                          "x": 447,
                                          "y": 356,
                                          "width": 1040,
                                          "height": 1040
                                        }
                                      }
                                    },
                                    {
                                      "imageUrl": url5,
                                      "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                          "x": 447,
                                          "y": 356,
                                          "width": 1040,
                                          "height": 1040
                                        }
                                      }
                                    },
                                    {
                                      "imageUrl": url6,
                                      "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                          "x": 447,
                                          "y": 356,
                                          "width": 1040,
                                          "height": 1040
                                        }
                                      }
                                    },
                                    {
                                      "imageUrl": url7,
                                      "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                          "x": 447,
                                          "y": 356,
                                          "width": 1040,
                                          "height": 1040
                                        }
                                      }
                                    },
                                    {
                                      "imageUrl": url8,
                                      "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                          "x": 447,
                                          "y": 356,
                                          "width": 1040,
                                          "height": 1040
                                        }
                                      }
                                    },
                                    {
                                      "imageUrl": url9,
                                      "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                          "x": 447,
                                          "y": 356,
                                          "width": 1040,
                                          "height": 1040
                                        }
                                      }
                                    },
                                    {
                                      "imageUrl": url10,
                                      "action": {
                                        "type": "uri",
                                        "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                                        "area": {
                                          "x": 447,
                                          "y": 356,
                                          "width": 1040,
                                          "height": 1040
                                        }
                                      }
                                    }
                                  ]
                                }
                              }
                              maxbots.sendFlex(to, data) 

                            elif teambotmax == "memberlist":
                                if msg.toType == 2:
                                    group = maxbots.getGroup(to)
                                    num = 0
                                    ret_ = "╭───「 รายชื่อสมาชิกกลุ่ม 」"
                                    for contact in group.members:
                                        num += 1
                                        ret_ += "\n│{}. {}".format(num, contact.displayName)
                                    ret_ += "\n╰───「 จำนวน {} สมาชิก 」".format(len(group.members))
                                    warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                                    warnanya1 = random.choice(warna1)
                                    teambotmaxZ = {
                                        "type": "flex",
                                        "altText": "{} ส่งวิดีโอ".format(maxbotsProfile.displayName),
                                        "contents": {
  "type": "bubble",
  "size": "giga",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "ON LINE",
        "weight": "bold",
        "color": "#1DB446",
        "size": "sm"
      },
      {
        "type": "separator",
        "margin": "xxl"
      },
      {
        "type": "text",
        "text": str(ret_),
        "align": "start",
        "color": warnanya1,
        "wrap": True,
        "gravity": "top"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "✦ กดที่นี่เพื่อติดต่อแอดมิน ✦",
        "size": "xs",
        "color": "#000000",
        "wrap": True,
        "align": "center"
      }
    ],
    "action": {
      "type": "uri",
      "label": "action",
      "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2"
    }
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}
}
                                    maxbots.sendFlex(to, teambotmaxZ)

                            elif teambotmax == "pendinglist":
                                if msg.toType == 2:
                                    group = maxbots.getGroup(to)
                                    ret_ = "╭───「 รายการสมาชิกที่รออนุมัติ 」"
                                    no = 0
                                    if group.invitee is None or group.invitee == []:
                                        return maxbots.sendReplyMessage(msg_id, to, "• ไม่มีสมาชิกค้างเชิญ")
                                    else:
                                        for pending in group.invitee:
                                            no += 1
                                            ret_ += "\n│{}. {}".format(str(no), str(pending.displayName))
                                        ret_ += "\n╰───「 จำนวน {} สมาชิก 」".format(str(len(group.invitee)))
                                        warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                                        warnanya1 = random.choice(warna1)
                                        teambotmaxZ = {
                                            "type": "flex",
                                            "altText": "{} ส่งวิดีโอ".format(maxbotsProfile.displayName),
                                            "contents": {
  "type": "bubble",
  "size": "giga",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "ON LINE",
        "weight": "bold",
        "color": "#1DB446",
        "size": "sm"
      },
      {
        "type": "separator",
        "margin": "xxl"
      },
      {
        "type": "text",
        "text": str(ret_),
        "align": "start",
        "color": warnanya1,
        "wrap": True,
        "gravity": "top"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "✦ กดที่นี่เพื่อติดต่อแอดมิน ✦",
        "size": "xs",
        "color": "#000000",
        "wrap": True,
        "align": "center"
      }
    ],
    "action": {
      "type": "uri",
      "label": "action",
      "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2"
    }
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}
}
                                        maxbots.sendFlex(to, teambotmaxZ)

                            elif teambotmax == "grouplist":
                                groups = maxbots.getGroupIdsJoined()
                                ret_ = "╭───「 รายชื่อกลุ่ม 」"
                                no = 0
                                for gid in groups:
                                    group = maxbots.getGroup(gid)
                                    no += 1
                                    ret_ += "\n│{}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                ret_ += "\n╰───「 จำนวน {} กลุ่ม 」".format(str(len(groups)))
                                warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                                warnanya1 = random.choice(warna1)
                                teambotmaxZ = {
                                            "type": "flex",
                                            "altText": "{} ส่งวิดีโอ".format(maxbotsProfile.displayName),
                                            "contents": {
  "type": "bubble",
  "size": "giga",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "ON LINE",
        "weight": "bold",
        "color": "#1DB446",
        "size": "sm"
      },
      {
        "type": "separator",
        "margin": "xxl"
      },
      {
        "type": "text",
        "text": str(ret_),
        "align": "start",
        "color": warnanya1,
        "wrap": True,
        "gravity": "top"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "✦ กดที่นี่เพื่อติดต่อแอดมิน ✦",
        "size": "xs",
        "color": "#000000",
        "wrap": True,
        "align": "center"
      }
    ],
    "action": {
      "type": "uri",
      "label": "action",
      "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2"
    }
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}
}
                                maxbots.sendFlex(to, teambotmaxZ)
#===============================MEDIA=============================================================                                   
                            elif teambotmax.startswith("soundcloud "):
                                def sdc():
                                    kitsunesplit = rynSplitText(msg.text.lower()).split(" ")
                                    r = requests.get('https://soundcloud.com/search?q={}'.format(rynSplitText(msg.text.lower())))
                                    soup = BeautifulSoup(r.text,'html5lib')
                                    data = soup.find_all(class_='soundTitle__titleContainer')
                                    data = soup.select('li > h2 > a')
                                    if len(kitsunesplit) == 1:
                                        a = '          🎺 NOTE PILIHAN LAGU 🎺\n____________________________________';no=0
                                        for b in data:
                                            no+=1
                                            a+= '\n{}. {}'.format(no,b.text)
                                        sendTextMax4(to,a)
                                    if len(kitsunesplit) == 2:
                                        a = data[int(kitsunesplit[1])-1];b = list(a)[0]
                                        kk = random.randint(0,999)
                                        sendTextMax4(to,'Judul: {}\nStatus: Waiting... For Upload'.format(a.text))
                                        hh=subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output {}.mp3 {}'.format(kk,'https://soundcloud.com{}'.format(a.get('href'))))
                                        try:maxbots.sendAudio(to,'{}.mp3'.format(kk))
                                        except Exception as e:sendTextMax3(to,' 「 ERROR 」\nJudul: {}\nStatus: {}\nImportant: Try again'.format(a.text,e))
                                        os.remove('{}.mp3'.format(kk))
                                ryn = Thread(target=sdc)
                                ryn.daemon = True
                                ryn.start()
                                ryn.join()

                            elif teambotmax == 'kalender':
                              if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = "❂➣ "+ hasil + " : " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n\n❂➣ Jam : 🔹 " + timeNow.strftime('%H:%M:%S') + " 🔹"
                                sendTextMax3(msg.to, readTime)
                         
                            elif teambotmax == "autolike on":
                              if msg._from in admin:
                                if settings["newWelcome"] == True:
                                    sendTextMax8(to, "• เปิดใช้งานการกดไลค์อัตโนมัติสำเร็จแล้ว")
                                else:
                                    settings["newWelcome"] = True
                                    sendTextMax8(to, "• เปิดใช้งานการกดไลค์อัตโนมัติสำเร็จแล้ว")
                                    
                            elif teambotmax == "autolike off":
                              if msg._from in admin:
                                if settings["newWelcome"] == False:
                                    sendTextMax8(to, "• ปิดใช้งานการกดไลค์อัตโนมัติสำเร็จแล้ว")
                                else:
                                    settings["newWelcome"] = False
                                    sendTextMax8(to, "• ปิดใช้งานการกดไลค์อัตโนมัติสำเร็จแล้ว")
           
                            elif teambotmax == "welcome2 on":
                              if msg._from in admin:
                                if settings["newWelcome"] == True:
                                    sendTextMax8(to, "• เปิดใช้งานต้อนรับอัตโนมัติสำเร็จแล้ว")
                                else:
                                    settings["newWelcome"] = True
                                    sendTextMax8(to, "• เปิดใช้งานต้อนรับอัตโนมัติสำเร็จแล้ว")
                                    
                            elif teambotmax == "welcome2 off":
                              if msg._from in admin:
                                if settings["newWelcome"] == False:
                                    sendTextMax8(to, "• ปิดใช้งานต้อนรับอัตโนมัติสำเร็จแล้ว")
                                else:
                                    settings["newWelcome"] = False
                                    sendTextMax8(to, "• ปิดใช้งานต้อนรับอัตโนมัติสำเร็จแล้ว")
                                                  
                            elif teambotmax == "welcome3 on":
                              if msg._from in admin:
                                if settings["sapa"] == True:
                                    sendTextMax8(to, "• ต้อนรับอัตโนมัติเปิดใช้งานอยู่")
                                else:
                                    settings["sapa"] = True
                                    sendTextMax8(to, "• เปิดใช้งาน ต้อนรับคนเข้ากลุ่ม อัตโนมัติ สำเร็จแล้ว")
                                    
                            elif teambotmax == "welcome3 off":
                              if msg._from in admin:
                                if settings["sapa"] == False:
                                    sendTextMax8(to, "• ต้อนรับอัตโนมัติถูกปิดการใช้งาน")
                                else:
                                    settings["sapa"] = False
                                    sendTextMax8(to, "• ปิดการใช้งานต้อนรับอัตโนมัติได้สำเร็จ")

                            elif teambotmax == "autoleave on":
                              if msg._from in admin:
                                if settings["autoLeave"] == True:
                                    sendTextMax8(to, "• ออกกลุ่มอัตโนมัติทำงานอยู่")
                                else:
                                    settings["autoLeave"] = True
                                    sendTextMax8(to, "• เปิดใช้งานออกกลุ่มอัตโนมัติสำเร็จแล้ว")

                            elif teambotmax == "autoleave off":
                              if msg._from in admin:
                                if settings["autoLeave"] == False:
                                    sendTextMax8(to, "• ออกกลุ่มอัตโนมัติปิดอยู่")
                                else:
                                    settings["autoLeave"] = False
                                    sendTextMax8(to, "• ปิดใช้งานออกกลุ่มอัตโนมัติสำเร็จแล้ว")

                            elif teambotmax == "leaveroom on":
                              if msg._from in admin:
                                if settings["leaveRoom"] == True:
                                    sendTextMax8(to, "• ออกแชทรวม ทำงานอยู่")
                                else:
                                    settings["leaveRoom"] = True
                                    sendTextMax8(to, "• เปิดใช้งาน ออกแชทรวม สำเร็จแล้ว")

                            elif teambotmax == "leaveroom off":
                              if msg._from in admin:
                                if settings["leaveRoom"] == False:
                                    sendTextMax8(to, "• ออกแชทรวม ปิดอยู่")
                                else:
                                    settings["leaveRoom"] = False
                                    sendTextMax8(to, "• ปิดใช้งาน ออกแชทรวม สำเร็จแล้ว")

                            elif teambotmax == "autoblock on":
                              if msg._from in admin:
                                if settings["autoBlock"] == True:
                                    sendTextMax8(to, "• บล็อกอัตโนมัติทำงานอยู่")
                                else:
                                    settings["autoBlock"] = True
                                    sendTextMax8(to, "• เปิดใช้งานบล็อกอัตโนมัติสำเร็จแล้ว")

                            elif teambotmax == "autoblock off":
                              if msg._from in admin:
                                if settings["autoBlock"] == False:
                                    sendTextMax8(to, "• บล็อกอัตโนมัติถูกปิดใช้งาน")
                                else:
                                    settings["autoBlock"] = False
                                    sendTextMax8(to, "• ปิดใช้งานบล็อกอัตโนมัติสำเร็จแล้ว")
                                    
                            elif teambotmax == "autoadd on":
                              if msg._from in admin:
                                if settings["autoAdd"] == True:
                                    sendTextMax8(to, "• เปิดใช้งานเพิ่มเพื่อนอัตโนมัติ")
                                else:
                                    settings["autoAdd"] = True
                                    sendTextMax8(to, "• เปิดใช้งานเพิ่มเพื่อนอัตโนมัติสำเร็จแล้ว")

                            elif teambotmax == "autoadd off":
                              if msg._from in admin:
                                if settings["autoAdd"] == False:
                                    sendTextMax8(to, "• ปิดใช้งานเพิ่มเพื่อนอัตโนมัติ")
                                else:
                                    settings["autoAdd"] = False
                                    sendTextMax8(to, "• ปิดใช้งานเพิ่มเพื่อนอัตโนมัติสำเร็จแล้ว")

                            elif teambotmax == "autojoin on":
                              if msg._from in admin:
                                if settings["autoJoin"] == True:
                                    sendTextMax8(to, "• การเข้าร่วมอัตโนมัติเปิดอยู่")
                                else:
                                    settings["autoJoin"] = True
                                    sendTextMax8(to, "• เปิดใช้งานการเข้าร่วมอัตโนมัติสำเร็จ")

                            elif teambotmax == "autojoin off":
                              if msg._from in admin:
                                if settings["autoJoin"] == False:
                                    sendTextMax8(to, "• การเข้าร่วมอัตโนมัติถูกปิดใช้งาน")
                                else:
                                    settings["autoJoin"] = False
                                    sendTextMax8(to, "• ปิดใช้งานการเข้าร่วมอัตโนมัติสำเร็จ")

                            elif teambotmax == "autojointicket on":
                              if msg._from in admin:
                                if settings["autoJoinTicket"] == True:
                                    sendTextMax8(to, "• มุดลิ้งอัตโนมัติเปิดใช้งานอยู่")
                                else:
                                    settings["autoJoinTicket"] = True
                                    sendTextMax8(to, "• เปิดใช้งานมุดลิ้งอัตโนมัติสำเร็จ")

                            elif teambotmax == "autojointicket off":
                              if msg._from in admin:
                                if settings["autoJoinTicket"] == False:
                                    sendTextMax8(to, "• มุดลิ้งอัตโนมัติถูกปิดการใช้งาน")
                                else:
                                    settings["autoJoinTicket"] = False
                                    sendTextMax8(to, "• ปิดใช้งานมุดลิ้งอัตโนมัติสำเร็จ")

                            elif teambotmax == "autoread on":
                              if msg._from in admin:
                                if settings["autoRead"] == True:
                                    sendTextMax8(to, "• เปิดอ่านอัตโนมัติ")
                                else:
                                    settings["autoRead"] = True
                                    sendTextMax8(to, "• เปิดใช้งานการอ่านอัตโนมัติสำเร็จแล้ว")

                            elif teambotmax == "autoread off":
                              if msg._from in admin:
                                if settings["autoRead"] == False:
                                    sendTextMax8(to, "• การอ่านอัตโนมัติถูกปิดการใช้งาน")
                                else:
                                    settings["autoRead"] = False
                                    sendTextMax8(to, "• ปิดใช้งานการอ่านอัตโนมัติสำเร็จแล้ว")

                            elif teambotmax == "respon on":
                              if msg._from in admin:
                                if settings["autoRespon"] == True:
                                    sendTextMax8(to, "• การตอบกลับอัตโนมัติเปิดใช้งาน")
                                else:
                                    settings["autoRespon"] = True
                                    sendTextMax8(to, "• เปิดใช้งานการตอบกลับอัตโนมัติสำเร็จแล้ว")

                            elif teambotmax == "respon off":
                              if msg._from in admin:
                                if settings["autoRespon"] == False:
                                    sendTextMax8(to, "• การตอบกลับอัตโนมัติถูกปิดใช้งาน")
                                else:
                                    settings["autoRespon"] = False
                                    sendTextMax8(to, "• ปิดใช้งานการตอบกลับอัตโนมัติสำเร็จแล้ว")

                            elif teambotmax == "respon2 on":
                              if msg._from in admin:
                                if settings["responMentionnya"] == True:
                                    sendTextMax8(to, "• การตอบกลับอัตโนมัติเปิดใช้งานอยู่")
                                else:
                                    settings["responMentionnya"] = True
                                    sendTextMax8(to, "• เปิดใช้งานการตอบกลับอัตโนมัติสำเร็จแล้ว")

                            elif teambotmax == "respon2 off":
                              if msg._from in admin:
                                if settings["responMentionnya"] == False:
                                    sendTextMax8(to, "• การตอบกลับอัตโนมัติถูกปิดการใช้งาน")
                                else:
                                    settings["responMentionnya"] = False
                                    sendTextMax8(to, "• ปิดการใช้งานการตอบกลับอัตโนมัติสำเร็จแล้ว")

                            elif teambotmax == "respon3 on":
                              if msg._from in admin:
                                if settings["responMaxNewVersion"] == True:
                                    sendTextMax8(to, "• การตอบกลับอัตโนมัติเปิดใช้งานอยู่")
                                else:
                                    settings["responMaxNewVersion"] = True
                                    sendTextMax8(to, "• เปิดใช้งานการตอบกลับอัตโนมัติสำเร็จแล้ว")

                            elif teambotmax == "respon3 off":
                              if msg._from in admin:
                                if settings["responMaxNewVersion"] == False:
                                    sendTextMax8(to, "• การตอบกลับอัตโนมัติถูกปิดการใช้งาน")
                                else:
                                    settings["responMaxNewVersion"] = False
                                    sendTextMax8(to, "• ปิดการใช้งานการตอบกลับอัตโนมัติสำเร็จแล้ว")

                            elif teambotmax == "autoreply on":
                              if msg._from in admin:
                                if settings["autoReply"] == True:
                                    sendTextMax8(to, "• การตอบกลับอัตโนมัติเปิดอยู่")
                                else:
                                    settings["autoReply"] = True
                                    sendTextMax8(to, "• เปิดใช้งานการตอบกลับอัตโนมัติสำเร็จแล้ว")

                            elif teambotmax == "autoreply off":
                              if msg._from in admin:
                                if settings["autoReply"] == False:
                                    sendTextMax8(to, "• การตอบกลับอัตโนมัติถูกปิดการใช้งาน")
                                else:
                                    settings["autoReply"] = False
                                    sendTextMax8(to, "• ปิดใช้งานการตอบกลับอัตโนมัติสำเร็จแล้ว")

                            elif teambotmax == "comment on":
                              if msg._from in admin:
                                if settings["commentOn"] == True:
                                    sendTextMax8(to, "• คอมเม้นอัตโนมัติเปิดอยู่")
                                else:
                                    settings["commentOn"] = True
                                    sendTextMax8(to, "• เปิดใช้งานคอมเม้นอัตโนมัติสำเร็จแล้ว")

                            elif teambotmax == "comment off":
                              if msg._from in admin:
                                if settings["commentOn"] == False:
                                    sendTextMax8(to, "• คอมเม้นอัตโนมัติถูกปิดการใช้งาน")
                                else:
                                    settings["commentOn"] = False
                                    sendTextMax8(to, "• ปิดใช้งานคอมเม้นอัตโนมัติสำเร็จแล้ว")

                            elif teambotmax == "checkcontact on":
                              if msg._from in admin:
                                if settings["checkContact"] == True:
                                    sendTextMax8(to, "• ตรวจสอบผู้ติดต่อใช้งานอยู่")
                                else:
                                    settings["checkContact"] = True
                                    sendTextMax8(to, "• เปิดใช้งานตรวจสอบผู้ติดต่อสำเร็จ")

                            elif teambotmax == "checkcontact off":
                              if msg._from in admin:                          
                                if settings["checkContact"] == False:
                                    sendTextMax8(to, "• ตรวจสอบผู้ติดต่อถูกปิดการใช้งาน")
                                else:
                                    settings["checkContact"] = False
                                    sendTextMax8(to, "• ปิดใช้งานตรวจสอบผู้ติดต่อสำเร็จ")

                            elif teambotmax == "checkpost on":
                              if msg._from in admin:                          
                                if settings["checkPost"] == True:
                                    sendTextMax8(to, "• ตรวจสอบโพสต์มีการใช้งาน")
                                else:
                                    settings["checkPost"] = True
                                    sendTextMax8(to, "• เปิดใช้งานตรวจสอบโพสต์เรียบร้อยแล้ว")

                            elif teambotmax == "checkpost off":
                              if msg._from in admin:                          
                                if settings["checkPost"] == False:
                                    sendTextMax8(to, "• ตรวจสอบโพสต์ถูกปิดการใช้งาน")
                                else:
                                    settings["checkPost"] = False
                                    sendTextMax8(to, "• ปิดใช้งานตรวจสอบโพสต์สำเร็จแล้ว")

                            elif teambotmax == "checksticker on":
                              if msg._from in admin:
                                if settings["checkSticker"] == True:
                                    sendTextMax8(to, "• ตรวจสอบรายละเอียดสติกเกอร์ที่ใช้งานอยู่")
                                else:
                                    settings["checkSticker"] = True
                                    sendTextMax8(to, "• เปิดใช้งานรายละเอียดสติ๊กเกอร์สำเร็จ")

                            elif teambotmax == "checksticker off":
                              if msg._from in admin:                          
                                if settings["checkSticker"] == False:
                                    sendTextMax8(to, "• ตรวจสอบรายละเอียดสติกเกอร์ปิดอยู่")
                                else:
                                    settings["checkSticker"] = False
                                    sendTextMax8(to, "• ปิดใช้งานรายละเอียดสติกเกอร์สำเร็จ")

                            elif teambotmax == "sticker on":
                              if msg._from in admin:                          
                                if to in settings["sticker"]:
                                    sendTextMax8(to, "• เปิดใช้งานสติ๊กเกอร์แล้ว")
                                else:
                                    if to not in settings["sticker"]:
                                        settings["sticker"].append(to)
                                    sendTextMax8(to, "• เปิดใช้งานสติ๊กเกอร์สำเร็จแล้ว")

                            elif teambotmax == "sticker off":
                              if msg._from in admin:                          
                                if to not in settings["sticker"]:
                                    sendTextMax8(to, "• สติกเกอร์ถูกปิดการใช้งาน")
                                else:
                                    if to in settings["sticker"]:
                                        settings["sticker"].remove(to)
                                    sendTextMax8(to, "• ปิดใช้งานสติกเกอร์สำเร็จแล้ว")

                            elif teambotmax == "deletefriend on":
                              if msg._from in admin:                          
                                if settings["delFriend"] == True:
                                    sendTextMax8(to, "• ส่งผู้ติดต่อ")
                                else:
                                    settings["delFriend"] = True
                                    sendTextMax8(to, "• ส่งผู้ติดต่อ")

                            elif teambotmax == "deletefriend off":
                              if msg._from in admin:                          
                                if settings["delFriend"] == False:
                                    sendTextMax8(to, "• ไม่ได้ใช้งานอยู่")
                                else:
                                    settings["delFriend"] = False
                                    sendTextMax8(to, "• ปิดใช้งานการลบเพื่อนสำเร็จแล้ว")

                            elif teambotmax == "unsend on":
                              if msg._from in maxbotsMid:
                                if settings["unsendMessage"] == True:
                                    sendTextMax8(to, "• ยกเลิกข้อความ ทำงานอยู่")
                                else:
                                    settings["unsendMessage"] = True
                                    sendTextMax8(to, "• เปิดใช้งาน ยกเลิกข้อความ สำเร็จแล้ว")

                            elif teambotmax == "unsend off":
                              if msg._from in maxbotsMid:
                                if settings["unsendMessage"] == False:
                                    sendTextMax8(to, "• ยกเลิกข้อความ ถูกปิดการใช้งาน")
                                else:
                                    settings["unsendMessage"] = False
                                    sendTextMax8(to, "• ปิดการใช้งาน ยกเลิกข้อความ สำเร็จแล้ว")

                            elif teambotmax == "call on":
                              if msg._from in maxbotsMid:
                                if settings["spamCall"] == True:
                                    sendTextMax8(to, "• on !!")
                                else:
                                    settings["spamCall"] = True
                                    sendTextMax8(to, "• on !!")

                            elif teambotmax == "call off":
                              if msg._from in maxbotsMid:
                                if settings["spamCall"] == False:
                                    sendTextMax8(to, "• off !!")
                                else:
                                    settings["spamCall"] = False
                                    sendTextMax8(to, "• off !!")

                            elif teambotmax == "เปิดดัก":
                              if msg._from in maxbotsMid:
                                if settings["TrapCode"] == True:
                                    sendTextMax8(to, "• ดักข้อความโค๊ด ทำงานอยู่")
                                else:
                                    settings["TrapCode"] = True
                                    sendTextMax8(to, "• เปิดใช้งาน ดักข้อความโค๊ด สำเร็จแล้ว")

                            elif teambotmax == "ปิดดัก":
                              if msg._from in maxbotsMid:
                                if settings["TrapCode"] == False:
                                    sendTextMax8(to, "• ดักข้อความโค๊ด ถูกปิดการใช้งาน")
                                else:
                                    settings["TrapCode"] = False
                                    sendTextMax8(to, "• ปิดการใช้งาน ดักข้อความโค๊ด สำเร็จแล้ว")

                            elif teambotmax == "decode on":
                              if msg._from in maxbotsMid:
                                if settings["decode"] == True:
                                    sendTextMax8(to, "• on !!")
                                else:
                                    settings["decode"] = True
                                    sendTextMax8(to, "• on !!")

                            elif teambotmax == "decode off":
                              if msg._from in maxbotsMid:
                                if settings["decode"] == False:
                                    sendTextMax8(to, "• off !!")
                                else:
                                    settings["decode"] = False
                                    sendTextMax8(to, "• off !!")

                            elif teambotmax == "เปิดกันรัน":
                              if msg._from in maxbotsMid:
                                if settings["maxReject"] == True:
                                    sendTextMax8(to, "• on !!")
                                else:
                                    settings["maxReject"] = True
                                    sendTextMax8(to, "• on !!")

                            elif teambotmax == "ปิดกันรัน":
                              if msg._from in maxbotsMid:
                                if settings["maxReject"] == False:
                                    sendTextMax8(to, "• off !!")
                                else:
                                    settings["maxReject"] = False
                                    sendTextMax8(to, "• off !!")

                            elif teambotmax == "watercolor on":
                              if msg._from in maxbotsMid:
                                if settings["watercolor"] == True:
                                    sendTextMax8(to, "• on !!")
                                else:
                                    settings["watercolor"] = True
                                    sendTextMax8(to, "• on !!")

                            elif teambotmax == "watercolor off":
                              if msg._from in maxbotsMid:
                                if settings["watercolor"] == False:
                                    sendTextMax8(to, "• off !!")
                                else:
                                    settings["watercolor"] = False
                                    sendTextMax8(to, "• off !!")

                            elif teambotmax == "drawink on":
                              if msg._from in maxbotsMid:
                                if settings["drawink"] == True:
                                    sendTextMax8(to, "• on !!")
                                else:
                                    settings["drawink"] = True
                                    sendTextMax8(to, "• on !!")

                            elif teambotmax == "drawink off":
                              if msg._from in maxbotsMid:
                                if settings["drawink"] == False:
                                    sendTextMax8(to, "• off !!")
                                else:
                                    settings["drawink"] = False
                                    sendTextMax8(to, "• off !!")

                            elif teambotmax == "respon4 on":
                              if msg._from in admin:
                                if settings["responMaxNewVersion2"] == True:
                                    sendTextMax8(to, "• การตอบกลับอัตโนมัติเปิดใช้งานอยู่")
                                else:
                                    settings["responMaxNewVersion2"] = True
                                    sendTextMax8(to, "• เปิดใช้งานการตอบกลับอัตโนมัติสำเร็จแล้ว")

                            elif teambotmax == "respon4 off":
                              if msg._from in admin:
                                if settings["responMaxNewVersion2"] == False:
                                    sendTextMax8(to, "• การตอบกลับอัตโนมัติถูกปิดการใช้งาน")
                                else:
                                    settings["responMaxNewVersion2"] = False
                                    sendTextMax8(to, "• ปิดการใช้งานการตอบกลับอัตโนมัติสำเร็จแล้ว")

                            elif 'Welcome ' in msg.text:
                              if msg._from in admin:
                                 spl = msg.text.replace('Welcome ','')
                                 if spl == 'on':
                                     if msg.to in welcome:
                                          msgs = "✯͜͡❂ ยินดีต้อนรับใช้งานอยู่"
                                     else:
                                          welcome.append(msg.to)
                                          ginfo = maxbots.getGroup(msg.to)
                                          msgs = "✯͜͡❂ ต้อนรับเปิดใช้งาน\n✯͜͡❂ กลุ่ม :\n" +str(ginfo.name)
                                     sendTextMax8(to, "✯͜͡❂ เปิดการใช้งาน\n" + msgs)
                                 elif spl == 'off':
                                       if msg.to in welcome:
                                            welcome.remove(msg.to)
                                            ginfo = maxbots.getGroup(msg.to)
                                            msgs = "✯͜͡❂ ต้อนรับถูกปิดใช้งาน\n✯͜͡❂  กลุ่ม :\n" +str(ginfo.name)
                                       else:
                                            msgs = "✯͜͡❂ ยินดีต้อนรับไม่ได้ใช้งานอีกต่อไป"
                                       sendTextMax8(to, "ปิดการใช้งาน\n" + msgs)

                            elif 'Protecturl ' in msg.text:
                              if msg._from in admin:
                                 spl = msg.text.replace('Protecturl ','')
                                 if spl == 'on':
                                     if msg.to in protectqr:
                                          msgs = "✯͜͡❂ เปิดใช้งานการป้องกัน URL"
                                     else:
                                          protectqr.append(msg.to)
                                          ginfo = maxbots.getGroup(msg.to)
                                          msgs = "✯͜͡❂ ป้องกันการเปิดใช้งาน URL\n✯͜͡❂ กลุ่ม :" +str(ginfo.name)
                                     teambotmaxText(to, "「เปิดการใช้งาน」\n" + msgs)
                                 elif spl == 'off':
                                       if msg.to in protectqr:
                                            protectqr.remove(msg.to)
                                            ginfo = maxbots.getGroup(msg.to)
                                            msgs = "✯͜͡❂ ป้องกัน URL ถูกปิดใช้งาน\n✯͜͡❂ กลุ่ม :" +str(ginfo.name)
                                       else:
                                            msgs = "✯͜͡❂ ป้องกัน URL ปิดอยู่"
                                       teambotmaxText(to, "「ปิดการใช้งาน」\n" + msgs)

                            elif 'Protectkick ' in msg.text:
                              if msg._from in admin:
                                 spl = msg.text.replace('Protectkick ','')
                                 if spl == 'on':
                                     if msg.to in protectkick:
                                          msgs = "✯͜͡❂ ป้องกันการเตะเปิดอยู่"
                                     else:
                                          protectkick.append(msg.to)
                                          ginfo = maxbots.getGroup(msg.to)
                                          msgs = "✯͜͡❂ ป้องกันการเตะถูกเปิดใช้งาน\n✯͜͡❂ กลุ่ม :" +str(ginfo.name)
                                     teambotmaxText(to, "「เปิดการใช้งาน」\n" + msgs)
                                 elif spl == 'off':
                                       if msg.to in protectkick:
                                            protectkick.remove(msg.to)
                                            ginfo = maxbots.getGroup(msg.to)
                                            msgs = "✯͜͡❂ ป้องกันการเตะถูกปิดใช้งาน\n✯͜͡❂ กลุ่ม :" +str(ginfo.name)
                                       else:
                                            msgs = "✯͜͡❂ ป้องกันการเตะปิด"
                                       teambotmaxText(to, "「ปิดการใช้งาน」\n" + msgs)

                            elif 'Protectinvite ' in msg.text:
                              if msg._from in admin:
                                 spl = msg.text.replace('Protectinvite ','')
                                 if spl == 'on':
                                     if msg.to in protectinvite:
                                          msgs = "✯͜͡❂ ป้องกันการเชิญมีการใช้งานแล้ว"
                                     else:
                                          protectinvite.append(msg.to)
                                          ginfo = maxbots.getGroup(msg.to)
                                          msgs = "✯͜͡❂ เปิดใช้งานการป้องกันการเชิญ\n✯͜͡❂ กลุ่ม :" +str(ginfo.name)
                                     teambotmaxText(to, "「เปิดการใช้งาน」\n" + msgs)
                                 elif spl == 'off':
                                       if msg.to in protectinvite:
                                            protectinvite.remove(msg.to)
                                            ginfo = maxbots.getGroup(msg.to)
                                            msgs = "✯͜͡❂ ป้องกันการเชิญถูกปิดใช้งาน\n✯͜͡❂ กลุ่ม :" +str(ginfo.name)
                                       else:
                                            msgs = "✯͜͡❂ ป้องกันคำเชิญไม่ทำงานอีกต่อไป"
                                       teambotmaxText(to,"「ปิดการใช้งาน」\n" + msgs)

                            elif 'Protectjoin ' in msg.text:
                              if msg._from in admin:
                                 spl = msg.text.replace('Protectjoin ','')
                                 if spl == 'on':
                                     if msg.to in protectjoin:
                                          msgs = "✯͜͡❂ ป้องกันการเข้าร่วมใช้งานอยู่"
                                     else:
                                          protectjoin.append(msg.to)
                                          ginfo = maxbots.getGroup(msg.to)
                                          msgs = "✯͜͡❂ เปิดใช้งานการป้องกันการเข้าร่วม\n✯͜͡❂ กลุ่ม :" +str(ginfo.name)
                                     teambotmaxText(to, "「เปิดการใช้งาน」\n" + msgs)
                                 elif spl == 'off':
                                       if msg.to in protectjoin:
                                            protectjoin.remove(msg.to)
                                            ginfo = maxbots.getGroup(msg.to)
                                            msgs = "✯͜͡❂ ป้องกันการเข้าร่วมถูกปิดใช้งาน\n✯͜͡❂ กลุ่ม :" +str(ginfo.name)
                                       else:
                                            msgs = "✯͜͡❂ ป้องกันการเข้าร่วมถูกปิด"
                                       teambotmaxText(to, "「ปิดการใช้งาน」\n" + msgs)

                            elif 'Protectcancel ' in msg.text:
                              if msg._from in admin:
                                 spl = msg.text.replace('Protectcancel ','')
                                 if spl == 'on':
                                     if msg.to in protectcancel:
                                          msgs = "✯͜͡❂ ป้องกันการยกเลิกเปิดอยู่"
                                     else:
                                          protectcancel.append(msg.to)
                                          ginfo = maxbots.getGroup(msg.to)
                                          msgs = "✯͜͡❂ เปิดใช้งานการป้องกันการยกเลิก\n✯͜͡❂ กลุ่ม : " +str(ginfo.name)
                                     teambotmaxText(to, "「เปิดการใช้งาน」\n" + msgs)
                                 elif spl == 'off':
                                       if msg.to in protectcancel:
                                            protectcancel.remove(msg.to)
                                            ginfo = maxbots.getGroup(msg.to)
                                            msgs = "✯͜͡❂ ป้องกันการยกเลิกถูกปิดใช้งาน\n✯͜͡❂ กลุ่ม : " +str(ginfo.name)
                                       else:
                                            msgs = "✯͜͡❂ ป้องกันการยกเลิกถูกปิด"
                                       teambotmaxText(to, "「ปิดการใช้งาน」\n" + msgs)

                            elif 'Protectname ' in msg.text:
                              if msg._from in admin:
                                 spl = msg.text.replace('Protectname ','')
                                 if spl == 'on':
                                     if msg.to in protectname:
                                          msgs = "✯͜͡❂ ป้องกันการเปลี่ยนชื่อเปิดอยู่"
                                     else:
                                          protectname.append(msg.to)
                                          ginfo = maxbots.getGroup(msg.to)
                                          msgs = "✯͜͡❂ เปิดใช้งานการป้องกันการเปลี่ยนชื่อ\n✯͜͡❂ กลุ่ม : " +str(ginfo.name)
                                     teambotmaxText(to, "「เปิดการใช้งาน」\n" + msgs)
                                 elif spl == 'off':
                                       if msg.to in protectname:
                                            protectname.remove(msg.to)
                                            ginfo = maxbots.getGroup(msg.to)
                                            msgs = "✯͜͡❂ ป้องกันการเปลี่ยนชื่อถูกปิดใช้งาน\n✯͜͡❂ กลุ่ม : " +str(ginfo.name)
                                       else:
                                            msgs = "✯͜͡❂ ป้องกันการเปลี่ยนชื่อถูกปิด"
                                       teambotmaxText(to, "「ปิดการใช้งาน」\n" + msgs)

                            elif 'Allpro ' in msg.text:
                              if msg._from in admin:
                                 spl = msg.text.replace('Allpro ','')
                                 if spl == 'on':
                                     if msg.to in protectqr:
                                          msgs = ""
                                     else:
                                          protectqr.append(msg.to)
                                     if msg.to in protectkick:
                                         msgs = ""
                                     else:
                                         protectkick.append(msg.to)
                                     if msg.to in protectname:
                                         msgs = ""
                                     else:
                                         protectname.append(msg.to)
                                     if msg.to in protectcancel:
                                         ginfo = maxbots.getGroup(msg.to)
                                         msgs = "✯͜͡❂ ปกป้องทั้งหมด\n✯͜͡❂ กลุ่ม : " +str(ginfo.name)
                                     else:
                                         protectcancel.append(msg.to)
                                         ginfo = maxbots.getGroup(msg.to)
                                         msgs = "✯͜͡❂ เปิดใช้งานการป้องกันทั้งหมดสำเร็จแล้ว\n✯͜͡❂ กลุ่ม : " +str(ginfo.name)
                                     teambotmaxText(to, "「เปิดการใช้งาน」\n" + msgs)
                                 elif spl == 'off':
                                       if msg.to in protectqr:
                                            protectqr.remove(msg.to)
                                       else:
                                            msgs = ""
                                       if msg.to in protectkick:
                                            protectkick.remove(msg.to)
                                       else:
                                            msgs = ""
                                       if msg.to in protectname:
                                            protectname.remove(msg.to)
                                       else:
                                            msgs = ""
                                       if msg.to in protectcancel:
                                            protectcancel.remove(msg.to)
                                            ginfo = maxbots.getGroup(msg.to)
                                            msgs = "✯͜͡❂ ปิดใช้งานการป้องกันทั้งหมดเรียบร้อยแล้ว\n✯͜͡❂ กลุ่ม : " +str(ginfo.name)
                                       else:
                                            ginfo = maxbots.getGroup(msg.to)
                                            msgs = "✯͜͡❂ การป้องกันทั้งหมดปิดอยู่\n✯͜͡❂ กลุ่ม : " +str(ginfo.name)
                                       teambotmaxText(to, "「ปิดการใช้งาน」\n" + msgs)
#==================================================================================================================================
                            elif teambotmax.startswith("setautoadd2: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["message"] = txt
                                    teambotmaxText(to, "✯͜͡❂ เปลี่ยนข้อความเพิ่มเพื่อนอัตโนมัติเป็น : 「{}」".format(txt))
                                except:
                                    teambotmaxText(to, "✯͜͡❂ ไม่สามารถเปลี่ยนข้อความเพิ่มเพื่อนอัตโนมัติได้")

                            elif teambotmax.startswith("setautoadd: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["autoAddMessage"] = txt
                                    teambotmaxText(to, "✯͜͡❂ เปลี่ยนข้อความเพิ่มเพื่อนอัตโนมัติเป็น : 「{}」".format(txt))
                                except:
                                    teambotmaxText(to, "✯͜͡❂ ไม่สามารถเปลี่ยนข้อความเพิ่มเพื่อนอัตโนมัติได้")

                            elif teambotmax.startswith("setautoblock: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["autoBlockMessage"] = txt
                                    teambotmaxText(to, "✯͜͡❂ เปลี่ยนข้อความบล็อกอัตโนมัติเป็น : 「{}」".format(txt))
                                except:
                                    teambotmaxText(to, "✯͜͡❂ ไม่สามารถเปลี่ยนข้อความบล็อกอัตโนมัติได้")
                                 
                            elif teambotmax.startswith("setmention: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["taggal"] = txt
                                    teambotmaxText(to, "✯͜͡❂ เปลี่ยนการกล่าวถึงเป็น : 「{}」".format(txt))
                                except:
                                    teambotmaxText(to, "✯͜͡❂ ไม่สามารถเปลี่ยนการกล่าวถึง ")
   
                            elif teambotmax.startswith("setrespon: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["autoResponMessage"] = txt
                                    teambotmaxText(to, "✯͜͡❂ เปลี่ยนข้อความตอบกลับเป็น : 「{}」".format(txt))
                                except:
                                    teambotmaxText(to, "✯͜͡❂ ไม่สามารถเปลี่ยนข้อความตอบกลับได้")

                            elif teambotmax.startswith("setautojoin: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["autoJoinMessage"] = txt
                                    teambotmaxText(to, "✯͜͡❂ เปลี่ยนข้อความการเข้าร่วมอัตโนมัติเป็น : 「{}」".format(txt))
                                except:
                                    teambotmaxText(to, "✯͜͡❂ ไม่สามารถเปลี่ยนข้อความเข้าร่วมอัตโนมัติได้")
                                    
                            elif teambotmax.startswith("setsider: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["mention"] = txt
                                    teambotmaxText(to, "✯͜͡❂ เปลี่ยนข้อความคนแอบเป็น : 「{}」".format(txt))
                                except:
                                    teambotmaxText(to, "✯͜͡❂ ไม่สามารถเปลี่ยนข้อความคนแอบ")
                          
                            elif teambotmax.startswith("setwelcome: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["welcome"] = txt
                                    teambotmaxText(to, "✯͜͡❂ เปลี่ยนข้อความต้อนรับเป็น : 「{}」".format(txt))
                                except:
                                    teambotmaxText(to, "✯͜͡❂ ไม่สามารถเปลี่ยนข้อความต้อนรับได้")

                            elif teambotmax.startswith("setleave: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["leave"] = txt
                                    teambotmaxText(to, "✯͜͡❂ เปลี่ยนข้อความคนออกเป็น : 「{}」".format(txt))
                                except:
                                    teambotmaxText(to, "✯͜͡❂ ไม่สามารถเปลี่ยนข้อความคนออก")

                            elif teambotmax.startswith("setmember: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = int(sep[1])
                                try:
                                    settings["memberCancel"]["members"] = txt
                                    teambotmaxText(to, "✯͜͡❂ สำเร็จในการตั้งกลุ่มเข้าร่วมอัตโนมัติดเป็น {}".format(txt))
                                except:
                                    teambotmaxText(to, "✯͜͡❂ ไม่สามารถเปลี่ยนกลุ่มเข้าร่วมอัตโนมัติ")

                            elif teambotmax.startswith("setautoanswerchat: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["autoAnswerMessage"] = txt
                                    teambotmaxText(to, "✯͜͡❂ เปลี่ยนข้อความตอบกลับอัตโนมัติเป็น : 「{}」".format(txt))
                                except:
                                    teambotmaxText(to, "✯͜͡❂ ไม่สามารถเปลี่ยนข้อความตอบรับอัตโนมัติได้")

                            elif teambotmax.startswith("setcomment: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["commentPost"] = txt
                                    teambotmaxText(to, "✯͜͡❂ สำเร็จ\n✯͜͡❂ ความคิดเห็น : 「{}」".format(txt))
                                except:
                                    teambotmaxText(to, "✯͜͡❂ ล้มเหลว")

                            elif teambotmax.startswith("addsettings to "):
                              if sender in admin:
                                txt = removeCmd("addsettings to", text)
                                settings["{}".format(txt)] = []
                                f=codecs.open('setting.json','w','utf-8')
                                json.dump(settings, f, sort_keys=True, indent=4,ensure_ascii=False)
                                maxbots.sendReplyMessage(msg_id, to, "Succesfully add {} to settings".format(txt))

                            elif teambotmax.startswith("addsettings "):
                              if sender in admin:
                              	txt = removeCmd("addsettings", text)
                              	settings["{}".format(txt)] = False
                              	f=codecs.open('setting.json','w','utf-8')
                              	json.dump(settings, f, sort_keys=True, indent=4,ensure_ascii=False)
                              	maxbots.sendReplyMessage(msg_id, to, "Succesfully add {} to settings".format(txt))

                            elif teambotmax.startswith("delsettings "):
                              if sender in admin:
                              	txt = removeCmd("delsettings", text)
                              	del settings["{}".format(txt)]
                              	maxbots.sendReplyMessage(msg_id, to, "Succesfully del {} in settings".format(txt))

                            elif teambotmax == "myurl":
                              if msg._from in admin:
                                maxbots.reissueUserTicket()
                                arr = maxbots.profile.displayName + " Ticket URL : http://line.me/ti/p/" + maxbots.getUserTicket().id
                                maxbots.sendReplyMessage(msg_id, to, arr)
                                
                            elif teambotmax.startswith("chatowner: "):
                                contact = maxbots.getContact(sender)
                                sep = text.split(" ")
                                ryan = text.replace(sep[0] + " ","")
                                for own in contact:
                                    result = "@!"
                                    result += "\nSender : {}".format(contact.displayName)
                                    result += "\nPesan : {}".format(ryan)
                                    result += "\nMid : {}".format(contact.mid)
                                    maxbots.sendReplyMessage(msg_id, to, "Succesfully send chat to Owner")
                                    maxbots.sendMention(own, result, [sender])
                                    maxbots.sendContact(own, sender)

                            elif teambotmax.startswith("invtogc "):
                                key = eval(msg.contentMetadata["MENTION"])
                                tar = key["MENTIONEES"][0]["M"]
                                dan = text.split("|")
                                grr = maxbots.getGroupIdsJoined()
                                maxbots.findAndAddContactsByMid(tar)
                                try:
                                    listGroup = grr[int(dan)-1]
                                    gri = maxbots.getGroup(listGroup)
                                    maxbots.inviteIntoGroup(gri.id, [tar])
                                    maxbots.sendMessage(to, "Succesfully invite {} to group {}".format(tar.displayName, gri.name))
                                except Exception as e:
                                    maxbots.sendMessage(to, str(e))

                            elif teambotmax.startswith('stag '):
                                sep = text.split(" ")
                                num = int(sep[1])                           
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        for var in range(0,num):
                                            maxbots.sendMention(to, "@!", [ls])

                            elif teambotmax.startswith('scall '):
                                sep = text.split(" ")
                                num = int(sep[1])
                                try:                           
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            for var in range(0,num):
                                                group = maxbots.getGroup(to)
                                                members = [ls]
                                                kunkun = maxbots.getContact("uc14c3d87a1123df7c8ffa9d7402e59a2").displayName
                                                maxbots.acquireGroupCallRoute(to)
                                                maxbots.inviteIntoGroupCall(to, contactIds=members)
                                            maxbots.sendMention(to, "✯͜͡❂ สแปมโทรสำเร็จแล้ว @!", [ls])
                                except Exception as error:
                                    maxbots.sendMessage(to, str(error))

                            elif teambotmax.startswith("schat"):
                              if sender in admin:
                                text = text.split(" ")
                                jmlh = int(text[2])
                                balon = jmlh * (text[3]+"\n")
                                if text[1] == "on":
                                    if jmlh <= 10000:
                                        for x in range(jmlh):
                                            maxbots.sendMessage(to, text[3])
                                    else:
                                        maxbots.sendMention(to, "✯͜͡❂ ขออภัยจำนวนมากเกินไป @!", [sender])
                                elif text[1] == "off":
                                  if jmlh <= 10000:
                                    maxbots.sendMessage(to, balon)
                                  else:
                                    maxbots.sendMention(to, "✯͜͡❂ ขออภัยจำนวนมากเกินไป @!", [sender])

                            elif teambotmax.startswith('sgift '):
                                if msg.toType == 2:
                                    sep = text.split(" ")
                                    strnum = text.replace(sep[0] + " ","")
                                    num = int(strnum)
                                    gf = "b07c07bc-fcc1-42e1-bd56-9b821a826f4f","7f2a5559-46ef-4f27-9940-66b1365950c4","53b25d10-51a6-4c4b-8539-38c242604143","a9ed993f-a4d8-429d-abc0-2692a319afde"
                                    txt = "~Gift~"
                                    maxbots.sendMentionWithFooter(to, txt, "Succesfully Spam gift to your pc", [sender])
                                    for var in range(0,num):
                                       contact = maxbots.getContact(sender)
                                       maxbots.sendGift(contact.mid, random.choice(gf), "theme")                

                            elif teambotmax == "gift":
                                gf = "b07c07bc-fcc1-42e1-bd56-9b821a826f4f","7f2a5559-46ef-4f27-9940-66b1365950c4","53b25d10-51a6-4c4b-8539-38c242604143","a9ed993f-a4d8-429d-abc0-2692a319afde"
                                contact = maxbots.getContact(sender)
                                maxbots.sendGift(contact.mid, random.choice(gf), "theme")                                
                                sendMention(to, "✯͜͡❂ ส่งไปแล้ว @! ของขวัญ", [sender])                                                         

                            elif teambotmax.startswith('call '):
                                if msg.toType == 2:
                                    sep = text.split(" ")
                                    strnum = text.replace(sep[0] + " ","")
                                    num = int(strnum)
                                    teambotmaxText(to, "✯͜͡❂ สแปมโทรไปที่กลุ่มสำเร็จ")
                                    for var in range(0,num):
                                       group = maxbots.getGroup(to)
                                       members = [mem.mid for mem in group.members]
                                       maxbots.acquireGroupCallRoute(to)
                                       maxbots.inviteIntoGroupCall(to, contactIds=members)

                            elif teambotmax.startswith("เขียน "):
                                sep = msg.text.split(" ")
                                pesan = msg.text.replace(sep[0] + " ","")
                                teambotmaxS = maxbots.getContact(maxbotsMid)
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                maxbots.reissueUserTicket()
                                teambotmaxZ = {
                                        "type": "flex",
                                        "altText": "ƬΣΛM BӨƬ MΛX",
                                        "contents": {
  "type": "bubble",
  "size": "giga",
  "direction": "ltr",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "ON LINE",
        "weight": "bold",
        "color": "#1DB446",
        "size": "sm",
        "style": "normal",
        "decoration": "none",
        "position": "relative",
        "align": "start",
        "gravity": "bottom",
        "wrap": True
      },
      {
        "type": "text",
        "text": "✦ เขียนข้อความ ✦",
        "weight": "bold",
        "size": "xxl",
        "margin": "md",
        "style": "normal",
        "decoration": "none",
        "position": "relative",
        "align": "center",
        "gravity": "bottom",
        "wrap": True,
        "color": "#FF6600"
      },
      {
        "type": "text",
        "text": "" + datetime.strftime(timeNow,'%Y-%m-%d'),
        "size": "xs",
        "color": "#000000",
        "wrap": True,
        "weight": "bold",
        "style": "normal",
        "decoration": "underline",
        "position": "relative",
        "align": "center"
      },
      {
        "type": "separator",
        "margin": "xxl",
        "color": "#667788"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "xxl",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": pesan,
                "size": "lg",
                "color": "#555555",
                "flex": 0,
                "margin": "md",
                "weight": "bold",
                "style": "normal",
                "decoration": "none",
                "position": "relative",
                "align": "start",
                "gravity": "top",
                "wrap": True,
                "offsetTop": "0px"
              }
            ]
          },
          {
            "type": "separator",
            "margin": "xxl",
            "color": "#667788"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "margin": "xxl",
            "contents": [
              {
                "type": "text",
                "text": "• ชื่อ : {}".format(str(teambotmaxS.displayName)),
                "size": "sm",
                "color": "#000000",
                "margin": "none",
                "decoration": "none",
                "position": "relative",
                "align": "start",
                "gravity": "top",
                "wrap": True,
                "weight": "bold"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "• เวลา : " + datetime.strftime(timeNow,'%H:%M:%S') + " นาที",
                "size": "sm",
                "color": "#000000",
                "wrap": True,
                "align": "start",
                "weight": "bold"
              }
            ]
          }
        ]
      },
      {
        "type": "separator",
        "margin": "xxl",
        "color": "#667788"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "margin": "md",
        "contents": [
          {
            "type": "text",
            "text": "✦ กดเพื่อเพิ่มเพื่อน ✦",
            "size": "xs",
            "color": "#FF0098",
            "flex": 0,
            "weight": "bold",
            "style": "normal",
            "decoration": "none",
            "position": "relative",
            "wrap": True,
            "align": "start",
            "gravity": "top",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://line.me/ti/p/~" + maxbots.profile.userid
            }
          },
          {
            "type": "text",
            "text": "✦ กดเพื่อเพิ่มเพื่อน ✦",
            "color": "#FF002D",
            "size": "xs",
            "align": "end",
            "weight": "bold",
            "style": "normal",
            "decoration": "none",
            "position": "relative",
            "gravity": "top",
            "wrap": True,
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://line.me/ti/p/%40jnx0914l"
            }
          }
        ],
        "position": "relative",
        "spacing": "xs"
      }
    ]
  },
  "styles": {
    "hero": {
      "separator": True
    },
    "footer": {
      "separator": True
    }
  }
}
}
                                maxbots.postTemplate(to, teambotmaxZ)

                            elif teambotmax.startswith(".ประกาศ "):
                                sep = text.split(" ")
                                pesan = text.replace(sep[0] + " ","")
                                groups = maxbots.getGroupIdsJoined()
                                teambotmaxS = maxbots.getContact(maxbotsMid)
                                for gr in groups:                                    
                                    friend = maxbots.getAllContactIds()
                                    group = maxbots.getGroupIdsJoined()
                                    maxbots.reissueUserTicket()
                                    teambotmaxZ = {
                                            "type": "flex",
                                            "altText": "ƬΣΛM BӨƬ MΛX",
                                            "contents": {
  "type": "bubble",
  "size": "giga",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "ON LINE",
        "weight": "bold",
        "color": "#1DB446",
        "size": "sm"
      },
      {
        "type": "image",
        "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus),
        "aspectMode": "cover",
        "size": "full"
      },
      {
        "type": "text",
        "text": "✦ ข้อความประกาศ ✦",
        "weight": "bold",
        "size": "xxl",
        "margin": "md",
        "align": "center",
        "wrap": True
      },
      {
        "type": "text",
        "text": "{}".format(str(teambotmaxS.displayName)),
        "size": "xs",
        "color": "#FF6E00",
        "wrap": True,
        "align": "center",
        "weight": "bold"
      },
      {
        "type": "separator",
        "margin": "xxl"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "xxl",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": pesan,
                "size": "xl",
                "color": "#555555",
                "flex": 0,
                "weight": "bold",
                "wrap": True
              }
            ]
          },
          {
            "type": "separator",
            "margin": "xxl"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "margin": "xxl",
            "contents": [
              {
                "type": "text",
                "text": "• เพื่อน",
                "size": "sm",
                "color": "#00B016",
                "weight": "bold"
              },
              {
                "type": "text",
                "text": "{}".format(str(len(friend))),
                "size": "sm",
                "color": "#ff0099",
                "align": "end",
                "weight": "bold"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "• กลุ่ม",
                "size": "sm",
                "color": "#00B016",
                "weight": "bold"
              },
              {
                "type": "text",
                "text": "{}".format(str(len(group))),
                "size": "sm",
                "color": "#ff0099",
                "align": "end",
                "weight": "bold"
              }
            ]
          }
        ]
      },
      {
        "type": "separator",
        "margin": "xxl"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "margin": "md",
        "contents": [
          {
            "type": "text",
            "text": "✦ กดเพื่อเพิ่มเพื่อน ✦",
            "size": "xs",
            "color": "#ff0000",
            "flex": 0,
            "weight": "bold",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://line.me/ti/p/~" + maxbots.profile.userid
            }
          },
          {
            "type": "text",
            "text": "✦ กดเพื่อเพิ่มเพื่อน ✦",
            "color": "#0011FF",
            "size": "xs",
            "align": "end",
            "weight": "bold",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://line.me/ti/p/%40jnx0914l"
            }
          }
        ]
      }
    ]
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}
}
                                    bcTemplate(gr, teambotmaxZ)
                                    time.sleep(1)
                                    print ("ประกาศกลุ่มเรียบร้อย")

                            elif teambotmax.startswith("ประกาศ2 "):
                                sep = text.split(" ")
                                pesan = text.replace(sep[0] + " ","")
                                groups = maxbots.getGroupIdsJoined()
                                teambotmaxS = maxbots.getContact(maxbotsMid)
                                for gr in groups:
                                    timeNow = time.time()
                                    runtime = timeNow - botStart
                                    runtime = format_timespan(runtime)
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    maxbots.reissueUserTicket()
                                    teambotmaxZ = {
                                            "type": "flex",
                                            "altText": "ƬΣΛM BӨƬ MΛX",
                                            "contents": {
  "type": "bubble",
  "size": "giga",
  "direction": "ltr",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "ON LINE",
        "weight": "bold",
        "color": "#1DB446",
        "size": "sm",
        "style": "normal",
        "decoration": "none",
        "position": "relative",
        "align": "start",
        "gravity": "bottom",
        "wrap": True
      },
      {
        "type": "text",
        "text": "✦ ข้อความประกาศ ✦",
        "weight": "bold",
        "size": "xxl",
        "margin": "md",
        "style": "normal",
        "decoration": "none",
        "position": "relative",
        "align": "center",
        "gravity": "bottom",
        "wrap": True,
        "color": "#FF6600"
      },
      {
        "type": "text",
        "text": "" + datetime.strftime(timeNow,'%Y-%m-%d'),
        "size": "xs",
        "color": "#000000",
        "wrap": True,
        "weight": "bold",
        "style": "normal",
        "decoration": "underline",
        "position": "relative",
        "align": "center"
      },
      {
        "type": "separator",
        "margin": "xxl",
        "color": "#667788"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "xxl",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": pesan,
                "size": "lg",
                "color": "#555555",
                "flex": 0,
                "margin": "md",
                "weight": "bold",
                "style": "normal",
                "decoration": "none",
                "position": "relative",
                "align": "start",
                "gravity": "top",
                "wrap": True,
                "offsetTop": "0px"
              }
            ]
          },
          {
            "type": "separator",
            "margin": "xxl",
            "color": "#667788"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "margin": "xxl",
            "contents": [
              {
                "type": "text",
                "text": "• ชื่อ : {}".format(str(teambotmaxS.displayName)),
                "size": "sm",
                "color": "#000000",
                "margin": "none",
                "decoration": "none",
                "position": "relative",
                "align": "start",
                "gravity": "top",
                "wrap": True,
                "weight": "bold"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "• เวลา : " + datetime.strftime(timeNow,'%H:%M:%S') + " นาที",
                "size": "sm",
                "color": "#000000",
                "wrap": True,
                "align": "start",
                "weight": "bold"
              }
            ]
          }
        ]
      },
      {
        "type": "separator",
        "margin": "xxl",
        "color": "#667788"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "margin": "md",
        "contents": [
          {
            "type": "text",
            "text": "✦ กดเพื่อเพิ่มเพื่อน ✦",
            "size": "xs",
            "color": "#FF0098",
            "flex": 0,
            "weight": "bold",
            "style": "normal",
            "decoration": "none",
            "position": "relative",
            "wrap": True,
            "align": "start",
            "gravity": "top",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://line.me/ti/p/~" + maxbots.profile.userid
            }
          },
          {
            "type": "text",
            "text": "✦ กดเพื่อเพิ่มเพื่อน ✦",
            "color": "#FF002D",
            "size": "xs",
            "align": "end",
            "weight": "bold",
            "style": "normal",
            "decoration": "none",
            "position": "relative",
            "gravity": "top",
            "wrap": True,
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "http://line.me/ti/p/%40jnx0914l"
            }
          }
        ],
        "position": "relative",
        "spacing": "xs"
      }
    ]
  },
  "styles": {
    "hero": {
      "separator": True
    },
    "footer": {
      "separator": True
    }
  }
}
}
                                    bcTemplate(gr, teambotmaxZ)
                                    time.sleep(1)
                                    print ("ประกาศกลุ่มเรียบร้อย")

                            elif teambotmax.startswith("ประกาศ3 "):
                                sep = text.split(" ")
                                pesan = text.replace(sep[0] + " ","")
                                groups = maxbots.getGroupIdsJoined()
                                teambotmaxS = maxbots.getContact(maxbotsMid)
                                for gr in groups:
                                    maxbots.reissueUserTicket()
                                    teambotmaxZ = {
                                            "type": "flex",
                                            "altText": "ƬΣΛM BӨƬ MΛX",
                                            "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "giga",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://www.img.live/images/2019/11/02/PicsArt_11-02-12.07.09.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "text",
                    "text": pesan,
                    "size": "md",
                    "color": "#ffffff",
                    "weight": "bold",
                    "align": "center",
                    "wrap": True,
                    "gravity": "top"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "icon",
                        "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus)
                      },
                      {
                        "type": "text",
                        "text": "กดตรงนี้เพื่อเพิ่มเพื่อนฉัน",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "https://line.me/ti/p/~" + maxbots.profile.userid
                        }
                      },
                      {
                        "type": "icon",
                        "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus)
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "icon",
                        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                      },
                      {
                        "type": "text",
                        "text": "กดตรงนี้เพื่อเพิ่มเพื่อนฉัน",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "http://line.me/ti/p/%40jnx0914l"
                        }
                      },
                      {
                        "type": "icon",
                        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "paddingAll": "20px",
            "paddingTop": "18px",
            "borderWidth": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "NEW",
                "color": "#ffffff",
                "align": "center",
                "size": "xs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "18px",
            "backgroundColor": "#ff334b",
            "offsetStart": "18px",
            "height": "25px",
            "width": "53px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#000000"
      }
    }
  ]
}
}
                                    bcTemplate(gr, teambotmaxZ)
                                    time.sleep(1)
                                    print ("ประกาศกลุ่มเรียบร้อย")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "test help":
                                teambotmax1 = ("#0008FF","#000000","#058700","#DE00D4","#05092A","#310206","#5300FC")
                                teambotmax2 = random.choice(teambotmax1)
                                maxbots.reissueUserTicket()
                                teambotmaxZ = {
                                        "type": "flex",
                                        "altText": "ƬΣΛM BӨƬ MΛX",
                                        "contents": {
  "type": "bubble",
  "size": "giga",
  "hero": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus),
        "size": "full",
        "aspectRatio": "1:1",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "uri": "https://line.me/ti/p/~" + maxbots.profile.userid
        }
      }
    ],
    "borderColor": "#000000",
    "borderWidth": "4px"
  }
}
}
                                maxbots.postTemplate(to, teambotmaxZ) 
                                teambotmaxZ = {
                                        "type": "flex",
                                        "altText": "ƬΣΛM BӨƬ MΛX",
                                        "contents": {
  "type": "bubble",
  "size": "giga",
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xl",
    "contents": [
      {
        "type": "box",
        "layout": "baseline",
        "spacing": "sm",
        "contents": [
          {
            "type": "icon",
            "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
          },
          {
            "type": "text",
            "text": "Help1 - 2",
            "wrap": True,
            "color": "#FFFFFF",
            "size": "md",
            "flex": 5,
            "weight": "bold"
          }
        ]
      },
      {
        "type": "box",
        "layout": "baseline",
        "spacing": "sm",
        "contents": [
          {
            "type": "icon",
            "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
          },
          {
            "type": "text",
            "text": "Help1 - 2",
            "wrap": True,
            "color": "#FFFFFF",
            "size": "md",
            "flex": 5,
            "weight": "bold"
          }
        ]
      },
      {
        "type": "box",
        "layout": "baseline",
        "spacing": "sm",
        "contents": [
          {
            "type": "icon",
            "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
          },
          {
            "type": "text",
            "text": "Help1 - 2",
            "wrap": True,
            "color": "#FFFFFF",
            "size": "md",
            "flex": 5,
            "weight": "bold"
          }
        ]
      },
      {
        "type": "box",
        "layout": "baseline",
        "spacing": "sm",
        "contents": [
          {
            "type": "icon",
            "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
          },
          {
            "type": "text",
            "text": "Help1 - 2",
            "wrap": True,
            "color": "#FFFFFF",
            "size": "md",
            "flex": 5,
            "weight": "bold"
          }
        ]
      },
      {
        "type": "box",
        "layout": "baseline",
        "spacing": "sm",
        "contents": [
          {
            "type": "icon",
            "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
          },
          {
            "type": "text",
            "text": "Help1 - 2",
            "wrap": True,
            "color": "#FFFFFF",
            "size": "md",
            "flex": 5,
            "weight": "bold"
          }
        ]
      },
      {
        "type": "box",
        "layout": "baseline",
        "spacing": "sm",
        "contents": [
          {
            "type": "icon",
            "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
          },
          {
            "type": "text",
            "text": "Help1 - 2",
            "wrap": True,
            "color": "#FFFFFF",
            "size": "md",
            "flex": 5,
            "weight": "bold"
          }
        ]
      },
      {
        "type": "box",
        "layout": "baseline",
        "spacing": "sm",
        "contents": [
          {
            "type": "icon",
            "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
          },
          {
            "type": "text",
            "text": "Help1 - 2",
            "wrap": True,
            "color": "#FFFFFF",
            "size": "md",
            "flex": 5,
            "weight": "bold"
          }
        ]
      },
      {
        "type": "box",
        "layout": "baseline",
        "spacing": "sm",
        "contents": [
          {
            "type": "icon",
            "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
          },
          {
            "type": "text",
            "text": "Help1 - 2",
            "wrap": True,
            "color": "#FFFFFF",
            "size": "md",
            "flex": 5,
            "weight": "bold"
          }
        ]
      },
      {
        "type": "box",
        "layout": "baseline",
        "spacing": "sm",
        "contents": [
          {
            "type": "icon",
            "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
          },
          {
            "type": "text",
            "text": "Help1 - 2",
            "wrap": True,
            "color": "#FFFFFF",
            "size": "md",
            "flex": 5,
            "weight": "bold"
          }
        ]
      },
      {
        "type": "box",
        "layout": "baseline",
        "spacing": "sm",
        "contents": [
          {
            "type": "icon",
            "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
          },
          {
            "type": "text",
            "text": "Help1 - 2",
            "wrap": True,
            "color": "#FFFFFF",
            "size": "md",
            "flex": 5,
            "weight": "bold"
          }
        ]
      }
    ],
    "borderColor": "#000000",
    "borderWidth": "4px",
    "backgroundColor": teambotmax2
  }
}
}
                                maxbots.postTemplate(to, teambotmaxZ) 
                                teambotmaxZ = {
                                        "type": "flex",
                                        "altText": "ƬΣΛM BӨƬ MΛX",
                                        "contents": {
  "type": "bubble",
  "size": "giga",
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "✦ ติดต่อคนขายบอท ✦",
          "uri": "https://line.me/ti/p/~" + maxbots.profile.userid
        },
        "color": "#000000"
      },
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "✦ ติดต่อแอดมินบอท ✦",
          "uri": "http://line.me/ti/p/%40jnx0914l"
        },
        "color": "#000000"
      }
    ],
    "flex": 0,
    "borderColor": "#000000",
    "borderWidth": "4px",
    "spacing": "sm",
    "backgroundColor": teambotmax2
  },
  "styles": {
    "hero": {
      "separator": False,
      "separatorColor": "#000000"
    },
    "body": {
      "separatorColor": "#FFFFFF",
      "separator": True
    },
    "footer": {
      "separatorColor": "#000000",
      "separator": True
    }
  }
}
}
                                maxbots.postTemplate(to, teambotmaxZ) 
#=======================ADD- STICKER ==================================================================================
                            if teambotmax in stickerss:
                                sid = stickerss[teambotmax]["STKID"]
                                spkg = stickerss[teambotmax]["STKPKGID"]
                                if "STKOPT" in stickerss[teambotmax]:
                                  url = "https://stickershop.line-scdn.net/stickershop/v1/sticker/"+sid+"/IOS/sticker_animation@2x.png"
                                else:
                                  url = "https://stickershop.line-scdn.net/stickershop/v1/sticker/"+sid+"/ANDROID/sticker.png"
                                maxSticker(to, url, "line://shop/detail/"+spkg)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "55" or teambotmax == "555" or teambotmax == "5555" or teambotmax == "55555":
                                maxSticker(to, "https://stickershop.line-scdn.net/stickershop/v1/sticker/17567226/IOS/sticker_animation@2x.png", "line://shop/detail/1471755")
                                maxbots.unsendMessage(msg_id)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "เออ":
                                maxSticker(to, "https://stickershop.line-scdn.net/stickershop/v1/sticker/17567226/IOS/sticker_animation@2x.png", "line://shop/detail/1471755")                                
                                maxbots.unsendMessage(msg_id)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "ไม่แคร์":
                                maxSticker(to, "https://stickershop.line-scdn.net/stickershop/v1/sticker/18125796/IOS/sticker_animation@2x.png", "line://shop/detail/1495172")
                                maxbots.unsendMessage(msg_id)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "จุ๊บ":
                                maxSticker(to, "https://stickershop.line-scdn.net/stickershop/v1/sticker/26538897/IOS/sticker_animation@2x.png", "line://shop/detail/10272")
                                maxbots.unsendMessage(msg_id)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "ฮ่าฮ่า":
                                maxSticker(to, "https://stickershop.line-scdn.net/stickershop/v1/sticker/5811369/ANDROID/sticker.png", "line://shop/detail/1142501")
                                maxbots.unsendMessage(msg_id)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "ตบ":
                                maxSticker(to, "https://stickershop.line-scdn.net/stickershop/v1/sticker/8421103/ANDROID/sticker.png", "line://shop/detail/1207313")
                                maxbots.unsendMessage(msg_id)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "แงๆ":
                                maxSticker(to, "https://stickershop.line-scdn.net/stickershop/v1/sticker/34866174/IOS/sticker_animation@2x.png", "line://shop/detail/3208994")
                                maxbots.unsendMessage(msg_id)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "วนๆ":
                                maxSticker(to, "https://stickershop.line-scdn.net/stickershop/v1/sticker/22987197/IOS/sticker_animation@2x.png", "line://shop/detail/1711359")
                                maxbots.unsendMessage(msg_id)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "addresponsticker":
                              if msg._from in admin:
                                settings["messageSticker"]["addStatus"] = True
                                settings["messageSticker"]["addName"] = "responSticker"
                                sendTextMax9(to, "✯͜͡❂ กรุณาส่งสติ๊กเกอร์")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "delresponsticker":
                              if msg._from in admin:
                                settings["messageSticker"]["listSticker"]["responSticker"] = None
                                sendTextMax9(to, "✯͜͡❂ ลบสติ๊กเกอร์แล้ว")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "addautoaddsticker":
                              if msg._from in admin:
                                settings["messageSticker"]["addStatus"] = True
                                settings["messageSticker"]["addName"] = "addSticker"
                                sendTextMax9(to, "✯͜͡❂ กรุณาส่งสติ๊กเกอร์")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "delautoaddsticker":
                              if msg._from in admin:
                                settings["messageSticker"]["listSticker"]["addSticker"] = None
                                sendTextMax9(to, "✯͜͡❂ ลบสติ๊กเกอร์แล้ว")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "addsidersticker":
                              if msg._from in admin:
                                settings["messageSticker"]["addStatus"] = True
                                settings["messageSticker"]["addName"] = "readerSticker"
                                sendTextMax9(to, "✯͜͡❂ กรุณาส่งสติ๊กเกอร์")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "delsidersticker":
                              if msg._from in admin:
                                settings["messageSticker"]["listSticker"]["readerSticker"] = None
                                sendTextMax9(to, "✯͜͡❂ ลบสติ๊กเกอร์แล้ว")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "addwelcomesticker":
                              if msg._from in admin:
                                settings["messageSticker"]["addStatus"] = True
                                settings["messageSticker"]["addName"] = "welcomeSticker"
                                sendTextMax9(to, "✯͜͡❂ กรุณาส่งสติ๊กเกอร์")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "delwelcomesticker":
                              if msg._from in admin:
                                settings["messageSticker"]["listSticker"]["welcomeSticker"] = None
                                sendTextMax9(to, "✯͜͡❂ ลบสติ๊กเกอร์สำเร็จแล้ว")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "addleavesticker":
                              if msg._from in admin:
                                settings["messageSticker"]["addStatus"] = True
                                settings["messageSticker"]["addName"] = "leaveSticker"
                                sendTextMax9(to, "✯͜͡❂ กรุณาส่งสติ๊กเกอร์")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "delleavesticker":
                              if msg._from in admin:
                                settings["messageSticker"]["listSticker"]["leaveSticker"] = None
                                sendTextMax9(to, "✯͜͡❂ ลบสติ๊กเกอร์สำเร็จแล้ว")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("addsticker "):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in stickers:
                                    settings["addSticker"]["status"] = True
                                    settings["addSticker"]["name"] = str(name.lower())
                                    stickers[str(name.lower())] = {}
                                    f = codecs.open('sticker.json','w','utf-8')
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextMax9(to, "✯͜͡❂ ส่งสติ๊กเกอร์ของคุณ")
                                else:
                                    sendTextMax9(to, "✯͜͡❂ มีสติกเกอร์ชื่อนี้แล้วในรายการ")                     
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("delsticker "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in stickers:
                                    del stickers[str(name.lower())]
                                    f = codecs.open("sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextMax9(to, "✯͜͡❂ นำสติกเกอร์ออกสำเร็จ {}".format( str(name.lower())))
                                else:
                                    sendTextMax9(to, "✯͜͡❂ สติกเกอร์ไม่ได้อยู่ในรายการ")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "list sticker":
                               if msg._from in admin:
                                 no = 0
                                 ret_ = "✯͜͡❂ รายการสติ๊กเกอร์\n\n"
                                 for sticker in stickers:
                                     no += 1
                                     ret_ += str(no) + ". " + sticker.title() + "\n"
                                 ret_ += "\n✯͜͡❂ ทั้งหมด {} สติกเกอร์".format(str(len(stickers)))
                                 teambotmaxText(to, ret_)
#============================ADD STICKER TEMPLATE====================================≠
                            elif teambotmax.startswith("addstp "):
                              ssn = maxbots.getContact(sender).mid
                              ssnd.append(ssn)
                              if sender in ssnd:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in stickers:
                                    settings["addStickertemplate"]["statuss"] = True
                                    settings["addStickertemplate"]["namee"] = str(name.lower())
                                    stickerstemplate[str(name.lower())] = {}
                                    f = codecs.open('stickertemplate.json','w','utf-8')
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextMax9(to, "✯͜͡❂ ส่งสติ๊กเกอร์ของคุณ")
                                else:
                                    sendTextMax9(to, "✯͜͡❂ มีสติกเกอร์ชื่อนี้แล้วในรายการ")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("delstp "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in stickerstemplate:
                                    del stickerstemplate[str(name.lower())]
                                    f = codecs.open("stickertemplate.json","w","utf-8")
                                    json.dump(stickerstemplate, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextMax9(to, "✯͜͡❂ นำสติกเกอร์ออกสำเร็จ\n {}".format( str(name.lower())))
                                else:
                                    sendTextMax9(to, "✯͜͡❂ สติกเกอร์ไม่ได้อยู่ในรายการ")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "list stp":
                               if msg._from in admin:
                                 no = 0
                                 ret_ = "✯͜͡❂ รายการสติกเกอร์ตัวใหญ่\n\n"
                                 for sticker in stickerstemplate:
                                     no += 1
                                     ret_ += str(no) + ". " + sticker.title() + "\n"
                                 ret_ += "\n✯͜͡❂ ทั้งหมด {} สติกเกอร์".format(str(len(stickers)))
                                 maxbots.sendMessageWithFooter(to, ret_)
#============================================================================================
                            elif teambotmax.startswith("changekey"):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                settings["tatan"] = "{}".format(txt)
                                maxbots.sendReplyMessage(msg_id, to, "✯͜͡❂ เปลี่ยนคีย์ด้วยคีย์สำเร็จ {}".format(settings["tatan"]))
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("changename: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                if len(name) <= 999:
                                    profile = maxbots.getProfile()
                                    profile.displayName = name
                                    maxbots.updateProfile(profile)
                                    maxbots.sendMessageWithFooter(to, "✯͜͡❂ เปลี่ยนชื่อเป็น : {}".format(name))
                              else:
                                  txt = ("Hmmmm gk bsa ya :(","Sorryy :(","Jgn Ubah Namaku :(")
                                  pop = random.choice(txt)
                                  maxbots.sendMessageWithFooter(to, pop)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("changebio: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                bio = text.replace(sep[0] + " ","")
                                if len(bio) <= 100000:
                                    profile = maxbots.getProfile()
                                    profile.statusMessage = bio
                                    maxbots.updateProfile(profile)
                                    maxbots.sendMessageWithFooter(to, "✯͜͡❂ เปลี่ยนสเตตัสเป็น : {}".format(bio))
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "check me":
                                maxbots.sendMention(to, "@!", [sender])
                                maxbots.sendFakeReplyContact(msg_id, to, sender)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "myprofile":
                                arr = []
                                teambotmaxS = maxbots.getContact(maxbotsMid)                                    
                                friend = maxbots.getAllContactIds()
                                group = maxbots.getGroupIdsJoined()
                                blockedlist = maxbots.getBlockedContactIds()
                                favorite = maxbots.getFavoriteMids()
                                userid = maxbots.getProfile().userid
                                region = maxbots.getProfile().regionCode
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                teambotmaxZ = {
                                        "type": "flex",
                                        "altText": "ƬΣΛM BӨƬ MΛX",
                                        "contents": {
  "type": "bubble",
  "size": "giga",
  "hero": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus),
        "aspectRatio": "1:1",
        "size": "full",
        "aspectMode": "cover"
      }
    ],
    "borderColor": "#000000",
    "borderWidth": "2px"
  }
}
}
                                maxbots.postTemplate(to, teambotmaxZ) 
                                teambotmaxZ = {
                                        "type": "flex",
                                        "altText": "ƬΣΛM BӨƬ MΛX",
                                        "contents": {
  "type": "bubble",
  "size": "giga",
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "contents": [
      {
        "type": "text",
        "text": "ข้อมูลโปรไฟล์",
        "wrap": True,
        "weight": "bold",
        "gravity": "center",
        "size": "xxl",
        "color": "#000000",
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "box",
        "layout": "baseline",
        "margin": "md",
        "contents": [
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
          },
          {
            "type": "text",
            "text": "5.0",
            "size": "sm",
            "color": "#999999",
            "margin": "md",
            "flex": 0
          }
        ]
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "กลุ่ม",
                "color": "#000000",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "{}".format(str(len(group))),
                "wrap": True,
                "size": "sm",
                "color": "#000000",
                "flex": 4
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "เพื่อน",
                "color": "#000000",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "{}".format(str(len(friend))),
                "wrap": True,
                "color": "#000000",
                "size": "sm",
                "flex": 4
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "บล็อก",
                "color": "#000000",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "{}".format(str(len(blockedlist))),
                "wrap": True,
                "color": "#000000",
                "size": "sm",
                "flex": 4
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "ปักหมุด",
                "color": "#000000",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "{}".format(str(len(favorite))),
                "wrap": True,
                "color": "#000000",
                "size": "sm",
                "flex": 4
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "วันที่",
                "color": "#000000",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "" + datetime.strftime(timeNow,'%Y-%m-%d'),
                "wrap": True,
                "color": "#000000",
                "size": "sm",
                "flex": 4
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "เวลา",
                "color": "#000000",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "" + datetime.strftime(timeNow,'%H:%M:%S') + " นาที",
                "wrap": True,
                "color": "#000000",
                "size": "sm",
                "flex": 4
              }
            ]
          }
        ]
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(maxbotsMid).pictureStatus),
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "cornerRadius": "100px",
            "width": "80px",
            "height": "80px",
            "borderColor": "#000000",
            "borderWidth": "2px"
          },
          {
            "type": "separator",
            "color": "#000000"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "• ชื่อ : {}".format(str(teambotmaxS.displayName)),
                "size": "md",
                "color": "#000000",
                "weight": "bold",
                "wrap": True
              },
              {
                "type": "text",
                "text": "• เวลาทำงาน : {}".format(str(runtime)),
                "size": "md",
                "color": "#000000",
                "weight": "bold",
                "wrap": True
              }
            ]
          }
        ],
        "spacing": "xl"
      }
    ],
    "borderColor": "#000000",
    "borderWidth": "2px"
  }
}
}
                                maxbots.postTemplate(to, teambotmaxZ)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "mymid":
                                contact = maxbots.getContact(sender)
                                maxbots.sendMention(to, "@!\n{}".format(contact.mid), [sender])
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "myname":
                                contact = maxbots.getContact(sender)
                                maxbots.sendMention(to, "@!\n{}".format(contact.displayName), [sender])
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "mybio":
                                contact = maxbots.getContact(sender)
                                maxbots.sendMention(to, "@!\n{}".format(contact.statusMessage), [sender])
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "mypicture":
                                contact = maxbots.getContact(sender)
                                maxbots.sendReplyImageWithURL(msg_id, to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "myvideoprofile":
                                contact = maxbots.getContact(sender)
                                if contact.videoProfile == None:
                                    return maxbots.sendMessage(to, "Anda tidak memiliki video profile")
                                maxbots.sendVideoWithURL(msg_id, to, "http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "mycover":
                                cover = maxbots.getProfileCoverURL(sender)
                                maxbots.sendReplyImageWithURL(msg_id, to, str(cover))
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "mycover url":
                                cover = maxbots.getProfileCoverURL(sender)
                                teambotmaxText(to, str(cover))
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("getmid "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        maxbots.sendMention(to, "@!: \n{}".format(ls), [ls])
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("getcontact "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                maxbots.sendContact(to, txt)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("getidline "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        checkticket = maxbots.getContact(ls).userid
                                        maxbots.sendMention(to, "@!: {}".format(checkticket), [ls])
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("getname "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = maxbots.getContact(ls)
                                        maxbots.sendMention(to, "@!: {}".format(contact.displayName), [ls])
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("getbio "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = maxbots.getContact(ls)
                                        maxbots.sendMention(to, "@!: {}".format(contact.statusMessage), [ls])
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("getpict "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        teambotmax1 = maxbots.getContact(ls)
                                        teambotmaxZ = {
                                                "type": "flex",
                                                "altText": "ƬΣΛM BӨƬ MΛX",
                                                "contents": {
  "type": "bubble",
  "size": "giga",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(ls).pictureStatus),
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:1",
        "gravity": "top"
      }
    ],
    "paddingAll": "0px",
    "borderColor": "#000000",
    "borderWidth": "3px",
    "cornerRadius": "5px",
    "action": {
      "type": "uri",
      "uri": "line://app/1548590302-1wOdbYEL/?type=image&img=https://os.line.naver.jp/os/p/{}".format(teambotmax1)
    }
  }
}
}
                                        maxbots.postTemplate(receiver, teambotmaxZ)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("getvideo "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = maxbots.getContact(ls)
                                        if contact.videoProfile == None:
                                            return maxbots.sendMention(to, "@!tidak memiliki video profile", [ls])
                                        maxbots.sendReplyVideoWithURL(msg.id, to, "http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("getcover "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        teambotmax1 = maxbots.getProfileCoverURL(ls)
                                        teambotmaxZ = {
                                                "type": "flex",
                                                "altText": "ƬΣΛM BӨƬ MΛX",
                                                "contents": {
  "type": "bubble",
  "size": "giga",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": teambotmax1,
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "2:3",
        "gravity": "top"
      }
    ],
    "paddingAll": "0px",
    "borderColor": "#000000",
    "borderWidth": "3px",
    "cornerRadius": "5px",
    "action": {
      "type": "uri",
      "uri": "line://app/1548590302-1wOdbYEL/?type=image&img=https://os.line.naver.jp/os/p/{}".format(teambotmax1)
    }
  }
}
}
                                        maxbots.postTemplate(receiver, teambotmaxZ)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("getme "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        teambotmax1 = maxbots.getContact(ls)
                                        teambotmax2 = maxbots.getProfileCoverURL(ls)
                                        teambotmaxZ = {
                                                "type": "flex",
                                                "altText": "ƬΣΛM BӨƬ MΛX",
                                                "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(ls).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "℘ɧσtσ ℘гσʄıɭε",
                    "size": "xl",
                    "color": "#ffffff",
                    "weight": "bold",
                    "align": "center"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "• ชื่อ : ",
                    "color": "#ebebeb",
                    "size": "sm",
                    "flex": 0
                  },
                  {
                    "type": "text",
                    "text": "{}".format(teambotmax1.displayName),
                    "color": "#ffffffcc",
                    "gravity": "bottom",
                    "flex": 0,
                    "size": "sm"
                  }
                ],
                "spacing": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "icon",
                        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                      },
                      {
                        "type": "text",
                        "text": "กดตรงนี้เพื่อติดต่อแอดมิน",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px"
                      },
                      {
                        "type": "icon",
                        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/%40jnx0914l"
                }
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#03303Acc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Profile",
                "color": "#ffffff",
                "align": "center",
                "size": "xs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "18px",
            "backgroundColor": "#ff334b",
            "offsetStart": "18px",
            "height": "25px",
            "width": "53px"
          }
        ],
        "paddingAll": "0px",
        "borderColor": "#ff0011",
        "borderWidth": "0px",
        "cornerRadius": "17px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": teambotmax2,
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "℘ɧσtσ ɕσvεг",
                    "size": "xl",
                    "color": "#ffffff",
                    "weight": "bold",
                    "align": "center"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "• ชื่อ : ",
                    "color": "#ebebeb",
                    "size": "sm",
                    "flex": 0
                  },
                  {
                    "type": "text",
                    "text": "{}".format(teambotmax1.displayName),
                    "color": "#ffffffcc",
                    "gravity": "bottom",
                    "flex": 0,
                    "size": "sm"
                  }
                ],
                "spacing": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "icon",
                        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                      },
                      {
                        "type": "text",
                        "text": "กดตรงนี้เพื่อติดต่อแอดมิน",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px"
                      },
                      {
                        "type": "icon",
                        "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "4px",
                "spacing": "sm",
                "borderColor": "#ffffff",
                "margin": "xxl",
                "height": "40px",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/%40jnx0914l"
                }
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#03303Acc",
            "paddingAll": "20px",
            "paddingTop": "18px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Cover",
                "color": "#ffffff",
                "align": "center",
                "size": "xs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "18px",
            "backgroundColor": "#ff334b",
            "offsetStart": "18px",
            "height": "25px",
            "width": "53px"
          }
        ],
        "paddingAll": "0px",
        "borderColor": "#ff0011",
        "borderWidth": "0px",
        "cornerRadius": "17px"
      }
    }
  ]
}
}
                                        maxbots.postTemplate(receiver, teambotmaxZ)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("cloneprofile "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        maxbots.cloneContactProfile(ls)
                                        maxbots.sendContact(to, sender)
                                        teambotmaxText(to, "Berhasil clone profile")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "friendlist":
                              if msg._from in admin:
                                contacts = maxbots.getAllContactIds()
                                num = 0
                                result = "╭───「 Friend List 」"
                                for listContact in contacts:
                                    contact = maxbots.getContact(listContact)
                                    num += 1
                                    result += "\n├ • {}. {}".format(num, contact.displayName)
                                result += "\n╰───「 Total {} Friend 」".format(len(contacts))
                                maxbots.sendReplyMessage(msg_id, to, result)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("friendinfo "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                contacts = maxbots.getAllContactIds()
                                try:
                                    listContact = contacts[int(query)-1]
                                    contact = maxbots.getContact(listContact)
                                    cover = maxbots.getProfileCoverURL(listContact)
                                    result = "╭───「 Details Profile 」"
                                    result += "\n├ • Display Name : @!"
                                    result += "\n├ • Mid : {}".format(contact.mid)
                                    result += "\n├ • Status Message : {}".format(contact.statusMessage)
                                    result += "\n├ • Picture Profile : http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                                    result += "\n├ • Cover : {}".format(str(cover))
                                    result += "\n╰───「 Finish 」"
                                    maxbots.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                                    maxbots.sendMention(to, result, [contact.mid])
                                except Exception as error:
                                    logError(error)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("delfriendmid "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                maxbots.deleteContact(txt)
                                maxbots.sendFakeMessage(to, "Done",txt)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("delfriend "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        maxbots.deleteContact(ls)
                                        maxbots.sendReplyMessage(msg_id, to, "Udah euy")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("addfavorite "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        maxbots.addFavorite(ls)
                                        maxbots.sendReplyMention(msg_id, to, "Succesfully add @! to Favorite Friend", [ls])
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("rename "):
                                sep = text.split(" ")
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        maxbots.renameContact(ls,sep[1])
                                        maxbots.sendReplyMention(msg_id, to, "Succesfully change @! display name to {}".format(sep[1]), [ls])
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "blocklist":
                              if msg._from in admin:
                                blockeds = maxbots.getBlockedContactIds()
                                num = 0
                                result = "╭───「 Block List 」"
                                for listBlocked in blockeds:
                                    contact = maxbots.getContact(listBlocked)
                                    num += 1
                                    result += "\n├ ⌬ {}. {}".format(num, contact.displayName)
                                result += "\n╰───「 Total {} Blocked 」".format(len(blockeds))
                                teambotmaxText(to, result)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("changegroupname: "):
                                if msg.toType == 2:
                                    sep = text.split(" ")
                                    groupname = text.replace(sep[0] + " ","")
                                    if len(groupname) <= 100:
                                        group = maxbots.getGroup(to)
                                        group.name = groupname
                                        maxbots.updateGroup(group)
                                        teambotmaxText(to, "Berhasil mengubah nama group menjadi : {}".format(groupname))
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("not"):
                                sep = text.split("|")
                                nom = sep[1]
                                nam = sep[2]
                                maxbots.sendContactHP(to, "Kntlll", nom, nam)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "foot":
                                con = {'AGENT_ICON': 'http://profile.line-cdn.net/0hcr26oFItPF0PTxGrOrtDCjMKMjB4YToVdyx1MypOZmR1LXMPMiF2b31GMD5xfSgPZCogOC1GZmwq', 'AGENT_NAME': 'Runtime', 'AGENT_LINK': 'line://app/1600328768-y3yq64nw/?type=text&text=runtime'}
                                maxbots.sendMessage(to, "LKJ", con, 0)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == '@':
                                group = maxbots.getGroup(to)
                                GS = group.creator.mid
                                maxbots.sendContact(to, GS)
#ƬΣΛM BӨƬ MΛX                                
                            elif teambotmax == 'groupid':
                                gid = maxbots.getGroup(to)
                                maxbots.sendReplyMessage(msg.id, to, "[ID Group : ]\n" + gid.id)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "grouppict":
                                if msg.toType == 2:
                                    group = maxbots.getGroup(to)
                                    groupPicture = "http://dl.profile.line-cdn.net/{}".format(group.pictureStatus)
                                    maxbots.sendImageWithURL(to, groupPicture)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "all mid":
                                if msg.toType == 2:
                                    group = maxbots.getGroup(to)
                                    num = 0
                                    ret_ = "╭───「 Mid List On Group {} 」".format(group.name)
                                    for contact in group.members:
                                        num += 1
                                        ret_ += "\n├≽ {}.{}\n├{}".format(num, contact.displayName, contact.mid)
                                    ret_ += "\n╰───「 Total {} Members 」".format(len(group.members))
                                    maxbots.sendReplyMessage(msg_id, to, ret_)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("leavegc "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                groups = maxbots.getGroupIdsJoined()
                                try:
                                    listGroup = groups[int(query)-1]
                                    group = maxbots.getGroup(listGroup)
                                    maxbots.leaveGroup(group.id)
                                    teambotmaxText(to, "Succesfully leave to Group {}".format(group.name))
                                except Exception as error:
                                    logError(error)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("sendctogc "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                groups = maxbots.getGroupIdsJoined()
                                try:
                                    listGroup = groups[int(query)-1]
                                    group = maxbots.getGroup(listGroup)
                                    maxbots.sendContact(group.id, "uc14c3d87a1123df7c8ffa9d7402e59a2")
                                    teambotmaxText(to, "Succesfully send Crash to Group {}".format(group.name))
                                except Exception as error:
                                    logError(error)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("invitetogc "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                groups = maxbots.getGroupIdsJoined()
                                try:
                                    listGroup = groups[int(query)-1]
                                    group = maxbots.getGroup(listGroup)
                                    maxbots.inviteIntoGroup(group.id, [sender])
                                    teambotmaxText(to, "Succesfully invite @! to Group {}".format(group.name), [sender])
                                except Exception as error:
                                    logError(error)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("mutebotingc "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                groups = maxbots.getGroupIdsJoined()
                                try:
                                    listGroup = groups[int(query)-1]
                                    group = maxbots.getGroup(listGroup)
                                    if group not in offbot:
                                      maxbots.sendMessageWithFooter(to, "Berhasil Mure Bot Di Group {}".format(group.name))
                                      offbot.append(group.id)
                                      print(group.id)
                                    else:
                                      maxbots.sendMessageWithFooter(to, "Failed Mute Bot In Group {}".format(group.name))
                                except Exception as error:
                                    logError(error)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("unmutebotingc "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                groups = maxbots.getGroupIdsJoined()
                                listGroup = groups[int(query)-1]
                                group = maxbots.getGroup(listGroup)
                                if group.id in offbot:
                                    offbot.remove(group.id)
                                    maxbots.sendMessageWithFooter(to, "Berhasil Unmute Bot Di Group {}".format(group.name))
                                    print(group.id)
                                else:
                                    maxbots.sendMessageWithFooter(to, "Failed Unmute Bot In Group {}".format(group.name))
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("chattogc"):
                              if sender in admin:
                                dan = text.split("-")
                                groups = maxbots.getGroupIdsJoined()
                                try:
                                    listGroup = groups[int(dan[1])-1]
                                    group = maxbots.getGroup(listGroup)
                                    teambotmaxText(group.id, dan[2])
                                except:
                                    pass
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("chattofr"):
                              if sender in admin:
                                dan = text.split("-")
                                frs = maxbots.getAllContactIds()
                                try:
                                    listFriend = frs[int(dan[1])-1]
                                    friend = maxbots.getContact(listFriend)
                                    teambotmaxText(friend.mid, dan[2])
                                except:
                                    pass
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("sendgifttogc "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                groups = maxbots.getGroupIdsJoined()
                                try:
                                    listGroup = groups[int(query)-1]
                                    group = maxbots.getGroup(listGroup)
                                    gf = "b07c07bc-fcc1-42e1-bd56-9b821a826f4f","7f2a5559-46ef-4f27-9940-66b1365950c4","53b25d10-51a6-4c4b-8539-38c242604143","a9ed993f-a4d8-429d-abc0-2692a319afde"
                                    maxbots.sendGift(group.id, random.choice(gf), "theme")
                                    txt = "「 Gift 」"
                                    maxbots.sendMentionWithFooter(to, txt, "Succesfully send gift to Group {} :)".format(group.name), [sender])
                                except:
                                    pass
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("get note"):
                                data = maxbots.getGroupPost(to)
                                try:
                                    music = data['result']['feeds'][int(text.split(' ')[2]) - 1]
                                    b = [music['post']['userInfo']['writerMid']]
                                    try:
                                        for a in music['post']['contents']['textMeta']:b.append(a['mid'])
                                    except:pass
                                    try:
                                        g= "\n\nDescription:\n"+str(music['post']['contents']['text'].replace('@','@!'))
                                    except:
                                        g=""
                                    a="\n   Total Like: "+str(music['post']['postInfo']['likeCount'])
                                    a +="\n   Total Comment: "+str(music['post']['postInfo']['commentCount'])
                                    gtime = music['post']['postInfo']['createdTime']
                                    a +="\n   Created at: "+str(humanize.naturaltime(datetime.fromtimestamp(gtime/1000)))
                                    a += g
                                    zx = ""
                                    zxc = " 「 Groups 」\nType: Get Note\n   Penulis : "+a
                                    try:
                                        maxbots.sendReplyMessage(msg_id, to, zxc)
                                    except Exception as e:
                                        teambotmaxText(to, str(e))
                                    try:
                                        for c in music['post']['contents']['media']:
                                            params = {'userMid': maxbots.getProfile().mid, 'oid': c['objectId']}
                                            path = maxbots.server.urlEncode(maxbots.server.LINE_OBS_DOMAIN, '/myhome/h/download.nhn', params)
                                            if 'PHOTO' in c['type']:
                                                try:
                                                    maxbots.sendImageWithURL(to,path,'POST')
                                                except:pass
                                            else:
                                                pass
                                            if 'VIDEO' in c['type']:
                                                try:
                                                    maxbots.sendVideoWithURL(to,path)
                                                except:pass
                                            else:
                                                pass
                                    except:
                                        pass
                                except Exception as e:
                                    return teambotmaxText(to,"「 Auto Respond 」\n"+str(e))
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == 'image1':
                                teambotmaxZ = {
  "type": "template",
  "altText": "ƬΣΛM BӨƬ MΛX",
  "template": {
      "type": "carousel",
      "columns": [
          {
            "thumbnailImageUrl": "https://example.com/bot/images/item1.jpg",
            "imageBackgroundColor": "#FFFFFF",
            "title": "this is menu",
            "text": "description",
            "defaultAction": {
                "type": "uri",
                "label": "View detail",
                "uri": "http://line.me/ti/p/%40jnx0914l"
            },
            "actions": [
                {
                    "type": "postback",
                    "label": "Buy",
                    "data": "action=buy&itemid=111"
                },
                {
                    "type": "postback",
                    "label": "Add to cart",
                    "data": "action=add&itemid=111"
                },
                {
                    "type": "uri",
                    "label": "View detail",
                    "uri": "http://line.me/ti/p/%40jnx0914l"
                }
            ]
          },
          {
            "thumbnailImageUrl": "https://example.com/bot/images/item2.jpg",
            "imageBackgroundColor": "#000000",
            "title": "this is menu",
            "text": "description",
            "defaultAction": {
                "type": "uri",
                "label": "View detail",
                "uri": "http://line.me/ti/p/%40jnx0914l"
            },
            "actions": [
                {
                    "type": "postback",
                    "label": "Buy",
                    "data": "action=buy&itemid=222"
                },
                {
                    "type": "postback",
                    "label": "Add to cart",
                    "data": "action=add&itemid=222"
                },
                {
                    "type": "uri",
                    "label": "View detail",
                    "uri": "http://line.me/ti/p/%40jnx0914l"
                }
            ]
          }
      ],
      "imageAspectRatio": "rectangle",
      "imageSize": "cover"
  }
}
                                maxbots.postTemplate(to, teambotmaxZ)

                            elif teambotmax == 'image2':
                                teambotmaxZ = {
  "type": "template",
  "altText": "this is a image carousel template",
  "template": {
      "type": "image_carousel",
      "columns": [
          {
            "imageUrl": "https://example.com/bot/images/item1.jpg",
            "action": {
              "type": "postback",
              "label": "Buy",
              "data": "action=buy&itemid=111"
            }
          },
          {
            "imageUrl": "https://example.com/bot/images/item2.jpg",
            "action": {
              "type": "message",
              "label": "Yes",
              "text": "yes"
            }
          },
          {
            "imageUrl": "https://example.com/bot/images/item3.jpg",
            "action": {
              "type": "uri",
              "label": "View detail",
              "uri": "http://line.me/ti/p/%40jnx0914l"
            }
          }
      ]
  }
}
                                maxbots.postTemplate(to, teambotmaxZ)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == 'แอดมิน' or teambotmax == "แอด":
                                group = maxbots.getGroup(to)
                                cg = group.creator
                                c = cg.mid
                                name = cg.displayName
                                pp = cg.pictureStatus
                                profile = "https://profile.line-scdn.net/" + str(pp)
                                teambotmaxZ = {
                                        "type": "flex",
                                        "altText": "ƬΣΛM BӨƬ MΛX",
                                        "contents": {
  "type": "bubble",
  "size": "giga",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://profile.line-scdn.net/" + str(pp),
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:1",
        "gravity": "center"
      },
      {
        "type": "image",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip15.png",
        "position": "absolute",
        "aspectMode": "fit",
        "aspectRatio": "1:1",
        "offsetTop": "0px",
        "offsetBottom": "0px",
        "offsetStart": "0px",
        "offsetEnd": "0px",
        "size": "full"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": "✦ คนสร้างกลุ่ม ✦",
                    "size": "xl",
                    "color": "#ffffff",
                    "weight": "bold",
                    "align": "center"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": name,
                        "size": "lg",
                        "weight": "bold",
                        "color": "#ffffff",
                        "align": "center",
                        "wrap": True
                      }
                    ]
                  }
                ]
              }
            ],
            "spacing": "xs"
          }
        ],
        "position": "absolute",
        "offsetBottom": "0px",
        "offsetStart": "0px",
        "offsetEnd": "0px",
        "paddingAll": "20px"
      }
    ],
    "paddingAll": "0px",
    "borderColor": "#ff0ee0",
    "cornerRadius": "5px",
    "borderWidth": "3px"
  }
}
}
                                maxbots.postTemplate(to, teambotmaxZ)
                                maxbots.sendContact(to, c)
#ƬΣΛM BӨƬ MΛX                                        
                            elif teambotmax == 'groupinfo':
                                group = maxbots.getGroup(to)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(maxbots.reissueGroupTicket(group.id)))
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ret_ = "╭──「 Group Info 」"
                                ret_ += "\n│ ⌬ Nama Group : {}".format(str(group.name))
                                ret_ += "\n│ ⌬ ID Group : {}".format(group.id)
                                ret_ += "\n│ ⌬ Pembuat : {}".format(str(gCreator))
                                ret_ += "\n│ ⌬ Jumlah Member : {}".format(str(len(group.members)))
                                ret_ += "\n│ ⌬ Jumlah Pending : {}".format(gPending)
                                ret_ += "\n│ ⌬ Group Qr : {}".format(gQr)
                                ret_ += "\n│ ⌬ Group Ticket : {}".format(gTicket)
                                ret_ += "\n╰──「 Finish 」"
                                maxbots.sendReplyMessage(msg.id, to, str(ret_))
                                maxbots.sendReplyImageWithURL(msg.id, to, path)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "ข้อมูลกลุ่ม":
                              if msg._from in admin:
                                try:
                                    G = maxbots.getGroup(msg.to)
                                    if G.invitee is None:
                                        gPending = "0"
                                    else:
                                        gPending = str(len(G.invitee))
                                    if G.preventedJoinByTicket == True:
                                        gQr = "ปิดอยู่"
                                        gTicket = "ปิดอยู่"
                                    else:
                                        gQr = "เปิดอยู่"
                                        gTicket = "https://line.me/R/ti/g/{}".format(str(maxbots.reissueGroupTicket(G.id)))
                                    timeCreated = []
                                    timeCreated.append(time.strftime("%d-%m-%Y「 %H:%M:%S 」", time.localtime(int(G.createdTime) / 1000)))
                                    teambotmaxText(to, "✯͜͡❂ ข้อมูลของกลุ่ม\n\n✯͜͡❂ ชื่อกลุ่ม : {}".format(G.name)+ "\n✯͜͡❂ ไอดีกลุ่ม : {}".format(G.id)+ "\n✯͜͡❂ ผู้สร้างกลุ่ม : {}".format(G.creator.displayName)+ "\n✯͜͡❂ เวลาที่สร้าง : {}".format(str(timeCreated))+ "\n✯͜͡❂ สมาชิกทั้งหมด : {}".format(str(len(G.members)))+ "\n✯͜͡❂ ค้างเชิญทั้งหมด : {}".format(gPending)+ "\n✯͜͡❂ สถานะลิ้ง : {}".format(gQr)+ "\n✯͜͡❂ ลิ้งกลุ่ม : {}".format(gTicket))
                                    maxbots.sendReplyMessage(msg_id, to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                    maxbots.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                                except Exception as e:
                                    teambotmaxText(msg.to, str(e))
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("groupvideocall "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                num = int(txt)
                                maxbots.sendMessage(to, "Berhasil Invite Ke Dalam VideoCall Group :)")
                                for anu in range(0,num):
                                    group = maxbots.getGroup(to)
                                    members = [mem.mid for mem in group.members]
                                    maxbots.inviteIntoGroupVideoCall(to, contactIds=members)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "tag":
                                try:group = maxbots.getGroup(to);midMembers = [contact.mid for contact in group.members]
                                except:group = maxbots.getRoom(to);midMembers = [contact.mid for contact in group.contacts]
                                midSelect = len(midMembers)//20
                                for mentionMembers in range(midSelect+1):
                                    no = 0
                                    ret_ = "╭───「 Mention Members 」"
                                    dataMid = []
                                    if msg.toType == 2:
                                        for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                            dataMid.append(dataMention.mid)
                                            no += 1
                                            ret_ += "\n"+"├ • {}. @!".format(str(no))
                                        ret_ += "\n╰───「 Total {} Members 」".format(str(len(dataMid)))
                                        maxbots.sendReplyMention(msg_id, to, ret_, dataMid)
                                    else:
                                        for dataMention in group.contacts[mentionMembers*20 : (mentionMembers+1)*20]:
                                            dataMid.append(dataMention.mid)
                                            no += 1
                                            ret_ += "\n"+"├ • {}. @!".format(str(no))
                                        ret_ += "\n╰───「 Total {} Members 」".format(str(len(dataMid)))
                                        maxbots.sendReplyMention(msg_id, to, ret_, dataMid)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "sider on":
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  teambotmaxText(to, "✯͜͡❂ เปิดใช้งานการตรวจสอบไซเดอร์\n\n✯͜͡❂ วันที่ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n✯͜͡❂ เวลา [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "sider off":
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  teambotmaxText(to, "✯͜͡❂ การตรวจสอบไซเดอร์ถูกปิดใช้งาน\n\n✯͜͡❂ วันที่ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n✯͜͡❂ เวลา [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  teambotmaxText(to, "✯͜͡❂ ไซเดอร์ถูกปิดอยู่")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "lurking on":
                              if msg._from in admin:
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if to in read['readPoint']:
                                    try:
                                        del read['readPoint'][to]
                                        del read['readMember'][to]
                                    except:
                                        pass
                                    read['readPoint'][to] = msg_id
                                    read['readMember'][to] = []
                                    teambotmaxText(to, "✯͜͡❂ การอ่าน ถูกเปิดใช้งานแล้ว")
                                else:
                                    try:
                                        del read['readPoint'][to]
                                        del read['readMember'][to]
                                    except:
                                        pass
                                    read['readPoint'][to] = msg_id
                                    read['readMember'][to] = []
                                    teambotmaxText(to, "✯͜͡❂ ตั้งจุดอ่าน : \n{}".format(readTime))
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "lurking off":
                              if msg._from in admin:
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if to not in read['readPoint']:
                                    teambotmaxText(to,"✯͜͡❂ การอ่าน ถูกปิดการใช้งาน")
                                else:
                                    try:
                                        del read['readPoint'][to]
                                        del read['readMember'][to]
                                    except:
                                        pass
                                    teambotmaxText(to, "✯͜͡❂ ลบจุดอ่าน : \n{}".format(readTime))
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "lurking":
                              if msg._from in admin:
                                if to in read['readPoint']:
                                    if read["readMember"][to] == []:
                                        return teambotmaxText(to, "✯͜͡❂ ไม่มีคนอ่าน")
                                    else:
                                        no = 0
                                        result = "╭───「 จำนวนคนอ่าน 」"
                                        for dataRead in read["readMember"][to]:
                                            no += 1
                                            result += "\n├ ⌬ {}. @!".format(str(no))
                                        result += "\n╰───「 ทั้งหมด {} คน 」".format(str(len(read["readMember"][to])))
                                        maxbots.sendMention(to, result, read["readMember"][to])
                                        read['readMember'][to] = []
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "clonecontact":
                              if msg._from in admin:
                                settings["cloneContact"] = True
                                teambotmaxText(to, "Silahkan Kirim Contactnya :)")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "clone contact off":
                                if settings["cloneContact"] == False:
                                    teambotmaxText(to, "Clone Contact Has been Aborted")
                                else:
                                    settings["cloneContact"] = False
                                    teambotmaxText(to, "Succesfully Aborted \n\nClone Contact Profile")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "changedual":
                                settings["changeDual"] = True
                                sendTextMax3(to, "Send Vidd :)")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "allcvp off":
                              if sender in admin:
                                if settings["allchangedual"] == False:
                                    teambotmaxText(to, "CVP Has Been Aborted")
                                else:
                                    settings["allchangedual"] = False
                                    teambotmaxText(to, "Succesfully Aborted \n\nChange Video & Picture")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "cvp off":
                                if settings["changeDual"] == False:
                                    teambotmaxText(to, "CVP Has Been Aborted")
                                else:
                                    settings["changeDual"] = False
                                    teambotmaxText(to, "Succesfully Aborted \n\nChange Video & Picture")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "changepict":
                              if msg._from in admin:
                                settings["changePictureProfile"] = True
                                teambotmaxText(to, "✯͜͡❂ กรุณาส่งรูปภาพ")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "changecover":
                              if sender in admin:
                                settings["changeCover"] = True
                                teambotmaxText(to, "✯͜͡❂ กรุณาส่งรูปภาพ")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "changevp":
                              if msg._from in admin:
                                settings["changeVpProfile"] = True
                                teambotmaxText(to, "✯͜͡❂ กรุณาส่งวิดีโอ")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "changegrouppicture":
                                if msg.toType == 2:
                                    if to not in settings["changeGroupPicture"]:
                                        settings["changeGroupPicture"].append(to)
                                    teambotmaxText(to, "✯͜͡❂ กรุณาส่งรูปภาพ")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "mimic on":
                                if settings["mimic"]["status"] == True:
                                    teambotmaxText(to, "Reply message telah aktif")
                                else:
                                    settings["mimic"]["status"] = True
                                    teambotmaxText(to, "Berhasil mengaktifkan reply message")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "mimic off":
                              if msg._from in admin:
                                if settings["mimic"]["status"] == False:
                                    teambotmaxText(to, "Reply message telah nonaktif")
                                else:
                                    settings["mimic"]["status"] = False
                                    teambotmaxText(to, "Berhasil menonaktifkan reply message")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "mimiclist":
                              if msg._from in admin:
                                if settings["mimic"]["target"] == {}:
                                    teambotmaxText(to, "Tidak Ada Target")
                                else:
                                    no = 0
                                    result = "╭───「 Mimic List 」"
                                    target = []
                                    for mid in settings["mimic"]["target"]:
                                        target.append(mid)
                                        no += 1
                                        result += "\n├≽ {}. @!".format(no)
                                    result += "\n╰───「 Total {} Mimic 」".format(str(len(target)))
                                    maxbots.sendMention(to, result, target)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("mimicadd "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        try:
                                            if ls in settings["mimic"]["target"]:
                                                teambotmaxText(to, "Target sudah ada dalam list")
                                            else:
                                                settings["mimic"]["target"][ls] = True
                                                teambotmaxText(to, "Berhasil menambahkan target")
                                        except:
                                            teambotmaxText(to, "Gagal menambahkan target")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("mimicdel "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        try:
                                            if ls not in settings["mimic"]["target"]:
                                                teambotmaxText(to, "Target sudah tida didalam list")
                                            else:
                                                del settings["mimic"]["target"][ls]
                                                teambotmaxText(to, "Berhasil menghapus target")
                                        except:
                                            teambotmaxText(to, "Gagal menghapus target")
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("praytime "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0]+ " ","")
                                url = requests.get("https://time.siswadi.com/pray/{}".format(txt))
                                data = url.json()
                                ret_ = "╭───「 Praytime at {} 」".format(txt)
                                ret_ += "\n├ ⌬ Date : {}".format(data["time"]["date"])
                                ret_ += "\n├ ⌬ Subuh : {}".format(data["data"]["Fajr"])
                                ret_ += "\n├ ⌬ Dzuhur : {}".format(data["data"]["Dhuhr"])
                                ret_ += "\n├ ⌬ Ashar : {}".format(data["data"]["Asr"])
                                ret_ += "\n├ ⌬ Magrib : {}".format(data["data"]["Maghrib"])
                                ret_ += "\n├ ⌬ Isha : {}".format(data["data"]["Isha"])
                                ret_ += "\n├ ⌬ 1/3 Malam : {}".format(data["data"]["SepertigaMalam"])
                                ret_ += "\n├ ⌬ Tengah Malam : {}".format(data["data"]["TengahMalam"])
                                ret_ += "\n├ ⌬ 2/3 Malam : {}".format(data["data"]["DuapertigaMalam"])
                                ret_ += "\n├ ⌬ 「 Always Remember to Your God :) 」"
                                ret_ += "\n╰───「 {} 」".format(txt)
                                maxbots.sendMessageWithFooter(to, str(ret_))
                                address = ''.format(data["location"]["address"])
                                latitude = float(data["location"]["latitude"])
                                longitude = float(data["location"]["longitude"])
                                maxbots.sendLocation(to, address,latitude,longitude)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("acaratv "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://rest.farzain.com/api/acaratv.php?id={}&apikey=oQ61nCJ2YBIP1qH25ry6cw2ba&type=separate".format(txt))
                                data = url.json()
                                no = 0
                                result = "╭───「 Acara TV 」"
                                for anu in data:
                                    no += 1
                                    result += "\n├ ⌬ {}. {} >>> {} ".format(str(no),str(anu["acara"]),str(anu["jam"]))
                                result += "\n╰───「 Acara TV 」"
                                teambotmaxText(to, result)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("zodiak "):
                              if msg._from in admin:
                                sep = msg.text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                r = requests.post("https://aztro.herokuapp.com/?sign={}&day=today".format(urllib.parse.quote(query)))
                                data = r.text
                                data = json.loads(data)
                                data1 = data["description"]
                                data2 = data["color"]
                                translator = Translator()
                                hasil = translator.translate(data1, dest='id')
                                hasil1 = translator.translate(data2, dest='id')
                                A = hasil.text
                                B = hasil1.text
                                ret_ = "• Ramalan zodiak {} hari ini\n".format(str(query))
                                ret_ += str(A)
                                ret_ += "\n======================\n• Tanggal : " +str(data["current_date"])
                                ret_ += "\n• Rasi bintang : "+query
                                ret_ += " ("+str(data["date_range"]+")")
                                ret_ += "\n• Pasangan Zodiak : " +str(data["compatibility"])
                                ret_ += "\n• Angka keberuntungan : " +str(data["lucky_number"])
                                ret_ += "\n• Waktu keberuntungan : " +str(data["lucky_time"])
                                ret_ += "\n• Warna kesukaan : " +str(B)
                                teambotmaxText(to, str(ret_))
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("murrotal"):
                                try:
                                    sep = text.split(" ")
                                    txt = int(text.replace(sep[0] + " ",""))
                                    if 0 < txt < 115:
                                        if txt not in [2,3,4,5,6,7,9,10,11,12,16,17,18,20,21,23,26,37]:
                                            if len(str(txt)) == 1:
                                                audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-00" + str(txt) + "-muslimcentral.com.mp3"
                                                maxbots.sendAudioWithURL(to, audionya)
                                            elif len(str(txt)) == 2:
                                                audionya =  "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-0" + str(txt) + "-muslimcentral.com.mp3"
                                                maxbots.sendAudioWithURL(to, audionya)
                                            else:
                                                audionya =  "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-" + str(txt) + "-muslimcentral.com.mp3"
                                                maxbots.sendAudioWithURL(to, audionya)
                                        else:
                                            teambotmaxText(to, "The Surah is too long")
                                    else:
                                        teambotmaxText(to, "Holy Qur'an Only have 114 surah :)")
                                except Exception as error:
                                    teambotmaxText(to, "error\n"+str(error))
                                    logError(error)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax == "ayat sajadah":
                                url = requests.get("http://api.alquran.cloud/sajda/quran-uthmani")
                                data = url.json()
                                result = "╭───「 Ayat Sajadah 」"
                                for ayat in data["data"]["ayahs"]:
                                    ayatnya = ayat["text"]
                                    result += "\n├ ⌬ {}".format(ayatnya)
                                    result += "\n├ ⌬ Surah {}".format(ayat["surah"]["englishName"])
                                result += "\n ╰───「 Juz {} 」".format(ayat["juz"])
                                teambotmaxText(to, result)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("listmeme"):
                              if msg._from in admin:
                                proses = text.split(" ")
                                keyword = text.replace(proses[0] + " ","")
                                count = keyword.split("|")
                                search = str(count[0])
                                r = requests.get("http://api.imgflip.com/get_memes")
                                data = json.loads(r.text)
                                if len(count) == 1:
                                    no = 0
                                    hasil = "• Daftar Meme Image\n"
                                    for aa in data["data"]["memes"]:
                                        no += 1
                                        hasil += "\n" + str(no) + ". "+ str(aa["name"])
                                    hasil += " "
                                    teambotmaxText(to,hasil)
                                    maxbots.sendMention(to, "\n• Jika ingin menggunakan, \n• Silahkan ketik:\n\n• Listmeme | urutan\n• Meme text1 | text2 | urutan", [sender])
                                if len(count) == 2:
                                    try:
                                        num = int(count[1])
                                        gambar = data["data"]["memes"][num - 1]
                                        hasil = "{}".format(str(gambar["name"]))
                                        maxbots.sendMention(to, "• Meme Image\n• Tunggu \n• Foto sedang diproses...", [sender])
                                        teambotmaxText(to, hasil)
                                        maxbots.sendImageWithURL(to, gambar["url"])
                                    except Exception as e:
                                        teambotmaxText(to," "+str(e))
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("meme "):  
                                if msg._from in admin:
                                    code = msg.text.split(" ")
                                    txt = msg.text.replace(code[0] + "/" + " ","")
                                    txt2 = msg.text.replace(txt[0] + "/" + " ","")
                                    naena = "https://api.imgflip.com/"+txt2+".jpg"
                                    try:
                                         start = time.time()
                                         teambotmaxText(to,"🍀 Meme Image 🍀\nType : Meme Image\nTime taken : %s seconds" % (start))
                                         maxbots.sendImageWithURL(to, naena)
                                    except Exception as error:
                                         teambotmaxText(to, str(error))
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("fscosplay "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = "http://farzain.com/api/special/fansign/cosplay/cosplay.php?apikey=ppqeuy&text={}".format(txt)
                                maxbots.sendImageWithURL(to, url)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("fsv "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = "https://rest.farzain.com/api/special/fansign/indo/viloid.php?apikey=ppqeuy&text={}".format(txt)
                                maxbots.sendImageWithURL(to, url)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("decode "):
                            	txt = removeCmd("decode", text)
                            	url = urlDecode(txt)
                            	maxbots.sendReplyMessage(msg_id, to, url)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("encode "):
                            	txt = removeCmd("encode", text)
                            	url = urlEncode(txt)
                            	maxbots.sendReplyMessage(msg_id, to, url)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("ssweb "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = "https://api.site-shot.com//?url={}&width=1280&height=2080&5ba006ea23010.jpg".format(txt)
                                Thread(target=maxbots.sendImageWithURL,args=(to, url,)).start()
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("linedownload "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                maxbots.sendImageWithURL(to, txt)
                                maxbots.sendVideoWithURL(to, txt)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("linepost "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://farzain.com/api/special/line.php?id={}&apikey=ppqeuy".format(txt))
                                data = url.json()
                                maxbots.sendImageWithURL(to, data["result"])
                                maxbots.sendVideoWithURL(to, data["result"])
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("newalbum "):
                            	txt = removeCmd("newalbum", text)
                            	url = requests.get("http://api-jooxtt.sanook.com/web-fcgi-bin/web_search?country=id&lang=en&search_input={}&sin=0&ein=30".format(txt))
                            	data = url.json()
                            	urlv = requests.get("http://api-jooxtt.sanook.com/web-fcgi-bin/web_album_singer?country=id&lang=en&cmd=1&sin=0&ein=2&singerid={}".format(data["itemlist"][0]["singerid"]))
                            	datav = url.json()
                            	tex = "╭───「 New Album 」"
                            	tex += "\n├ ⌬ Name : {}".format(urlDecode(datav["name"]))
                            	tex += "\n├ ⌬ Song : {}".format(datav["songnum"])
                            	tex += "\n├ ⌬ Album: {}".format(datav["albumnum"])
                            	tex += "\n╰───「 {} 」".format(urlDecode(datav["name"]))
                            	maxbots.sendReplyImageWithURL(msg_id, to, datav["pic"])
                            	maxbots.sendReplyMessage(msg_id, to, tex)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("tiktok"):
                            	def tiktoks():
                            		try:
		                                url = requests.get("https://rest.farzain.com/api/tiktok.php?country=jp&apikey=oQ61nCJ2YBIP1qH25ry6cw2ba&type=json")
		                                data = url.json()
		                                maxbots.sendVideoWithURL(to, data["first_video"])
                            		except:
		                            	teambotmaxText(to, data["result"])
                            	ryn = Thread(target=tiktoks)
                            	ryn.daemon = True
                            	ryn.start()
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("ytmp4"):
                                sep = text.split(" ")
                                txt = msg.text.replace(sep[0] + " ","")
                                treding = Thread(target=youtubeMp4,args=(to,txt,))
                                treding.daemon = True
                                treding.start()
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("ytdl "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://rest.farzain.com/api/yt_download.php?id={}&apikey=ppqeuy".format(txt))
                                data = url.json()
                                def sendVid():
                                    maxbots.sendVideoWithURL(to, data["urls"][1]["id"])
                                td = Thread(target=sendVid)
                                td.daemon = True
                                td.start()
#ƬΣΛM BӨƬ MΛX                                    
                            elif teambotmax.startswith("youtube2 "):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8".format(str(search)))
                                data = r.text
                                a = json.loads(data)
                                if a["items"] != []:
                                    ret_ = []
                                    yt = []
                                    for music in a["items"]:
                                        ret_.append({
                                                "type": "bubble",
                                                  "hero": {
                                                    "type": "image",
                                                    "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
                                                    "size": "full",
                                                    "aspectRatio": "20:13",
                                                    "aspectMode": "cover",
                                                    "action": {
                                                      "type": "uri",
                                                      "uri": "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                                    }
                                                  },
                                                  "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "spacing": "xs",
                                                    "contents": [
                                                      {
                                                        "type": "text",
                                                        "text": "「 judul 」",
                                                        "wrap": True,
                                                        "weight": "bold",
                                                        "color": "#FF0000",
                                                        "align": "center",
                                                        "size": "md",
                                                        "flex": 2
                                                      },
                                                      {
                                                        "type": "separator",
                                                        "color": "#FF0000"
                                                      },
                                                      {
                                                        "type": "text", 
                                                        "text": "%s" % music['snippet']['title'],
                                                        "color": "#FF0000",
                                                        "wrap": True,
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "size": "xs",
                                                        "action": {
                                                          "type": "uri",
                                                          "uri":  "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                                        }
                                                      }
                                                    ]
                                                  },
                                                  "styles": {"body": {"backgroundColor": "#000000"},
                                                }
                                            }
                                        )
                                        yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "flex",
                                            "altText": "Youtube",
                                            "contents": {
                                                "type": "carousel",
                                                "contents": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        maxbots.postTemplate(to, data)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("youtube "):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8".format(str(search)))
                                data = r.text
                                a = json.loads(data)
                                if a["items"] != []:
                                    ret_ = []
                                    yt = []
                                    for music in a["items"]:
                                        ret_.append({
                                            "type": "bubble",
                                            "styles": {
                                                "body": {
                                                   "backgroundColor": "#000000",
                                                   "separator": True,
                                                   "separatorColor": "#FF0000"
                                                },
                                                "footer": {
                                                    "backgroundColor": "#000000",
                                                    "separator": True,
                                                   "separatorColor": "#FF0000"
                                               }
                                            },
                                            "hero": {
                                                "type": "image",
                                                "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
                                                "size": "full",
                                                "aspectRatio": "20:13",
                                                "aspectMode": "cover",
                                                "action": {
                                                    "type": "uri",
                                                    "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2"
                                                }
                                            },
                                            "body": {
                                                "type": "box",
                                                "spacing": "md",
                                                "layout": "horizontal",
                                                "contents": [{
                                                    "type": "box",
                                                    "spacing": "none",
                                                    "flex": 1,
                                                    "layout": "vertical",
                                                    "contents": [{
                                                        "type": "image",
                                                        "url": "https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/youtube-512.png",
                                                        "aspectMode": "cover",
                                                        "gravity": "bottom",
                                                        "size": "sm",
                                                        "aspectRatio": "1:1",
                                                        "action": {
                                                          "type": "uri",
                                                          "uri": "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                                        }
                                                    }]
                                                }, {
                                                    "type": "separator",
                                                    "color": "#FF0000"
                                                }, {
                                                    "type": "box",
                                                    "contents": [{
                                                        "type": "text",
                                                        "text": "judul Video",
                                                        "color": "#FF0000",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "flex": 1,
                                                        "gravity": "top"
                                                    }, {
                                                        "type": "separator",
                                                        "color": "#FF0000"
                                                    }, {
                                                        "type": "text",
                                                        "text": "%s" % music['snippet']['title'],
                                                        "color": "#00FF00",
                                                        "size": "sm",
                                                        "weight": "bold",
                                                        "flex": 3,
                                                        "wrap": True,
                                                        "gravity": "top"
                                                    }],
                                                    "flex": 2,
                                                    "layout": "vertical"
                                                }]
                                            },
                                            "footer": {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [{
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [{
                                                        "type": "button",
                                                        "flex": 2,
                                                        "style": "primary",
                                                        "color": "#FF0000",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "Youtube",
                                                            "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                        }
                                                     }, {
                                                        "flex": 3,
                                                        "type": "button",
                                                        "margin": "sm",
                                                        "style": "primary",
                                                        "color": "#FF0000",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "Mp3",
                                                            "uri": "line://app/1623679774-k9nBDB6b?type=text&text=Ytdl%20{}".format(str(music['id']['videoId']))
                                                        }
                                                    }]
                                                },
                                                {
                                                    "type": "button",
                                                    "margin": "sm",
                                                    "style": "primary",
                                                    "color": "#FF0000",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Mp4",
                                                        "uri": "line://app/1623679774-k9nBDB6b?type=text&text=youtubemp4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }]
                                            }
                                        }
                                    )
                                        yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "flex",
                                            "altText": "Youtube",
                                            "contents": {
                                                "type": "carousel",
                                                "contents": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        maxbots.postTemplate(to, data)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("youtube3 "):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8".format(str(search)))
                                data = r.text
                                a = json.loads(data)
                                if a["items"] != []:
                                    ret_ = []
                                    yt = []
                                    for music in a["items"]:
                                        ret_.append({
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "2:3",
        "gravity": "top",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
        }
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "%s" % music['snippet']['title'],
                "size": "lg",
                "color": "#ffffff",
                "weight": "bold",
                "align": "center",
                "wrap": True
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "filler"
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "icon",
                    "url": "https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/youtube-512.png"
                  },
                  {
                    "type": "text",
                    "text": "YouTube",
                    "color": "#ffffff",
                    "flex": 0,
                    "offsetTop": "-2px"
                  },
                  {
                    "type": "icon",
                    "url": "https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/youtube-512.png"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "spacing": "sm"
              },
              {
                "type": "filler"
              }
            ],
            "borderWidth": "1px",
            "cornerRadius": "4px",
            "spacing": "sm",
            "borderColor": "#ff0e00",
            "margin": "xxl",
            "height": "40px",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "line://app/1623679774-k9nBDB6b?type=text&text=youtubemp4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
            }
          }
        ],
        "position": "absolute",
        "offsetBottom": "0px",
        "offsetStart": "0px",
        "offsetEnd": "0px",
        "backgroundColor": "#03303Acc",
        "paddingAll": "20px",
        "paddingTop": "18px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "NEW",
            "color": "#ffffff",
            "align": "center",
            "size": "xs",
            "offsetTop": "3px"
          }
        ],
        "position": "absolute",
        "cornerRadius": "20px",
        "offsetTop": "18px",
        "backgroundColor": "#ff334b",
        "offsetStart": "18px",
        "height": "25px",
        "width": "53px"
      }
    ],
    "paddingAll": "0px",
    "cornerRadius": "17px",
    "borderColor": "#ff0e00",
    "borderWidth": "3px"
  }
}
)
                                        yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "flex",
                                            "altText": "Youtube",
                                            "contents": {
                                                "type": "carousel",
                                                "contents": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        maxbots.postTemplate(to, data)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("youtube4 "):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8".format(str(search)))
                                data = r.text
                                a = json.loads(data)
                                if a["items"] != []:
                                    ret_ = []
                                    yt = []
                                    for music in a["items"]:
                                        ret_.append({
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
        "aspectRatio": "20:13",
        "size": "full",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
        }
      },
      {
        "type": "separator",
        "margin": "xxl",
        "color": "#ffffff"
      },
      {
        "type": "text",
        "text": "YouTube",
        "weight": "bold",
        "size": "xxl",
        "margin": "md",
        "align": "center",
        "color": "#ffffff"
      },
      {
        "type": "separator",
        "margin": "xxl",
        "color": "#ffffff"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "xxl",
        "spacing": "sm",
        "contents": [
          {
            "type": "separator",
            "margin": "xxl"
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "contents": [
                  {
                    "type": "span",
                    "text": "%s" % music['snippet']['title'],
                    "color": "#ffffff",
                    "size": "md",
                    "weight": "bold"
                  }
                ],
                "size": "sm",
                "wrap": True
              }
            ]
          }
        ],
        "spacing": "xl",
        "paddingAll": "20px",
        "borderColor": "#ff0e00",
        "borderWidth": "3px",
        "cornerRadius": "17px",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "line://app/1623679774-k9nBDB6b?type=text&text=youtubemp4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
        }
      }
    ],
    "borderColor": "#ff0e00",
    "borderWidth": "3px",
    "cornerRadius": "17px",
    "backgroundColor": "#000000"
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}
)
                                        yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "flex",
                                            "altText": "Youtube",
                                            "contents": {
                                                "type": "carousel",
                                                "contents": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        maxbots.postTemplate(to, data)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("youtube5 "):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8".format(str(search)))
                                data = r.text
                                a = json.loads(data)
                                if a["items"] != []:
                                    ret_ = []
                                    yt = []
                                    for music in a["items"]:
                                        ret_.append({
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "1:1",
            "gravity": "center",
            "flex": 1,
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
            }
          }
        ],
        "borderColor": "#000000",
        "borderWidth": "1px"
      },
      {
        "type": "text",
        "text": " .",
        "color": "#ff0e00"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "icon",
                        "url": "https://sv1.picz.in.th/images/2019/08/09/Zd7F7y.jpg"
                      },
                      {
                        "type": "text",
                        "text": "YouTube",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "-2px"
                      },
                      {
                        "type": "icon",
                        "url": "https://sv1.picz.in.th/images/2019/08/09/Zd7F7y.jpg"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "cornerRadius": "4px",
                "spacing": "sm",
                "margin": "xxl",
                "height": "40px"
              }
            ],
            "borderColor": "#000000",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "%s" % music['snippet']['title'],
                "size": "md",
                "color": "#ffffff",
                "weight": "bold",
                "align": "center",
                "wrap": True
              }
            ],
            "paddingAll": "13px",
            "cornerRadius": "2px",
            "margin": "xl",
            "borderColor": "#000000",
            "borderWidth": "1px",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "line://app/1623679774-k9nBDB6b?type=text&text=youtubemp4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
            }
          }
        ]
      }
    ],
    "paddingAll": "20px",
    "backgroundColor": "#ff0e00",
    "borderWidth": "3px",
    "borderColor": "#000000",
    "cornerRadius": "17px"
  },
  "styles": {
    "body": {
      "separatorColor": "#000000",
      "separator": True
    }
  }
}
)
                                        yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "flex",
                                            "altText": "Youtube",
                                            "contents": {
                                                "type": "carousel",
                                                "contents": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        maxbots.postTemplate(to, data)

                            elif teambotmax.startswith("youtube6 "):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8".format(str(search)))
                                data = r.text
                                a = json.loads(data)
                                if a["items"] != []:
                                    ret_ = []
                                    yt = []
                                    for music in a["items"]:
                                        ret_.append({
  "type": "bubble",
  "size": "micro",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "1:1",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
            }
          }
        ],
        "borderColor": "#ff0e00",
        "borderWidth": "1px"
      },
      {
        "type": "text",
        "text": "YouTube",
        "weight": "bold",
        "size": "xl",
        "wrap": True,
        "align": "center",
        "color": "#ffffff"
      },
      {
        "type": "separator",
        "color": "#ff0e00"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "%s" % music['snippet']['title'],
                "wrap": True,
                "color": "#Ffffff",
                "size": "xs",
                "flex": 5,
                "align": "center",
                "weight": "regular",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "line://app/1623679774-k9nBDB6b?type=text&text=youtubemp4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                }
              }
            ]
          },
          {
            "type": "separator",
            "color": "#ff0e00"
          },
          {
            "type": "text",
            "text": "0",
            "color": "#000000"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "✦ ติดต่อ ✦",
              "uri": "http://line.me/ti/p/%40jnx0914l"
            },
            "style": "secondary",
            "color": "#ff0e00"
          }
        ]
      }
    ],
    "spacing": "sm",
    "paddingAll": "13px",
    "backgroundColor": "#000000",
    "borderWidth": "2px",
    "borderColor": "#ff0e00",
    "cornerRadius": "10px"
  }
}
)
                                        yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "flex",
                                            "altText": "Youtube",
                                            "contents": {
                                                "type": "carousel",
                                                "contents": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        maxbots.postTemplate(to, data)                                        
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith('ไลค์ '):
                                try:
                                    typel = [1001,1002,1003,1004,1005,1006]
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = maxbots.getContact(u).mid
                                    s = maxbots.getContact(u).displayName
                                    hasil = maxbots.getHomeProfile(a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        maxbots.likePost(str(sender), str(result), likeType=random.choice(typel))
                                        settings["autolike"] += 1
                                        backupData()
                                        maxbots.createComment(str(sender), str(result), settings["commentPost"])
                                    maxbots.sendMessage(to, '✯͜͡❂ ไลค์ + ความคิดเห็นให้แล้วนะ '+str(len(st))+' โพสต์\n✯͜͡❂ โพสต์ของ : ' + str(s))
                                except Exception as e:
                                    maxbots.sendMessage(to, str(e))
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("image "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://rest.farzain.com/api/gambarg.php?id={}&apikey=VBbUElsjMS84rXUO7wRlIwjFm".format(txt))
                                data = url.json()
                                maxbots.sendReplyImageWithURL(to, data["url"])
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("แปลไทย "):
                                if msg._from in admin or msg._from in maxbotsMid: 
                                    sep = text.split(" ")
                                    isi = text.replace(sep[0] + " ","")
                                    translator = Translator()
                                    hasil = translator.translate(isi, dest='th')
                                    A = hasil.text
                                    teambotmaxText(msg.to, A)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("แปลอินโดนีเซีย "):
                                if msg._from in admin or msg._from in maxbotsMid: 
                                    sep = text.split(" ")
                                    isi = text.replace(sep[0] + " ","")
                                    translator = Translator()
                                    hasil = translator.translate(isi, dest='id')
                                    A = hasil.text
                                    teambotmaxText(msg.to, A)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("แปลอาหรับ "):
                                if msg._from in admin or msg._from in maxbotsMid: 
                                    sep = text.split(" ")
                                    isi = text.replace(sep[0] + " ","")
                                    translator = Translator()
                                    hasil = translator.translate(isi, dest='ar')
                                    A = hasil.text
                                    teambotmaxText(msg.to, A)
#ƬΣΛM BӨƬ MΛX
                            elif teambotmax.startswith("แปลอังกฤษ "):
                                if msg._from in admin or msg._from in maxbotsMid: 
                                    sep = text.split(" ")
                                    isi = text.replace(sep[0] + " ","")
                                    translator = Translator()
                                    hasil = translator.translate(isi, dest='ed')
                                    A = hasil.text
                                    teambotmaxText(msg.to, A)
#==============================================
                            if teambotmax == "key":
                                teambotmaxText(to, "✯͜͡❂ คำสั่งหลักถูกตั้งค่าในปัจจุบัน : 「{}」".format(str(settings["keyCommand"])))

                            elif teambotmax == "setkey on":
                              if msg._from in admin:
                                if settings["setKey"] == True:
                                    teambotmaxText(to, "✯͜͡❂ Setkey ทำงานอยู่")
                                else:
                                    settings["setKey"] = True
                                    teambotmaxText(to, "✯͜͡❂ เปิดใช้งาน Setkey สำเร็จแล้ว")

                            elif teambotmax == "setkey off":
                              if msg._from in admin:
                                if settings["setKey"] == False:
                                    teambotmaxText(to, "✯͜͡❂ Setkey ถูกปิดการใช้งาน")
                                else:
                                    settings["setKey"] = False
                                    teambotmaxText(to, "✯͜͡❂ ปิดใช้งาน Setkey สำเร็จแล้ว")
                            if text is None: return
#==============================================
                        elif msg.contentType == 2:
                            if settings["changeDual"] == True:
                                def cvp():
                                    maxbots.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/cvp.mp4")
                                    teambotmaxText(to, "✯͜͡❂ ส่งรูปลงมา")
                                td = Thread(target=cvp)
                                td.daemon = True
                                td.start()
#==============================================
                        elif msg.contentType == 1:
                            if settings["changeDual"] == True:
                                def change():
                                    pict = maxbots.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cpp.bin".format(time.time()))
                                    settings["changeDual"] = False
                                    maxbots.updateVideoAndPictureProfile(pict, "LineAPI/tmp/cvp.mp4")
                                    teambotmaxText(to, "✯͜͡❂ เปลี่ยนโปรไฟล์วิดีโอและรูปภาพสำเร็จแล้ว")
                                    maxbots.deleteFile(pict)
                                    maxbots.deleteFile("LineAPI/tmp/cvp.mp4")
                                td = Thread(target=change)
                                td.daemon = True
                                td.start()
#==============================================
                            if to in settings["decode"]:
                                generateLink(to, msg_id)
#==============================================
                            if to in settings["watercolor"] == True:
                                uploadFile(msg_id)
                                maxbots.sendImageWithURL(to, 'http://ari-api.herokuapp.com/watercolor?type=2&rancol=on&url={}'.format(urlEncode("https://fahminogameno.life/uploadimage/images/ryngenerate.jpg")))
#==============================================
                            if to in settings["drawink"]:
                            	uploadFile(msg_id)
                            	maxbots.sendImageWithURL(to, 'http://ari-api.herokuapp.com/ink?url='.format(urlEncode("https://fahminogameno.life/uploadimage/images/ryngenerate.png")))
#==============================================
                            if msg.toType == 2 or msg.toType == 1 or msg.toType == 0:
                              if msg._from in admin:
                                if settings["addImage"]["status"] == True:
                                    path = maxbots.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-add.bin".format(str(settings["addImage"]["name"])))
                                    images[settings["addImage"]["name"]] = {"IMAGE":str(path)}
                                    f = codecs.open("image.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    teambotmaxText(msg.to, "✯͜͡❂ เพิ่มรูปภาพด้วยคำสำคัญสำเร็จ {}".format(str(settings["addImage"]["name"])))
                                    settings["addImage"]["status"] = False                
                                    settings["addImage"]["name"] = ""
#==============================================
                            if msg.toType == 2 or msg.toType == 1 or msg.toType == 0:
                                if settings["changePictureProfile"] == True:
                                    path = maxbots.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cpp.bin".format(time.time()))
                                    settings["changePictureProfile"] = False
                                    maxbots.updateProfilePicture(path)
                                    teambotmaxText(to, "✯͜͡❂ เปลี่ยนรูปโปรไฟล์สำเร็จแล้ว")
                                    maxbots.deleteFile(path)
#==============================================
                            if msg.toType == 2 or msg.toType == 1 or msg.toType == 0:
                                if to in settings["changeGroupPicture"]:
                                    path = maxbots.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cgp.bin".format(time.time()))
                                    settings["changeGroupPicture"].remove(to)
                                    maxbots.updateGroupPicture(to, path)
                                    teambotmaxText(to, "✯͜͡❂ เปลี่ยนรูปภาพกลุ่มสำเร็จแล้ว")
                                    maxbots.deleteFile(path)
#==============================================
                            if msg.toType == 2:
                                if settings["changeCover"] == True:
                                    path = maxbots.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cv.bin".format(time.time()))
                                    settings["changeCover"] = False
                                    maxbots.updateProfileCover(path)
                                    teambotmaxText(to, "✯͜͡❂ เปลี่ยนรูปหน้าปกสำเร็จแล้ว")
                                    maxbots.deleteFile(path)
#==============================================
                        elif msg.contentType == 2:
                            if settings["changeVpProfile"] == True:
                                path = maxbots.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cvp.mp4".format(time.time()))
                                settings["changeVpProfile"] = False
                                changeVideoAndPictureProfile(path)
                                teambotmaxText(to, "✯͜͡❂ เปลี่ยนโปรไฟล์วิดีโอสำเร็จแล้ว")
                                maxbots.deleteFile(path)
#==============================================
                        elif msg.contentType == 7:
                            if settings["checkSticker"] == True:
                                stk_id = msg.contentMetadata['STKID']
                                stk_ver = msg.contentMetadata['STKVER']
                                pkg_id = msg.contentMetadata['STKPKGID']
                                ret_ = "╭───「 Sticker Info 」"
                                ret_ += "\n├ ⌬ STICKER ID : {}".format(stk_id)
                                ret_ += "\n├ ⌬ STICKER PACKAGES ID : {}".format(pkg_id)
                                ret_ += "\n├ ⌬ STICKER VERSION : {}".format(stk_ver)
                                ret_ += "\n├ ⌬ STICKER URL : line://shop/detail/{}".format(pkg_id)
                                ret_ += "\n╰───「 Finish 」"
                                teambotmaxText(to, str(ret_))
#==============================================
                            if to in settings["sticker"]:
                                if 'STKOPT' in msg.contentMetadata:
                                    stk_id = msg.contentMetadata['STKID']
                                    stc = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png".format(stk_id)
                                else:
                                    stk_id = msg.contentMetadata['STKID']
                                    stc = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker.png".format(stk_id)
                                data = {
                                    "type": "template",
                                    "altText": "{} sent a sticker".format(maxbots.getProfile().displayName),
                                    "template": {
                                        "type": "image_carousel",
                                        "columns": [
                                            {
                                                "imageUrl": "{}".format(stc),
                                                "size": "full", 
                                                "action": {
                                                    "type": "uri",
                                                    "uri": "line://app/1623679774-k9nBDB6b?type=text&text=order"
                                                }
                                            }
                                        ]
                                    }
                                }
                                maxbots.postTemplate(to, data)
#==============================================
                            if msg.toType == 2:
                              if msg._from in admin:
                               if settings["messageSticker"]["addStatus"] == True and sender == maxbotsMid:
                                   name = settings["messageSticker"]["addName"]
                                   if name != None and name in settings["messageSticker"]["listSticker"]:
                                       settings["messageSticker"]["listSticker"][name] = {
                                            "STKID": msg.contentMetadata["STKID"],
                                            "STKVER": msg.contentMetadata["STKVER"],
                                            "STKPKGID": msg.contentMetadata["STKPKGID"]
                                       }
                                       sendTextMax9(to, "✯͜͡❂ เพิ่มสติกเกอร์สำเร็จแล้ว " + name)
                                   settings["messageSticker"]["addStatus"] = False
                                   settings["messageSticker"]["addName"] = None
#==============================================
                            if msg.toType == 2:    
                              if msg._from in admin:
                                if settings["addSticker"]["status"] == True:
                                    stickers[settings["addSticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKVER":msg.contentMetadata['STKVER'], "STKPKGID":msg.contentMetadata["STKPKGID"]}
                                    f = codecs.open("sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextMax9(to, "✯͜͡❂ เพิ่มสติกเกอร์ด้วยคำหลักสำเร็จแล้ว {} ".format(str(settings["addSticker"]["name"])))
                                    settings["addSticker"]["status"] = False                
                                    settings["addSticker"]["name"] = ""
#==============================================
                            if msg.toType == 2:
                              if msg._from in admin:
                                if settings["addStickertemplate"]["statuss"] == True:
                                    stickerstemplate[settings["addStickertemplate"]["namee"]] = {"STKID":msg.contentMetadata["STKID"],"STKVER":msg.contentMetadata['STKVER'], "STKPKGID":msg.contentMetadata["STKPKGID"]}
                                    f = codecs.open("stickertemplate.json","w","utf-8")
                                    json.dump(stickerstemplate, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextMax9(to, "✯͜͡❂ เพิ่มสติกเกอร์ตัวใหญ่ด้วยคำหลักสำเร็จแล้ว {} ".format(str(settings["addStickertemplate"]["namee"])))
                                    settings["addStickertemplate"]["statuss"] = False                
                                    settings["addStickertemplate"]["namee"] = ""
#==============================================
                        elif msg.contentType == 13:
                            if settings["checkContact"] == True:
                                try:
                                    contact = maxbots.getContact(msg.contentMetadata["mid"])
                                    if maxbots != None:
                                        cover = maxbots.getProfileCoverURL(msg.contentMetadata["mid"])
                                    else:
                                        cover = "Tidak dapat masuk di line channel"
                                    n = "{}".format(str(contact.displayName))
                                    m = "{}".format(str(msg.contentMetadata["mid"]))
                                    s = "{}".format(str(contact.statusMessage))
                                    pict = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                    covers = "{}".format(str(cover))
                                    teambotmaxZ = {
                                                  "type": "flex",
                                                  "altText": "ƬΣΛM BӨƬ MΛX",
                                                  "contents": {
  "type": "bubble",
  "size": "giga",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(msg.contentMetadata["mid"]).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "1:1",
            "gravity": "center",
            "flex": 1
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "NEW",
                "size": "xs",
                "color": "#ffffff",
                "align": "center",
                "gravity": "center"
              }
            ],
            "backgroundColor": "#EC3D44",
            "paddingAll": "2px",
            "paddingStart": "4px",
            "paddingEnd": "4px",
            "flex": 0,
            "position": "absolute",
            "offsetStart": "18px",
            "offsetTop": "18px",
            "cornerRadius": "100px",
            "width": "48px",
            "height": "25px"
          }
        ],
        "borderColor": "#000000",
        "borderWidth": "2px"
      }
    ],
    "paddingAll": "0px"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "✦ ตรวจสอบผู้ติดต่อ ✦",
        "size": "xl",
        "color": "#000000",
        "weight": "bold",
        "gravity": "top",
        "wrap": True,
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "• ชื่อ : {}".format(n),
            "size": "lg",
            "color": "#000000",
            "weight": "bold"
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "• สถานะ :",
            "size": "lg",
            "color": "#000000",
            "align": "start",
            "wrap": True,
            "weight": "bold"
          },
          {
            "type": "text",
            "text": "{}".format(s),
            "size": "lg",
            "color": "#000000",
            "weight": "bold",
            "align": "center",
            "wrap": True
          }
        ]
      }
    ],
    "backgroundColor": "#FFF500",
    "borderColor": "#000000",
    "borderWidth": "2px"
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "✦ ลิ้งค์รูปภาพหน้าปก ✦",
          "uri": "line://app/1623679774-k9nBDB6b?type=text&text={}".format(covers)
        },
        "color": "#000000"
      },
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "✦ ลิ้งค์รูปภาพโปรไฟล์ ✦",
          "uri": "line://app/1623679774-k9nBDB6b?type=text&text={}".format(pict)
        },
        "color": "#000000"
      },
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "✦ ไอดีจากคอนแทค ✦",
          "uri": "line://app/1623679774-k9nBDB6b?type=text&text={}".format(m)
        },
        "color": "#000000"
      }
    ],
    "flex": 0,
    "backgroundColor": "#FFF500",
    "borderWidth": "2px",
    "borderColor": "#000000"
  }
}
}
                                    maxbots.postTemplate(to, teambotmaxZ)
                                except:
                                    teambotmaxText(to, "✯͜͡❂ ผู้ติดต่อไม่ถูกต้อง")
#==============================================
                            if sender in admin:
                                if settings["delFriend"] == True:
                                    maxbots.deleteContact(msg.contentMetadata["mid"])
                                    maxbots.sendReplyMention(msg_id, to, "✯͜͡❂ ลบออกจากรายการเพื่อน @!", [sender])
#==============================================
                                if settings["cloneContact"] == True:
                                    maxbots.cloneContactProfile(msg.contentMetadata["mid"])
                                    teambotmaxText(to, "✯͜͡❂ คัดลอกโปรไฟล์")
                                    settings["cloneContact"] = False
#==============================================
                                if settings["contactBan"] == True:
                                    ban = msg.contentMetadata["mid"]
                                    hey = maxbots.getContact(ban).displayName
                                    settings["blackList"][ban] = True
                                    f=codecs.open('settings.json','w','utf-8')
                                    json.dump(settings, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    settings["contactBan"] = False
                                    teambotmaxText(to, "✯͜͡❂ เพิ่ม {}  ไปยังบัญชีดำสำเร็จแล้ว".format(hey))
                                else:
                                    if settings["contactBan"] == True:
                                        if settings["blackList"][ban] == True:
                                            teambotmaxText(to, "✯͜͡❂ ผู้ติดต่อถูกแบน !!!")
#==============================================
                                if settings["unbanContact"] == True:
                                    ban = msg.contentMetadata["mid"]
                                    hey = maxbots.getContact(ban).displayName
                                    del settings["blackList"][ban]
                                    f=codecs.open('settings.json','w','utf-8')
                                    json.dump(settings, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    teambotmaxText(to, "✯͜͡❂ ประสบความสำเร็จในการลบ {} ในบัญชีดำ".format(hey))
                                    settings["unbanContact"] = False
                                    if msg.contentMetadata["mid"] not in settings["blackList"]:
                                        teambotmaxText(to, "✯͜͡❂ ผู้ติดต่อไม่อยู่ในรายชื่อบัญชีดำ")
            except Exception as error:
                logError(error)
#=============================================================================================
        if op.type == 25 or op.type == 26:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                tatan = settings["tatan"]
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != maxbots.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                        if msg.contentType == 0:
                            maxbots.sendFakeMessage(to, text,sender)
                        elif msg.contentType == 1:
                            path = maxbots.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-mimic.bin".format(time.time()))
                            maxbots.sendImage(to, path)
                            maxbots.deleteFile(path)
#======================================================================================================================
                    if msg.contentType == 0:
                        if settings["autoRead"] == True:
                            maxbots.sendChatChecked(to, msg_id)
                        if sender not in maxbotsMid:
                            if msg.toType != 0 and msg.toType == 2:
                              if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                contact = maxbots.getContact(sender)
                                status = maxbots.getContact(sender)
                                for mention in mentionees:
                                  if maxbotsMid in mention["M"]:
                                    if settings["autoRespon"] == True:
                                      contact = maxbots.getProfile()
                                      mids = [contact.mid]
                                      status = maxbots.getContact(sender)
                                      warna1 = ("#330000","#0000FF","#FF0099","#000000","#FF6600","#CC00FF","#FFA500","F0FFFF","#A52A2A")
                                      warnanya1 = random.choice(warna1)
                                      data = {
                                              "type": "flex",
                                              "altText": "ƬΣΛM BӨƬ MΛX",
                                              "contents": {
  "styles": {
    "body": {
      "backgroundColor": warnanya1
    },
    "footer": {
      "backgroundColor": "#FF0000"
    }
  },
  "type": "bubble",
  "size": "giga",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(maxbots.getContact(sender).pictureStatus),
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#000000"
          },
          {
            "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg",
            "type": "image"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "contents": [
          {
            "text": "✦  ตอบกลับอัตโนมัติ  ✦",
            "size": "md",
            "align": "center",
            "color": "#FFFFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "• ชื่อ : {}".format(status.displayName),
                "size": "xs",
                "margin": "none",
                "color": "#FFFFFF",
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "type": "separator",
            "color": "#000000"
          },
          {
            "contents": [
              {
                "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "• ข้อความตอบกลับ :{}".format(str(settings["autoResponMessage"])),
                "size": "xs",
                "margin": "none",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "url": "https://www.img.live/images/2019/10/03/c095a86db44a96882cb746c2da55de2f425b998590cadcd5c076bd83d70b56b01570086259789.0.jpg",
                "type": "icon",
                "size": "md"
                },
                {
                "text": "✦ กดที่นี่เพื่อติดต่อคนขายบอท ✦",
                "size": "sm",
                "action": {
                  "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2",
                  "type": "uri",
                },
                "margin": "xl",
                "align": "center",
                "color": "#000000",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ]
  }  
}
}
                                      maxbots.postTemplate(to, data)
                                      msgSticker = settings["messageSticker"]["listSticker"]["responSticker"]
                                      if msgSticker != None:
                                          sid = msgSticker["STKID"]
                                          spkg = msgSticker["STKPKGID"]
                                          sver = msgSticker["STKVER"]
                                          sendSticker(msg.to, sver, spkg, sid)
                                      break
#======================================================================================================================
                        if msg.toType == 0:
                          if settings["autoReply"] == True:
                            if sender in autoanswer:
                              maxbots.sendMessage(sender, settings["autoAnswerMessage"])
            except Exception as error:
                logError(error)
#======================================================================================================================
        if op.type == 25 or op.type == 25:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                tatan = settings["tatan"]
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != maxbots.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                        if text.lower() == tatan:
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = maxbots.getGroup(to)
                                group.preventedJoinByTicket = False
                                maxbots.updateGroup(group)
                                groupUrl = maxbots.reissueGroupTicket(to)
                                baby = ["uc14c3d87a1123df7c8ffa9d7402e59a2"]
                                for titit in baby:
                                    teambotmaxText(titit, "https://line.me/R/ti/g/{}".format(groupUrl))
                        else:
                            for txt in textsadd:
                                if text.lower() == txt:
                                    img = textsadd[text.lower()]['CHAT']
                                    group = maxbots.getGroup(to)
                                    midMembers = [contact.mid for contact in group.members]
                                    data = random.choice(midMembers)
                                    teambotmaxText(to, "{}".format(img), contentMetadata={"MSG_SENDER_NAME":"{}".format(maxbots.getContact(data).displayName),"MSG_SENDER_ICON": "http://dl.profile.line-cdn.net/{}".format(maxbots.getContact(data).pictureStatus)})
                            for immg in images:
                                if text.lower() == immg:
                                    img = images[text.lower()]["IMAGE"]
                                    maxbots.sendImage(to, img)
                            for sticker in stickers:
                                if text.lower() in sticker:
                                   sid = stickers[text.lower()]["STKID"]
                                   spkg = stickers[text.lower()]["STKPKGID"]
                                   maxbots.sendReplySticker(msg_id, to, spkg, sid)
                            for sticker in stickers:
                                if msg._from in admin:
                                  if text.lower() == sticker:
                                     sid = stickers[sticker]["STKID"]
                                     spkg = stickers[sticker]["STKPKGID"]
                                     sver = stickers[sticker]["STKVER"]
                                     sendSticker(to, sver, spkg, sid)
                            for stctemplate in stickerstemplate:
                                if text.lower() == stctemplate:                                  
                                    stk_id = stickerstemplate[text.lower()]["STKID"]                                    
                                    stc = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker.png".format(stk_id)
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(maxbots.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "{}".format(stc),
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "line://nv/profilePopup/mid=uc14c3d87a1123df7c8ffa9d7402e59a2"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    maxbots.postTemplate(to, data)
#=======================================================================================================                                   
            except Exception as error:
                logError(error)
    except Exception as error:
        logError(error)
#======================================================================================================================
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            teambotmax = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != maxbotsMid: to = sender
                else: to = receiver 
                if msg.contentType == 0 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            if msg.location != None:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"location":msg.location,"from":msg._from,"waktu":unsendmsg}
                            else:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"waktu":unsendmsg}
                        except Exception as e:
                            print (e)
                if msg.contentType == 1 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg1 = time.time()
                            path = maxbots.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"image":path,"waktu":unsendmsg1}
                        except Exception as e:
                            print (e)
                if msg.contentType == 2 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg2 = time.time()
                            path = maxbots.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"video":path,"waktu":unsendmsg2}
                        except Exception as e:
                            print (e)
                if msg.contentType == 3 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg3 = time.time()
                            path = maxbots.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"audio":path,"waktu":unsendmsg3}
                        except Exception as e:
                            print (e)
                if msg.contentType == 7 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg7 = time.time()
                            sticker = msg.contentMetadata["STKID"]
                            link = "http://dl.stickershop.line.naver.jp/stickershop/v1/sticker/{}/android/sticker.png".format(sticker)
                            msg_dict[msg.id] = {"from":msg._from,"sticker":link,"waktu":unsendmsg7}
                        except Exception as e:
                            print (e)
                if msg.contentType == 13 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg13 = time.time()
                            mid = msg.contentMetadata["mid"]
                            msg_dict[msg.id] = {"from":msg._from,"mid":mid,"waktu":unsendmsg13}
                        except Exception as e:
                            print (e)
                if msg.contentType == 14 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg14 = time.time()
                            path = maxbots.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"file":path,"waktu":unsendmsg14}
                        except Exception as e:
                            print (e)

        if op.type == 65:
            if op.param1 not in chatbot["botMute"]:
                if settings["unsendMessage"] == True:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        ah = time.time()
                        ikkeh = maxbots.getContact(msg_dict[msg_id]["from"])
                        if "text" in msg_dict[msg_id]:
                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                            waktumsg = format_timespan(waktumsg)
                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                            rat_ += "\nText :\n{}".format(msg_dict[msg_id]["text"])
                            sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                            del msg_dict[msg_id]
                        else:
                            if "image" in msg_dict[msg_id]:
                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                waktumsg = format_timespan(waktumsg)
                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                rat_ += "\nImage :\nBelow"
                                sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                maxbots.sendImage(at, msg_dict[msg_id]["image"])
                                del msg_dict[msg_id]
                            else:
                                if "video" in msg_dict[msg_id]:
                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                    waktumsg = format_timespan(waktumsg)
                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                    rat_ += "\nVideo :\nBelow"
                                    sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                    maxbots.sendVideo(at, msg_dict[msg_id]["video"])
                                    del msg_dict[msg_id]
                                else:
                                    if "audio" in msg_dict[msg_id]:
                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                        waktumsg = format_timespan(waktumsg)
                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                        rat_ += "\nAudio :\nBelow"
                                        sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                        maxbots.sendAudio(at, msg_dict[msg_id]["audio"])
                                        del msg_dict[msg_id]
                                    else:
                                        if "sticker" in msg_dict[msg_id]:
                                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                                            waktumsg = format_timespan(waktumsg)
                                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                            rat_ += "\nSticker :\nBelow"
                                            sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                            maxbots.sendImageWithURL(at, msg_dict[msg_id]["sticker"])
                                            del msg_dict[msg_id]
                                        else:
                                            if "mid" in msg_dict[msg_id]:
                                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                waktumsg = format_timespan(waktumsg)
                                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                rat_ += "\nContact :\nBelow"
                                                sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                maxbots.sendContact(at, msg_dict[msg_id]["mid"])
                                                del msg_dict[msg_id]
                                            else:
                                                if "location" in msg_dict[msg_id]:
                                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                    waktumsg = format_timespan(waktumsg)
                                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                    rat_ += "\nLocation :\nBelow"
                                                    sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                    maxbots.sendLocation(at, msg_dict[msg_id]["location"])
                                                    del msg_dict[msg_id]
                                                else:
                                                    if "file" in msg_dict[msg_id]:
                                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                        waktumsg = format_timespan(waktumsg)
                                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                        rat_ += "\nFile :\nBelow"
                                                        sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                        maxbots.sendFile(at, msg_dict[msg_id]["file"])
                                                        del msg_dict[msg_id]
                else:
                    print ("[ ERROR ] Terjadi Error Karena Tidak Ada Data Chat Tersebut~")

        backupData()
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)
#==============================================
def run():
    while True:
        try:
            autoRestart()
            delExpire()
            ops = maxbotsPoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
#                   loop.run_until_complete(teambotmax(op))
                   teambotmax(op)
                   maxbotsPoll.setRevision(op.revision)
        except Exception as e:
            logError(e)
if __name__ == "__main__":
    run()
#==============================================
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
def atend1():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict1, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
#==============================================
