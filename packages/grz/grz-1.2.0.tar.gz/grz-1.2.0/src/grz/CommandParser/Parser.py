# CommandParser/Parser.py
import subprocess
from ..ErrorHandler.Handler import ErrorHandler

def get_current_port():
    return 5432

def generate_help_message():
    help_text = """Available commands:
    start        - Start the openGauss database
    stop         - Stop the openGauss database
    restart      - Restart the openGauss database
    ----------------------------------------------------------------------------
    status       - Show detailed status of the database cluster
    generateconf - Generate and distribute configuration files
    check        - Check cluster state with specified option
    checkos      - Check operating system compatibility
    checkperf    - Check system performance 
    ----------------------------------------------------------------------------
    wdr          - Generate WDR performance report (requires --file_path)
    collect      - Collect diagnostic logs (requires --start_time, --end_time)
    help         - Show this help message"""
    return help_text

class CommandParser:
    def __init__(self):
        self.error_handler = ErrorHandler()
        self.command_map = {
            "start": "gs_om -t start",
            "stop": "gs_om -t stop",
            "restart": "gs_om -t restart",
            "status": "gs_om -t status --detail",
            "generateconf": "gs_om -t generateconf -X /opt/software/openGauss/clusterconfig.xml --distribute",
            "check": "gs_check -U omm -i CheckClusterState",
            "checkos": lambda option: f'gs_checkos -i {option}',
            "checkperf": "gs_checkperf",
            "wdr": lambda file_path: f'touch {file_path} && gsql -d postgres -p {get_current_port()} -r',
            "collect": lambda start_time, end_time: f'gs_collector --begin-time="{start_time}" --end-time="{end_time}"',
            "help": ''
        }

    def parse_and_execute_command(self, args):
        command = args.command.lower()
        available_commands = list(self.command_map.keys())

        if not self.error_handler.check_invalid_command(command, available_commands):
            return

        required_args_map = {
            "checkos": ["option"],
            "wdr": ["file_path"],
            "collect": ["start_time", "end_time"]
        }
        
        if command in required_args_map:
            required_args = required_args_map[command]
            if not self.error_handler.check_missing_argument(args, required_args):
                return

        if command == "help":
            print(generate_help_message())
            return

        if callable(self.command_map[command]):
            if command == "checkos":
                full_command = self.command_map[command](args.option)
            elif command == "wdr":
                full_command = self.command_map[command](args.file_path)
            elif command == "collect":
                full_command = self.command_map[command](args.start_time, args.end_time)
        else:
            full_command = self.command_map[command]

        result = subprocess.run(full_command, shell=True, capture_output=True, text=True)
        print(result.stdout if result.returncode == 0 else result.stderr)
