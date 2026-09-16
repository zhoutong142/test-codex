"""一个简单的命令行猜数字小游戏。"""

from __future__ import annotations

import random


def play_game(lower: int = 1, upper: int = 100) -> None:
    """运行一局猜数字游戏。"""
    target = random.randint(lower, upper)
    attempts = 0

    print(f"我已经想好了一个 {lower} 到 {upper} 之间的整数。")
    print("请输入你的猜测：")

    while True:
        try:
            user_input = input("> ").strip()
        except EOFError:
            print("游戏结束，欢迎下次再玩！")
            return

        try:
            guess = int(user_input)
        except ValueError:
            print("请输入一个有效的整数。")
            continue

        if not lower <= guess <= upper:
            print(f"请输入 {lower} 到 {upper} 之间的整数。")
            continue

        attempts += 1

        if guess < target:
            print("太小了，再试一次！")
        elif guess > target:
            print("太大了，再试一次！")
        else:
            print(f"恭喜你猜对了！你一共猜了 {attempts} 次。")
            break


if __name__ == "__main__":
    play_game()
