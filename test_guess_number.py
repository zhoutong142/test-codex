"""guess_number 模块的基本测试。"""

import unittest
from unittest.mock import patch

import guess_number


class PlayGameTests(unittest.TestCase):
    @patch("builtins.print")
    @patch("builtins.input", side_effect=["50", "42"])
    @patch("guess_number.random.randint", return_value=42)
    def test_game_gives_hints_and_reports_attempts(self, _randint, _input, mock_print):
        guess_number.play_game()

        messages = [call.args[0] for call in mock_print.call_args_list]
        self.assertIn("太大了，再试一次！", messages)
        self.assertIn("恭喜你猜对了！你一共猜了 2 次。", messages)

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["abc", "101", "42"])
    @patch("guess_number.random.randint", return_value=42)
    def test_game_rejects_invalid_input_without_counting_it(
        self, _randint, _input, mock_print
    ):
        guess_number.play_game()

        messages = [call.args[0] for call in mock_print.call_args_list]
        self.assertIn("请输入一个有效的整数。", messages)
        self.assertIn("请输入 1 到 100 之间的整数。", messages)
        self.assertIn("恭喜你猜对了！你一共猜了 1 次。", messages)

    @patch("builtins.print")
    @patch("builtins.input", side_effect=EOFError)
    @patch("guess_number.random.randint", return_value=42)
    def test_game_exits_cleanly_when_input_ends(self, _randint, _input, mock_print):
        guess_number.play_game()

        messages = [call.args[0] for call in mock_print.call_args_list]
        self.assertIn("游戏结束，欢迎下次再玩！", messages)


if __name__ == "__main__":
    unittest.main()
