def count_upper_case(message):
    count  = 0
    for c in message:
        if c.isupper():
            count += 2 
        return  count
print(count_upper_case("Hello World"))
