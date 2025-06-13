import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../' )))

try:
    from modules.cli.cli import CommandLine
except ImportError as Ie:
    print(f"[ + ] Import Error [modules.tests.cli]: {Ie}")

# Intializing the CommandLine class

cli = CommandLine()

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
