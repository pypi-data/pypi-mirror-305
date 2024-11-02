import requests
import zipfile
# 引入进度条库
from tqdm import tqdm
import os
from . import log

LocalPath = os.path.dirname(os.path.abspath(__file__)).replace(os.sep, '//')

def download_file(url="https://github.com/NapNeko/NapCatQQ/releases/download/v3.4.5/NapCat.Shell.zip"):
    log.info("Downloading NcatBot...","NcatBot:start")
    proxies = {
        "http": "http://127.0.0.1:7890",
        "https": "http://127.0.0.1:7890",
    }
    try:
      response = requests.get(url, stream=True, timeout=30, proxies=proxies)  # 设置超时时间为30秒
      total_size = int(response.headers.get('content-length', 0))  # 获取总大小
      if response.status_code == 200:
          file_path = os.path.join(LocalPath, "NapCat.Shell.zip")
          buffer = bytearray()
          with open(file_path, "wb") as f:
              with tqdm(total=total_size, unit='B', unit_scale=True, desc="NapCat.Shell.zip") as bar:
                  for data in response.iter_content(chunk_size=1024):  # 每次下载1024字节
                      buffer.extend(data)
                      if len(buffer) >= 8192:  # 当缓冲区达到8KB时写入文件
                          f.write(buffer)
                          bar.update(len(buffer))
                          buffer.clear()
                  if buffer:  # 写入剩余的数据
                      f.write(buffer)
                      bar.update(len(buffer))
          log.info("文件下载成功！","NcatBot:start")
          # 解压文件
          extract_path = os.path.join(LocalPath, "NapCatFiles")
          with zipfile.ZipFile(file_path, 'r') as zip_ref:
              zip_ref.extractall(extract_path)
          log.info("文件解压成功！", "NcatBot:start")
          os.remove(file_path)
      else:
          log.error(f"下载失败，状态码: {response.status_code}")
          exit()
    except requests.exceptions.Timeout:
      log.error("下载失败，请求超时")
      exit()
    except requests.exceptions.ConnectionError:
      log.error("下载失败，连接错误")
      exit()
    except requests.exceptions.HTTPError:
      log.error("下载失败，HTTP错误")
      exit()
    except requests.exceptions.RequestException as e:
      log.error(f"下载失败，请求异常: {e}")
      exit()
    except zipfile.BadZipFile:
      log.error("解压失败，文件损坏")
      exit()
    except Exception as e:
      log.error(f"未知错误: {e}")
      exit()

def download_file_1(url="https://github.com/NapNeko/NapCatQQ/releases/download/v3.4.5/napcat.packet.exe"):
    log.info("Downloading NcatBot...","NcatBot:start")
    proxies = {
        "http": "http://127.0.0.1:7890",
        "https": "http://127.0.0.1:7890",
    }
    try:
      response = requests.get(url, stream=True, timeout=30, proxies=proxies)  # 设置超时时间为30秒
      total_size = int(response.headers.get('content-length', 0))  # 获取总大小
      if response.status_code == 200:
          file_path = LocalPath + "//NapCatFiles//napcat.packet.exe"
          # 保存，无需使用进度条
          with open(file_path, "wb") as f:
              f.write(response.content)

      else:
          log.error(f"下载失败，状态码: {response.status_code}")
    except requests.exceptions.Timeout:
        log.error("下载失败，请求超时")
        exit()
def download_file_2(url="https://github.com/NapNeko/NapCatQQ/releases/download/v3.4.5/napcat.packet.production.py"):
    log.info("Downloading NcatBot...","NcatBot:start")
    proxies = {
        "http": "http://127.0.0.1:7890",
        "https": "http://127.0.0.1:7890",
    }
    try:
      response = requests.get(url, stream=True, timeout=30, proxies=proxies)  # 设置超时时间为30秒
      total_size = int(response.headers.get('content-length', 0))  # 获取总大小
      if response.status_code == 200:
          file_path = LocalPath + "//NapCatFiles//napcat.packet.production.py"
          # 保存，无需使用进度条
          with open(file_path, "wb") as f:
              f.write(response.content)
      else:
          log.error(f"下载失败，状态码: {response.status_code}")
    except requests.exceptions.Timeout:
        log.error("下载失败，请求超时")
        exit()