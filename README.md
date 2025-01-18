# System Design Labs 2025
## Bloom Filter Implementation with Malicious URL Testing

### Author: 
Wilmer Leon

### Contact
[https://www.linkedin.com/in/wilmer-leon/](https://www.linkedin.com/in/wilmer-leon/)

### Blog
[https://medium.com/@wjleon](https://medium.com/@wjleon)

## Description

This script implements a Bloom filter data structure for efficient set membership testing. 
It provides tools for creating and managing Bloom filters with configurable size and false positive rates, making it suitable for large-scale duplicate detection tasks. While the title mentions "Malicious URL Testing," this implementation primarily focuses on demonstrating the core functionality of a Bloom filter. The "malicious URL" testing is simulated by testing for non-existent elements and measuring the false positive rate.

## Usage

To run this script:

1.  Ensure you have Java 11 or higher installed.
2.  Make sure you have Maven installed to manage dependencies.
3.  Clone or download this repository.
4.  Navigate to the root directory of the project in your terminal.
5.  Execute the following Maven command:

    ```bash
    mvn exec:java -Dexec.mainClass="io.systemdesignlabs.BloomFilterExample"
    ```

## Operations

This program does not take any command-line arguments or user inputs. It performs the following operations automatically:

1.  **Creates a Bloom filter:** It initializes a Bloom filter with a specified number of expected entries and a desired false positive probability.
2.  **Populates the Bloom filter:** The filter is populated with a large number of synthetic elements.
3.  **Serializes the Bloom filter:** The filter is then saved to disk as a binary file for potential reuse.
4.  **Tests for membership:** The program checks if specific elements are members of the filter and simulates checks for false positives.

## Dependencies

*   **Java 11 or higher**
*   **Google Guava library:** Included via Maven in the `pom.xml` file.

## Details

The program executes the following steps:

1.  **Creation:** A Bloom filter is created with a capacity of 10,000,000 entries and a false positive probability of 1%.
2.  **Population:** The filter is populated with 10 million unique string elements in the form "element1", "element2", ..., "element10000000".
3.  **Serialization:** The populated Bloom filter is serialized to a file named `bloomfilter.bin`.
4.  **Membership testing:**
    *   It tests for the presence of elements known to be added to the filter (e.g., "element1", "element2"), demonstrating correct positive lookups.
    *   It tests for the presence of a non-existent element "element0", demonstrating negative lookups
    *   It then tests with a large amount of non-existent elements to simulate false positives, reporting the total number of false positives found out of 1,000,000 checks and gives some specific cases.

## Output

The program outputs information to the console, including:

*   The parameters of the created Bloom filter.
*   Confirmation messages for each operation performed (creation, population, serialization).
*   The results of membership tests.
*   The number of false positives encountered.
*   A note explaining that a Bloom filter is a probabilistic structure and that false positives are to be expected.

## Note

Bloom filters are probabilistic data structures; they may return true positives or false positives, but never false negatives. The false positive rate can be configured to the desired level by changing the initialization parameters of the filter.

This implementation is a simplified example aimed at educational purposes and should not be used in high-security applications without further scrutiny.
content_copy
download
Use code with caution.
Markdown