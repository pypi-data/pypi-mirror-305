# CommandCollector/Collector.py

import argparse

class CommandCollector:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Command collector for openGauss operations")
        self.subparsers = self.parser.add_subparsers(dest="command", required=True)

        # 定义各个命令
        self.subparsers.add_parser("start", help="启动 openGauss")
        self.subparsers.add_parser("stop", help="停止 openGauss")
        self.subparsers.add_parser("restart", help="重启 openGauss")
        self.subparsers.add_parser("status", help="查看 openGauss 状态")
        self.subparsers.add_parser("generateconf", help="生成配置文件")
        self.subparsers.add_parser("check", help="检查 openGauss 整体健康状态")

        checkos_parser = self.subparsers.add_parser("checkos", help="检查操作系统参数")
        checkos_parser.add_argument("option", help="检查选项")

        self.subparsers.add_parser("checkperf", help="检查性能")

        wdr_parser = self.subparsers.add_parser("wdr", help="生成 WDR 报告")
        wdr_parser.add_argument("file_path", help="WDR 报告的文件路径")

        collect_parser = self.subparsers.add_parser("collect", help="收集数据库运行日志")
        collect_parser.add_argument("start_time", help="日志收集的开始时间")
        collect_parser.add_argument("end_time", help="日志收集的结束时间")

        self.subparsers.add_parser("help", help="显示所有命令的帮助信息")

    def set_command(self, command):
        self.command = command

    def get_command(self):
        return self.parser.parse_args()  # 返回解析后的命令对象
