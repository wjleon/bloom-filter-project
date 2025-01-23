"""
Bloom Filter Implementation with Malicious URL Testing

Author: Wilmer Leon (Original Java Implementation)
Python Adaptation: Claude
Contact: https://www.linkedin.com/in/wilmer-leon/

Description:
This script implements a Bloom filter data structure for efficient set membership testing.
It provides tools for creating and managing Bloom filters with configurable size and false
positive rates, making it suitable for large-scale duplicate detection tasks. Includes
functionality for testing with simulated malicious URLs.

Usage:
Run the script with the following command:
    python bloom_filter_example.py

Operations:
This program does not take any operations, it just performs the creation, population, serialization and
testing.

Dependencies:
- Python 3.7 or higher
- pybloom_live package (install via: pip install pybloom_live)
"""

from pybloom_live import BloomFilter
import pickle
import sys
from typing import Optional

class BloomFilterExample:
    # Class constants
    NUM_ENTRIES = 10_000_000  # Using underscores for readability
    FALSE_POSITIVE_PROBABILITY = 0.01
    BLOOM_FILTER_FILE = "bloomfilter.bin"

    @staticmethod
    def create_bloom_filter() -> BloomFilter:
        """
        Creates a Bloom filter with specified parameters.

        Returns:
            BloomFilter: A newly created BloomFilter instance
        """
        return BloomFilter(capacity=BloomFilterExample.NUM_ENTRIES, 
                         error_rate=BloomFilterExample.FALSE_POSITIVE_PROBABILITY)

    @staticmethod
    def populate_bloom_filter(filter: BloomFilter) -> None:
        """
        Populates the given Bloom filter with elements.

        Args:
            filter (BloomFilter): The Bloom filter to be populated
        """
        for i in range(1, BloomFilterExample.NUM_ENTRIES + 1):
            filter.add(f"element{i}")

    @staticmethod
    def serialize_bloom_filter(filter: BloomFilter) -> None:
        """
        Serializes the Bloom filter to disk.

        Args:
            filter (BloomFilter): The Bloom filter to be serialized
        """
        try:
            with open(BloomFilterExample.BLOOM_FILTER_FILE, 'wb') as file_output:
                pickle.dump(filter, file_output)
        except IOError as e:
            print(f"Error serializing Bloom filter: {e}", file=sys.stderr)

    @staticmethod
    def test_membership(filter: BloomFilter) -> None:
        """
        Tests membership of elements in the Bloom filter, including checking for false positives.

        Args:
            filter (BloomFilter): The Bloom filter to test
        """
        print("Testing membership...")
        
        # Known positive cases
        print(f"Contains 'element1': {('element1' in filter)}")
        print(f"Contains 'element2': {('element2' in filter)}")
        
        # Known negative case
        print(f"Contains 'element0': {('element0' in filter)}")
        
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
        print("Note: Bloom filters are probabilistic structures; membership testing can return true for elements not added (false positives).")

def main():
    """Main execution function"""
    print("-------------------------------------------------------------------")
    print(f"This program will:")
    print(f"1. Create a Bloom filter with {BloomFilterExample.NUM_ENTRIES} expected entries.")
    print("2. Populate the Bloom filter with synthetic elements.")
    print("3. Serialize the Bloom filter to disk.")
    print("4. Test the Bloom filter for membership and check for false positives.")
    print("-------------------------------------------------------------------")
    print("Starting Bloom Filter Example...")

    # 1. Create Bloom Filter
    filter = BloomFilterExample.create_bloom_filter()
    print("Bloom filter created.")

    # 2. Add Elements
    BloomFilterExample.populate_bloom_filter(filter)
    print(f"Bloom filter populated with {BloomFilterExample.NUM_ENTRIES} elements.")

    # 3. Serialize to disk
    BloomFilterExample.serialize_bloom_filter(filter)
    print(f"Bloom filter serialized to: {BloomFilterExample.BLOOM_FILTER_FILE}")

    # 4. Test for Membership
    BloomFilterExample.test_membership(filter)
    print("Bloom Filter Example Complete.")

if __name__ == "__main__":
    main()