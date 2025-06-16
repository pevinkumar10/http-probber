try:
    from http_prober.modules.core import HttpProberCore

except ImportError as Ie:
    print(f"[ + ] Import Error [modules.http-prober]: {Ie}")
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

        # Initializing the class.
        http_prober_core = HttpProberCore() 

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