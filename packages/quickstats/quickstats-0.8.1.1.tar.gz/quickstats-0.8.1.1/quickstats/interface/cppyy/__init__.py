import quickstats
quickstats.core.methods._require_module("cppyy")

from quickstats.interface.cppyy.core import *
from quickstats.interface.cppyy.macros import load_macros, load_macro

load_macros()