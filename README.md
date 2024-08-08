# Document for File Manipulation multi project

## organizeFiles.py

This script organizes files in the current directory into subdirectories based on their file types. The subdirectories are predefined in the `SUBDIRECTORIES` dictionary.

### Subdirectories

The script categorizes files into the following subdirectories:

- **DOCUMENTS**: `.pdf`, `.rtf`, `.txt`
- **AUDIO**: `.mp3`, `.m4a`
- **VIDEO**: `.mov`, `.mp4`, `.avi`
- **IMAGE**: `.jpg`, `.jpeg`, `.png`
- **MISC**: Any other file types not listed above

### Functions

#### `PickDirectory(value)`

- **Description**: Determines the category of a file based on its suffix.
- **Parameters**: 
  - `value` (str): The file suffix.
- **Returns**: 
  - `category` (str): The category name for the given suffix. Returns 'MISC' if the suffix is not found.

#### `organizeDirectory()`

- **Description**: Organizes files in the current directory into subdirectories based on their file types.
- **Behavior**:
  - Skips directories.
  - Creates subdirectories if they do not exist.
  - Moves files into their respective subdirectories.

### Usage

To use the script, simply run it in the directory you want to organize.



# FileRead.py

This script reads a text file containing records of individuals with their name, age, and pass/fail status. It then separates these records into two different files based on their pass/fail status.

## Input File Format

The input file (`inputFile.txt`) should contain records in the following format:

NAME AGE STATUS

- [`NAME`] The name of the individual.
- [`AGE`] The age of the individual.
- `STATUS`: 'P' for passed, 'F' for failed.

Example: John 25 P Jane 22 F Doe 30 P


## Output Files
- ['passFile.txt'] Contains records of individuals who have passed.
- ['failFile.txt'] Contains records of individuals who have failed.

## Functions

### Main Script

- **Description**: 
  - Opens the input file for reading.
  - Opens two output files for writing.
  - Reads each line from the input file, splits the line by spaces, and checks the status.
  - Writes the record to ['PassFile.txt'] if the status is 'P'.
  - Writes the record to ['failFile.txt'] if the status is 'F'.
  - Closes all files after processing.

## Usage
To use the script, ensure you have an [`inputFile.txt`] in the same directory as the script. Then run the script.
