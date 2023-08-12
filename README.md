# Codeforces Virtual Contest Internal Rank Calculator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Streamlit Version](https://img.shields.io/badge/streamlit-0.89.0-blue)
![Pandas Version](https://img.shields.io/badge/pandas-1.3.3-blue)

The Codeforces Virtual Contest Internal Rank Calculator is a Python program that utilizes Streamlit and Pandas to generate internal rankings for participants who submitted a Google Form circulated for a virtual or original Codeforces contest. This tool is designed to streamline the process of calculating and visualizing participant ranks based on contest IDs and their performance in the latest attempt.

## Features

- **Google Sheet Integration**: The program connects to a specified Google Sheet where participant data is stored. It fetches the necessary information to calculate ranks.
- **Contest Filtering**: Participants' data is filtered based on the provided contest ID, allowing you to calculate ranks for specific contests.
- **Rank Calculation**: The program calculates internal ranks based on the latest attempt for each participant, considering both virtual and original contests.
- **Interactive Visualization**: The generated rank list is displayed using a Streamlit web application, making it easy to view and share with others.
- **Export Options**: You can export the generated rank list as a CSV file for further analysis or record-keeping.

## Dashboard 
https://github.com/Priyanshu-U/Codeforces_Virtual_Contest_Internal_Rank_Calculator/assets/62770722/f2e682a7-f46a-4972-9363-756e53e53acc
## Installation

1. Clone this repository to your local machine using:
   
`git clone https://github.com/yourusername/Codeforces_Virtual_Contest_Internal_Rank_Calculator.git`

2. Navigate to the project directory:
`cd Codeforces_Virtual_Contest_Internal_Rank_Calculator`

3. Install the required Python packages using pip:
`pip install -r requirements.txt`


## Usage

1. Set up a Google Form and connect it to a Google Sheet where participant data is collected.

2. Obtain the Google Sheet's sharing link and extract the `key` parameter from it. It should look something like:
`https://docs.google.com/spreadsheets/d/{key}/edit`


3. Open the `config.py` file and update the following variables:
- `SPREADSHEET_KEY`: Replace with the extracted key from the Google Sheet URL.
- `CONTEST_ID_COLUMN`: The column name in the Google Sheet that contains the contest IDs.
- `RANK_COLUMN`: The column name that holds participants' ranks for each contest attempt.

4. Run the Streamlit app:
`streamlit run main.py`


5. The Streamlit app will open in your default web browser. Enter the desired contest ID and click the "Generate Ranks" button to view the internal rank list.

6. You can export the generated rank list as a CSV file by clicking the "Export CSV" button.

## Contributing

Contributions are welcome! If you find a bug or have a suggestion, please open an issue or create a pull request. Make sure to follow the project's coding style and guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy ranking! If you encounter any issues or have questions, feel free to contact us or open an issue in this repository.
