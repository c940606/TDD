# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:49:29 2020

@author: zeh0814
"""

import unittest
from TDD import main

class MainTest(unittest.TestCase):
    """用于测试TDD.py"""
    #setUp初始化
    #s = main(x,target) #自己函数的输出
    def setUp(self):
        print("\n")
        print("test_case_start")
        pass
    #销毁
    def tearDown(self):
        pass
    #具体的测试用例，使用test开头
    def test_tdd(self):
        """是否能正确处理给出的数字"""
        main_str = main(3,19)  #将函数返回的结果存储到变量main_str中
        print(main_str)
        self.assertEqual(main_str,'3*3+3*3+3/3')#断言方法,用来核实得到的结果是否与我们预期的一致。
   

if __name__ == '__main__':
    #x,target = map(int,input().split())
    unittest.main()