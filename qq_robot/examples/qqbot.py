from colorama import init, Fore

import sys, os

init(autoreset=True)

def refresh_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    print(Fore.CYAN + "--------------------------------")
    print(Fore.MAGENTA + "QQ 频道机器人控制台🤖")
    print(Fore.GREEN + "             ——made by 不吃李子😄\n")

    print(Fore.CYAN + "1. 机器人at被动回复")


def main():
    refresh_terminal()
    while True:
        print_menu()
        try:
            choice = input("请输入指令：")
            if choice == "1":
                refresh_terminal()
                os.system("python ./examples/demo_at_reply.py")


            else:
                print(Fore.RED + "指令错误，请重新输入")
        except KeyboardInterrupt:
            print("\n程序被用户中断")
            sys.exit(0)
if __name__ == "__main__":
    main()