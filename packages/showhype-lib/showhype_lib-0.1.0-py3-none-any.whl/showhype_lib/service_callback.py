import aiohttp
import asyncio
import json
from urllib.parse import urlparse, urlencode, parse_qsl
import logging

# 服务回调
async def service_callback(callback_url: str, process_result: str):
    if not callback_url:
        logging.error("callback_url 为空")
        return False

    logging.info(f"callback_url: {callback_url}")

    if process_result == None or not process_result.startswith("http"):
        callback_data = {"status": "fail", "msg" : process_result}
    else:
        callback_data = {"status": "success", "msg" : process_result}

    logging.info(f"callback_data: {callback_data}")
    
    max_retries = 3
    retry_delay = 1.0

    async def attempt_callback():
        try:
            json_data = json.dumps(callback_data)
            # post回调
            async with aiohttp.ClientSession() as client:
                async with client.post(callback_url, data=json_data) as response:
                    if response.status == 200:
                        resp_message = await response.text()
                        logging.info(f"回调响应: {resp_message}")
                        resp_json = json.loads(resp_message)
                        if resp_json.get("code") == 0:
                            return True
                        else:
                            return False
                    else:
                        logging.error(f"回调失败: {response.status}")
                        return False
        except Exception as e:
            logging.error(f"回调尝试出错: {e}")
            return False

    for attempt in range(max_retries):
        if await attempt_callback():
            logging.info(f"回调成功")
            return True
        if attempt < max_retries - 1:
            logging.info(f"回调失败,将在 {retry_delay} 秒后重试 (尝试 {attempt + 1}/{max_retries})")
            await asyncio.sleep(retry_delay)
    
    logging.error(f"回调失败,已达到最大重试次数 ({max_retries})")
    return False
    
