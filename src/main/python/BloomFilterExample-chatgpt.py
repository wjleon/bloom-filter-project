"""
Bloom Filter Implementation with Malicious URL Testing

Author: Wilmer Leon
Contact: https://www.linkedin.com/in/wilmer-leon/

Description:
This script implements a Bloom filter data structure for efficient set membership testing.
It provides tools for creating and managing Bloom filters with configurable size and false
positive rates, making it suitable for large-scale duplicate detection tasks. Includes
functionality for testing with simulated malicious URLs.

Dependencies:
- Python 3.7 or higher
- pybloom-live library (install using `pip install pybloom-live`)
"""

import pickle
from pybloom_live import BloomFilter


# Constants
NUM_ENTRIES = 10_000_000  # Expected number of elements in the filter
FALSE_POSITIVE_PROBABILITY = 0.01  # Desired false positive rate
BLOOM_FILTER_FILE = "bloomfilter.pkl"  # File for storing the serialized Bloom filter


def create_bloom_filter(num_entries, false_positive_rate):
    """
    Creates a Bloom filter with specified parameters.

    Args:
        num_entries (int): Expected number of elements in the Bloom filter.
        false_positive_rate (float): Desired false positive rate.

    Returns:
        BloomFilter: A newly created Bloom filter.
    """
    return BloomFilter(capacity=num_entries, error_rate=false_positive_rate)


def populate_bloom_filter(bloom_filter, num_entries):
    """
    Populates the Bloom filter with synthetic elements.

    Args:
        bloom_filter (BloomFilter): The Bloom filter to populate.
        num_entries (int): The number of elements to add.
    """
    for i in range(1, num_entries + 1):
        bloom_filter.add(f"element{i}")


def serialize_bloom_filter(bloom_filter, file_path):
    """
    Serializes the Bloom filter to disk.

    Args:
        bloom_filter (BloomFilter): The Bloom filter to serialize.
        file_path (str): The file path to save the serialized Bloom filter.
    """
    with open(file_path, "wb") as file:
        pickle.dump(bloom_filter, file)


def deserialize_bloom_filter(file_path):
    """
    Deserializes the Bloom filter from disk.

    Args:
        file_path (str): The file path to load the serialized Bloom filter.

    Returns:
        BloomFilter: The deserialized Bloom filter.
    """
    with open(file_path, "rb") as file:
        return pickle.load(file)


def test_membership(bloom_filter, max_tries=1_000_000):
    """
    Tests membership of elements in the Bloom filter, including false positive checks.

    Args:
        bloom_filter (BloomFilter): The Bloom filter to test.
        max_tries (int): The number of checks to perform for false positives.
    """
    print("Testing membership...")

    # Known positive cases
    print("Contains 'element1':", "element1" in bloom_filter)
    print("Contains 'element2':", "element2" in bloom_filter)

    # Known negative case
    print("Contains 'element0':", "element0" in bloom_filter)

    # False positive testing
    num_false_positives = 0
    for tries in range(max_tries):
        test_element = f"element10000000{tries}"
        if test_element in bloom_filter:
            num_false_positives += 1
            if tries < 10:
                print(f"False positive at: {test_element}")

    print(f"Total False Positives: {num_false_positives} out of {max_tries} checks.")
    print("Note: Bloom filters are probabilistic; false positives are expected.")


def main():
    """
    Main function to demonstrate the Bloom filter functionality.
    """
    print("-------------------------------------------------------------")
    print("This program will:")
    print("1. Create a Bloom filter with 10 million expected entries.")
    print("2. Populate the Bloom filter with synthetic elements.")
    print("3. Serialize the Bloom filter to disk.")
    print("4. Test the Bloom filter for membership and check for false positives.")
    print("-------------------------------------------------------------")
    print("Starting Bloom Filter Example...")

    # Create the Bloom filter
    bloom_filter = create_bloom_filter(NUM_ENTRIES, FALSE_POSITIVE_PROBABILITY)
    print("Bloom filter created.")

    # Populate the Bloom filter
    populate_bloom_filter(bloom_filter, NUM_ENTRIES)
    print(f"Bloom filter populated with {NUM_ENTRIES} elements.")

    # Serialize the Bloom filter to disk
    serialize_bloom_filter(bloom_filter, BLOOM_FILTER_FILE)
    print(f"Bloom filter serialized to: {BLOOM_FILTER_FILE}")

    # Test the Bloom filter for membership
    test_membership(bloom_filter)

    print("Bloom Filter Example Complete.")


if __name__ == "__main__":
    main()
