# -*- coding: utf-8 -*-
"""Python_Section_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qEjXF9XZME_X6wLItZGsgmPpN_jlmFil

# PYTHON SECTION -1

Q1. **Reverse List by N Elements**

Problem Statement:

Write a function that takes a list and an integer n, and returns the list with every group of n elements reversed. If there are fewer than n elements left at the end, reverse all of them.

Requirements:

You must not use any built-in slicing or reverse functions to directly reverse the sublists.
The result should reverse the elements in groups of size n.
"""

from typing import Dict, List

import pandas as pd

def reverse_by_n_elements(lst: List[int], n: int) -> List[int]:
    """
    Reverses the input list by groups of n elements.
    """
    # Resultant list to store the reversed elements
    result = []

    # Iterate over the list in chunks of size n
    for i in range(0, len(lst), n):
        # Reverse the current chunk manually and add it to the result
        current_chunk = lst[i:i + n]
        reversed_chunk = []
        for j in range(len(current_chunk) - 1, -1, -1):
            reversed_chunk.append(current_chunk[j])
        result.extend(reversed_chunk)

    return result

reverse_by_n_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)

"""Q2. **Lists & Dictionaries**

Problem Statement:

Write a function that takes a list of strings and groups them by their length. The result should be a dictionary where:

The keys are the string lengths.
The values are lists of strings that have the same length as the key.

Requirements:

Each string should appear in the list corresponding to its length.
The result should be sorted by the lengths (keys) in ascending order.
"""

from typing import List, Dict

def group_by_length(lst: List[str]) -> Dict[int, List[str]]:
    """
    Groups the strings by their length and returns a dictionary.
    """
    # Dictionary to store groups by length
    length_groups = {}

    # Iterate over each string in the list
    for string in lst:
        length = len(string)
        # Add the string to the corresponding list in the dictionary
        if length not in length_groups:
            length_groups[length] = []
        length_groups[length].append(string)

    # Sort the dictionary by key (length)
    sorted_length_groups = dict(sorted(length_groups.items()))

    return sorted_length_groups

lst = ["apple", "banana", "kiwi", "pear", "peach", "plum", "cherry"]
result = group_by_length(lst)
print(result)

"""Q3. **Flatten a Nested Dictionary**

Problem Statement

You are given a nested dictionary that contains various details (including lists and sub-dictionaries). Your task is to write a Python function that flattens the dictionary such that:

Nested keys are concatenated into a single key with levels separated by a dot (.).
List elements should be referenced by their index, enclosed in square brackets (e.g., sections[0]).
For example, if a key points to a list, the index of the list element should be appended to the key string, followed by a dot to handle further nested dictionaries.

Requirements:

1. Nested Dictionary: Flatten nested dictionaries into a single level, concatenating keys.
2. Handling Lists: Flatten lists by using the index as part of the key.
3. Key Separator: Use a dot (.) as a separator between nested key levels.
4. Empty Input: The function should handle empty dictionaries gracefully.
5. Nested Depth: You can assume the dictionary has a maximum of 4 levels of nesting.
"""

from typing import Dict, Any

def flatten_dict(nested_dict: Dict, sep: str = '.') -> Dict:
    """
    Flattens a nested dictionary into a single-level dictionary with dot notation for keys.

    :param nested_dict: The dictionary object to flatten
    :param sep: The separator to use between parent and child keys (defaults to '.')
    :return: A flattened dictionary
    """
    # Resultant flattened dictionary
    flat_dict = {}

    # Helper function to recursively flatten the dictionary
    def flatten(current_item: Any, parent_key: str = ''):
        if isinstance(current_item, dict):
            for key, value in current_item.items():
                # Construct new key with separator
                new_key = f"{parent_key}{sep}{key}" if parent_key else key
                # Recur for the next level of nesting
                flatten(value, new_key)
        elif isinstance(current_item, list):
            for index, item in enumerate(current_item):
                # Use index as part of the key for lists
                new_key = f"{parent_key}[{index}]"
                # Recur for the next level of nesting
                flatten(item, new_key)
        else:
            # Base case: add the flattened key-value pair
            flat_dict[parent_key] = current_item

    # Start the recursion with the initial dictionary
    flatten(nested_dict)

    return flat_dict

nested_dict = {
    "name": "Alice",
    "address": {
        "city": "Wonderland",
        "postal": {
            "code": 12345,
            "area": "North"
        }
    },
    "sections": [
        {"title": "Introduction", "content": "Hello"},
        {"title": "Conclusion", "content": "Goodbye"}
    ]
}

result = flatten_dict(nested_dict)
result

"""Q4. **Generate Unique Permutations**

Problem Statement:

You are given a list of integers that may contain duplicates. Your task is to generate all unique permutations of the list. The output should not contain any duplicate permutations.
"""

from typing import List

def unique_permutations(nums: List[int]) -> List[List[int]]:
    """
    Generate all unique permutations of a list that may contain duplicates.

    :param nums: List of integers (may contain duplicates)
    :return: List of unique permutations
    """
    # Result list to store unique permutations
    result = []

    # Sort the input list to handle duplicates
    nums.sort()

    # Helper function for backtracking
    def backtrack(path, used):
        # If the current path contains all elements, add it to the result
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            # Skip used elements or duplicates
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue

            # Mark the element as used
            used[i] = True
            # Recur with the current number added to the path
            path.append(nums[i])
            backtrack(path, used)
            # Undo the choice for the next iteration
            path.pop()
            used[i] = False

    # Boolean array to mark elements as used
    used = [False] * len(nums)
    # Start backtracking with an empty path
    backtrack([], used)

    return result

nums = [1, 1, 2]
result = unique_permutations(nums)
result

"""Q5. **Find All Dates in a Text**

Problem Statement:

You are given a string that contains dates in various formats (such as "dd-mm-yyyy", "mm/dd/yyyy", "yyyy.mm.dd", etc.). Your task is to identify and return all the valid dates present in the string.

You need to write a function find_all_dates that takes a string as input and returns a list of valid dates found in the text. The dates can be in any of the following formats:

1. dd-mm-yyyy
2. mm/dd/yyyy
3. yyyy.mm.dd

You are required to use regular expressions to identify these dates.
"""

import re
from typing import List

def find_all_dates(text: str) -> List[str]:
    """
    This function takes a string as input and returns a list of valid dates
    in 'dd-mm-yyyy', 'mm/dd/yyyy', or 'yyyy.mm.dd' format found in the string.

    Parameters:
    text (str): A string containing the dates in various formats.

    Returns:
    List[str]: A list of valid dates in the formats specified.
    """
    # Regular expressions for the different date formats
    date_patterns = [
        r'\b\d{2}-\d{2}-\d{4}\b',  # dd-mm-yyyy
        r'\b\d{2}/\d{2}/\d{4}\b',  # mm/dd/yyyy
        r'\b\d{4}\.\d{2}\.\d{2}\b' # yyyy.mm.dd
    ]

    # List to store all found dates
    found_dates = []

    # Search for all date patterns in the text
    for pattern in date_patterns:
        matches = re.findall(pattern, text)
        found_dates.extend(matches)

    return found_dates

text = "The event is scheduled on 12-09-2024 and the deadline for submission is 09/15/2024. Another important date is 2024.10.01."
result = find_all_dates(text)
result

"""Q6. **Decode Polyline, Convert to DataFrame with Distances**

Problem Statement

You are given a polyline string, which encodes a series of latitude and longitude coordinates. Polyline encoding is a method to efficiently store latitude and longitude data using fewer bytes. The Python polyline module allows you to decode this string into a list of coordinates.

Write a function that performs the following operations:

1. Decode the polyline string using the polyline module into a list of (latitude, longitude) coordinates.
2. Convert these coordinates into a Pandas DataFrame with the following columns:
   1. latitude: Latitude of the coordinate.
   2. longitude: Longitude of the coordinate.
   3. distance: The distance (in meters) between the current row's coordinate and the previous row's one. The first row will have a distance of 0 since there is no previous point.
3. Calculate the distance using the Haversine formula for points in successive rows.
"""

! pip install polyline

import pandas as pd
import polyline
import math
from typing import List

def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the Haversine distance between two points on the Earth in meters.

    Args:
        lat1 (float): Latitude of the first point.
        lon1 (float): Longitude of the first point.
        lat2 (float): Latitude of the second point.
        lon2 (float): Longitude of the second point.

    Returns:
        float: Distance between the two points in meters.
    """
    # Radius of the Earth in meters
    R = 6371000

    # Convert latitudes and longitudes from degrees to radians
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    # Haversine formula
    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance in meters
    distance = R * c
    return distance

def polyline_to_dataframe(polyline_str: str) -> pd.DataFrame:
    """
    Converts a polyline string into a DataFrame with latitude, longitude, and distance between consecutive points.

    Args:
        polyline_str (str): The encoded polyline string.

    Returns:
        pd.DataFrame: A DataFrame containing latitude, longitude, and distance in meters.
    """
    # Decode the polyline string into a list of (latitude, longitude) coordinates
    coordinates = polyline.decode(polyline_str)

    # Create a DataFrame from the list of coordinates
    df = pd.DataFrame(coordinates, columns=['latitude', 'longitude'])

    # Calculate distances between consecutive points
    distances = [0.0]  # The first point has a distance of 0
    for i in range(1, len(coordinates)):
        lat1, lon1 = coordinates[i - 1]
        lat2, lon2 = coordinates[i]
        # Calculate the distance using the Haversine formula
        distance = haversine_distance(lat1, lon1, lat2, lon2)
        distances.append(distance)

    # Add the distance column to the DataFrame
    df['distance'] = distances

    return df

polyline_str = "_p~iF~ps|U_ulLnnqC_mqNvxq`@"
result = polyline_to_dataframe(polyline_str)
result

"""Q7. **Matrix Rotation and Transformation**

Problem Statement

Write a function that performs the following operations on a square matrix (n x n):

1. Rotate the matrix by 90 degrees clockwise.
2. After rotation, for each element in the rotated matrix, replace it with the sum of all elements in the same row and column (in the rotated matrix), excluding itself.

The function should return the transformed matrix.
"""

from typing import List

def rotate_and_multiply_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Rotate the given matrix by 90 degrees clockwise, then replace each element
    with the sum of all elements in the same row and column (excluding itself) in the rotated matrix.

    Args:
    - matrix (List[List[int]]): 2D list representing the matrix to be transformed.

    Returns:
    - List[List[int]]: A new 2D list representing the transformed matrix.
    """
    n = len(matrix)

    # Step 1: Rotate the matrix by 90 degrees clockwise
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n - 1 - i] = matrix[i][j]

    # Step 2: Replace each element with the sum of its row and column elements (excluding itself)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            row_sum = sum(rotated[i]) - rotated[i][j]
            col_sum = sum(rotated[k][j] for k in range(n)) - rotated[i][j]
            result[i][j] = row_sum + col_sum

    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = rotate_and_multiply_matrix(matrix)
result

"""Q8. **Time Check**

You are given a dataset, dataset-1.csv, containing columns id, id_2, and timestamp (startDay, startTime, endDay, endTime). The goal is to verify the completeness of the time data by checking whether the timestamps for each unique (id, id_2) pair cover a full 24-hour period (from 12:00:00 AM to 11:59:59 PM) and span all 7 days of the week (from Monday to Sunday).

Create a function that accepts dataset-1.csv as a DataFrame and returns a boolean series that indicates if each (id, id_2) pair has incorrect timestamps. The boolean series must have multi-index (id, id_2).

"""

import pandas as pd

df = pd.read_csv('/content/dataset-1.csv')

df.head()

from datetime import datetime, timedelta

def time_check(df: pd.DataFrame) -> pd.Series:
    """
    Verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair
    cover a full 24-hour period for all 7 days of the week.

    Args:
        df (pd.DataFrame): DataFrame with columns 'id', 'id_2', 'startDay', 'startTime', 'endDay', 'endTime'

    Returns:
        pd.Series: A boolean series indicating whether each (id, id_2) pair has incomplete timestamps.
    """
    # Define the days of the week in order
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Helper function to convert day and time to a datetime object for easier comparison
    def convert_to_datetime(day, time):
        day_index = days_of_week.index(day)
        return datetime(2024, 1, day_index + 1) + timedelta(
            hours=int(time.split(":")[0]),
            minutes=int(time.split(":")[1]),
            seconds=int(time.split(":")[2])
        )

    # Group by (id, id_2) and check each group
    completeness_check = {}
    grouped = df.groupby(['id', 'id_2'])

    for (id_val, id2_val), group in grouped:
        # Create a set to track covered periods across all days of the week
        covered_intervals = {day: [] for day in days_of_week}

        # Record all time intervals in the week for the group
        for _, row in group.iterrows():
            start = convert_to_datetime(row['startDay'], row['startTime'])
            end = convert_to_datetime(row['endDay'], row['endTime'])

            current = start
            while current <= end:
                current_day = days_of_week[(current.weekday() + 1) % 7]
                covered_intervals[current_day].append((current.time(), end.time()))
                current += timedelta(days=1)

        # Check if each day covers the full 24 hours
        completeness_check[(id_val, id2_val)] = all(len(intervals) == 24 for intervals in covered_intervals.values())

    # Create a multi-index boolean series for the result
    return pd.Series(completeness_check)

# Call function and print results for dataset
time_check_result = time_check(df)
time_check_result