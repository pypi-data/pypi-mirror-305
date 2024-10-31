#! /usr/bin/env python
# -*- coding: utf-8 -*-


import pandas
import numpy as np
from astropy import coordinates, units
from astrobject.utils import tools

class PhotoReference():

    def __init__(self, coords):
        """ """
        if coordinates is not None:
            self.set_coords(*coords)
        
    # ============== #
    #   Method       #
    # ============== #
    @classmethod
    def from_coords(cls, radec):
        """ """
        return cls(radec)

    @classmethod
    def from_refimage(cls, refimage):
        """ """
        this = cls(None)
        this.set_refimage(refimage)
        return this
    
    # ------- #
    # SETTER  #
    # ------- #
    def set_coords(self, ra, dec, download_ref=True, refband="r"):
        """ set the coordinate of the source
        """
        self._radec = ra,dec
        if download_ref:
            self.download_reference(band=refband)
            
    def set_refimage(self, refimage):
        """ """
        self._refimage = refimage
        self._pixels = np.mgrid[0:self.refimage.shape[0],0:self.refimage.shape[1]].T


    # ------- #
    # CONVERT #
    # ------- #
    def flux_to_count(self, flux):
        """ returns image counts from given flux in erg/s/cm/A """
        return flux/(10**(-(2.406+self.refimage.mab0)/2.5
                                  )/(self.refimage.lbda**2)) # in counts

    def flux_to_mag(self, flux):
        """ returns AB mag from flux in erg/s/cm/A """
        return tools.flux_to_mag(flux, wavelength=self.refimage.lbda)[0] # in AB

    def mag_to_count(self, mag):
        """ returns image counts from given AB mag  """
        return self.flux_to_count(self.mag_to_flux(mag))

    def mag_to_flux(self, mag):
        """ returns flux in erg/s/cm/A from given AB mag  """
        return tools.mag_to_flux(mag, wavelength=self.refimage.lbda)[0] # in erg/s/cm2/A

    def count_to_flux(self, count):
        """ returns flux in erg/s/cm/A from the given image counts """
        return count * (10**(-(2.406+self.refimage.mab0)/2.5)
                            /(self.refimage.lbda**2))
    
    def count_to_mag(self, count):
        """ returns AB mag from the given image counts """
        return self.flux_to_mag(self.count_to_flux(count))
    
    # ------- #
    # GETTER  #
    # ------- #
    def get_segmap(self, targetmag=None, on="fakeimage",
                       thresh=0.1, deblend_cont=1e-4,
                       source_kwargs={}, update=True, **kwargs):
        """ """
        import sep
        if targetmag is not None:
            self.build_pointsource_image(targetmag, **source_kwargs)

        sepo, segmap = sep.extract( getattr(self,on), thresh, segmentation_map=True,
                                        deblend_cont=deblend_cont, **kwargs)
        sepout = pandas.DataFrame(sepo)
        # Some measurements
        deltax, deltay = (self.coords_refpixel - sepout[['x','y']].values).T
        sepout["dist_to_target"] = np.sqrt(deltax**2+deltay**2)
        if update:
            self._sepout = sepout
            self._segmap = segmap
            
        return segmap, sepout

        
    def get_segmap_value(self, which="target", maxdist=None):
        """ """
        if which == "target":
            coords = self.coords_refpixel 
            if maxdist is None:
                maxdist = 2
                
        elif which == "host":
            coords = self.get_host_coords(inpixels=True)
            if maxdist is None:
                maxdist = 5
        else:
            raise ValueError("which could either be 'target' or 'host'")
        
        deltax,deltay = (coords - self._sepout[['x','y']].values).T
        pixel_dist    = np.sqrt(deltax**2+deltay**2)
        nearest = np.argsort(pixel_dist)[0]
        if maxdist is not "None" and pixel_dist[nearest]>maxdist:
            print("refcoords ", coords)
            return None
    
        return nearest+1 # because segmap object start at 1 not 0

    def get_segmap_contours(self, which="target", alpha=0.2, aspolygon=False, inpixels=True):
        """ Returns the contour of the segmentation map corresponding to either the host or the target.
        This contours are in `refimage` pixels 
        """
        from .utils import points_to_contour, polygon_to_vertices
        which_id = self.get_segmap_value(which)
        if which_id is None:
            return None
        which_pixels  = self._pixels[self.segmap==which_id]
        
        poly_, _ =  points_to_contour(which_pixels, alpha=alpha)

        # Output
        if aspolygon and inpixels:
            return poly_

        pixels = polygon_to_vertices(poly_)
        if inpixels:
            return pixels

        radecs = self.refimage.pixel_to_coords(*pixels.T)
        if not aspolygon:
            return radecs
        
        from shapely import geometry
        return geometry.Polygon(radecs)


    def get_iso_contours(self, iso, unit="mag", on="fakeimage", asdict=False):
        """ """
        from skimage import measure
        
        if unit not in ["mag", "flux", "count"]:
            raise ValueError("unit must be mag, flux or count. %s given"%unit)
        
        iso = np.atleast_1d(iso)
        isocounts = iso if unit =="count" else self.mag_to_count(iso) if unit == "mag" else self.flux_to_count(iso)
        if asdict:
            return {iso_:[np.stack([c[:,1], c[:,0]]).T for c in measure.find_contours(getattr(self,on), iso_)] for iso_ in isocounts}
        
        return [[np.stack([c[:,1], c[:,0]]).T for c in measure.find_contours(getattr(self,on), iso_)] for iso_ in isocounts]

    def get_host_coords(self, source="sep", inpixels=False):
        """ """
        host_radec = self._pstarget.get_nearest_catdata(source=source,relative=True)[["raMean","decMean"]].values[0]
        if not inpixels:
            return host_radec
        return self.refimage.coords_to_pixel(*host_radec)

    # ------- #
    # LOADER  #
    # ------- #
    def download_reference(self, band="r"):
        """ """
        from pymage import panstarrs
        if not self.has_coords():
            raise AttributeError("No coordinate set.")
        self._pstarget = panstarrs.PS1Target.from_coord(*self.coords)
        self._pstarget.download_cutout("r")
        self.set_refimage(self._pstarget.imgcutout["r"])
        

    def load_psfimage(self, sigma_pixels=4):
        """ """
        from scipy.stats import multivariate_normal
        self._psfimage_normed = multivariate_normal.pdf(self._pixels, self.coords_refpixel,
                                                        cov=sigma_pixels)

    def load_segmap(self, targetmag=None, **kwargs):
        """ """
        _ = self.get_segmap(targetmag=targetmag,
                            update=True,  **kwargs)
    

    # ------- #
    # Project #
    # ------- #
    def project_to_slice(self, slice_, spaxelarcsec, targetspaxel=[0,0], fakeimage=True, gaussianconvol=0):
        """ """
        import pyifu
        from pixelproject import grid
        data = self.fakeimage if fakeimage else self.dataimage

        if gaussianconvol is not None and gaussianconvol>0:
            from scipy.ndimage import gaussian_filter
            data = gaussian_filter(data, gaussianconvol)
            
        # Base Grid
        g = grid.Grid.from_stamps(data, -self.coords_refpixel)
        
        # Get spaxel vertices
        vertices = slice_.get_spaxel_polygon(True, format="array") - targetspaxel
        vertices *= spaxelarcsec/self.refimage.pixel_size_arcsec.value
        
        # Spaxels as Grid aligned with gref
        g2 = grid.Grid.from_vertices(vertices)
        gproject = g.project_to(g2)
        # Get the data to return a slice
        data = gproject.geodataframe["data"].values
        flagnan = slice_.is_spaxels_nan() # removed spaxels

        return pyifu.get_slice(data, xy = slice_.xy.T[~flagnan], 
                                   spaxel_vertices=slice_.spaxel_vertices, 
                                   indexes=slice_.indexes[~flagnan],
                                   lbda=slice_.lbda, header=slice_.header)
    
    # ------- #
    # METHODS #
    # ------- #
    def build_pointsource_image(self, mag,  sigma_pixels=None, **kwargs):
        """ """
        
        if not hasattr(self, "_psfimage_normed") or sigma_pixels is not None:
            self.load_psfimage(sigma_pixels=sigma_pixels, **kwargs)
        
        flux = tools.mag_to_flux(mag, wavelength=self.refimage.lbda)[0] # in erg/s/cm2/A
        self._counts = flux/(10**(-(2.406+self.refimage.mab0)/2.5
                                  )/(self.refimage.lbda**2)) # in counts
                                  
        self._psfimage = self._counts*self._psfimage_normed
        

    def show(self, inlog=True):
        """ """
        import matplotlib.pyplot as mpl
        fig = mpl.figure(figsize=[8,3])
        axref = fig.add_axes([0.07,0.2,0.25,0.7])
        axfake = fig.add_axes([0.35,0.2,0.25,0.7])
        axsegmap = fig.add_axes([0.7,0.2,0.25,0.7])
    
        if inlog:
            data = np.log10(self.dataimage) 
            fake = np.log10(self.fakeimage)
        else:
            data = self.dataimage
            fake = self.fakeimage
        
        prop = dict(origin="lower", vmax=np.percentile(data[data==data], 98), vmin=np.percentile(data[data==data], 2))
        axref.imshow(data, **prop)
        axfake.imshow(fake, **prop)
    
        axsegmap.imshow( self.segmap, origin="lower")

        for ax_ in [axref,axfake, axsegmap]:
            ax_.scatter(*self.coords_refpixel, marker="x", color="C1", lw=1)
            ax_.scatter(*self.get_host_coords(inpixels=True), marker=".", color="C1")
            
        # rm ticks
        _ = [[ax_.set_yticks([]),ax_.set_xticks([])] for ax_ in [axref, axfake]]
        # Labels
    
        axref.set_title("Reference")
        axfake.set_title("Faked PSF")
        axsegmap.set_title("Segmap on Faked")
        return fig

    # ============== #
    #  Properties    #
    # ============== #
    @property 
    def coords(self):
        """ """
        if not hasattr(self, "_radec"):
            self._radec = None
        return self._radec

    @property
    def coords_refpixel(self):
        """ """
        if not hasattr(self,"_coords_refpixel"):
            if not self.has_coords():
                raise AttributeError("No coordinates set")
            if not self.has_refimage():
                raise AttributeError("No reference image")
            self._coords_refpixel = self.refimage.coords_to_pixel(*self.coords)
            
        return self._coords_refpixel
    
    def has_coords(self):
        """ """
        return self.coords is not None

    # // Host & Catalog
    @property
    def catdata(self):
        """ """
        return self._pstarget.catdata

    
    def host_coords(self):
        """ """
        return 
    
        self._refimage.coords_to_pixel(*self._pstarget.get_nearest_catdata()[["raMean","decMean"]].values[0])
        
    # // Image
    @property
    def dataimage(self):
        """ self.refimage.data """
        return self.refimage.data
    
    @property
    def refimage(self):
        """ """
        if not hasattr(self,"_refimage"):
            raise AttributeError("no reference image set. see download_reference or set_refimage")
        return self._refimage
    
    def has_refimage(self):
        """ """
        return hasattr(self,"_refimage") and self._refimage is not None

    # // PSF Image
    @property
    def psfimage(self):
        """ """
        if not hasattr(self,"_psfimage"):
            raise AttributeError("no psf image set. see build_pointsource_image ")
        return self._psfimage

    @property
    def fakeimage(self):
        """ """
        return self.dataimage + self.psfimage

    @property
    def segmap(self):
        """ Segmentation map of the fakeimage"""
        if not hasattr(self,"_segmap"):
            return None
            
        return self._segmap


