import os
from os import path
import subprocess
import sys
import importlib

"""首次启动检测必需包和文件"""
def install_and_import(packages):
    for package in packages:
        try:
            # 尝试导入包
            importlib.import_module(package)
        except ImportError:
            # 如果包不存在，使用pip安装
            print(f"'{package}' 未安装，正在安装...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"'{package}' 安装成功")

# import requests
# import zipfile
# import shutil
# import platform

# def download_chrome_testing():
#     # cwd = os.get_cwd()
#     cwd = path.abspath(path.dirname(__file__))
#     chrome_dir = cwd + '/chrome-testing'

#     if not os.path.isdir(chrome_dir):
#         print('正在准备配置一个ChatGPT自动化专用的浏览器，请稍等。。。')
#         print()

#         print('判断系统版本，找到合适的chrome')
#         os_type = platform.system()
#         if os_type == "Windows":
#                 tag = 'win64'
#                 print("当前系统是 Windows")
#         elif os_type == "Linux":
#                 tag = 'linux64'
#                 print("当前系统是 Linux")
#         elif os_type == "Darwin":
#                 info = subprocess.run(["sysctl", "-n", "machdep.cpu.brand_string"], 
#                                 capture_output=True, text=True)
#                 if "Apple" in info.stdout:
#                     tag = 'mac-arm64'
#                     print("当前系统是 macOS (Apple Silicon ARM64)")
#                 else:
#                     tag = 'mac-x64'
#                     print("当前系统是 macOS (Intel 64-bit)")

        
#         response = requests.get('https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json')
#         url = [version['url']
#                 for version in response.json()['versions'][0]['downloads']['chrome']
#                     if version['platform'] == tag][0]

#         print('下载中...')
#         # 下载zip文件
#         zip_filename = cwd + '/chrome-testing.zip'
#         response = requests.get(url)

#         # 将zip文件保存到本地
#         with open(zip_filename, 'wb') as file:
#             file.write(response.content)
#         print('下载完成')

#         print('解压中...')
#         # 解压缩文件
#         with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
#             zip_ref.extractall("temp_chrome_dir")

#         # 获取解压缩后的原文件夹名称
#         extracted_folder_name = os.listdir("temp_chrome_dir")[0]

#         # 将原文件夹重命名为 'B'
#         shutil.move(os.path.join("temp_chrome_dir", extracted_folder_name), chrome_dir)

#         # 清理临时文件
#         os.remove(zip_filename)
#         shutil.rmtree("temp_chrome_dir")
#         print('解压完成')
#         print('')

#         print('Chrome浏览器将自动启动，点击不登录后会进入ChatGPT主页，请在这里登录你的ChatGPT账号，然后关闭浏览器')

#         chat_bot = ChatGPTAutomation()

def run_uvicorn():
    install_and_import(['fastapi', 'deepl', 'selenium', 'nltk', 'pyperclip', 'uvicorn', 'webdriver_manager']) # 检查包依赖
    # download_chrome_testing() # 下载一个供Selenium使用的Chrome

    print('检查是不是已经登录ChatGPT...')
    try:
        from chatgpt_on_selenium import ChatGPTAutomation
    except:
        try:
            from .chatgpt_on_selenium import ChatGPTAutomation
        except:
            from AutoTrans.chatgpt_on_selenium import ChatGPTAutomation

    chat_bot = ChatGPTAutomation()
    chat_bot.quit()
    print('已登录。')

    import socket
    port = 3006
    for t in range(3006, 4006):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('localhost', t)) != 0:
                port = t
                break
    else:
        raise RuntimeError("没有可用的端口，请重启系统。")


    import webbrowser
    webbrowser.open(f'http://127.0.0.1:{port}/')

    # 获取当前脚本所在的目录，也就是包的路径
    package_path = os.path.dirname(os.path.abspath(__file__))

    # 改变工作目录到包路径
    os.chdir(package_path)
    
    # 构建命令并运行
    import platform
    os_type = platform.system()
    if os_type == "Windows":
        command = f'start uvicorn __init__:app --port {port} --reload'
    elif os_type == "Linux":
        command = f'uvicorn __init__:app --port {port} --reload'
    elif os_type == "Darwin":
        command = f'uvicorn __init__:app --port {port} --reload'

    # 注意：为了支持 Windows 的 start 命令，这里需要使用 shell=True
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    run_uvicorn()