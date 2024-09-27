# Auction Program

This is a simple Python auction program that accepts bids from multiple users and identifies the highest bidder.

## Features

- Collects names and bids from multiple users.
- Allows new bids until there are no more bidders.
- Clears the screen after each bid entry for a cleaner interface (only works on Windows due to the use of `cls` command).
- Displays the name of the person with the highest bid at the end.

## How It Works

1. The program starts by welcoming users to the auction.
2. It repeatedly prompts for a user's name and bid.
3. Users can indicate if there are additional bidders by typing `'yes'`. If no additional bidders are present, they type `'no'` to end the bidding process.
4. Once bidding ends, the program displays the name of the highest bidder.

## Installation

1. Clone the repository or download the `auction.py` file.
2. Make sure you have Python installed on your system.

## Usage

1. Run the `auction.py` file:
2. Follow the prompts to enter names and bids.
3. Indicate if there are additional bidders by typing `'yes'` or end the auction by typing `'no'`.
4. The program will display the name of the person with the highest bid once bidding ends.

## Dependencies

- **Python 3.x**: The program is built using standard Python libraries, so no additional installations are required.

## Important Note

- The `clear_screen()` function uses the `os.system('cls')` command, which is specific to Windows. If you're using a different operating system, you can modify it to use `os.system('clear')` for Linux or macOS.

## License

This project is licensed under the MIT License.

