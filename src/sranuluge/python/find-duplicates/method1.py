properties_list_1 = ["a", "b", "c", "d", "e"]
properties_list_2 = ["f", "g", "w", "i", "h"]

# using nested loops
def is_list_contain_duplicates_1(arr1, arr2):
    for item in arr1:
        for nested_item in arr2:
            if item == nested_item:
                return True
    return False
# O(a * b) Time complexity 
# O(1)      Space complexity

print(f'Method-01 {is_list_contain_duplicates_1(properties_list_1, properties_list_2)})')