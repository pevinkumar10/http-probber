try:
    import asyncio
    import aiohttp

except ImportError as Ie:
    print(f"[ + ] Import Error [modules.prober]: {Ie}'")
    exit(1)

class HttpProber:
    def __init__(self,timeout,verbose = False):
        self.verbose = verbose
        self.timeout = timeout

    async def make_request(self,url,client_session):
        
        result = {
            "url":None,
            "Status":None
        }
        try:
            async with client_session.get(url) as response:
                status_code = response.status

                result["url"] = url
                result["Status"] = status_code

        except aiohttp.client_exceptions.InvalidURL:
            if self.verbose:
                print(f"[ + ]: Invalid url: {url}")

            result["url"] = url
            result["Status"] = "Invalid"

            return result
        
        except aiohttp.ClientConnectorDNSError:
            if self.verbose:
                print(f"[ + ]: Connection Error: {url}")

            result["url"] = url
            result["Status"] = "Error"

            return result

        return result

    async def probber(self,urls):
        tasks = []
        async with aiohttp.ClientSession() as client_session:

            for url in urls:
                tasks.append(self.make_request(url,client_session))

            results = await asyncio.gather(*tasks)
                
            return results

    def run(self,urls):
        if self.verbose:
            print(f"[ + ] Total urls to check: {len(urls)}")

        return asyncio.run(self.probber(urls))
    
if __name__ == "__main__":

    urls = ["https://google.com",
            "https://facebook.com",
            "https://instagram.com",
            "https://example.com",
            "https://google.com",
            "https://facebook.com",
            "https://instagram.com",
            "https://google.com",
            "https://facebook.com",
            "https://instagram.com",
            "https://example.com",
            "https://google.com",
            "https://facebook.com",
            "https://instagram.com",
            "https://example.com",
            "https://example.com",
            "https://google.com",
            "https://facebook.com",
            "https://instagram.com",
            "https://example.com",
            "https://google.com",
            "https://facebook.com",
            "https://instagram.com",
            "https://example.com",
            "https://google.com",
            "https://facebook.com",
            "https://instagram.com",
            "https://example.com"
            "https://tesgdknzsknxkckxz"
            ]

    probber = HttpProber(timeout = 0.1,verbose = True)
    print(probber.run(urls))