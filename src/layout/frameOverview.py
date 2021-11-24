from os import getcwd
from os.path import join
from tkinter import Text, PhotoImage
from tkinter.constants import BOTH, END, DISABLED, NORMAL, RAISED, GROOVE
from tkinter.font import *
from tkinter.ttk import *

KEY_HEADER_TEXT = 'header_text'
KEY_HEADERS = 'headers'
WIDTH_OVERVIEW = 132


class FrameOverview:

    def __init__(self, notebook: Notebook, **kwargs):
        self._frame = Frame(notebook)

        # Create a smaller logo
        logo = PhotoImage(file=join(getcwd(), 'assets', 'images', 'EleonoraLogoBiker.png')).subsample(2, 2)

        logo_container = Label(self.frame, image=logo, borderwidth=1)
        logo_container.img = logo
        logo_container.grid(column=1, row=1, pady=1, columnspan=2)

        # Create a Header
        header_text = kwargs.get(KEY_HEADER_TEXT)
        header = Label(self.frame, text=header_text, font=Font(weight=BOLD, ))


        header.grid(row=1, column=0, columnspan=2, ipady=1)

        # Create a Text widget for showing the data
        self._overview = Text(self.frame, borderwidth=21, relief=RAISED)
        self.overview.config(width=WIDTH_OVERVIEW)
        self.overview.config(bg='#49A')
        self._overview.grid(row=2, column=1, columnspan=2)

        self.frame.grid_columnconfigure(2, weight=1)
        headers = kwargs.get(KEY_HEADERS)
        # Insert the entity attributes as headers.
        formatted_headers = self._formatLine(headers)
        self.overview.insert(END, formatted_headers)

        # Insert a line between the headers and the actual data
        line = '-' * WIDTH_OVERVIEW + '\n'
        self.overview.insert(END, line)

        self.overview.config(state=DISABLED)

        self.frame.pack(fill=BOTH, expand=True)


    def _formatLine(self, data) -> str:

        # Determine how many items there needs to be on one line
        numberOfItems = len(data)

        # Determine how many space a single item takes
        spacePerItem = (WIDTH_OVERVIEW // numberOfItems) - 3
        formattedLine = ''

        # Add all values onto the formatted line separating them with a pipe `*`
        for idx in range(0, len(data)):
            entry = data[idx]

            formattedLine += f'{str(entry).ljust(spacePerItem)}'

            # Don't add a pipe after the last value
            if idx is not len(data) - 1:
                formattedLine += '* '

        return '* ' + formattedLine + '\n'

    def insertData(self, objects):
        self.overview.config(state=NORMAL)
        # Insert every entity in Text widget
        for entry in objects:
            formatted_entry = self._formatLine(entry.values())
            self.overview.insert(END, formatted_entry)

        self.overview.config(state=DISABLED)


    @property
    def frame(self):
        return self._frame

    @property
    def overview(self):
        return self._overview
