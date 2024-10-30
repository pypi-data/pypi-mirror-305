import asyncio
import urllib
from logging import Logger
from typing import Any, Optional
from promptflow.tracing import trace

import aiohttp
import logging


# This is adapted from microsoft_webxt_llm_plugins_bingapi.WebXTBingConnector
class WebXTBingConnector:
    """
    A search engine connector that uses the Bing Search API to perform a web search
    """

    _app_id: str
    _logger: Logger

    def __init__(self, app_id: str = "BD9C40AA6A35BAE3947D68548EF90E9FDFC694A2", logger: Optional[Logger] = None) -> None:
        self._app_id = app_id
        self._logger = logger or logging.getLogger(__name__)

        if not self._app_id:
            raise ValueError("Bing App Id cannot be null. Please set correct variable app_id.")

    @trace
    async def search_async(self, query: str, num_results: int, offset: int) -> Any:
        """
        Returns the search results of the query provided by pinging the Bing web search API.
        Returns `num_results` results and ignores the first `offset`.

        :param query: search query
        :param num_results: the number of search results to return
        :param offset: the number of search results to ignore
        :return: list of search results
        """
        if not query:
            raise ValueError("query cannot be 'None' or empty.")

        if not num_results:
            num_results = 1
        if not offset:
            offset = 0

        num_results = int(num_results)
        offset = int(offset)

        if num_results <= 0:
            raise ValueError("num_results value must be greater than 0.")
        if num_results >= 50:
            raise ValueError("num_results value must be less than 50.")

        if offset < 0:
            raise ValueError("offset must be greater than 0.")

        self._logger.info(
            f"Received request for bing web search with \
                params:\nquery: {query}\nnum_results: {num_results}\noffset: {offset}"
        )

        _base_url = "https://www.bingapis.com/api/v7/search"
        market = "en-US"
        setLang = "en-US"
        _request_url = (
            f"{_base_url}?q={urllib.parse.quote_plus(query)}&count={num_results}&offset={offset}&appid={self._app_id}&mkt={market}&setLang={setLang}"
        )

        self._logger.info(f"Sending GET request to {_request_url}")

        async with aiohttp.ClientSession() as session:
            async with session.get(_request_url, raise_for_status=True) as response:
                response.raise_for_status()
                data = await response.json()
                self._logger.info(data)
                return data


def search_sync(query: str, num_results: int = 1, offset: int = 0):
    connector = WebXTBingConnector("BD9C40AA6A35BAE3947D68548EF90E9FDFC694A2")
    return asyncio.run(connector.search_async(query=query, num_results=num_results, offset=offset))


if __name__ == "__main__":
    result = search_sync("hello world")
    import json
    print(json.dumps(result, indent=4))
