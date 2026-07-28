from utils import classify


class Inventory:
    """
    Store objects and count them by classification.
    """

    def __init__(self):
        """
        Initialize an empty inventory.
        """
        self.items = []
        self.counts = {}

    def add(self, obj):
        """
        Add an object to the inventory.

        Args:
            obj (dict): Object to add.
        """

        self.items.append(obj)

        bin_name = classify(obj)

        self.counts[bin_name] = self.counts.get(bin_name, 0) + 1

    def count(self):
        """
        Return the number of objects in each bin.

        Returns:
            dict: Counts for every bin.
        """
        return self.counts

    def avg_weight(self):
        """
        Calculate the average weight of all objects.

        Returns:
            float: Average weight.
        """

        if not self.items:
            return 0

        total = sum(obj["weight_g"] for obj in self.items)

        return total / len(self.items)

    def __repr__(self):
        """
        Return a readable representation of the inventory.
        """

        return f"Inventory(items={len(self.items)}, counts={self.counts})"