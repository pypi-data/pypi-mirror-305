#! /usr/bin/env python
# -*- coding: utf-8 -*-


import pandas

import warnings
from pixelproject import grid
import numpy as np

def slice_to_squaregrid(slice_, size=None, asarray=False, buffer=None):
    """ """    
    if size is None:
        gridsize = int(np.max(np.abs(slice_.convexhull_vertices)))+1
    else:
        gridsize = size
        
    pixels = np.mgrid[0:gridsize*2,0:gridsize*2]-gridsize
    pixels_flat = np.concatenate(pixels.T, axis=0)

    flagnan = np.asarray(np.sum(np.isnan(slice_.xy), axis=0), dtype="bool")
        
    gg = grid.Grid(pixels_flat)
    sg = grid.Grid(slice_.xy.T[~flagnan], slice_.spaxel_vertices)
    sg.add_data(slice_.data[~flagnan], "data")
    if slice_.has_variance():
        sg.add_data(slice_.variance[~flagnan], "variance")

    sout = sg.project_to(gg)
    if buffer is not None:
        # ignoring spaxel outsize the buffered countour
        flagout = slice_.contains(*pixels_flat.T, buffer=buffer)
        sout.geodataframe.loc[sout.geodataframe.index[~flagout],"data"] = np.NaN
        if "variance" in sout.geodataframe.columns:
            sout.geodataframe.loc[sout.geodataframe.index[~flagout],"variance"] = np.NaN

    if not asarray:
        return sout
    
    return sout.geodataframe["data"].values.reshape(gridsize*2,gridsize*2), pixels_flat
    


class SliceModeller():
    """ """
    def __init__(self, slice_, photoref):
        """ """
        self.set_slice(slice_)
        self.set_photoref(photoref)

    # -------- #
    #  SETTER  #
    # -------- #        
    def set_slice(self, slice_):
        """ """
        self._slice = slice_

    def set_photoref(self, photoref):
        """ """
        self._photoref = photoref

    def set_target(self, targetpos, mag):
        """ """
        self._targetprop = {}
        self.update_targetprop(targetpos=targetpos, mag=mag)


    def set_correlation_extent(self, xmin, xmax, ymin, ymax):
        """ """
        self._corr_extent = xmin, xmax, ymin, ymax
        
    def update_targetprop(self, targetpos=None, mag=None):
        """ """
        if targetpos is not None:
            self.targetprop["pos"] = np.asarray(targetpos)
        if mag is not None:
            self.targetprop["mag"] = mag

    # -------- #
    # LOADER   #
    # -------- #
    def load_modelslice(self, mag=None, targetpos=None, seeing=None, refseeing=1, **kwargs):
        """ """
        self._slice_model = self.get_modelslice(mag=mag, targetpos=targetpos, seeing=seeing, refseeing=refseeing, **kwargs)

    def load_gridslice(self, model=False, buffer=-2):
        """ """
        if not model:
            self._gridslice, gridpixels = slice_to_squaregrid(self.slice, asarray=True, buffer=buffer)
        else:
            self._gridslice_model, gridpixels = slice_to_squaregrid(self.slice_model, asarray=True, buffer=buffer)
            
        if not hasattr(self,"gridpixels"):
            self.gridpixels = gridpixels
        elif model and not np.all(gridpixels == self.gridpixels):
            warnings.warn("Model gridpixels is not the same as the current gridpixels")
            
        self.gridpixels = gridpixels
            
        
    # -------- #
    # GETTER   #
    # -------- #
    def get_aligned_targetpos(self):
        """ """
        return self.target_pos-self.offset

    
    def get_modelslice(self, mag=None, targetpos=None, seeing=None, refseeing=1, slicearcsec=0.55):
        """ """
        if targetpos is None:
            targetpos = self.target_pos
        if mag is None:
            mag = self.target_mag
            
        self.photoref.build_pointsource_image(mag, refseeing/self.ref_pixelsize)
        addseeing = None if seeing is None else np.sqrt(seeing**2 - refseeing**2)/self.ref_pixelsize
        return self.photoref.project_to_slice(self.slice, slicearcsec, targetpos,
                                            gaussianconvol=addseeing)

    def get_larger_fullrectangle(self, model=False, ilarger=1):
        """ """
        data = self.gridslice if not model else self.gridslice_model
        
        pixelsin = self.gridpixels[np.concatenate(~np.isnan(data))]
        (left, bottom),(right, top) = np.asarray(np.percentile(pixelsin, [0, 100], axis=0) - self.gridextent[:2], dtype="int")
        
        square = {}
        for vi in range(bottom, top):
            for hi in range(left,right):
                for vd in range(bottom, top)[::-1]:
                    if vd<=vi: 
                        continue
                    for hd in range(left, right)[::-1]:
                        if hd<=hi: 
                            continue
                        if np.any(np.isnan(data[vi:vd,hi:hd])):
                            continue
                        square["%d %d %d %d"%(vi,vd,hi,hd)] = (vd-vi)**2 + (hd-hi)**2
        return np.asarray([np.asarray(l.split(), dtype="int")
                            for l in np.asarray(list(square.keys()))[np.argsort(list(square.values()))[-ilarger:]]])


    def get_correlate2d(self, mode="full", autocorrelate=False, **kwargs):
        """ """
        from scipy import signal
        in1 = self.gridslice[self.correlate_gridextent[0]:self.correlate_gridextent[1],
                              self.correlate_gridextent[2]:self.correlate_gridextent[3]]
        in2 = self.gridslice_model[self.correlate_gridextent[0]:self.correlate_gridextent[1],
                              self.correlate_gridextent[2]:self.correlate_gridextent[3]]
        if autocorrelate:
            return signal.correlate2d(in2, in2, mode=mode, **kwargs)
        
        return signal.correlate2d(in1, in2, mode=mode, **kwargs)    

    def derive_shift(self, **kwargs):
        """ """
        from scipy import ndimage
        corr2d = self.get_correlate2d(**{**{"mode":"full"},**kwargs})
        centroid_x = corr2d.shape[0]/2
        centroid_y = corr2d.shape[1]/2
        self._offset_info = {"corr2d_centroid":np.asarray(corr2d.shape)/2-0.5,
                             "corr2d_maximum":np.asarray(ndimage.maximum_position(corr2d)),
                             "corr2d":corr2d
                             }
        self._offset = (self._offset_info["corr2d_centroid"] - self._offset_info["corr2d_maximum"]
                            )[::-1]
        return self._offset

    # --------- #
    #  PLOTTER  #
    # --------- #
    def show(self, savefile=None, show=True):
        """ """
        import matplotlib.pyplot as mpl
        from matplotlib.patches import Rectangle
        
        fig = mpl.figure(figsize=[8,4.5])
    
        axd = fig.add_axes([0.1,0.1,0.5,0.83])
        axm = fig.add_axes([0.66,0.61,0.22,0.35])    
        axc = fig.add_axes([0.67,0.1,0.2,0.48])
        
        # Data
        prop = dict(origin="lower", zorder=3, aspect="auto", extent=self.gridextent[[0,2,1,3]]) #left, right, bottom, top)
        axd.imshow(self.gridslice, **prop)
        axm.imshow(self.gridslice_model, **prop)
        # Target
        axd.scatter(*self.get_aligned_targetpos(), marker="x", color="C1", zorder=4,s=80)
        
        [ax_.scatter(*self.target_pos, marker="o", 
                         facecolors="None",
                         edgecolors="0.7", zorder=4, s=50) for ax_ in [axd, axm]]
        [ax_.add_patch(Rectangle(np.asarray(self.correlate_gridextent)[[2,0]]+self.gridextent[[0,1]]-0.5, 
                                         self.correlate_gridextent[3]-self.correlate_gridextent[2],
                                         self.correlate_gridextent[1]-self.correlate_gridextent[0], 
                                         zorder=6, facecolor="None", edgecolor="0.7"))
        for ax_ in [axd, axm]]
    
        # Corremap
        _ = prop.pop("extent")
        axc.imshow(self._offset_info["corr2d"], **prop)
        axc.axhline(self._offset_info["corr2d_centroid"][0], color="0.7", lw=1, zorder=9)
        axc.axvline(self._offset_info["corr2d_centroid"][1], color="0.7", lw=1, zorder=9)
        axc.scatter(*self._offset_info["corr2d_maximum"][::-1], marker="x", color="C1", s=80, zorder=10)
        
        axm.set_axis_off()
    
        # Data
        fig.text(0.1+0.5/2, 0.1+0.83 + 0.01, "Data", va="bottom", ha="center", 
                     fontsize="large")
        # Model    
        fig.text(0.66+0.22/2, 0.1+0.83 + 0.01, "Model", va="bottom", ha="center", 
                     fontsize="large")
        # Cross Correlation
        0.67,0.1,0.2,0.48
        fig.text(0.67+0.2/2, 0.1+0.48+0.005, "Cross Correlation", va="bottom", ha="center", 
                     fontsize="large")

        if show:
            fig.show()
        return fig

    
    # ================ #
    #   Properties     #
    # ================ #
    #
    #
    #
    @property
    def offset(self):
        """ """
        if not hasattr(self,"_offset"):
            self.derive_shift()
        return self._offset
    
    @property
    def ref_pixelsize(self):
        """ """
        return self.photoref.refimage.pixel_size_arcsec.value if self.has_photoref() else None

    @property
    def correlate_gridextent(self):
        """ """
        if not hasattr(self, "_corr_extent"):
            warnings.warn("Loading the correlation extent as the largest available rectangle")
            self.set_correlation_extent(*self.get_larger_fullrectangle()[0])
            
        return self._corr_extent
        
    #
    # - Target Position
    #
    @property
    def has_target(self):
        """ """
        return hasattr(self,"_targetprop") 
    @property
    def targetprop(self):
        """ Position of the target in the IFU """
        if not hasattr(self,"_targetprop"):
            raise AttributeError("No target position defined, run set_target() or update_targetprop")
        
        return self._targetprop
    
    @property
    def target_pos(self):
        """ Position of the target in the IFU """
        return self.targetprop["pos"]

    @property
    def target_mag(self):
        """ Magnitude of the target """
        return self.targetprop["mag"]
    
    #
    # - Slice
    #
    def has_slice(self):
        """ """
        return self.slice is not None
    
    @property
    def slice(self):
        """ """
        if not hasattr(self,"_slice"):
            self._slice = None
        return self._slice

    @property
    def gridslice(self):
        """ """
        if not hasattr(self,"_gridslice"):
            if self.has_slice():
                self.load_gridslice(model=False, buffer=-2)
            else:
                return None
            
        return self._gridslice

    @property
    def gridextent(self):
        """ """
        if not hasattr(self,"gridpixels"):
            raise AttributeError("no grid laoded. self.gridpixels is not set yet.")
        
        return np.concatenate(np.percentile(self.gridpixels, [0,100], axis=0))

    #
    # - Model Slice
    #
    @property
    def slice_model(self):
        """ """
        if not hasattr(self,"_slice_model"):
            if not self.has_slice():
                raise AttributeError("a origin Slice is required to build a mode")
            warnings.warn("Loading slice_model using default parameter. Change by using self.load_slice_model")
            self.load_modelslice()
            
        return self._slice_model
    #
    # - PhotoRef
    #
    def has_photoref(self):
        """ """
        return self.photoref is not None
    
    @property
    def photoref(self):
        """ """
        if not hasattr(self,"_photoref"):
            self._photoref = None
        return self._photoref

    @property
    def gridslice_model(self):
        """ """
        if not hasattr(self,"_gridslice_model"):
            if self.has_slice():
                self.load_gridslice(model=True, buffer=-2)
            else:
                return None
            
        return self._gridslice_model
