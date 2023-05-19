# Messenger Always Active

_A simple bot to keep your Messenger activity status to 'Active' all the time_

## Requirements

- A Windows or Linux machine
- Python 3.5+
- Selenium with the Chrome Webdriver in `PATH`

## Usage

```bash
python run.py <username> <password> <chatID>
```

`username` is your Messenger email address

`password` is your Messenger password

`chatID` is the ID of the conversation that will be opened on launch. It is recommended that this is a conversation to yourself in order to prevent undesired 'read' notifications. You can go to [messenger.com](https://messenger.com/), open a conversation to yourself and copy the identifier in the URL bar.
