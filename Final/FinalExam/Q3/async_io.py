"""
(5 marks total)

This program conducts HTTP get requests using asyncio to retrieve Item
information from a PokeAPI endpoint. Documentation for the endpoint can
be found here:  "https://pokeapi.co/docs/v2#item"

Requirements:
Complete the code by implementing the async class method "get_items" in
the ItemRetriever class. This method should take in a list of item names
or ids (a list of strings) and use asyncio alongside the aiohttp package
to start a ClientSession and conduct GET requests concurrently.

The code does not need to contain docstrings or implement any error
handling for invalid data. A main method has been provided for you to
test with. DO NOT MODIFY any other code except the get_items class
method.
"""

import asyncio
import aiohttp


class Item:

    def __init__(self, name, cost, fling_power, **kwargs):
        self.name = name
        self.cost = cost
        self.fling_power = fling_power
        self.details = kwargs

    def __str__(self):
        formatted_str = f"Name: {self.name}\n" \
                        f"-----------------\n" \
                        f"Cost: {self.cost}\n" \
                        f"Fling Power: {self.fling_power}\n\n"
        return formatted_str


class ItemRetriever:

    ENDPOINT = "https://pokeapi.co/api/v2/item/{0}/"

    @staticmethod
    async def get_request(url:str, session: aiohttp.ClientSession):
        response = await session.request(method="GET", url=url)
        json_response = await response.json()
        return json_response

    @classmethod
    async def get_items(cls, item_data_set: list) -> list:
        """
        Takes in a list of argumentrs representing item id's and/or
        names and starts an aiohttp ClientSession to conduct get
        requests based on these arguments to create Item objects.
        :param item_data_set: a list of strings, each element should
                              represent an item name or id.
        :return: a list of Item objects
        """
        # TODO: Implement this method to conduct get requests
        #  concurrently.
        async with aiohttp.ClientSession() as session:
            list_tasks = [asyncio.create_task(ItemRetriever.get_request(ItemRetriever.ENDPOINT.format(item_data), session)) for item_data in item_data_set]
            responses = await asyncio.gather(*list_tasks)
            item_list = [Item(**response) for response in responses]
            return item_list


def main():
    item_data_set = ["1", "2", "fresh-water"]
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    items = loop.run_until_complete(ItemRetriever.get_items(item_data_set))
    for item in items:
        print(item)


if __name__ == '__main__':
    main()