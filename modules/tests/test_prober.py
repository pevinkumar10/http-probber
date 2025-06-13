try:
    import pytest
    import aiohttp
    from modules.prober.prober import HttpProber

except ImportError as Ie:
    print(f"[ + ] Import Error [modules.tests.prober]: {Ie}")

prober = HttpProber()

@pytest.mark.asyncio
async def test_make_request():
    url = 'https://google.com'
    status = 200

    async with aiohttp.ClientSession() as client_session:
        result = await prober.make_request(url,client_session)

    assert result["status"] == status

@pytest.mark.asyncio
async def test_prober():
    urls = [
        "https://google.com",
        "https://instagram.com",
        "https://facebook.com"
    ]
    expected = [
                {
                    "url":"https://google.com",
                    "status":200
                },
                {
                    "url":"https://instagram.com",
                    "status":200
                },
                {
                    "url":"https://facebook.com",
                    "status":200
                }
            ]
    results = await prober.probber(urls)

    assert expected == results

def test_run():
    urls = [
        "https://google.com",
        "https://instagram.com",
        "https://facebook.com"
    ]
    expected = [
                {
                    "url":"https://google.com",
                    "status":200
                },
                {
                    "url":"https://instagram.com",
                    "status":200
                },
                {
                    "url":"https://facebook.com",
                    "status":200
                }
            ]
    
    results = prober.run(urls)

    assert expected == results
