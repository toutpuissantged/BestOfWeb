from tkinter import Button, Tk, Label, Entry , StringVar, IntVar, Radiobutton, messagebox, Menu
from tkinter.ttk import Frame

from data.store import Store
from core.FileInterface import *
from core.argparse import ArgsParse
from view.FileMenu import FileMenu
from view.EditMenu import EditMenu
from view.HelpMenu import HelpMenu
from view.tab import TabContronller
from view.index import Index
from view.home import Home
from core.jsonparser import JsonParser

from controllers.search import Search