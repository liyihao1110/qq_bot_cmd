from colorama import init, Fore
import subprocess
import sys, os, yaml, json

# 初始化colorama
init(autoreset=True)


def refresh_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_menu():
    print(Fore.CYAN + "--------------------------------")
    print(Fore.MAGENTA + "QQ 频道机器人控制台🤖")
    print(Fore.GREEN + "             ——made by 不吃李子😄")
    print(Fore.YELLOW + "1. 开启机器人")
    print(Fore.CYAN + "2. 退出程序")
    print(Fore.RED + "3. 获取本地公网IP")
    print(Fore.CYAN + "4. 前往QQ官方机器人开放平台")
    print(Fore.YELLOW + "5. 配置GPT_API")

def gpt_api():
    refresh_terminal()
    print(Fore.MAGENTA + "API配置界面🤖")
    # 检查config.json文件是否存在
    if os.path.exists('./examples/config.json'):
        print(Fore.GREEN + "json配置文件存在...")
    else:
        api()

def api():
    refresh_terminal()
    print(Fore.RED + "配置文件不存在，请先配置机器人！")
    print(Fore.CYAN + "--------------------------------")
    print(Fore.MAGENTA + "QQ 频道机器人控制台🤖")
    print(Fore.GREEN + "             ——made by 不吃李子😄\n")
    print(Fore.YELLOW + "请选择机器人大模型：\n")
    print(Fore.CYAN + "1. 讯飞大模型")
    model = input(Fore.CYAN + "你的选择是: ")

    # 如果yaml写入失败，则输出错误信息
    if model == "1":
        refresh_terminal()
        print(Fore.CYAN + "--------------------------------")
        print(Fore.MAGENTA + "QQ 频道机器人控制台🤖")
        print(Fore.GREEN + "             ——made by 不吃李子😄\n")
        api = input(Fore.YELLOW + "跳转获取讯飞api(y/n)：")
        if api == "y":
            os.system("start https://console.xfyun.cn/services/bm4")
            APPID = input(Fore.CYAN + "请输入你的APPID: ")
            APPSECRET = input(Fore.CYAN + "请输入你的APPSecret: ")
            APIKey = input(Fore.CYAN + "请输入你的APIKey: ")
            with open('./examples/config.json', 'w') as f:
                json.dump({'appid': f"{APPID}", 'secret': f"{APPSECRET}", 'key': f"{APIKey}"}, f)
                print(Fore.GREEN + "配置文件写入成功！")
        elif api == "n":
            refresh_terminal()

def qqweb():
    os.system("start https://q.qq.com/#/")
def login():
    refresh_terminal()
    print(Fore.RED + "配置文件不存在，请先配置机器人！")
    print(Fore.CYAN + "--------------------------------")
    print(Fore.MAGENTA + "QQ 频道机器人控制台🤖")
    print(Fore.GREEN + "             ——made by 不吃李子😄\n")
    print(Fore.YELLOW + "请输入机器人的APPID和APPSecret\n")
    app_id = input(Fore.CYAN + ">>>APPID: ")
    app_secret = input(Fore.CYAN + ">>>APPSecret: ")
    # 如果yaml写入失败，则输出错误信息
    if app_id == "" or app_secret == "":
        print(Fore.RED + "APPID或APPSecret不能为空！")
    else:
        # 将输入的APPID和APPSecret保存到config.yaml文件中
        with open('./examples/config.yaml', 'w') as f:
            yaml.dump({'appid': f"{app_id}", 'secret': f"{app_secret}"}, f)
        # 如果yaml成功写入，则输出成功信息
            print(Fore.GREEN + "配置文件写入成功！")
            yn = input(Fore.CYAN + "是否启动机器人🤖？(y/n)：")
            if yn == "y":
                os.system("python ./examples/qqbot.py")
                sys.exit(0)
            elif yn == "n":
                refresh_terminal()
            else:
                print(Fore.RED + "输入错误，请重新输入！")
                login()
        # 如果yaml写入失败，则输出错误信息
        if app_id == "" or app_secret == "":
            print(Fore.RED + "APPID或APPSecret不能为空！")

def start_bot():
    refresh_terminal()
    print(Fore.MAGENTA + "机器人已开启")
    # 检查config.yaml文件是否存在
    if os.path.exists('./examples/config.yaml'):
        print(Fore.GREEN + "配置文件存在，正在启动机器人...")
        os.system("python ./examples/qqbot.py")
        sys.exit(0)
    else:
        login()


def get_public_ip():
    try:
        ip = subprocess.check_output(["curl", "-s", "ifconfig.me"], shell=True).decode().strip()
        print(Fore.GREEN + f"你的公网IP是: {ip}")
    except Exception as e:
        print(Fore.RED + f"获取IP时发生错误：{e}")


def main():
    refresh_terminal()
    while True:
        print_menu()
        try:
            choice = input("请输入指令：")
            if choice == "1":
                refresh_terminal()
                start_bot()
            elif choice == "2":
                refresh_terminal()
                print(Fore.YELLOW + "程序已退出")
                sys.exit(0)
            elif choice == "3":
                refresh_terminal()
                get_public_ip()
            elif choice == "4":
                refresh_terminal()
                qqweb()
            elif choice == "5":
                refresh_terminal()
                gpt_api()

            else:
                print(Fore.RED + "指令错误，请重新输入")
        except KeyboardInterrupt:
            print("\n程序被用户中断")
            sys.exit(0)


if __name__ == "__main__":
    main()
