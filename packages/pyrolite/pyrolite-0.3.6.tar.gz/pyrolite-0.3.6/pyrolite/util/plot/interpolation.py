"""
Line interpolation for matplotlib lines and paths.
"""

import matplotlib.collections
import matplotlib.path
import numpy as np
import scipy.interpolate

from ..log import Handle

logger = Handle(__name__)


def interpolate_path(
    path, resolution=100, periodic=False, aspath=True, closefirst=False, **kwargs
):
    """
    Obtain the interpolation of an existing path at a given
    resolution. Keyword arguments are forwarded to
    :func:`scipy.interpolate.splprep`.

    Parameters
    -----------
    path : :class:`matplotlib.path.Path`
        Path to interpolate.
    resolution :class:`int`
        Resolution at which to obtain the new path. The verticies of
        the new path will have shape (`resolution`, 2).
    periodic : :class:`bool`
        Whether to use a periodic spline.
    periodic : :class:`bool`
        Whether to return a :code:`matplotlib.path.Path`, or simply
        a tuple of x-y arrays.
    closefirst : :class:`bool`
        Whether to first close the path by appending the first point again.

    Returns
    --------
    :class:`matplotlib.path.Path` | :class:`tuple`
        Interpolated :class:`~matplotlib.path.Path` object, if
        `aspath` is :code:`True`, else a tuple of x-y arrays.
    """
    x, y = path.vertices.T
    if x.size > 4:
        if closefirst:
            x = np.append(x, x[0])
            y = np.append(y, y[0])
        # s=0 forces the interpolation to go through every point

        tck, _ = scipy.interpolate.splprep(
            [x[:-1], y[:-1]], s=0, per=periodic, **kwargs
        )
        xi, yi = scipy.interpolate.splev(np.linspace(0.0, 1.0, resolution), tck)
        # could get control points for path and construct codes here
        codes = None
        pth = matplotlib.path.Path(np.vstack([xi, yi]).T, codes=codes)
        if aspath:
            return pth
        else:
            return pth.vertices.T
    else:
        return path.vertices.T


def interpolated_patch_path(patch, resolution=100, **kwargs):
    """
    Obtain the periodic interpolation of the existing path of a patch at a
    given resolution.

    Parameters
    -----------
    patch : :class:`matplotlib.patches.Patch`
        Patch to obtain the original path from.
    resolution :class:`int`
        Resolution at which to obtain the new path. The verticies of the new path
        will have shape (`resolution`, 2).

    Returns
    --------
    :class:`matplotlib.path.Path`
        Interpolated :class:`~matplotlib.path.Path` object.
    """
    pth = patch.get_path()
    tfm = patch.get_transform()
    pathtfm = tfm.transform_path(pth)
    return interpolate_path(
        pathtfm, resolution=resolution, aspath=True, periodic=True, **kwargs
    )


def get_contour_paths(src, resolution=100, minsize=3):
    """
    Extract the paths of contours from a contour plot.

    Parameters
    ------------
    ax : :class:`matplotlib.axes.Axes` |
        Axes to extract contours from.
    resolution : :class:`int`
        Resolution of interpolated splines to return.

    Returns
    --------
    contourspaths : :class:`list` (:class:`list`)
        List of lists, each represnting one line collection (a single contour). In the
        case where this contour is multimodal, there will be multiple paths for each
        contour.
    contournames : :class:`list`
        List of names for contours, where they have been labelled, and there are no
        other text artists on the figure.
    contourstyles : :class:`list`
        List of styles for contours.

    Notes
    ------
        This method assumes that contours are the only
        :code:`matplotlib.collections.LineCollection` objects within an axes;
        and when this is not the case, additional non-contour objects will be returned.
    """
    if isinstance(src, matplotlib.axes.Axes):

        def _iscontour(c):
            # contours/default lines don't have markers - allows distinguishing scatter
            return (
                isinstance(c, matplotlib.collections.PathCollection)
                and c.get_sizes().size == 0
            ) or isinstance(c, matplotlib.collections.LineCollection)

        linecolls = [
            c for c in src.collections if (_iscontour(c) and len(c.get_paths()))
        ]
        names = [None for lc in linecolls]
        if all([len(a.get_text()) for a in src.texts]):
            if len(src.texts) == len(linecolls):
                names = [a.get_text() for a in src.texts]
            else:
                logger.debug("Can't line up labels/text with contours.")
    elif isinstance(src, matplotlib.contour.ContourSet):
        names = src.labelTexts
        linecolls = src.collections
        linecolls = [c for c in src.collections if len(c.get_paths())]

    rgba = [lc.get_edgecolors() for lc in linecolls]
    styles = [{"color": c} for c in rgba]
    return (
        [
            [
                interpolate_path(
                    p,
                    resolution=resolution,
                    periodic=True,
                    aspath=False,
                )
                for p in lc.get_paths()
            ]
            for lc in linecolls
        ],
        names,
        styles,
    )
