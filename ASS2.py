# Title: Assignment 2
# Name: Griffin Miller
# Date: 24 March 2024

# Imports
import time
import random
import winsound

# Function to Merge Sort 
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            # Play a sound effect for each swap
            winsound.Beep(1000, 100)  

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Function to print each step of the sorting process
def print_steps(arr):
    for step in arr:
        print(step)
        # Delay between steps for visualization
        time.sleep(0.5)  

# Main function
if __name__ == "__main__":
    # Given array
    product_id = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]

    print("Original Array:")
    print(product_id)

    # Sorting processes
    print("\nMerge Sort:")
    merge_sort_steps = []
    # Initial step
    merge_sort_steps.append(list(product_id))  
    merge_sort(product_id)
    # Final step
    merge_sort_steps.append(list(product_id))  
    print_steps(merge_sort_steps)

    # Sorting process with random input
    print("\nMerge Sort Simulation:")
    # Example array of 10 random numbers
    arr = random.sample(range(1, 101), 10)  
    print("Original Array:", arr)
    merge_sort_steps = []
    # Initial step
    merge_sort_steps.append(list(arr))  
    merge_sort(arr)
    # Final step
    merge_sort_steps.append(list(arr))  
    print_steps(merge_sort_steps)
