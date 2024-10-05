import asyncio
import aiohttp
import time
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def make_request(session, url, data):
    try:
        async with session.post(url, json=data, timeout=10) as response:
            if response.status == 200:
                return await response.json()
            else:
                content = await response.text()
                logger.error(f"Error: Status {response.status}, Content: {content}")
                return None
    except Exception as e:
        logger.error(f"Request failed: {str(e)}")
        return None

async def run_load_test(num_requests, requests_per_second):
    url = "https://www.liveinfo.org/api/rewrite_links"
    data = {"url": "https://example.com"}

    async with aiohttp.ClientSession() as session:
        tasks = []
        start_time = time.time()
        for _ in range(num_requests):
            tasks.append(make_request(session, url, data))
            if len(tasks) >= requests_per_second:
                responses = await asyncio.gather(*tasks)
                elapsed = time.time() - start_time
                if elapsed < 1:
                    await asyncio.sleep(1 - elapsed)
                tasks = []
                start_time = time.time()

        if tasks:
            await asyncio.gather(*tasks)

    end_time = time.time()
    total_time = end_time - start_time
    requests_per_second = num_requests / total_time

    logger.info(f"Completed {num_requests} requests in {total_time:.2f} seconds")
    logger.info(f"Requests per second: {requests_per_second:.2f}")

    with open('load_test_output.txt', 'w') as f:
        f.write(f"Completed {num_requests} requests in {total_time:.2f} seconds\n")
        f.write(f"Requests per second: {requests_per_second:.2f}\n")

if __name__ == "__main__":
    num_requests = 100  # Simulate 100 requests (about 1 minute of load)
    requests_per_second = 2  # Slightly higher than 1.4 to account for network delays
    asyncio.run(run_load_test(num_requests, requests_per_second))
