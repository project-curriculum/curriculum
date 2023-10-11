import pandas as pd
import os

# Set the working directory to the directory containing your notebook
os.chdir('/Users/jongarcia/codeup-data-science/curriculum')


def get_file():
    # The file appears to be space-separated and lacks headers, so we'll specify those
    column_names = ['timestamp', 'curriculum_topic', 'user_id', 'cohort_id', 'ip_address']
    df = pd.read_csv("anonymized-curriculum-access.txt", delim_whitespace=True, names=column_names)
    return df


def create_info_dataframe(df):
    # Initialize lists to store information for each column
    column_names = []
    null_counts = []
    null_percentages = []
    zero_counts = []
    blank_counts = []
    unique_value_counts = []
    data_types = []

    # Iterate through the columns of the DataFrame
    for column in df.columns:
        column_names.append(column)
        null_count = df[column].isnull().sum()
        null_counts.append(null_count)
        total_count = len(df)
        null_percentage = (null_count / total_count) * 100
        null_percentages.append(np.round(null_percentage))
        zero_count = (df[column] == 0).sum()
        zero_counts.append(zero_count)
        blank_count = (df[column] == " ").sum()
        blank_counts.append(blank_count)
        unique_count = df[column].nunique()
        unique_value_counts.append(unique_count)
        data_type = df[column].dtype
        data_types.append(data_type)

    # Create the information DataFrame
    info_df = pd.DataFrame({
        "Column": column_names,
        "Null_Count": null_counts,
        "Null_Percentage": null_percentages,
        "Zero_Count": zero_counts,
        "Blank_Count": blank_counts,
        "Unique_Values": unique_value_counts,
        "Data_Type": data_types
    })

    return info_df