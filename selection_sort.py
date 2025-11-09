# Selection Sort - Simple Comparison-Based Sorting Algorithm
# Find minimum element and swap it to the front, repeat for remaining array

def selection_sort(arr):
    """
    Selection Sort Algorithm Implementation
    
    ALGORITHM: Divide array into sorted and unsorted portions
    1. Find minimum element in unsorted portion
    2. Swap it with first element of unsorted portion
    3. Move boundary between sorted and unsorted portions
    4. Repeat until entire array is sorted
    
    Time Complexity: O(n²) - always, regardless of input
    Space Complexity: O(1) - in-place sorting
    """
    n = len(arr)  # Get array length
    
    # Outer loop: iterate through each position to be filled
    # i represents the boundary between sorted [0...i-1] and unsorted [i...n-1] portions
    for i in range(n):
        # Step 1: Find minimum element in unsorted portion [i...n-1]
        min_index = i  # Assume current element is minimum
        
        # Inner loop: scan remaining unsorted elements to find actual minimum
        for j in range(i + 1, n):
            # Compare current element with assumed minimum
            if arr[j] < arr[min_index]:
                min_index = j  # Update minimum index if smaller element found
        
        # Step 2: Swap minimum element with first element of unsorted portion
        # This places minimum element in its correct sorted position
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
        # After swap: [0...i] is sorted, [i+1...n-1] is unsorted
        # Sorted portion grows by 1, unsorted portion shrinks by 1
    
    return arr

# Demonstration with step-by-step execution
def selection_sort_verbose(arr):
    """Selection sort with detailed step-by-step output for learning"""
    print(f"Initial array: {arr}")
    print("=" * 50)
    
    n = len(arr)
    
    for i in range(n):
        min_index = i
        print(f"\nStep {i+1}: Finding minimum in unsorted portion {arr[i:]}")
        
        # Find minimum in unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                print(f"  New minimum found: {arr[j]} at index {j}")
        
        # Perform swap if necessary
        if min_index != i:
            print(f"  Swapping {arr[i]} (index {i}) with {arr[min_index]} (index {min_index})")
            arr[i], arr[min_index] = arr[min_index], arr[i]
        else:
            print(f"  {arr[i]} is already in correct position")
        
        print(f"  Array after step {i+1}: {arr}")
        print(f"  Sorted portion: {arr[:i+1]}, Unsorted portion: {arr[i+1:]}")
    
    print(f"\nFinal sorted array: {arr}")
    return arr

# Example usage with multiple test cases
print("SELECTION SORT ALGORITHM DEMONSTRATION")
print("=" * 60)

# Test Case 1: Random array
print("\n🔸 TEST CASE 1: Random Array")
arr1 = [64, 25, 12, 22, 11]
print("Original array:", arr1)
sorted_arr1 = selection_sort(arr1.copy())
print("Sorted array:  ", sorted_arr1)

# Test Case 2: Already sorted array (best case)
print("\n🔸 TEST CASE 2: Already Sorted Array (Best Case)")
arr2 = [1, 2, 3, 4, 5]
print("Original array:", arr2)
sorted_arr2 = selection_sort(arr2.copy())
print("Sorted array:  ", sorted_arr2)

# Test Case 3: Reverse sorted array (worst case)
print("\n🔸 TEST CASE 3: Reverse Sorted Array (Worst Case)")
arr3 = [5, 4, 3, 2, 1]
print("Original array:", arr3)
sorted_arr3 = selection_sort(arr3.copy())
print("Sorted array:  ", sorted_arr3)

# Test Case 4: Array with duplicates
print("\n🔸 TEST CASE 4: Array with Duplicates")
arr4 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print("Original array:", arr4)
sorted_arr4 = selection_sort(arr4.copy())
print("Sorted array:  ", sorted_arr4)

# Verbose demonstration for educational purposes
print("\n" + "=" * 60)
print("STEP-BY-STEP EXECUTION TRACE")
print("=" * 60)
arr_demo = [64, 25, 12, 22, 11]
selection_sort_verbose(arr_demo)

# ============================================================================
# DETAILED ALGORITHM EXPLANATION
# ============================================================================

"""
SELECTION SORT ALGORITHM STEP-BY-STEP:

CONCEPT: Repeatedly select the minimum element from unsorted portion 
and place it at the beginning of unsorted portion

VISUALIZATION:
Initial: [64, 25, 12, 22, 11]
         |--- unsorted portion ---|

Step 1: Find min(64,25,12,22,11) = 11, swap with position 0
        [11, 25, 12, 22, 64]
         ^    |-- unsorted --|
        sorted

Step 2: Find min(25,12,22,64) = 12, swap with position 1  
        [11, 12, 25, 22, 64]
         ^    ^   |-- unsorted --|
           sorted

Step 3: Find min(25,22,64) = 22, swap with position 2
        [11, 12, 22, 25, 64]
         ^    ^    ^   |unsorted|
              sorted

Step 4: Find min(25,64) = 25, already in position 3
        [11, 12, 22, 25, 64]
         ^    ^    ^    ^   |u|
                 sorted

Step 5: Only one element left, automatically sorted
        [11, 12, 22, 25, 64]
         ^    ^    ^    ^    ^
                 sorted

INVARIANT: After i iterations, first i elements are in their final sorted positions

KEY CHARACTERISTICS:
✓ Simple to understand and implement
✓ In-place sorting (O(1) extra space)
✓ Performs well on small datasets
✓ Number of swaps is minimal: at most n-1 swaps
✗ Always O(n²) time, even for sorted input
✗ Not stable (equal elements may change relative order)
✗ Not adaptive (doesn't perform better on partially sorted data)
"""

# ============================================================================
# COMPREHENSIVE VIVA QUESTIONS AND ANSWERS
# ============================================================================

"""
🎯 BASIC LEVEL QUESTIONS:

Q1: How does Selection Sort work?
A1: Selection Sort divides array into sorted and unsorted portions:
    1. Find minimum element in unsorted portion
    2. Swap it with first element of unsorted portion  
    3. Expand sorted portion by 1, shrink unsorted portion by 1
    4. Repeat until entire array is sorted

Q2: What is the time complexity of Selection Sort?
A2: O(n²) in all cases (best, average, worst)
    - Outer loop runs n times
    - Inner loop runs (n-1) + (n-2) + ... + 1 = n(n-1)/2 times
    - Total comparisons: always n(n-1)/2, regardless of input

Q3: What is the space complexity of Selection Sort?
A3: O(1) - constant extra space
    - Only uses a few variables (min_index, temp for swapping)
    - Sorts in-place without additional arrays
    - Space usage doesn't depend on input size

🎯 INTERMEDIATE LEVEL QUESTIONS:

Q4: Is Selection Sort stable? Why or why not?
A4: No, Selection Sort is NOT stable
    - Equal elements may change their relative order during swapping
    - Example: [2a, 1, 2b] → [1, 2b, 2a] (2b comes before 2a after sorting)
    - Long-distance swaps can move equal elements past each other

Q5: How many swaps does Selection Sort perform?
A5: At most (n-1) swaps, which is optimal among comparison-based sorts
    - Each iteration swaps at most once (when min element isn't already in position)
    - This makes it useful when swap operations are expensive
    - Contrast with Bubble Sort which can perform O(n²) swaps

Q6: When would you choose Selection Sort over other algorithms?
A6: Use Selection Sort when:
    - Array size is very small (≤10-20 elements)
    - Swapping is expensive (minimizes number of swaps)
    - Simplicity is more important than efficiency
    - Memory is extremely limited (O(1) space complexity)

🎯 ADVANCED LEVEL QUESTIONS:

Q7: Compare Selection Sort with Insertion Sort and Bubble Sort?
A7: 
    Selection Sort:
    ✓ Minimal swaps: O(n)
    ✗ Always O(n²) comparisons
    ✗ Not adaptive or stable
    
    Insertion Sort:
    ✓ Adaptive: O(n) for nearly sorted data
    ✓ Stable and online
    ✗ More swaps: O(n²) in worst case
    
    Bubble Sort:
    ✓ Adaptive: can terminate early
    ✓ Stable
    ✗ Maximum swaps: O(n²)

Q8: Can Selection Sort be made stable? How?
A8: Yes, but at the cost of additional space or time:
    - Instead of swapping, shift elements and insert minimum at correct position
    - Use additional array to maintain original order of equal elements
    - Modified algorithm would be O(n²) time, O(n) space or O(n³) time, O(1) space

Q9: What is the minimum number of comparisons Selection Sort needs?
A9: Always exactly n(n-1)/2 comparisons
    - Cannot be reduced because algorithm must examine every element
    - Even if array is sorted, algorithm doesn't know without checking
    - Not adaptive - doesn't take advantage of existing order

Q10: How would you optimize Selection Sort?
A10: Several optimizations possible:
     - Bidirectional Selection Sort: find both min and max in each pass
     - Early termination: stop when remaining portion is sorted
     - Hybrid approach: switch to Insertion Sort for small subarrays
     - However, asymptotic complexity remains O(n²)

🎯 IMPLEMENTATION QUESTIONS:

Q11: Implement Selection Sort to sort in descending order?
A11: Change comparison condition:
     if arr[j] > arr[max_index]:  # Find maximum instead of minimum
         max_index = j
     Rest of algorithm remains same

Q12: How to make Selection Sort work with custom comparison function?
A12: Add comparison function parameter:
     def selection_sort(arr, compare_func):
         # Replace arr[j] < arr[min_index] with:
         if compare_func(arr[j], arr[min_index]):
             min_index = j

Q13: Implement Selection Sort recursively?
A13: def recursive_selection_sort(arr, start=0):
         if start >= len(arr) - 1:
             return
         min_idx = find_min_index(arr, start)
         arr[start], arr[min_idx] = arr[min_idx], arr[start]
         recursive_selection_sort(arr, start + 1)

Q14: How to count number of comparisons and swaps?
A14: Add counters as global variables or return them:
     comparisons = 0
     swaps = 0
     # Increment counters in appropriate places
     # Return (sorted_array, comparisons, swaps)

Q15: Implement Selection Sort for linked lists?
A15: More complex due to pointer manipulation:
     - Cannot directly access elements by index
     - Need to traverse list to find minimum
     - Swapping requires careful pointer updates
     - Generally not recommended for linked lists
"""
