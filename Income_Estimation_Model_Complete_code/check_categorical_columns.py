
## check_categorical_columns

def check_categorical_columns(df, categorical_cols):
    """
    Check if any categorical columns contain numerical values or NaNs.
    """
    for col in categorical_cols:
        if df[col].dtype != 'object':  # Check if the column is not of type 'object'
            print(f"Column {col} is not of type 'object'. It has type: {df[col].dtype}")
            print(f"Unique values in {col}: {df[col].unique()}")
        elif df[col].isnull().any():  # Check if the column contains NaN values
            print(f"Column {col} contains NaN values.")
        else:
            print(f"Column {col} seems fine.")
        
        # Check for numerical data in categorical columns
        numerical_data = df[col][df[col].apply(lambda x: isinstance(x, (int, float)))]
        if not numerical_data.empty:
            print(f"Column {col} contains numerical data: {numerical_data.unique()}")

# # List of categorical columns
# categorical_cols = ['de_gender', 'de_maritalStatus', 'de_city', 'de_barangay', 'de_province',
#                     'de_dependentsCount', 'de_subIndustryDescription', 'de_Education_type',
#                     'deviceType', 'osversion_v2', 'brand', 'app_first_app_cat',
#                     'app_last_app_cat', 'de_natureofwork_grouped']
