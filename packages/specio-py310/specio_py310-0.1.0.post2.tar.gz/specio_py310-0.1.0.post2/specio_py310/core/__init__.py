""" This subpackage provides the core functionality of specio_py310
(everything but the plugins).
"""

from .util import Spectrum, Dict
from .format import Format, FormatManager
from .exceptions import CannotReadSpectraError
from .request import Request

__all__ = ['Spectrum',
           'Dict',
           'Format',
           'FormatManager',
           'CannotReadSpectraError',
           'Request']
