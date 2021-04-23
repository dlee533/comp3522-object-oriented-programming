from ChristmasFactory import ChristmasFactory
from EasterFactory import EasterFactory
from HalloweenFactory import HalloweenFactory
import pandas as pd
import math
from pathlib import Path

from Order import Order


class OrderProcessor:
    """
    Static class for processing order
    """
    FACTORY_MAPPING = {"Easter": EasterFactory(),
                       "Halloween": HalloweenFactory(),
                       "Christmas": ChristmasFactory()}

    @staticmethod
    def read_order(file_path):
        """
        Reads excel file and return order_list with orders matching the description.
        :param file_path: string
        :return: list of Order
        """
        if not Path(file_path).exists():
            raise FileNotFoundError(f"File ({file_path}) not found!")

        orders_list = []
        data_frame = pd.read_excel(open(file_path, 'rb'))
        rows = data_frame.to_dict("records")
        for row in rows:
            # dictionary comprehension with non empty value {header: value}
            row = {key: value for key, value in row.items()
                   if type(value) not in (float, int) or math.isnan(value) is False}
            row["factory_object"] = OrderProcessor.FACTORY_MAPPING[row["holiday"]]
            row.pop("holiday")
            orders_list.append(Order(**row))
        return orders_list
