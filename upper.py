def count_upper_case(message):
    return sum([ 1 for n in message if n.isupper()])
    
assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("AA") == 2, "Two upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("£$%%^") == 0, "Special characters"
assert count_upper_case("AAA") == 5, "3 upper case" 

print("All testes passed")