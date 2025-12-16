import numpy

sentence = input("Enter a full sentence: \n")
sentence_words = sentence.split(" ")
set_result = set(sentence_words)
tuple_result = tuple(sorted(set_result))
array_result = numpy.array(tuple_result)

print(f"Original sentence: {sentence}")
print(f"Set of unique words: {set_result}")
print(f"Alphabetically sorted tuple: {tuple_result}")
print(f"NumPy array of words: {array_result}")