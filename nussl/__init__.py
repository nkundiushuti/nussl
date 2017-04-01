#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .spectral_utils import *
from utils import *
from constants import *
from .audio_signal import AudioSignal
from separation_base import SeparationBase
from Duet import Duet
from Nmf import NMF, DistanceType
from repet import Repet
from repet_sim import RepetSim
from ft2d import FT2D
from overlap_add import OverlapAdd
from rpca import RPCA
from ideal_mask import IdealMask
from projet import Projet
from projet_lite import ProjetLite
from projet_repet import ProjetRepet
from ica import ICA
from melodia import Melodia
from evaluation import Evaluation

__version__ = '0.1.5a10'

version = __version__  # aliasing version
short_version = '.'.join(version.split('.')[:-1])

__title__ = 'nussl'
__description__ = 'A flexible sound source separation library.'
__uri__ = 'https://github.com/interactiveaudiolab/nussl'

__author__ = 'C. Grief, E. Manilow, F. Pishdadian'
__email__ = 'ethanmanilow2015@u.northwestern.edu'

__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2016 Interactive Audio Lab'
