def dataframe_to_dict(results, elements):
    """
    Convert DataFrame to dictionary with Element as keys and # Element as values,
    including elements with counts of 0.

    Args:
    results (DataFrame): DataFrame with 'Element' and '# Element' columns.
    elements (list): List of all elements to include in the dictionary.

    Returns:
    dict: Dictionary with Element as keys and # Element as values.
    """
    # Initialize an empty dictionary with all elements and counts set to 0
    d = {element: 0 for element in elements}

    # Iterate through DataFrame rows and update the counts
    for index, row in results.iterrows():
        d[row['Element']] = row['# Element']

    return d