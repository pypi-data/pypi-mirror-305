import websocket
from NcatBot.start import download_file_1, download_file_2
from box import Box
import json
from . import log
import os
from .start import download_file
import yaml
import time

LocalPath = os.path.dirname(os.path.abspath(__file__)).replace(os.sep, '//')

with open("config.yaml", 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)
    qqaccount=config['QQaccount']

def check_napcat_files():
    # 检查NapCatFiles 是否存在，不存在则下载
    if not os.path.exists(f"{LocalPath}//NapCatFiles"):
        log.warning("NapCatFiles not found, downloading...", "NcatBot:ws")
        download_file()
        download_file_1()
        download_file_2()
        log.info("NapCatFiles download success,retry later", "NcatBot:ws")
        exit()
    elif os.path.exists(f"{LocalPath}//NapCatFiles"):
        try:
            if os.path.exists(LocalPath+ f"//NapCatFiles//config//onebot11_{qqaccount}.json"):
                # 启动launcher
                os.system(f"cd {LocalPath}//NapCatFiles// && start launcher.bat {qqaccount}")
                log.info("QQ用户存在，自动登入","NcatBot:ws")
            elif not os.path.exists(LocalPath+ f"//NapCatFiles//config//onebot11_{qqaccount}.json"):
                log.warning("QQ用户不存在，无法自动登入，请先扫码登入后重启Napcat","NcatBot:ws")
                os.system(f"cd {LocalPath}//NapCatFiles// && start launcher.bat")
                time.sleep(3)
                # 打开NapCatFiles//cache//qrcode.png并且以图片方式打开它
                os.system(f"start {LocalPath}//NapCatFiles//cache//qrcode.png")
                exit()
        except Exception as e:
            log.error(f"出错：{e}","NcatBot:ws")
            exit()

class QQBot:
    def __init__(self, http_port, ws_port, hotload=True):
        self.url = f"ws://localhost:{ws_port}"
        self.http_port = http_port
        self.ws_port = ws_port
        self.ws = websocket.WebSocketApp(self.url,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.msg_handlers = {}
        self.hotload = hotload


    def run(self, reportSelfMessage=False,musicSignUrl=""):
        if self.hotload:
            check_napcat_files()
        elif self.hotload==False:
            log.info("已关闭热重载，确保客户端启动！","NcatBot:ws")
        with open(LocalPath+f"//NapCatFiles//config//onebot11_{qqaccount}.json",'r', encoding='utf-8') as f:
            json_content=json.load(f)
        json_content.update({
            'http': {'enable': True, 'port': self.http_port},
            'ws': {'enable': True, 'port': self.ws_port},
            'reportSelfMessage': reportSelfMessage,
            'musicSignUrl': musicSignUrl
        })
        with open(LocalPath+f"//NapCatFiles//config//onebot11_{qqaccount}.json",'w', encoding='utf-8') as f:
            json.dump(json_content,f,ensure_ascii=False,indent=4)
        self.ws.run_forever(reconnect=True)

    def on_message(self, ws, message):
        msg = json.loads(message)
        msg = Box(msg)
        msg_type = msg.post_type
        if msg_type in self.msg_handlers:
            for handler in self.msg_handlers[msg_type]:
                handler(msg)

    def on_error(self, ws, error):
        pass

    def on_close(self, ws, close_status_code, close_msg):
        log.warning(f"Websocket closed", "warning")

    def msg_register(self, msg_type):
        def decorator(func):
            if msg_type not in self.msg_handlers:
                self.msg_handlers[msg_type] = []
            self.msg_handlers[msg_type].append(func)
            return func
        return decorator

