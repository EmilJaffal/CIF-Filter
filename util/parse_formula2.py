# List of elements
elements = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K',
            'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb',
            'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs',
            'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta',
            'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa',
            'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt',
            'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
            
invalid_symbols = [char for char in set(''.join(elements)) if char.isalpha() and char.upper() not in elements and char != '.']

# Function to parse the formula and extract elements
def parse_formula2(formula):
    elements_list = []
    counts_list = []
    error = None  # Initialize variable to store the error message
    current_element = ''
    current_count = ''
    for i, char in enumerate(formula, start=1):
        if char.isdigit():  # if character is a number
            current_count += char
        elif char.isupper():  # if character is uppercase letter
            if current_element:
                if current_element.capitalize() in elements:  # Check both capital and lowercase versions
                    elements_list.append(current_element.capitalize())
                    counts_list.append(int(current_count) if current_count else 1)
                    current_count = ''
                    current_element = char
                else:
                    error = f"'{current_element}' is not a valid element"
                    break
            else:
                current_element = char
        elif char.islower():  # if character is lowercase letter
            current_element += char
        elif char in invalid_symbols:  # if character is an invalid symbol
            error = f"'{char}' is not a valid symbol"
            break
        elif char == '.':  # Skip the '.' character
            continue
        else:  # if character is not recognized
            error = f"'{char}' is not recognized"
            break
    if current_element.capitalize() in elements:  # Check both capital and lowercase versions
        elements_list.append(current_element.capitalize())
        counts_list.append(int(current_count) if current_count else 1)
    else:
        error = f"'{current_element}' is not a valid element"
    return elements_list, counts_list, error