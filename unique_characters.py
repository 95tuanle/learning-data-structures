def has_unique_chars(data):
    unique_date = set(data)
    return len(unique_date) == len(data)


print(has_unique_chars("sample"))
print(has_unique_chars("hello world"))
print(has_unique_chars("linkedin"))
print(has_unique_chars("python"))
