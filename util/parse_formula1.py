# Function to parse the formula and extract elements
def parse_formula1(formula):
    elements_list = []
    counts_list = []
    current_element = ""
    current_count = ""
    for char in formula:
        if (
            char.isdigit() or char == "."
        ):  # if character is a digit or a period
            current_count += char
        elif char.isupper():  # if character is uppercase letter
            if current_element:
                elements_list.append(current_element)
                counts_list.append(
                    float(current_count)
                    if current_count and current_count != "."
                    else 1
                )
                current_count = ""
            current_element = char
        elif char.islower():  # if character is lowercase letter
            current_element += char
    # Add the last element and count
    if current_element:
        elements_list.append(current_element)
        counts_list.append(
            float(current_count)
            if current_count and current_count != "."
            else 1
        )
    return elements_list, counts_list
