try:
    from modules.cli.cli import CommandLine
    from modules.core import HttpProberCore

except ImportError as Ie:
    print(f"[ + ] Import Error [modules.core]: {Ie}")
    exit(1)

class HttpProber:
    def core_handler(self):
        
        commandline = CommandLine()
        http_prober_core = HttpProberCore()
        
        print(commandline.get_banner()) 

        http_prober_core.run()

if __name__ == "__main__":
    prober = HttpProber()
    prober.core_handler()