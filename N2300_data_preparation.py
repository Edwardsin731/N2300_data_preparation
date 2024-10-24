import os
import pandas as pd
import glob

def check_file_exists(file_path):
    # Check if the file exists
    return os.path.isfile(file_path)

def find_matching_files(pattern):
    # Find all files matching the given pattern
    return glob.glob(pattern)

def convert_to_csv(input_file, output_file):
    # Check if the input file exists
    if not check_file_exists(input_file):
        print(f"Input file {input_file} does not exist")
        return

    # Check if the output file already exists
    if check_file_exists(output_file):
        print(f"File {output_file} already exists")
        return

    # Read the input file
    data = pd.read_csv(input_file, delim_whitespace=True)

    data.columns = ["Time(s)", "Voltage"]

    # Save the data to a CSV file
    data.to_csv(output_file, index=False)

    print(f"Data has been converted to {output_file}")

def batch_convert(pattern, output_folder=''):
    # Find all matching files
    matching_files = find_matching_files(pattern)
    if not matching_files:
        print("No matching files found.")
        return

    # Convert each matching file to CSV
    for i, input_file in enumerate(matching_files, start=1):
        # Generate output file name with the pattern coc_i_output.csv
        base_name = f"fen_{i}_output.csv"
        output_file = os.path.join(output_folder, base_name) if output_folder else base_name
        # Convert the file
        convert_to_csv(input_file, output_file)

# Specify the file path along with the pattern
file_path = '/content/fentanyl_rawdata'  # Update this to the directory where your text files are located
pattern = os.path.join(file_path, 'fen *.txt')  # Example pattern to match files like coc 4.txt, coc 5.txt, etc.
output_folder = '/content/fentanyl_dataset'  # Specify an output folder if needed, otherwise keep it empty

# Perform batch conversion
batch_convert(pattern, output_folder)
