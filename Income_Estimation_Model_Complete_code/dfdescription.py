
def dfdescription(df):
    print(f"The shape of the data frame is :\t {df.shape}")
    print(f"The data types of columns in dataframe is: \n{df.dtypes}")
    print(f"The description of numerical columns is:\t {df.describe()}")
