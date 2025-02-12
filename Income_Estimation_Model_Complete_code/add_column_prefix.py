
def add_column_prefix(df: pd.DataFrame, 
                      prefix: str, 
                      columns: Union[str, List[str]] = None):
    """
    Add a prefix to specified columns in a DataFrame.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The input DataFrame whose columns need to be renamed
    prefix : str
        The prefix to be added to selected column names
    columns : str or list of str, optional
        The specific column(s) to add prefix to. 
        If None, applies prefix to all columns.
    
    Returns:
    --------
    pandas.DataFrame
        A new DataFrame with prefixed column names
    
    Examples:
    ---------
    >>> data = pd.DataFrame({
    ...     'name': ['Alice', 'Bob'], 
    ...     'age': [25, 30], 
    ...     'city': ['New York', 'San Francisco']
    ... })
    >>> 
    >>> # Add prefix to specific columns
    >>> prefixed_data = add_column_prefix(data, 'user_', ['name', 'age'])
    >>> print(prefixed_data.columns)
    Index(['user_name', 'user_age', 'city'], dtype='object')
    
    >>> # Add prefix to all columns
    >>> all_prefixed = add_column_prefix(data, 'user_')
    >>> print(all_prefixed.columns)
    Index(['user_name', 'user_age', 'user_city'], dtype='object')
    """
    # Create a copy of the DataFrame to avoid modifying the original
    df_copy = df.copy()
    
    # If no specific columns are provided, use all columns
    if columns is None:
        columns = df.columns.tolist()
    
    # Ensure columns is a list
    if isinstance(columns, str):
        columns = [columns]
    
    # Validate that specified columns exist in the DataFrame
    invalid_columns = set(columns) - set(df.columns)
    if invalid_columns:
        raise ValueError(f"Columns not found in DataFrame: {invalid_columns}")
    
    # Create a dictionary to map selected column names to new column names
    rename_dict = {col: f"{prefix}{col}" for col in columns}
    
    # Rename the specified columns
    df_copy.rename(columns=rename_dict, inplace=True)
    
    return df_copy
