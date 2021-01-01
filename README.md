Messenger Always Active
=======================

A simple bot to keep your Messenger activity status to 'Active' all the time

Requirements
------------

* A Windows or Linux server running 24/7
* Microsoft Edge, Firefox or any other browser
* python 3.5+

Usage
-----

```bash
python3 run.py <MessengerID> [Browser]
```

`MessengerID` is the ID of the conversation that will be opened on launch. It is recommended that this is a conversation to yourself in order to prevent undesired 'read' notifications. You can go to [messenger.com](https://messenger.com/), open a conversation to yourself and copy the identifier in the URL bar.

`Browser` is the path to a different browser. This option is only supported under Linux.
