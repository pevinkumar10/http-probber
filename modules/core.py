try:
    from modules.cli.cli import CommandLine
    from modules.prober.prober import HttpProber

except ImportError as Ie:
    print(f"[ + ] Import Error [modules.core]: {Ie}")


class HttpProberCore:
    pass