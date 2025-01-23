import os
from pybloom_live import BloomFilter
from typing import Optional

# Constants
NUM_ENTRIES = 10_000_000  # Number of expected entries
FALSE_POSITIVE_PROBABILITY = 0.01  # Desired false positive probability
BLOOM_FILTER_FILE = "bloomfilter.bin"  # File to serialize the Bloom filter


def create_bloom_filter() -> BloomFilter:
    """
    Creates a Bloom filter with the specified parameters.

    Returns:
        BloomFilter: A newly created Bloom filter.
    """
    return BloomFilter(NUM_ENTRIES, FALSE_POSITIVE_PROBABILITY)


def populate_bloom_filter(filter: BloomFilter) -> None:
    """
    Populates the given Bloom filter with synthetic elements.

    Args:
        filter (BloomFilter): The Bloom filter to populate.
    """
    for i in range(1, NUM_ENTRIES + 1):
        filter.add(f"element{i}")


def serialize_bloom_filter(filter: BloomFilter, file_path: str = BLOOM_FILTER_FILE) -> None:
    """
    Serializes the Bloom filter to disk.

    Args:
        filter (BloomFilter): The Bloom filter to serialize.
        file_path (str): The file path to save the Bloom filter.
    """
    try:
        with open(file_path, "wb") as file:
            filter.tofile(file)
        print(f"Bloom filter serialized to: {file_path}")
    except IOError as e:
        print(f"Error serializing Bloom filter: {e}")


def deserialize_bloom_filter(file_path: str = BLOOM_FILTER_FILE) -> Optional[BloomFilter]:
    """
    Deserializes a Bloom filter from disk.

    Args:
        file_path (str): The file path to load the Bloom filter from.

    Returns:
        Optional[BloomFilter]: The deserialized Bloom filter, or None if an error occurs.
    """
    try:
        with open(file_path, "rb") as file:
            return BloomFilter.fromfile(file)
    except IOError as e:
        print(f"Error deserializing Bloom filter: {e}")
        return None


def test_membership(filter: BloomFilter) -> None:
    """
    Tests membership of elements in the Bloom filter, including checking for false positives.

    Args:
        filter (BloomFilter): The Bloom filter to test.
    """
    print("Testing membership...")

    # Known positive cases
    print(f"Contains 'element1': {f'element1' in filter}")
    print(f"Contains 'element2': {f'element2' in filter}")

    # Known negative case
    print(f"Contains 'element0': {f'element0' in filter}")

    # Checking for false positives
    tries = 0
    num_false_positives = 0
    MAX_TRIES = 1_000_000

    while tries < MAX_TRIES:
        if f"element10000000{tries}" in filter:
            num_false_positives += 1
            if tries < 10:
                print(f"False positive at: element10000000{tries}")
        tries += 1

    print(f"Total False positives: {num_false_positives} out of {MAX_TRIES} checks.")
    print("Note: Bloom filters are probabilistic structures; 'in' can return True for elements not added (false positives).")


def main() -> None:
    """
    Main function to demonstrate Bloom filter creation, population, serialization, and testing.
    """
    print("-------------------------------------------------------------------")
    print("This program will:")
    print(f"1. Create a Bloom filter with {NUM_ENTRIES} expected entries.")
    print("2. Populate the Bloom filter with synthetic elements.")
    print("3. Serialize the Bloom filter to disk.")
    print("4. Test the Bloom filter for membership and check for false positives.")
    print("-------------------------------------------------------------------")
    print("Starting Bloom Filter Example...")

    # 1. Create Bloom Filter
    bloom_filter = create_bloom_filter()
    print("Bloom filter created.")

    # 2. Add Elements
    populate_bloom_filter(bloom_filter)
    print(f"Bloom filter populated with {NUM_ENTRIES} elements.")

    # 3. Serialize to disk
    serialize_bloom_filter(bloom_filter)

    # 4. Test for Membership
    test_membership(bloom_filter)

    print("Bloom Filter Example Complete.")


if __name__ == "__main__":
    main()