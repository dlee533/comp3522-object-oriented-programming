from ItemFactory import ItemFactory
import datetime

from Lab8.Dvd import Dvd


class DvdFactory(ItemFactory):
    """
    Responsible for creating Dvd objects.
    """
    def create_item(self, **kwargs):
        """
        Return a Dvd object.
        :param kwargs: key-value pairs consisting of call_num, title, num_copies details
        :return: Dvd object
        """
        while True:
            try:
                release_date = input("Enter release date (yyyy-mm-dd): ")
                if release_date != datetime.datetime.strptime(release_date, '%Y-%m-%d').strftime('%Y-%m-%d'):
                    raise ValueError
            except ValueError:
                print("Incorrect release format entered. Format should be in yyyy-mm-dd")
            else:
                break
        region_code = input("Enter region code: ")
        return Dvd(release_date, region_code, **kwargs)
