__doc__ = """
.. _Memmaps
:mod:`Memmaps` -- CAMx Memmap Interfaces
========================================

.. module:: Memmaps
   :platform: Unix, Windows
   :synopsis: Provides an easy access point for memory map based
              :ref:`PseudoNetCDF` file interfaces for all CAMx
              related files.  See PseudoNetCDF.sci_var.PseudoNetCDFFile
              for interface details
.. moduleauthor:: Barron Henderson <barronh@unc.edu>
"""
__all__ = ['cloud_rain',
    'height_pressure',
    'humidity',
    'ipr',
    'irr',
    'landuse',
    'one3d',
    'point_source',
    'temperature',
    'uamiv',
    'vertical_diffusivity',
    'wind']
    
from cloud_rain.Memmap import cloud_rain
from height_pressure.Memmap import height_pressure
from humidity.Memmap import humidity
from ipr.Memmap import ipr
from irr.Memmap import irr
from landuse.Memmap import landuse
from one3d.Memmap import one3d
from point_source.Memmap import point_source
from temperature.Memmap import temperature
from uamiv.Memmap import uamiv
from vertical_diffusivity.Memmap import vertical_diffusivity
from wind.Memmap import wind
