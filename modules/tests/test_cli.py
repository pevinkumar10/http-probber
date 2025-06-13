try:
    from modules.cli.cli import CommandLine
    from colorama import Fore,Style
    
except ImportError as Ie:
    print(f"[ + ] Import Error [modules.tests.cli]: {Ie}")

# Intializing the CommandLine class

cli = CommandLine()

blue = Fore.BLUE
red = Fore.RED
blue = Fore.BLUE
white = Fore.WHITE
magenta = Fore.MAGENTA
bright = Style.BRIGHT
green = Fore.GREEN
red = Fore.RED
bold = Style.BRIGHT
reset = Style.RESET_ALL

def test_banner():
    banner = cli.get_banner()
    expected = """
        
          ___ ___   __    __                  __________              ___.                 
         /   |   \\_/  |__/  |_______          \\______   \\_______  ____\\_ |__   ___________ 
        /    ~    \\   __\\   __\\____ \\   ______ |     ___/\\_  __ \\/  _ \\| __ \\_/ __ \\_  __ \\
        \\    Y    /|  |  |  | |  |_> > /_____/ |    |     |  | \\(  <_> ) \\_\\ \\  ___/|  | \\/
         \\___|_  / |__|  |__| |   __/          |____|     |__|   \\____/|___  /\\___  >__|   
               \\/             |__|                                         \\/     \\/       
                                                   

                Async tool to enumerate status code using aiohttp.
                          Github : pevinkumar10
        """

    assert banner.strip() == expected.strip()


def test_helpmenu():
    help_menu = cli.get_help()
    expected = f"""
        {bold}{white}[{reset}{bold}{blue}DESCRIPTION{reset}{white}]{reset}: {white}{bold}http-prober{reset} {white}is a tool used to enumerate status code from the given url(s) by{reset}{bold}{green}pevinkumar10{reset}.\n
            {bold}{white}[{reset}{bold}{blue}Usage{reset}{white}]{reset}: http-prober [ options ]\n
                    {white}http-prober {bold}{white}<{reset}{bold}{blue}Flags{reset}{bold}{white}>\n
            [{reset}{bold}{blue}Flags{reset}{bold}{white}]
                    [{reset}{bold}{blue}Input{reset}{bold}{white}]{reset}
                        -u,   --url                     :  Url to check status code.                                                
                        -uL,  --url-list                :  List of urls to scan status code.  

                    [{reset}{bold}{blue}Options{reset}{bold}{white}]{reset}
                        -t,   --threads                 :  Number of threads (default : 40)               

                    {bold}{white}[{reset}{bold}{blue}Debug{reset}{bold}{white}]{reset}
                        -d,   --debug                   :  To set debug flag.
                        -h,   --help                    :  To see all the available options.

            """
    assert help_menu.strip() == expected.strip()
