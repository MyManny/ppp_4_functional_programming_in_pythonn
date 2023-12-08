unsorted_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sorted_list = sorted(unsorted_list, key=lambda x: x[1])

print("Unsorted list of tuples:", unsorted_list)
print("Sorted list of tuples:", sorted_list)

original_list = [3, 6, 9, 2]

cubed_list = list(map(lambda x: x**3, original_list))

print("Original list:", original_list)
print("List after lambda function:", cubed_list)


input_list = [3, 6, 9, 2]

even_odd_function = lambda x: x % 2 == 0

result_list = [even_odd_function(x) for x in input_list]

print("Input list:", input_list)
print("List after lambda function and list comprehension:", result_list)


numbers_list = [x for x in range(1, 101)]
print(numbers_list)

sentence = "The quick brown fox jumped over the fence."

word_length_dict = {word: len(word) for word in sentence.split()}
print(word_length_dict)
