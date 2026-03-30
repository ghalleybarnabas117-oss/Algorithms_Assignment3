"""
Search Assignment Starter Code
Implement three search algorithms and benchmark their performance.
"""

import json
import time
import random


# ============================================================================
# PART 1: Linear Search
# ============================================================================

def linear_search(data, target):
    """
    Search for target in data using linear search.
    
    Linear search checks each element sequentially until finding the target
    or reaching the end of the list.
    
    Args:
        data (list): List to search (can be sorted or unsorted)
        target: Item to find
    
    Returns:
        int: Index of target if found, -1 if not found
    
    Time Complexity: O(n) - must check up to n elements
    Space Complexity: O(1) - uses constant extra space
    
    Example:
        linear_search([5, 2, 8, 1, 9], 8) returns 2
        linear_search([5, 2, 8, 1, 9], 7) returns -1
    """
    # TODO: Implement linear search that loops through each element and returns its index if found and -1 if not found.
    
    # pass # Delete pass and write your code here
def linear_search(data, target):
    """
    Search for target in data using linear search.
    """
    for i in range(len(data)):
        if data[i] == target:
            return i  # Found it!
    return -1  # Not found   


# ============================================================================
# PART 2: Binary Search (Iterative)
# ============================================================================

def binary_search_iterative(data, target):
    """
    Search for target in SORTED data using iterative binary search.
    
    Binary search repeatedly divides the search space in half by comparing
    the target to the middle element.
    
    Args:
        data (list): SORTED list to search
        target: Item to find
    
    Returns:
        int: Index of target if found, -1 if not found
    
    Time Complexity: O(log n) - divides search space in half each iteration
    Space Complexity: O(1) - uses constant extra space
    
    IMPORTANT: This only works on SORTED data!
    
    Example:
        binary_search_iterative([1, 2, 5, 8, 9], 8) returns 3
        binary_search_iterative([1, 2, 5, 8, 9], 7) returns -1
    """
    # TODO: Implement iterative binary search that uses iteration to find the target. Return the index if found and -1 if not found.
    
    # pass # Delete pass and write your code here
def binary_search_iterative(data, target):
    """
    Search for target in SORTED data using iterative binary search.
    """
    left = 0
    right = len(data) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if data[mid] == target:
            return mid  # Found it
        elif data[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
    
    return -1  # Not found    


# ============================================================================
# PART 3: Binary Search (Recursive)
# ============================================================================

def binary_search_recursive(data, target, left=None, right=None):
    """
    Search for target in SORTED data using recursive binary search.
    
    This is the recursive version of binary search, which naturally expresses
    the divide-and-conquer approach.
    
    Args:
        data (list): SORTED list to search
        target: Item to find
        left (int): Left boundary of search space (defaults to 0)
        right (int): Right boundary of search space (defaults to len(data)-1)
    
    Returns:
        int: Index of target if found, -1 if not found
    
    Time Complexity: O(log n)
    Space Complexity: O(log n) - recursion call stack
    
    Example:
        binary_search_recursive([1, 2, 5, 8, 9], 8) returns 3
    """
    # Handle default parameters on first call
    if left is None:
        left = 0
    if right is None:
        right = len(data) - 1
    
    # TODO: Implement recursive binary search that uses recursion to find the target. Return the index if found and -1 if not found. Note that default parameters are already handled above.

    
    # pass # Delete pass and write your code here
def binary_search_recursive(data, target, left=None, right=None):
    """
    Search for target in SORTED data using recursive binary search.
    """
    if left is None:
        left = 0
    if right is None:
        right = len(data) - 1
    
    # Base case: empty search space
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if data[mid] == target:
        return mid  # Found target
    elif data[mid] < target:
        return binary_search_recursive(data, target, mid + 1, right)  # Right half
    else:
        return binary_search_recursive(data, target, left, mid - 1)  # Left half

    


# ============================================================================
# BENCHMARKING & TESTING
# ============================================================================

def load_dataset(filename):
    """Load a dataset from JSON file."""
    with open(f"datasets/{filename}", "r") as f:
        return json.load(f)


def load_test_cases():
    """Load test cases for validation."""
    with open("datasets/test_cases.json", "r") as f:
        return json.load(f)


def test_search_correctness():
    """Test that search functions work correctly."""
    print("= - starter_code.py:178"*70)
    print("TESTING SEARCH CORRECTNESS - starter_code.py:179")
    print("= - starter_code.py:180"*70 + "\n")
    
    # Simple test data
    sorted_data = [1, 3, 5, 7, 9, 11, 13, 15]
    unsorted_data = [7, 2, 9, 1, 5, 13, 3, 11]
    
    print("Test 1: Linear search on unsorted data - starter_code.py:186")
    result = linear_search(unsorted_data, 9)
    print(f"linear_search({unsorted_data}, 9) = {result} - starter_code.py:188")
    print(f"Expected: 2, Got: {result}, {'✓ PASS' if result == 2 else '✗ FAIL'} - starter_code.py:189")
    
    print("\nTest 2: Linear search  item not found - starter_code.py:191")
    result = linear_search(unsorted_data, 99)
    print(f"linear_search({unsorted_data}, 99) = {result} - starter_code.py:193")
    print(f"Expected: 1, Got: {result}, {'✓ PASS' if result == 1 else '✗ FAIL'} - starter_code.py:194")
    
    print("\nTest 3: Binary search iterative on sorted data - starter_code.py:196")
    result = binary_search_iterative(sorted_data, 9)
    print(f"binary_search_iterative({sorted_data}, 9) = {result} - starter_code.py:198")
    print(f"Expected: 4, Got: {result}, {'✓ PASS' if result == 4 else '✗ FAIL'} - starter_code.py:199")
    
    print("\nTest 4: Binary search iterative  item not found - starter_code.py:201")
    result = binary_search_iterative(sorted_data, 10)
    print(f"binary_search_iterative({sorted_data}, 10) = {result} - starter_code.py:203")
    print(f"Expected: 1, Got: {result}, {'✓ PASS' if result == 1 else '✗ FAIL'} - starter_code.py:204")
    
    print("\nTest 5: Binary search recursive on sorted data - starter_code.py:206")
    result = binary_search_recursive(sorted_data, 13)
    print(f"binary_search_recursive({sorted_data}, 13) = {result} - starter_code.py:208")
    print(f"Expected: 6, Got: {result}, {'✓ PASS' if result == 6 else '✗ FAIL'} - starter_code.py:209")
    
    print("\nTest 6: Binary search recursive  item not found - starter_code.py:211")
    result = binary_search_recursive(sorted_data, 8)
    print(f"binary_search_recursive({sorted_data}, 8) = {result} - starter_code.py:213")
    print(f"Expected: 1, Got: {result}, {'✓ PASS' if result == 1 else '✗ FAIL'} - starter_code.py:214")


def benchmark_algorithm(search_func, data, targets):
    """
    Benchmark a search algorithm on given data with multiple targets.
    
    Args:
        search_func: The search function to test
        data: The dataset to search
        targets: List of items to search for
    
    Returns:
        float: Average time per search in seconds
    """
    start = time.time()
    
    for target in targets:
        search_func(data, target)
    
    end = time.time()
    return (end - start) / len(targets)


def benchmark_all_datasets():
    """Benchmark all search algorithms on all datasets."""
    print("\n - starter_code.py:240" + "="*70)
    print("BENCHMARKING SEARCH ALGORITHMS - starter_code.py:241")
    print("= - starter_code.py:242"*70 + "\n")
    
    datasets = {
        "customer_ids.json": "Unsorted Customer IDs (100K)",
        "product_catalog.json": "Pre-sorted Product Catalog (50K)",
        "config_settings.json": "Small Config Settings (500)",
        "dictionary_words.json": "Dictionary Words (10K)"
    }
    
    test_cases = load_test_cases()
    
    for filename, description in datasets.items():
        print(f"Dataset: {description} - starter_code.py:254")
        print("" * 70)
        
        data = load_dataset(filename)
        dataset_key = filename.replace(".json", "")
        
        # Get targets to search for (mix of present and absent)
        targets = test_cases[dataset_key]["present"][:50] + test_cases[dataset_key]["absent"][:50]
        random.shuffle(targets)
        
        # Benchmark linear search
        linear_time = benchmark_algorithm(linear_search, data, targets)
        print(f"Linear Search:              {linear_time*1000:.4f} ms per search - starter_code.py:266")
        
        # For unsorted data, sort it first for binary search
        if "unsorted" in description.lower() or "small config" in description.lower():
            sorted_data = sorted(data)
            sort_start = time.time()
            sorted(data)
            sort_time = time.time() - sort_start
            print(f"Time to sort data:          {sort_time*1000:.2f} ms (onetime cost) - starter_code.py:274")
        else:
            sorted_data = data
            sort_time = 0
        
        # Benchmark binary search iterative
        binary_iter_time = benchmark_algorithm(binary_search_iterative, sorted_data, targets)
        print(f"Binary Search (Iterative):  {binary_iter_time*1000:.4f} ms per search - starter_code.py:281")
        
        # Benchmark binary search recursive
        binary_rec_time = benchmark_algorithm(binary_search_recursive, sorted_data, targets)
        print(f"Binary Search (Recursive):  {binary_rec_time*1000:.4f} ms per search - starter_code.py:285")
        
        # Calculate speedup
        if binary_iter_time > 0:
            speedup = linear_time / binary_iter_time
            print(f"Binary speedup:             {speedup:.2f}x faster than linear - starter_code.py:290")
        
        print()


def analyze_preprocessing_costs():
    """Analyze when sorting overhead is worth it."""
    print("= - starter_code.py:297"*70)
    print("PREPROCESSING COST ANALYSIS - starter_code.py:298")
    print("= - starter_code.py:299"*70 + "\n")
    
    # Use customer IDs dataset (unsorted, large)
    data = load_dataset("customer_ids.json")
    test_cases = load_test_cases()
    targets = test_cases["customer_ids"]["present"][:100]
    
    # Measure sort time
    sort_start = time.time()
    sorted_data = sorted(data)
    sort_time = time.time() - sort_start
    
    # Measure search times
    linear_time = benchmark_algorithm(linear_search, data, targets[:10])
    binary_time = benchmark_algorithm(binary_search_iterative, sorted_data, targets[:10])
    
    print(f"Dataset: Customer IDs (100,000 unsorted entries) - starter_code.py:315")
    print(f"Onetime sort cost: {sort_time*1000:.2f} ms - starter_code.py:316")
    print(f"Linear search time: {linear_time*1000:.4f} ms per search - starter_code.py:317")
    print(f"Binary search time: {binary_time*1000:.4f} ms per search - starter_code.py:318")
    print(f"Time saved per search: {(linear_time  -
          binary_time)*1000:.4f} ms\n")
    
    # Calculate break-even point
    time_saved_per_search = linear_time - binary_time
    if time_saved_per_search > 0:
        searches_to_break_even = sort_time / time_saved_per_search
        print(f"Breakeven point: {int(searches_to_break_even)} searches - starter_code.py:326")
        print(f"After {int(searches_to_break_even)} searches, sorting + binary search becomes faster\n - starter_code.py:327")


if __name__ == "__main__":
    print("SEARCH ASSIGNMENT  STARTER CODE - starter_code.py:331")
    print("Implement the search functions above, then run tests.\n - starter_code.py:332")
    
    # Uncomment these as you complete each part:
    
    # test_search_correctness()
    test_search_correctness()
    
    # benchmark_all_datasets()
    benchmark_all_datasets()
    
    # analyze_preprocessing_costs()
    analyze_preprocessing_costs()
    
    print("\n⚠ Uncomment the test functions in the main block to run benchmarks! - starter_code.py:345")