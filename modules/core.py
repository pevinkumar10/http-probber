try:
    from modules.cli.cli import CommandLine
    from modules.prober.prober import HttpProber
    from modules.utils.utils import read_from_file

except ImportError as Ie:
    print(f"[ + ] Import Error [modules.core]: {Ie}")
    exit(1)


class HttpProberCore:

    def __init__(self,verbose = False):
        self.verbose = verbose
        self.default_semaphore_count = 100
        self.commandline = CommandLine()

    def main(self):
        arguments = self.commandline.get_arguments()

        if arguments.help:
            print(self.commandline.get_help())
            exit()

        if arguments.url and arguments.url_list:
            print("Usage: http-prober ( -u / --url-list ) [options] \nDuplicate Input entry, Use --help to see more options.")
            exit(1)
        
        else:
            if arguments.url or arguments.url_list:
                if arguments.verbose:
                    self.verbose = True
                    print(f"[ + ] Verbose mode enabled.")

                urls = []
                semaphore_count = arguments.concurrency if arguments.concurrency else self.default_semaphore_count
                
                if semaphore_count != self.default_semaphore_count:
                    print(f"[ + ] Semaphore Count configured to {semaphore_count}")

                prober = HttpProber(verbose = self.verbose ,semaphore_count = semaphore_count)
                
                if arguments.url: 
                    urls.append(str(arguments.url))

                    if self.verbose:
                        print(f"[ + ] Total urls to check: {len(urls)}.")

                elif arguments.url_list:
                    contents = read_from_file(arguments.url_list)

                    if contents:
                        urls.extend(contents)

                    if self.verbose:
                        print(f"[ + ] Total urls to check: {len(urls)}")
                
                print(f"[ + ] Http Prober started !!")

                prober_result = prober.run(urls)

                if prober_result:
                    print(f"\n[ + ] Result:")
                    for result in prober_result:
                        print(f"      {result["url"]} [{result["status"]}]")

                else:
                    print(f"[ ! ] Something went wrong,try again")
                    exit(1)

            else:
                print("Usage: http-prober ( -u / --url-list ) [options] \nUse --help to see more options.")
                exit(1)

    def run(self):
        self.main()