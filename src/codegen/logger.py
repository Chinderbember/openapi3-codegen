from colorama import init as colorama_init
from colorama.ansi import AnsiFore, Fore


class Logger:
    def __init__(self) -> None:
        colorama_init(autoreset=True)

    @staticmethod
    def _print_with_color(color: AnsiFore, message: str) -> None:
        print(f"{color}{message}")

    def warning(self, message: str) -> None:
        self._print_with_color(Fore.YELLOW, message)

    def error(self, message: str) -> None:
        self._print_with_color(Fore.RED, message)

    def success(self, message: str) -> None:
        self._print_with_color(Fore.GREEN, message)

    def info(self, message: str) -> None:
        self._print_with_color(Fore.BLUE, message)


logger = Logger()
