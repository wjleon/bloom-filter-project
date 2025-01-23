"""
Bloom Filter Implementation with Malicious URL Testing

Author: Wilmer Leon
Contact: https://www.linkedin.com/in/wilmer-leon/

Description:
This script implements a Bloom filter data structure for efficient set membership testing.
It provides tools for creating and managing Bloom filters with configurable size and false
positive rates, making it suitable for large-scale duplicate detection tasks. Includes
functionality for testing with simulated malicious URLs.

Usage:
Run the script directly:
    python bloom_filter_example.py

Operations:
 This program does not take any operations, it just performs the creation, population,
 serialization and testing.

Dependencies:
- Python 3.7 or higher
- pybloom_live library (install with pip)
"""
import sys
from pybloom_live import BloomFilter
import pickle
import os


NUM_ENTRIES = 10_000_000  # Using underscores for readability
FALSE_POSITIVE_PROBABILITY = 0.01
BLOOM_FILTER_FILE = "bloomfilter.bin"


def create_bloom_filter() -> BloomFilter:
    """
    Creates a Bloom filter with specified parameters.

    Returns:
        A newly created BloomFilter.
    """
    return BloomFilter(capacity=NUM_ENTRIES, error_rate=FALSE_POSITIVE_PROBABILITY)


def populate_bloom_filter(filter: BloomFilter):
    """
    Populates the given Bloom filter with elements.

    Args:
        filter: The Bloom filter to be populated.
    """
    for i in range(1, NUM_ENTRIES + 1):
        filter.add(f"element{i}")


def serialize_bloom_filter(filter: BloomFilter):
    """
    Serializes the Bloom filter to the disk using pickle.

    Args:
        filter: The Bloom filter to be serialized.
    """
    try:
        with open(BLOOM_FILTER_FILE, "wb") as file:
            pickle.dump(filter, file)
    except Exception as e:
        print(f"Error serializing Bloom filter: {e}", file=sys.stderr)


def test_membership(filter: BloomFilter):
    """
    Tests membership of elements in the Bloom filter, including checking for false positives.

    Args:
        filter: The Bloom filter to test.
    """
    print("Testing membership...")

    # Known positive cases
    print(f"Contains 'element1': {'element1' in filter}")
    print(f"Contains 'element2': {'element2' in filter}")

    # Known negative case
    print(f"Contains 'element0': {'element0' in filter}")

    # Checking for false positives
    tries = 0
    num_false_positives = 0
    MAX_TRIES = 1_000_000
    while tries < MAX_TRIES:
        test_element = f"element10000000{tries}"
        if test_element in filter:
            num_false_positives += 1
            if tries < 10:
                 print(f"False positive at: {test_element}")
        tries += 1

    print(f"Total False positives: {num_false_positives} out of {MAX_TRIES} checks.")
    print("Note: Bloom filters are probabilistic structures; 'in' operator can return true for elements not added (false positives).")


def main():
    print("-------------------------------------------------------------------")
    print("This program will:")
    print(f"1. Create a Bloom filter with {NUM_ENTRIES} expected entries.")
    print("2. Populate the Bloom filter with synthetic elements.")
    print("3. Serialize the Bloom filter to disk.")
    print("4. Test the Bloom filter for membership and check for false positives.")
    print("-------------------------------------------------------------------")
    print("Starting Bloom Filter Example...")

    # 1. Create Bloom Filter
    filter = create_bloom_filter()
    print("Bloom filter created.")

    # 2. Add Elements
    populate_bloom_filter(filter)
    print(f"Bloom filter populated with {NUM_ENTRIES} elements.")

    # 3. Serialize to disk
    serialize_bloom_filter(filter)
    print(f"Bloom filter serialized to: {BLOOM_FILTER_FILE}")

    # 4. Test for Membership
    test_membership(filter)

    print("Bloom Filter Example Complete.")

if __name__ == "__main__":
    main()