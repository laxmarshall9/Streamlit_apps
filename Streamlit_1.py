import streamlit, pandas, matplotlib.pyplot

# To run file, paste into terminal: streamlit run Streamlit_1.py

# To check configuration, paste into Terminal: streamlit config show
# Streamlit will automatically read config.toml file but it must be properly located within directory.
# Directory configuration: folder within same folder as where this file is being run:
#    Folder named: .streamlit
#    file: config.toml


streamlit.title("Example Streamlit Site")

# ______________________________________________
# Widget 1 (Top-level widget) - File Uploader
# ______________________________________________

source_file = streamlit.file_uploader("Choose any xlsx file", type="xlsx") # Widget used to upload the file

if source_file is not None:
    data_frame = pandas.read_excel(source_file, skiprows=1) # Reads the excel file and returns a dataframe which can be parsed by using the headers of each column as key values
    streamlit.write("File upload successful") # Feedback to the user indicating no error encountered while reading the file
    
    # ________________________________________
    # Widget 2 (Sub-level 1) - Data Preview
    # ________________________________________

    streamlit.subheader("Data Preview")
    streamlit.write(data_frame.head()) # Previews the first 5 rows of data
    
    # ________________________________________
    # Widget 3 (Sub-level 1) - Data Summary
    # ________________________________________

    streamlit.subheader("Data Summary")
    streamlit.write(data_frame.describe()) # Gives a brief analysis of some common data parameters (min value, max value, count, etc.)

    # ________________________________________
    # Widget 4 (Sub-level 1) - Data Filter
    # ________________________________________

    streamlit.subheader("Filter Data")
    columns = data_frame.columns.tolist() # Creates a list of column names from source file
    selected_column = streamlit.selectbox("Select column to filter by", columns) # Dropdown box for column selection
    unique_values = data_frame[selected_column].unique() # Gets only unique values from contents of the selected column
    selected_value = streamlit.selectbox("Select value", unique_values) # Dropdown box of unique values within selected column
    filtered_data = data_frame[data_frame[selected_column] == selected_value] # Displays only the rows which match the selected unique value within the selected column
    streamlit.write(filtered_data) # Publishes the above functionality into the user interface

    # ________________________________________
    # Widget 5 (Sub-level 1) - Data Plotter
    # ________________________________________

    streamlit.subheader("Plot Data")
    x_column = streamlit.selectbox("Select x-axis column", columns)
    y_column = streamlit.selectbox("Select y-axis column", columns)

    if streamlit.button("Generate Plot"): # Creates a button and below defines what will happen when the button is pressed
        streamlit.line_chart(filtered_data.set_index(x_column)[y_column]) # Sets the x-axis (i.e. relevant key within the pandas dataframe) and plots the corresponding y values (i.e. values within the corresponding column per the value at each corresponding index/row within the dataset)

else:
    streamlit.write("Feed me!!")


