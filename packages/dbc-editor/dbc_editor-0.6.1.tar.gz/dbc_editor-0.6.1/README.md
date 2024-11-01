# dbc-editor

An editor for CAN bus database files like dbc or sym,
based on [cantools](https://github.com/cantools/cantools) and [urwid](http://urwid.org/).


# Usage

Pass the file that you want to open as command line argument.
You can also pass the name of a not existing file in order to create a new file.

When you open the program a list of all messages defined in the passed file is displayed.
If it is a new file this list is empty.

How to navigate in the list view:
- 'arrow up' / 'arrow down' to select a message
- 'G'/'\_' to jump to last/first line
- 'arrow right' to display the signals of the currently selected message
- 'arrow left' to return from the list of signals to the list of messages
- 'i' to edit the selected message (if you are in the list of messages) / signal (if you are in the list of signals)
- 'v' to get a visualization of the message layout
- '+' to create a new message/signal
- '-' to delete the selected message/signal
- 'w' to write/save
- 'q' to quit
- '1' if you are in the list of messages: sort by message id
- '2' if you are in the list of messages: sort by message name
- '0' if you are in the list of messages: sort by the order how they appear in the dbc file

How to navigate in the edit view:
- 'arrow up' / 'arrow down' to select the entry field
- 'arrow left' / 'arrow right' to select a radio button.
  Be careful to not press these buttons too often:

  - If you are on the left most position, pressing 'arrow left' returns to the list view. If you have made changes it will ask you whether you want to save the changes. You can press 'escape' in this dialog to return to the edit view.
  - If you are on the right most position, pressing 'arrow right' saves the changes and returns to the list view. (Same like 'enter')

  Maybe I will change this in the future but this does not have a priority.

- 'enter' to save changes and return to the list of messages/signals
- 'escape' to discard changes and return to the list of messages/signals


# Installation

```
$ pipx install dbc-editor
```

# TODO

Missing message attributes:
- senders
- send_type
- cycle_time

Missing signal attributes:
- initial
- minimum
- maximum
