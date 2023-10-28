# Finding whether two arrays contains the same elements

properties_list_1 = ["a", "b", "c", "d", "e"]
properties_list_2 = ["f", "g", "w", "i", "h"]

# using nested loops
def is_list_contain_duplicates(arr1, arr2):
    for item in arr1:
        for nested_item in arr2:
            if item == nested_item:
                return True
    return False
# O(a * b) Time complexity 
# O(1)      Space complexity

#Using map
map_values = {}
def is_list_contain_duplicates_1(arr1, arr2):
    for item in arr1:
        if item not in map_values:
            map_values[item] = True
    
    for nested_item in arr2:
        if nested_item in map_values:
            return map_values[nested_item]
    return False

# O(a + b) when comes to the time complexity => good
# O(a) Space complexity bad => creating a objet

print(is_list_contain_duplicates_1(properties_list_1, properties_list_2))