try:
    from http_prober.modules.cli.cli import CommandLine
    from http_prober.modules.core import HttpProberCore

except ImportError as Ie:
    print(f"[ + ] Import Error [modules.core]: {Ie}")
    exit(1)

class HttpProber:
    """
        Class to probe the http status code from url(s) using asynchronous programming.

        Args:
            None
        Retruns:
            None
    """
    def core_handler(self) -> None:
        """
            Http Prober handler to start the core.

            Args:
                None

            Results:
                None
        """

        # Initializing the classes.
        commandline = CommandLine()
        http_prober_core = HttpProberCore()
        
        # Prining HttpProber's banner. 
        print(commandline.get_banner()) 

        # Starting the Http Prober core.
        http_prober_core.run()


def main() -> None:
    """
        Main function to start Core handler.

        Args:
            None
            
        Returns:
            None
    """
    prober = HttpProber()
    prober.core_handler()

if __name__ == "__main__":
    main()