import aiohttp.connector


try:
    import asyncio
    import aiohttp
    from time import perf_counter

except ImportError as Ie:
    print(f"[ + ] Import Error [modules.prober]: {Ie}'")
    exit(1)

class HttpProber:
    def __init__(self,timeout = 2.5,verbose = False, semaphore_count = 100):
        self.timeout = timeout
        self.verbose = verbose
        self.semaphore = asyncio.Semaphore(semaphore_count)

    async def make_request(self,url,client_session):
        
        result = {
            "url":None,
            "status":None
        }

        async with self.semaphore:
            try:

                async with client_session.get(url) as response:
                    status_code = response.status
                    result["url"] = url
                    result["status"] = status_code

                    return result

            except aiohttp.client_exceptions.InvalidURL:
                result["url"] = url
                result["status"] = "Invalid url"

                return result
            
            except asyncio.TimeoutError:
                result["url"] = url
                result["status"] = "Timeout"

                return result   

            except aiohttp.ClientConnectorDNSError:
                result["url"] = url
                result["status"] = "Connection Error"

                return result
            
            except aiohttp.client_exceptions.ClientResponseError:
                result["url"] = url
                result["status"] = "Error"

                return result 
            
            except Exception:
                result["url"] = url
                result["status"] = "Error"

                return result

    async def prober(self,urls):
        tasks = []

        timeout = aiohttp.ClientTimeout(self.timeout)

        async with aiohttp.ClientSession(timeout = timeout) as client_session:

            for url in urls:
                tasks.append(self.make_request(url,client_session))

            results = await asyncio.gather(*tasks)
                        
        return results


    def run(self,urls):

        if self.verbose:
            print(f"[ + ] Total urls to check: {len(urls)}")
        
        start_time = perf_counter()
        results = asyncio.run(self.prober(urls))
        end_time = perf_counter()

        if self.verbose:
            print(f"[ + ] Http probing completed in: {end_time - start_time} sec")

        return results
    
if __name__ == "__main__":

    urls = [
        "https://www.reddit.com",
        "https://www.bing.com",
        "https://www.yahoo.com",
        "https://www.netflix.com",
        "https://www.nytimes.com",
        "https://www.theguardian.com",
        "https://www.cloudflare.com",
        "https://www.ibm.com",
        "https://www.intel.com",
        "https://www.adobe.com",
        "https://www.canva.com",
        "https://www.salesforce.com",
        "https://www.dropbox.com",
        "https://www.spotify.com",
        "https://www.airbnb.com",
        "https://www.booking.com",
        "https://www.twitch.tv",
        "https://www.nike.com",
        "https://www.samsung.com",
        "https://www.paypal.com",
        "https://www.office.com",
        "https://www.stackexchange.com",
        "https://www.cloudflarestatus.com",
        "https://www.iana.org",
        "https://www.mozilla.org",
        "https://www.python.org",
        "https://www.nodejs.org",
        "https://www.docker.com",
        "https://www.kali.org",
        "https://www.w3.org"
    ]

    probber = HttpProber(verbose = True)
    results = probber.run(urls)

    print(results)