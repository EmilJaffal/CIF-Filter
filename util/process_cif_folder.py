import os
import pandas as pd
import click


def process_cif_folder(folder_path):
    """
    Process data from a folder containing CIF files
    """
    entries = []
    formulas = []

    # Loop through the directory and its subdirectories
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".cif"):
                # Extract the filename without extension
                entry = os.path.splitext(filename)[0]
                file_path = os.path.join(root, filename)

                # Read the file and extract the desired information
                with open(file_path, "r") as file:
                    # Keep track of which line we're processing
                    line_count = 0
                    for line in file:
                        line_count += 1
                        if line_count == 3:  # Check if it's the third line
                            # Split the line by '#'
                            parts = line.split("#")
                            if len(parts) > 2:
                                # Extract the second part, and remove leading/trailing whitespace
                                formula = parts[2].strip()
                                # Break the formula at the first space
                                formula = formula.split(" ")[0]
                                # Append the extracted data to the lists
                                entries.append(entry)
                                formulas.append(formula)
                            else:
                                click.secho(
                                    f"Warning: Line '{line}' in file '{filename}' does not contain enough '#' characters.",
                                    fg="yellow",
                                )
                            break  # Break the loop after finding the formula

    # Create a DataFrame from the lists
    data = pd.DataFrame({"Entry": entries, "Formula": formulas})
    return data
