TEXT_TO_FIND = "old"

input_text = input()
first_occurrence_index = input_text.find(TEXT_TO_FIND)
last_occurrence_index = input_text.rfind(TEXT_TO_FIND)
print(max(first_occurrence_index, last_occurrence_index))
