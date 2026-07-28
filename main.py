import json
import os
from datetime import datetime

from utils import load_test_data, filter, classify, DEFAULT_DATA
from inventory import Inventory


def main():
    """
    Main function to run the inventory system.
    """

    objects = load_test_data()

    objects.append(
        {"id": 7, "color": "red", "weight_g": 90}
    )

    print("Filtered objects (weight >= 100):")
    print(filter(objects, min_weight=100))

    inventory = Inventory()

    for obj in objects:

        try:
            inventory.add(obj)

            obj["test_result"] = {
                "status": "SUCCESS",
                "message": "Object processed successfully"
            }

        except KeyError as e:

            obj["test_result"] = {
                "status": "ERROR",
                "message": f"Missing key {e}"
            }

            print(f"Skipped object id={obj.get('id')} : missing key {e}")

    print("\nInventory:")
    print(inventory)

    print("\nCounts:")
    print(inventory.count())

    print("\nAverage Weight:")
    print(inventory.avg_weight())

    current_time = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")

    file_name = os.path.splitext(DEFAULT_DATA)[0]

    output_file = f"{file_name}_tested_at_{current_time}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(objects, f, indent=4)

    print(f"\nOutput file saved as: {output_file}")


if __name__ == "__main__":
    main()