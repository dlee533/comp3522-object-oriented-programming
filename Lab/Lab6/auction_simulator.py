"""
Implements the observer pattern and simulates a simple auction.
"""
import random


class Auctioneer:
    """
    The auctioneer acts as the "core". This class is responsible for
    tracking the highest bid and notifying the bidders if it changes.
    """

    def __init__(self):
        """
        Initializes auctioneer.
        """
        self.bidders = []
        self._highest_bid = 0
        self._highest_bidder = None

    def register_bidder(self, bidder):
        """
        Adds a bidder to the list of tracked bidders.
        :param bidder: object with __call__(auctioneer) interface.
        """
        self.bidders.append(bidder)

    def reset_auctioneer(self):
        """
        Resets the auctioneer. Removes all the bidders and resets the
        highest bid to 0.
        """
        self.bidders.clear()
        self._highest_bid = 0
        self._highest_bidder = None

    def get_highest_bid(self):
        """
        Return highest bid.
        :return: float, _highest_bid
        """
        return self._highest_bid

    def get_highest_bidder(self):
        """
        Return highest bid.
        :return: str, _highest_bidder
        """
        return self._highest_bidder

    def _notify_bidders(self):
        """
        Executes all the bidder callbacks. Should only be called if the
        highest bid has changed.
        """
        for bidder in self.bidders:
            if self._highest_bidder is not bidder:
                bidder(self)

    def accept_bid(self, bid, bidder):
        """
        Accepts a new bid and updates the highest bid. This notifies all
        the bidders via their callbacks.
        :param bid: a float.
        :precondition bid: should be higher than the existing bid.
        :param bidder: The object with __call__(auctioneer) that placed
        the bid.
        """
        if bidder != "Starting Bid":
            print(f"{bidder} bidded {bid} in response to {self._highest_bidder}'s bid of {self._highest_bid}!")

        self._highest_bid = bid
        self._highest_bidder = bidder

        self._notify_bidders()


class Bidder:

    def __init__(self, name, budget=100.00, bid_probability=0.35, bid_increase_perc=1.1):
        """
        Initialize the object with given arguments.
        :param name: string
        :param budget: float
        :param bid_probability: flaot
        :param bid_increase_perc: flaot
        :precondition: name must be a string
        :precondition: budget must be a float
        :precondition: bid_probability must be a float
        :precondition: bid_increase_perc must be a float
        """
        self.name = name
        self.bid_probability = bid_probability
        self.budget = budget
        self.bid_increase_perc = bid_increase_perc
        self.highest_bid = 0

    def __call__(self, auctioneer):
        """
        Notifies the bidder to consider bidding.
        :param auctioneer: Auctioneer
        :precondition: auctioneer must be an Auctioneer
        :return: None
        """
        possible_bid = self.bid_increase_perc * auctioneer.get_highest_bid()
        if possible_bid < self.budget and random.random() <= self.bid_probability:
            self.highest_bid = possible_bid
            auctioneer.accept_bid(possible_bid, self)

    def __str__(self):
        """
        Returns the name of the bidder
        :return: str, name
        """
        return self.name


class Auction:
    """
    Simulates an auction. Is responsible for driving the auctioneer and
    the bidders.
    """

    def __init__(self, bidders):
        """
        Initialize an auction. Requires a list of bidders that are
        attending the auction and can bid.
        :param bidders: sequence type of objects of type Bidder
        """
        self._bidders = bidders
        self._auctioneer = Auctioneer()
        for bidder in bidders:
            self._auctioneer.register_bidder(bidder)

    def simulate_auction(self, item, start_price):
        """
        Starts the auction for the given item at the given starting
        price. Drives the auction till completion and prints the results.
        :param item: string, name of item.
        :param start_price: float
        """
        print(f"Auctioning {item} starting at {start_price}!")

        self._auctioneer.accept_bid(start_price, "Starting Bid")

        summary = {bidder.name: bidder.highest_bid for bidder in self._bidders}

        print(f"\nThe winner of the auction is: "
              f"{self._auctioneer.get_highest_bidder()} at ${self._auctioneer.get_highest_bid()}\n")

        print("Highest Bids Per Bidder")
        for bidder, highest_bid in summary.items():
            print(f"Bidder: {bidder}\tHighest Bid: {highest_bid}")


def create_bidder():
    name = input("Bidder's name: ")
    budget = float(input("Bidder's budget: "))
    bid_probability = random.random()
    bid_increase_perc = float(input("Bid increase percentage: "))
    return Bidder(name, budget, bid_probability, bid_increase_perc)


def main():
    bidders = []

    # Hardcoding the bidders.
    bidders.append(Bidder("Jojo", 3000, random.random(), 1.2))
    bidders.append(Bidder("Melissa", 7000, random.random(), 1.5))
    bidders.append(Bidder("Priya", 15000, random.random(), 1.1))
    bidders.append(Bidder("Kewei", 800, random.random(), 1.9))
    bidders.append(Bidder("Scott", 4000, random.random(), 2))

    while input("Add bidder(y/n): ").lower() == 'y':
        try:
            bidders.append(create_bidder())
        except ValueError:
            print("Incorrect input")

    auction_item = input("Name of item being auctioned: ")
    while True:
        try:
            starting_price = float(input("Starting price of item being auctioned: "))
            break
        except ValueError:
            print("Incorrect input")

    print("\n\nStarting Auction!!")
    print("------------------")
    my_auction = Auction(bidders)
    my_auction.simulate_auction(auction_item, starting_price)


if __name__ == '__main__':
    main()
