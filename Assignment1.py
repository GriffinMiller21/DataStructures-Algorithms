# Title: Assignment 1
# Date: 18 Feburary 2024
# Author: Griffin M. (100715751)
# Description: This assignment will help us navigate the 
# use of algorithms to sort out large inventory and be able
# to modify the current records.

import time

# Open the file in read mode
product_data = "product_data.txt"

# Loading and Storing that data into a linked list.
try:
    with open(product_data, 'r') as file:
        # Read all lines from the file and store them in a list
        product_list = file.read().splitlines()

except FileNotFoundError:
    print(f"The file '{product_data}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Creating a class to hold all methods and sorting algorithm
class Manage_products:
    def __init__(self, new_product_list=product_list):
        if new_product_list is None:
            new_product_list = []
        self.products = new_product_list

    # Method for inserting an item
    def insert_item(self, index, item):
        #Inserts the specified item at the specified index
        if len(item) == 4:
            self.products.insert(index, item)
        else:
            print("Invalid item structure. Item should have 4 attributes.")

    # Method for deleting an item
    def delete_item(self, index):
        #Deletes the item at the specified index from the list
        if 0 <= index:
            del self.products[index]
        else:
            print(f"Index {index} is out of range.")
    
    # Method for updating an item
    def update_item(self, index, new_item):
        #Updates the item at the specified index with a new value
        if 0 <= index < len(self.products) and len(new_item) == 4:
            self.products[index] = new_item
        else:
            print(f"Index {index} is out of range or invalid item structure.")

    # Method for findind an item by the index number
    def search_item(self, index):
        #Searches for the item at the specified index in the list
        if 0 <= index < len(self.products):
            return f"Item at index {index}: {self.products[index]}"
        else:
            return f"Index {index} is out of range."

    # Method for displaying the list
    def display_list(self):
        #Displays the current state of the list
        print(self.products)

    # The bubble sort algorithm being used
    def bubble_sort(self):
        """Sorts the list using the bubble sort algorithm."""
        n = len(self.products)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                # Compare based on the second attribute (assuming it's a string)
                if self.products[j][1] > self.products[j + 1][1]:
                    # Swap the elements if they are in the wrong order
                    self.products[j], self.products[j + 1] = self.products[j + 1], self.products[j]

    # Saving the modified data to an output text file
    def save_to_txt(self, file_path):
        #saves the list to a text file."""
        with open(file_path, 'w') as file:
            for item in self.products:
                # Convert each item to a string and write to the file
                file.write(f"{str(item)}\n")

# Running the methods and displaying the outputs
if __name__ == "__main__":
    product_manager = Manage_products()

    # Insert new product
    new_product = 101, "lightswitch", 29.99, "Electronics"
    product_manager.insert_item(1, new_product)
    print("The new product inserted is: ", new_product)

    # Update product
    old_item = product_manager.search_item(5)
    update_item = 101, "zooyork", 39.99, "Clothing"
    product_manager.update_item(5, update_item)
    new_item = product_manager.search_item(5)
    print(old_item, "has been updated to", new_item)

    # Delete product
    result = product_manager.search_item(2)
    product_manager.delete_item(2)
    print(result, "has been deleted")

    # Search product
    result = product_manager.search_item(2)
    print(result)

    # Bubble Sort
    start_time = time.time()
    product_manager.bubble_sort()
    end_time = time.time()
    print("Bubble Sort Time:", end_time - start_time)

    # Save the sorted list to a text file
    file_path = "sorted_products.txt"
    product_manager.save_to_txt(file_path)
    print(f"\nList saved to {file_path}")   