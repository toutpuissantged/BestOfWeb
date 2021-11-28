from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import scrolledtext

from data.store import Store
from core.FileInterface import *
from core.argparse import ArgsParse
from view.FileMenu import FileMenu
from view.EditMenu import EditMenu
from view.HelpMenu import HelpMenu
from view.baseTheme import BaseTheme
from view.tab import TabContronller
from view.index import Index
from core.jsonparser import JsonParser

from controllers.search import Search