# main.py

import argparse
from .CommandCollector.Collector import CommandCollector
from .CommandParser.Parser import CommandParser
from .ErrorHandler.Handler import ErrorHandler

def grz():
    collector = CommandCollector()
    command_args = collector.get_command()  # 获取解析后的命令对象
    error_handler = ErrorHandler()

    try:
        # 直接使用解析后的命令对象
        CommandParser().parse_and_execute_command(command_args)  # 使用解析的命令
    except Exception as e:
        error_handler.handle_error(e)

def main():
    grz()

