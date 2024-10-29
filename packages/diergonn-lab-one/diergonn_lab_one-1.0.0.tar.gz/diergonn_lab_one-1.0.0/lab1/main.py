"""Module providing a function to print even numbers of an array."""

import json

def even(arr):
    """Module returning even numbers of an array."""

    result = []
    for ele in arr["data"]:
        if ele % 2 == 0:
            result.append(ele)

    return result

if __name__ == "__main__":
    with open('version.json', encoding="utf-8") as f:
        data = json.load(f)
    print(even(data))
