# csv2ies

Let's import users from a CSV file into an IES instance via it's REST API.

## Installation

`pip install csv2ies`

## Usage

- Needed user pools need to be created in user management beforehand.
- Open your folder with your CSV File in the terminal.
- Create an empty config via `csv2ies config`
- Edit the created config.json file accordingly to your needs
- Add Aliases to match user pool names to anchors
- Run the import: `csv2ies run`