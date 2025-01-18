/**
 * Bloom Filter Implementation with Malicious URL Testing
 *
 * Author: Wilmer Leon
 * Contact: https://www.linkedin.com/in/wilmer-leon/
 *
 * Description:
 * This script implements a Bloom filter data structure for efficient set membership testing.
 * It provides tools for creating and managing Bloom filters with configurable size and false
 * positive rates, making it suitable for large-scale duplicate detection tasks. Includes
 * functionality for testing with simulated malicious URLs.
 *
 * Usage:
 * Run the script with the following command:
 *     mvn exec:java -Dexec.mainClass="org.example.BloomFilterExample"
 *
 * Operations:
 *  This program does not take any operations, it just performs the creation, population, serialization and
 *  testing.
 *
 * Dependencies:
 * - Java 11 or higher
 * - Google Guava library (included via Maven in pom.xml)
 */
package io.systemdesignlabs;

import com.google.common.hash.BloomFilter;
import com.google.common.hash.Funnels;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

public class BloomFilterExample {

    private static final int NUM_ENTRIES = 10_000_000; // Using underscores for readability
    private static final double FALSE_POSITIVE_PROBABILITY = 0.01;
    private static final String BLOOM_FILTER_FILE = "bloomfilter.bin";

    public static void main(String[] args) {
        System.out.println("-------------------------------------------------------------------");
        System.out.println("This program will:");
        System.out.println("1. Create a Bloom filter with " + NUM_ENTRIES + " expected entries.");
        System.out.println("2. Populate the Bloom filter with synthetic elements.");
        System.out.println("3. Serialize the Bloom filter to disk.");
        System.out.println("4. Test the Bloom filter for membership and check for false positives.");
        System.out.println("-------------------------------------------------------------------");
        System.out.println("Starting Bloom Filter Example...");


        // 1. Create Bloom Filter
        BloomFilter<String> filter = createBloomFilter();
        System.out.println("Bloom filter created.");

        // 2. Add Elements
        populateBloomFilter(filter);
        System.out.println("Bloom filter populated with " + NUM_ENTRIES + " elements.");

        // 3. Serialize to disk
        serializeBloomFilter(filter);
        System.out.println("Bloom filter serialized to: " + BLOOM_FILTER_FILE);

        // 4. Test for Membership
        testMembership(filter);

        System.out.println("Bloom Filter Example Complete.");
    }

    /**
     * Creates a Bloom filter with specified parameters.
     *
     * @return A newly created BloomFilter.
     */
    private static BloomFilter<String> createBloomFilter() {
        return BloomFilter.create(
                Funnels.stringFunnel(StandardCharsets.UTF_8),
                NUM_ENTRIES,
                FALSE_POSITIVE_PROBABILITY
        );
    }

    /**
     * Populates the given Bloom filter with elements.
     * @param filter The Bloom filter to be populated.
     */
    private static void populateBloomFilter(BloomFilter<String> filter) {
        for (int i = 1; i <= NUM_ENTRIES; i++) {
            filter.put("element" + i);
        }
    }


    /**
     * Serializes the Bloom filter to the disk.
     * @param filter The Bloom filter to be serialized.
     */
    private static void serializeBloomFilter(BloomFilter<String> filter) {
        try (FileOutputStream fileOutputStream = new FileOutputStream(BLOOM_FILTER_FILE)) {
            filter.writeTo(fileOutputStream);
        } catch (IOException e) {
            System.err.println("Error serializing Bloom filter: " + e.getMessage());
        }
    }

    /**
     * Tests membership of elements in the Bloom filter, including checking for false positives.
     * @param filter The Bloom filter to test.
     */
    private static void testMembership(BloomFilter<String> filter) {
        System.out.println("Testing membership...");

        // Known positive cases
        System.out.println("Contains 'element1': " + filter.mightContain("element1"));
        System.out.println("Contains 'element2': " + filter.mightContain("element2"));

        // Known negative case
        System.out.println("Contains 'element0': " + filter.mightContain("element0"));

        // Checking for false positives
        int tries = 0;
        int numFalsePositives = 0;
        final int MAX_TRIES = 1_000_000;
        while (tries < MAX_TRIES) {
            if (filter.mightContain("element10000000" + tries)) {
                numFalsePositives++;
                if(tries < 10){
                    System.out.println("False positive at: element10000000" + tries);
                }
            }
            tries++;
        }
        System.out.println("Total False positives: " + numFalsePositives + " out of "+ MAX_TRIES + " checks.");
        System.out.println("Note: Bloom filters are probabilistic structures; 'mightContain()' can return true for elements not added (false positives).");
    }
}