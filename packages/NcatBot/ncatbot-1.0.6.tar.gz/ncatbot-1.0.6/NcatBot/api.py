import requests
import os

class GroupHttper:
    def __init__(self, url):
        self.url = url

    def send_group_msg(self, group_id, text):
        # 构造发送消息的json数据
        data = {
            "group_id": group_id,
            "message": [{"type": "text", "data": {"text": text}}]
        }
        requests.post(self.url+"/send_group_msg", json=data)

    def send_group_msg_reply(self, group_id, message_id, text):
        # 构造回复消息的json数据
        data = {
            "group_id": group_id,
            "message_id": message_id,
            "message": [{"type": "reply", "data": {"id": message_id}}, {"type": "text", "data": {"text": f" {text}"}}]
        }
        requests.post(self.url+"/send_group_msg", json=data)

    def send_group_msg_at(self, group_id, user_id, text):
        # 构造艾特消息的json数据
        data = {
            "group_id": group_id,
            "message": [{"type": "at", "data": {"qq": user_id}}, {"type": "text", "data": {"text": f" {text}"}}]
        }
        requests.post(self.url+"/send_group_msg", json=data)

    def send_group_msg_img(self, group_id, image):
        new_file = os.path.abspath(os.path.join(os.getcwd(), image)).replace('\\', '\\\\')
        data={
            "group_id": group_id,
            "message": [{"data": {"file": "file:///" + new_file}, "type": "image"}],
        }
        requests.post(self.url+"/send_group_msg", json=data)

    def send_group_msg_file(self, group_id, file):
        new_file = os.path.abspath(os.path.join(os.getcwd(), file)).replace('\\', '\\\\')
        data={
            "group_id": group_id,
            "message": [{"data": {"file": "file:///" + new_file}, "type": "file"}],
        }
        requests.post(self.url+"/send_group_msg", json=data)

    def send_group_msg_video(self, group_id, video):
        new_file = os.path.abspath(os.path.join(os.getcwd(), video)).replace('\\', '\\\\')
        data={
            "group_id": group_id,
            "message": [{"data": {"file": "file:///" + new_file}, "type": "video"}],
        }
        requests.post(self.url+"/send_group_msg", json=data)

    def send_group_msg_record(self, group_id, record):
        new_file = os.path.abspath(os.path.join(os.getcwd(), record)).replace('\\', '\\\\')
        data={
            "group_id": group_id,
            "message": [{"data": {"file": "file:///" + new_file}, "type": "record"}],
        }
        requests.post(self.url+"/send_group_msg", json=data)

    def send_group_msg_face(self, group_id, face_id):
        data={
            "group_id": group_id,
            "message": [{"data": {"id": face_id}, "type": "face"}],
        }
        requests.post(self.url+"/send_group_msg", json=data)

    def send_group_msg_dice(self, group_id, dice_type):
        data={
            "group_id": group_id,
            "message": [{"data": {"result": dice_type}, "type": "dice"}],
        }
        requests.post(self.url+"/send_group_msg", json=data)

    def send_group_msg_rps(self, group_id, rps_type):
        data={
            "group_id": group_id,
            "message": [{"data": {"result": rps_type}, "type": "rps"}],
        }
        requests.post(self.url+"/send_group_msg", json=data)

    def send_group_msg_qqmusic(self, group_id,music_id):
        data={
            "group_id": group_id,
            "message": [{"data": {"type": "qq", "id": music_id}, "type": "music"}],
        }
        requests.post(self.url+"/send_group_msg", json=data)

    def send_group_msg_music(self, group_id,music_id):
        data={
            "group_id": group_id,
            "message": [{"data": {"type": "163", "id": music_id}, "type": "music"}],
        }
        requests.post(self.url+"/send_group_msg", json=data)

    def send_group_msg_custommusic(self,group_id,music_url,music_audio,music_title,music_image):
        data={
            "group_id": group_id,
            "message": [
                {"data": {"type": "custom", "url": music_url, "audio": music_audio, "title": music_title, "image": music_image}, "type": "music"}
            ]
        }
        requests.post(self.url+"/send_group_msg", json=data)

class PrivateHttper:
    def __init__(self, url):
        self.url = url

    def send_private_msg(self, user_id, text):
        # 构造发送私聊消息的json数据
        data = {
            "user_id": user_id,
            "message": [{"type": "text", "data": {"text": text}}]
        }
        requests.post(self.url+"/send_private_msg", json=data)

    def send_private_msg_reply(self, user_id, message_id, text):
        # 构造回复私聊消息的json数据
        data = {
            "user_id": user_id,
            "message_id": message_id,
            "message": [{"type": "reply", "data": {"id": message_id}}, {"type": "text", "data": {"text": f" {text}"}}]
        }
        requests.post(self.url+"/send_private_msg", json=data)

    def send_private_msg_img(self, user_id, image):
        new_file = os.path.abspath(os.path.join(os.getcwd(), image)).replace('\\', '\\\\')
        data={
            "user_id": user_id,
            "message": [{"data": {"file": "file:///" + new_file}, "type": "image"}],
        }
        requests.post(self.url+"/send_private_msg", json=data)

    def send_private_msg_file(self, user_id, file):
        new_file = os.path.abspath(os.path.join(os.getcwd(), file)).replace('\\', '\\\\')
        data={
            "user_id": user_id,
            "message": [{"data": {"file": "file:///" + new_file}, "type": "file"}],
        }
        requests.post(self.url+"/send_private_msg", json=data)

    def send_private_msg_video(self, user_id, video):
        new_file = os.path.abspath(os.path.join(os.getcwd(), video)).replace('\\', '\\\\')
        data={
            "user_id": user_id,
            "message": [{"data": {"file": "file:///" + new_file}, "type": "video"}],
        }
        requests.post(self.url+"/send_private_msg", json=data)

    def send_private_msg_record(self, user_id, record):
        new_file = os.path.abspath(os.path.join(os.getcwd(), record)).replace('\\', '\\\\')
        data={
            "user_id": user_id,
            "message": [{"data": {"file": "file:///" + new_file}, "type": "record"}],
        }
        requests.post(self.url+"/send_private_msg", json=data)

    def send_private_msg_face(self, user_id, face_id):
        data={
            "user_id": user_id,
            "message": [{"data": {"id": face_id}, "type": "face"}],
        }
        requests.post(self.url+"/send_private_msg", json=data)

    def send_private_msg_dice(self, user_id, dice_type):
        data={
            "user_id": user_id,
            "message": [{"data": {"result": dice_type}, "type": "dice"}],
        }
        requests.post(self.url+"/send_private_msg", json=data)

    def send_private_msg_rps(self, user_id, rps_type):
        data={
            "user_id": user_id,
            "message": [{"data": {"result": rps_type}, "type": "rps"}],
        }
        requests.post(self.url+"/send_private_msg", json=data)

    def send_private_msg_qqmusic(self, user_id,music_id):
        data={
            "user_id": user_id,
            "message": [{"data": {"type": "qq", "id": music_id}, "type": "music"}],
        }
        requests.post(self.url+"/send_private_msg", json=data)

    def send_private_msg_music(self, user_id,music_id):
        data={
            "user_id": user_id,
            "message": [{"data": {"type": "163", "id": music_id}, "type": "music"}],
        }
        requests.post(self.url+"/send_private_msg", json=data)

    def send_private_msg_custommusic(self,user_id,music_url,music_audio,music_title,music_image):
        data={
            "user_id": user_id,
            "message": [
                {"data": {"type": "custom", "url": music_url, "audio": music_audio, "title": music_title, "image": music_image}, "type": "music"}
            ]
        }
        requests.post(self.url+"/send_private_msg", json=data)

class OtherHttper:
    def __init__(self, url):
        self.url = url

    def delete_msg(self, message_id):
        # 构造撤回消息的json数据
        data = {
            "message_id": message_id
        }
        requests.post(self.url+"/delete_msg", json=data)

    def get_friend_msg_history(self, user_id):
        # 构造获取好友消息历史的json数据
        data = {
            "user_id": user_id
        }
        return requests.post(self.url+"/get_friend_msg_history", json=data).json()
    
    def get_group_msg_history(self, group_id, message_seq, count):
        # 构造获取群消息历史的json数据
        data = {
            "group_id": group_id,
            "message_seq": message_seq,
            "count": count
        }
        return requests.post(self.url+"/get_group_msg_history", json=data).json()
    
    def get_login_info(self):
        # 构造获取登录信息的json数据
        return requests.get(self.url+"/get_login_info").json()
    
    def get_status(self):
        # 构造获取状态的json数据
        return requests.post(self.url+"/get_status").json()
    
    def clean_cache(self):
        # 构造清理缓存的json数据
        return requests.get(self.url+"/clean_cache").json()
    
    def set_online_status(self, status,ext_status,battery_status):
        # 构造设置在线状态的json数据
        data = {
            "status": status,
            "ext_status": ext_status,
            "battery_status": battery_status
        }
        return requests.post(self.url+"/set_online_status", json=data).json()
    
    def ocr_image(self, image):
        # 构造OCR图片的json数据
        new_file = os.path.abspath(os.path.join(os.getcwd(), image)).replace('\\', '\\\\')
        data={
            "image": "file:///" + new_file
        }
        return requests.post(self.url+"/ocr_image", json=data).json()
    
    def send_like(self, user_id, times):
        # 构造发送好友赞的json数据
        data = {
            "user_id": user_id,
            "times": times
        }
        return requests.post(self.url+"/send_like", json=data).json()
    
    def get_friend_list(self, no_cache=False):
        # 构造获取好友列表的json数据
        data = {
            "no_cache": no_cache
        }
        return requests.post(self.url+"/get_friend_list", json=data).json()
    
    def set_friend_add_request(self, flag, approve=True, remark=""):
        # 构造处理加好友请求的json数据
        data = {
            "flag": flag,
            "approve": approve,
            "remark": remark
        }
        return requests.post(self.url+"/set_friend_add_request", json=data).json()
    
    def set_qq_avatar(self, file):
        # 构造设置QQ头像的json数据
        new_file = os.path.abspath(os.path.join(os.getcwd(), file)).replace('\\', '\\\\')
        data={
            "file": "file:///" + new_file
        }
        requests.post(self.url+"/set_qq_avatar", json=data).json()

    def get_stranger_info(self, user_id):
        # 构造获取陌生人信息的json数据
        data = {
            "user_id": user_id
        }
        return requests.post(self.url+"/get_stranger_info", json=data).json()
    
    def get_friends_with_category(self):
        # 构造获取好友分组的json数据
        return requests.get(self.url+"/get_friends_with_category").json()
    
    def friend_poke(self, user_id):
        # 构造好友戳一戳的json数据
        data = {
            "user_id": user_id
        }
        return requests.post(self.url+"/friend_poke", json=data).json()
    
    def delete_friend(self, user_id):
        # 构造删除好友的json数据
        data = {
            "user_id": user_id
        }
        return requests.post(self.url+"/delete_friend", json=data).json()
    
    def get_profile_like(self):
        # 构造获取好友点赞列表的json数据
        return requests.get(self.url+"/get_profile_like").json()
    
    def get_group_list(self, no_cache=False):
        # 构造获取群列表的json数据
        data = {
            "no_cache": no_cache
        }
        return requests.post(self.url+"/get_group_list", json=data).json()
    
    def get_group_info(self, group_id):
        # 构造获取群信息的json数据
        data = {
            "group_id": group_id
        }
        return requests.post(self.url+"/get_group_info", json=data).json()
    
    def get_group_member_list(self, group_id, no_cache=False):
        # 构造获取群成员列表的json数据
        data = {
            "group_id": group_id,
            "no_cache": no_cache
        }
        return requests.post(self.url+"/get_group_member_list", json=data).json()
    
    def get_group_member_info(self, group_id, user_id):
        # 构造获取群成员信息的json数据
        data = {
            "group_id": group_id,
            "user_id": user_id
        }
        return requests.post(self.url+"/get_group_member_info", json=data).json()
    
    def group_poke(self, group_id, user_id):
        # 构造群戳一戳的json数据
        data = {
            "group_id": group_id,
            "user_id": user_id
        }
        return requests.post(self.url+"/group_poke", json=data).json()
    
    def set_group_add_request(self, flag, approve=True, reason=""):
        # 构造处理加群请求的json数据
        data = {
            "flag": flag,
            "approve": approve,
            "reason": reason
        }
        return requests.post(self.url+"/set_group_add_request", json=data).json()
    
    def set_group_leave(self, group_id):
        # 构造退出群聊的json数据
        data = {
            "group_id": group_id
        }
        return requests.post(self.url+"/set_group_leave", json=data).json()
    
    def set_group_admin(self, group_id, user_id, enable=True):
        # 构造设置群管理员的json数据
        data = {
            "group_id": group_id,
            "user_id": user_id,
            "enable": enable
        }
        return requests.post(self.url+"/set_group_admin", json=data).json()
    
    def set_group_card(self, group_id, user_id, card):
        # 构造设置群名片的json数据
        data = {
            "group_id": group_id,
            "user_id": user_id,
            "card": card
        }
        return requests.post(self.url+"/set_group_card", json=data).json()
    
    def set_group_ban(self, group_id, user_id, duration=60):
        # 构造群组禁言的json数据
        data = {
            "group_id": group_id,
            "user_id": user_id,
            "duration": duration
        }
        return requests.post(self.url+"/set_group_ban", json=data).json()
    
    def set_group_whole_ban(self, group_id, enable=True):
        # 构造全员禁言的json数据
        data = {
            "group_id": group_id,
            "enable": enable
        }
        return requests.post(self.url+"/set_group_whole_ban", json=data).json()
    
    def set_group_name(self, group_id, group_name):
        # 构造设置群名称的json数据
        data = {
            "group_id": group_id,
            "group_name": group_name
        }
        return requests.post(self.url+"/set_group_name", json=data).json()
    
    def set_group_kick(self, group_id, user_id, reject_add_request=False):
        # 构造群组踢人的json数据
        data = {
            "group_id": group_id,
            "user_id": user_id,
            "reject_add_request": reject_add_request
        }
        return requests.post(self.url+"/set_group_kick", json=data).json()
    
    def set_group_special_title(self, group_id, user_id, special_title):
        # 构造设置群头衔的json数据
        data = {
            "group_id": group_id,
            "user_id": user_id,
            "special_title": special_title
        }
        return requests.post(self.url+"/set_group_special_title", json=data).json()
    
    def get_group_honor_info(self, group_id):
        # 构造获取群荣誉信息的json数据
        data = {
            "group_id": group_id
        }
        return requests.post(self.url+"/get_group_honor_info", json=data).json()
    
    def get_essence_msg_list(self, group_id):
        # 构造获取精华消息列表的json数据
        data = {
            "group_id": group_id
        }
        return requests.post(self.url+"/get_essence_msg_list", json=data).json()
    
    def set_essence_msg(self, message_id):
        # 构造设置精华消息的json数据
        data = {
            "message_id": message_id
        }
        return requests.post(self.url+"/set_essence_msg", json=data).json()
    
    def delete_essence_msg(self, message_id):
        # 构造删除精华消息的json数据
        data = {
            "message_id": message_id
        }
        return requests.post(self.url+"/delete_essence_msg", json=data).json()
    
    def get_group_root_files(self, group_id):
        # 构造获取群根目录文件列表的json数据
        data = {
            "group_id": group_id
        }
        return requests.post(self.url+"/get_group_root_files", json=data).json()
    
    def upload_group_file(self, group_id, file, name):
        # 构造上传群文件到根目录的json数据
        new_file = os.path.abspath(os.path.join(os.getcwd(), file)).replace('\\', '\\\\')
        data={
            "group_id": group_id,
            "file": "file:///" + new_file,
            "name": name
        }
        return requests.post(self.url+"/upload_group_file", json=data).json()
    
    def delete_group_file(self, group_id, file_id):
        # 构造删除群文件的json数据
        data = {
            "group_id": group_id,
            "file_id": file_id
        }
        return requests.post(self.url+"/delete_group_file", json=data).json()
    
    def create_group_file_folder(self, group_id, folder_name):
        # 构造创建群文件夹的json数据
        data = {
            "group_id": group_id,
            "name": folder_name
        }
        return requests.post(self.url+"/create_group_file_folder", json=data).json()
    
    def delete_group_folder(self, group_id, folder_id):
        # 构造删除群文件夹的json数据
        data = {
            "group_id": group_id,
            "folder_id": folder_id
        }
        return requests.post(self.url+"/delete_group_folder", json=data).json()
    
    def get_group_file_url(self, file_id):
        # 构造获取群文件下载链接的json数据
        data = {
            "file_id": file_id
        }
        return requests.post(self.url+"/get_group_file_url", json=data).json()
    
    def get_group_at_all_remain(self, group_id):
        # 构造获取群@全体成员剩余次数的json数据
        data = {
            "group_id": group_id
        }
        return requests.post(self.url+"/get_group_at_all_remain", json=data).json()
    
    def send_group_notice(self, group_id, content, image=None):
        # 构造发送群公告的json数据
        data = {
            "group_id": group_id,
            "content": content
        }
        if image:
            new_file = os.path.abspath(os.path.join(os.getcwd(), image)).replace('\\', '\\\\')
            data["image"] = "file:///" + new_file
        return requests.post(self.url+"/send_group_notice", json=data).json()
    
    def get_group_notice(self, group_id):
        # 构造获取群公告的json数据
        data = {
            "group_id": group_id
        }
        return requests.post(self.url+"/get_group_notice", json=data).json()
    
    def get_group_system_msg(self, group_id):
        # 构造获取群系统消息的json数据
        data = {
            "group_id": group_id
        }
        return requests.get(self.url+"/get_group_system_msg", json=data).json()
    
    def get_group_ignore_add_request(self, group_id):
        # 构造获取群消息屏蔽的json数据
        data = {
            "group_id": group_id
        }
        return requests.post(self.url+"/get_group_ignore_add_request", json=data).json()
