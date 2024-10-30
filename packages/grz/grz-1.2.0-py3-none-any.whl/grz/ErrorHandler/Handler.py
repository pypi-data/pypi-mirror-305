# ErrorHandler/Handler.py

class ErrorHandler:
    def handle_error(self, error):
        if isinstance(error, ValueError):
            print(f"[Error] Invalid input: {error}")
        elif isinstance(error, FileNotFoundError):
            print("[Error] File not found. Please check the file path.")
        elif isinstance(error, PermissionError):
            print("[Error] Permission denied. Please check your permissions.")
        elif isinstance(error, KeyError):
            print(f"[Error] Missing key: {error}")
        else:
            print(f"[Error] An unexpected error occurred: {error}")

    def check_missing_argument(self, args, required_args):
        """
        检查是否缺少必要的参数。
        :param args: 用户提供的参数。
        :param required_args: 当前命令所需的参数列表。
        :return: 缺少参数则返回False,否则返回True。
        """
        missing_args = [arg for arg in required_args if not getattr(args, arg, None)]
        if missing_args:
            print(f"[Error] Missing required arguments: {', '.join(missing_args)}")
            return False
        return True

    def check_invalid_command(self, command, available_commands):
        """
        检查命令是否有效。
        :param command: 用户输入的命令。
        :param available_commands: 支持的命令列表。
        :return: 若命令有效则返回True否则返回False。
        """
        if command not in available_commands:
            print(f"[Error] Unknown command '{command}'. Type 'help' to see available commands.")
            return False
        return True
