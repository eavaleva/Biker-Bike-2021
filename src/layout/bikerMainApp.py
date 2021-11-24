from os import chdir, getcwd
from os.path import join
from pathlib import Path
from tkinter import Tk, PhotoImage, ttk, Text
from tkinter.constants import BOTH, END, GROOVE
from tkinter.ttk import Notebook, Frame, Label
from typing import Type


from .frameOverview import FrameOverview
from ..utils import DatabaseConnection
from ..models import Accessoires, Fiets, Medewerker, Klant

WINDOW_TITLE = 'Biker'
WINDOW_DEFAULT_WIDTH = 800
WINDOW_DEFAULT_HEIGHT = 600
TAB_MAIN_MENU_TEXT = 'Hoofdmenu'
TAB_ACCESSOIRE_TEXT = 'Accessoires'
TAB_FIETS_TEXT = 'Fiets'
TAB_KLANT_TEXT = 'Klant'
TAB_MEDEWERKER_TEXT = 'Medewerker'
HEADER_ACCESSOIRE_TEXT = 'Overzicht accessoires'
HEADER_FIETS = 'Overzicht Fietsen'
HEADER_KLANT = 'Overzicht Klant'
HEADER_MEDEWERKER = 'Overzicht Medewerker'


# Get the current file location of this file
FILE_LOCATION = Path(__file__)

# Change the working directory of the Python script to where the project root would be
chdir(FILE_LOCATION.parent.parent.parent)


class BikerApp:
    def __init__(self):
        self._database_connection = DatabaseConnection()
        # Create and configure the application window
        self._app = Tk()
        self._app.title(WINDOW_TITLE)
        self._app.minsize(WINDOW_DEFAULT_WIDTH, WINDOW_DEFAULT_HEIGHT)


        self._notebook = Notebook(self.app)

        # Make sure the notebook uses all available space of the application window
        self._notebook.pack(expand=True, fill=BOTH)

        self.accessoriesFrame = FrameOverview(
            self.notebook,
            header_text=HEADER_ACCESSOIRE_TEXT,
            headers=['Merk', 'Type', 'Dagprijs in €', 'Nieuwprijs in €']

        )
        self.fietsFrame = FrameOverview(self.notebook,
            header_text= HEADER_FIETS,
            headers=['Type', 'Merk', 'Dagprijs in €', 'Borgprijs  in €']
        )
        self.klantFrame = FrameOverview(self.notebook,
            header_text=HEADER_KLANT,
            headers=['Voornaam', 'Achternaam', 'Adres', 'Postcode', 'Plaats', 'Land']
        )
        self.medewerkerFrame = FrameOverview(
            self.notebook,
            header_text=HEADER_MEDEWERKER,
            headers=['Voornaam', 'Achternaam', 'Rol', 'Login']
        )

        self._createMainMenuFrame()

        # Create frames

        # self.accessoriesFrame = FrameOverview(self.notebook, header_text=HEADER_ACCESSOIRE_TEXT)
        self.notebook.add(self.accessoriesFrame.frame, text=TAB_ACCESSOIRE_TEXT)
        self.notebook.add(self.fietsFrame.frame, text=TAB_FIETS_TEXT)
        self.notebook.add(self.klantFrame.frame, text=TAB_KLANT_TEXT)
        self.notebook.add(self.medewerkerFrame.frame, text=TAB_MEDEWERKER_TEXT)



    def _createMainMenuFrame(self):
        """
        Create the Main menu frame with a logo and an area to show some text.
        """
        self._mainMenuFrame = Frame(self._notebook)

        # Add the text to the main menu frame
        text = Text(self._mainMenuFrame, height=10, width=60, relief=GROOVE, borderwidth=12)
        text.pack(side="bottom", pady=10)
        text.insert(END,
                    'Welkom bij het hoofdmenu van de Biker Applicatie! \n'
                    'Klik op de knop hierboven om accessoires in te lezen.')
        text.config(font=('New Times Roman', 14, 'normal',))
        text.config(foreground='black', background='AliceBlue')

        text.config(state='disabled')

        # Add the logo to the main menu frame
        banner = self._createBanner(self._mainMenuFrame)
        banner.pack()


        # Add button to main frame menu
        self.buttonAcc = ttk.Button(
            self._mainMenuFrame,
            text='Klik hier om the lijst met accessoires te zien',
            command=lambda: self._createOnButton(self.accessoriesFrame, 'Accessoires', self.buttonAcc, Accessoires))
        self.buttonAcc.state(['!disabled'])
        self.buttonAcc.pack(side='top', pady=6)

        self.buttonMedewerker = ttk.Button(
            self._mainMenuFrame,
            text='Klik hier om the lijst met medewerkers  te zien',
            command=lambda: self._createOnButton(self.medewerkerFrame, 'Medewerker', self.buttonMedewerker, Medewerker)
        )
        self.buttonMedewerker.state(['!disabled'])
        self.buttonMedewerker.pack(side='bottom', pady=6,)

        self.buttonKlant = ttk.Button(
            self._mainMenuFrame,
            text='Klik hier om the lijst met klanten te zien',
            command=lambda: self._createOnButton(self.klantFrame, 'Klant', self.buttonKlant, Klant)
        )
        self.buttonKlant.state(['!disabled'])
        self.buttonKlant.pack(side='bottom', pady=6,)

        self.buttonFiets = ttk.Button(
            self._mainMenuFrame,
            text='Klik hier om the lijst met fietsen te zien',
            command=lambda: self._createOnButton(self.fietsFrame, 'Fiets', self.buttonFiets, Fiets)
        )
        self.buttonFiets.state(['!disabled'])
        self.buttonFiets.pack(side='bottom', pady=6)

        self._mainMenuFrame.pack(fill=BOTH, expand=True)
        self._notebook.add(self._mainMenuFrame, text=TAB_MAIN_MENU_TEXT)


    def _createOnButton(self, frame: FrameOverview, table: str, btn: ttk.Button, object_type: Type):
        frame.insertData(self._database_connection.get_data(table, object_type))
        self.notebook.select(frame.frame)

        btn.config(state='disabled')

       # self.accessoriesFrame.insertData(readData(join('assets', 'data', 'accessories.csv'), Accessoires))
       #  self.accessoriesFrame.insertData(self._database_connection.get_accessoires())
       #  self.notebook.select(self.accessoriesFrame.frame)
       #
       #  self.buttonAcc.state(['disabled'])

    def _createBanner(self, parent: Frame) -> Label:
        banner = PhotoImage(file=join(getcwd(), 'assets', 'images', 'EleonoraLogoBiker.png', ))
        bannerContainer = Label(parent, image=banner)

        # With the code hereunder u make sure to store the image object to variable location tha would not be garbage collected as long as u need to use it.
        # You store reference to the photoImage object in the tk label image object itself since tk is holding on to that image en preventing it from being gabage collected.
        bannerContainer.img = banner

        return bannerContainer

    @property
    def app(self) -> Tk:
        return self._app

    @property
    def notebook(self) -> Notebook:
        return self._notebook
