def classify(obj: dict):
    """
    Classify an object into the correct bin based on
    temperature, color, and shape.

    Args:
        obj (dict): Object information.

    Returns:
        str: Name of the destination bin.
    """

    if obj["temperature_c"] > 50:
        return "hot_bin"

    elif obj["color"] == "red":
        return "red_bin"

    elif obj["shape"] == "sphere":
        return "sphere_bin"

    else:
        return "general_bin"


def filter(objects: list[dict], min_weight = None, color=None):
    """
    Filter objects by minimum weight and/or color.

    Args:
        objects (list): List of objects.
        min_weight (int): Minimum allowed weight.
        color (str): Required object color.

    Returns:
        list: Filtered objects.
    """

    if min_weight < 0:
        raise ValueError("Min Weight must be non-ngatve")

    

    result = []

    for obj in objects:

        if min_weight is not None:
            if obj["weight_g"] < min_weight:
                continue

        if color is not None:
            if obj["color"] != color:
                continue

        result.append(obj)

    return result