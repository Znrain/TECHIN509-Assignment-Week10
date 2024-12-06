import sys
import os
# 添加 models 文件夹到路径中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'models')))

import unittest
from models.board import Board  # 导入 Board 类

class TestCheckWinner(unittest.TestCase):
    def test_check_winner(self):
        # 初始化 Board 对象
        board = Board()

        # 模拟一些游戏情况
        board.update_board(0, 0, 'X')
        board.update_board(1, 1, 'X')
        board.update_board(2, 2, 'X')
        
        # 检查赢家
        winner = board.check_winner()

        # 断言赢家是 'X'
        self.assertEqual(winner, 'X')

if __name__ == '__main__':
    unittest.main()
