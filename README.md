# Pending Instagram Follow Requests Remover

A Python automation script that helps you cancel pending Instagram follow requests using your Instagram data export and Selenium.

## Features

* Reads usernames from Instagram's exported `pending_follow_requests.html` file.
* Automatically visits each profile with a pending follow request.
* Cancels pending follow requests one by one.
* Uses Selenium to interact with Instagram through a real browser session.
* Includes delays between actions to reduce the risk of Instagram rate limits.

## Requirements

* Python 3.8+
* Google Chrome
* ChromeDriver compatible with your Chrome version

## Installation

Clone the repository:

```bash
git clone https://github.com/HAKAM08/PendigFollowersRemoval.git
cd PendigFollowersRemoval
```

Install dependencies:

```bash
pip install beautifulsoup4 selenium
```

## Getting Your Instagram Export

1. Open Instagram.
2. Go to **Settings → Accounts Center → Your Information and Permissions → Download Your Information**.
3. Request a download of your Instagram data.
4. Extract the downloaded archive.
5. Locate the file:

```text
followers_and_following/pending_follow_requests.html
```

6. Place the file in the same directory as the script.

## Usage

Run the script:

```bash
python3 script.py
```

The script will:

1. Parse `pending_follow_requests.html`.
2. Extract all usernames with pending follow requests.
3. Open Chrome.
4. Prompt you to log in to Instagram manually.
5. Visit each profile and cancel the pending follow request.

Example:

```text
Found 35 usernames
Processing username1
✓ Cancelled request for username1
Processing username2
✓ Cancelled request for username2
```

## Project Structure

```text
.
├── script.py
├── pending_follow_requests.html
└── README.md
```

## Important Notes

* This tool requires manual login to Instagram.
* Instagram's interface may change over time, which can break the button selectors used by Selenium.
* Use responsibly and avoid excessive automation that may violate Instagram's Terms of Service.
* The script intentionally waits between actions to reduce the chance of triggering Instagram's anti-bot protections.

## Disclaimer

This project is intended for educational and personal account management purposes only. The author is not responsible for any account restrictions or actions resulting from the use of this software.

## License

MIT License
