import pandas as pd



# Define a function to clean the DataFrame based on groupby columns and a column to filter
import pandas as pd

# Define a function to clean the DataFrame based on groupby columns and a column to filter
def clean_traffic_data(df, groupby_cols, column_to_clean):
    # Group by the specified columns and count the occurrences
    traffic_program = df.groupby(groupby_cols)[column_to_clean].value_counts().reset_index(name='visit_count')

    # Remove the homepage from the list
    traffic_program = traffic_program[traffic_program[column_to_clean] != '/']

    # List of common file extensions
    file_extensions = ['.txt', '.jpg', '.jpeg', '.png', '.pdf', '.doc', '.xls', '.csv', '.json', '.html', '.svg', '.java', '.zip', '.gif', '.ico']

    # Define a function to check if a URL contains a file extension
    def contains_file_extension(url):
        for ext in file_extensions:
            if ext in url:
                return False
        return True

    # Filter rows where the URL doesn't contain a file extension
    traffic_program = traffic_program[traffic_program[column_to_clean].apply(contains_file_extension)]

    # Sort the DataFrame by groupby columns and 'visit_count'
    traffic_program = traffic_program.sort_values(groupby_cols + ['visit_count'], ascending=[True, False])

    return traffic_program
