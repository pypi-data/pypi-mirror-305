import copy
from itertools import cycle

import numpy as np
from cycler import Cycler

from matplotlib import pyplot as plt, patches, cm
from matplotlib.colors import Normalize, BoundaryNorm, LinearSegmentedColormap
from matplotlib.lines import Line2D
import matplotlib.colors as mcolors
import matplotlib.patheffects as pe

from swmm_api import SwmmInput
from swmm_api.input_file import SEC
from swmm_api.input_file.macros import complete_vertices, links_dict
from swmm_api.input_file.section_labels import *
from swmm_api.input_file.sections import Polygon, SubCatchment, BackdropSection


def get_matplotlib_colormap(cmap, set_under='lightgray', set_bad='blackk'):
    cmap = copy.copy(plt.cm.get_cmap(cmap))

    if set_under:
        cmap.set_under(set_under)
    if set_bad:
        cmap.set_bad('black')
    return cmap


def get_color_mapper(cmap, vmin, vmax):
    norm = Normalize(vmin=vmin, vmax=vmax)
    return lambda x: cmap(norm(x))


def custom_color_mapper(cmap, vmin=None, vmax=None, set_under='lightgray', set_bad='black'):
    cmap = get_matplotlib_colormap(cmap, set_under, set_bad)
    return get_color_mapper(cmap, vmin=vmin, vmax=vmax)


def get_discrete_colormap(cmap):
    # cmap = copy.copy(plt.cm.get_cmap(cmap))  # define the colormap
    # extract all colors from the .jet map
    cmaplist = [cmap(i) for i in range(cmap.N)]
    # force the first color entry to be grey
    cmaplist[0] = (.85, .85, .85, 1.0)

    # create the new map
    cmap = LinearSegmentedColormap.from_list('Custom cmap', cmaplist, cmap.N)

    return cmap


def set_inp_dimensions(ax: plt.Axes, inp: SwmmInput):
    map_dim = inp[MAP]['DIMENSIONS']
    x_min, x_max = map_dim['lower-left X'], map_dim['upper-right X']
    delta_x = x_max - x_min
    y_min, y_max = map_dim['lower-left Y'], map_dim['upper-right Y']
    delta_y = y_max - y_min
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)


def init_empty_map_plot() -> (plt.Figure, plt.Axes):
    fig, ax = plt.subplots(layout='constrained')  # type: plt.Figure, plt.Axes
    ax.set_axis_off()
    ax.set_aspect('equal')
    return fig, ax


def get_auto_size_function(value_min, value_max, size_min, size_max):
    diff_values = value_max - value_min
    diff_size = size_max - size_min

    def new_size(value):
        if (diff_values == 0) or (diff_size == 0):
            return size_min
        return (value - value_min) / diff_values * diff_size + size_min

    return new_size


def darken_color(color):
    lc = mcolors.rgb_to_hsv(mcolors.to_rgb(color))

    if lc[2] > 0.5:
        lc[2] -= .5
    elif lc[2] <= .5:
        lc[2] /= 2

    return mcolors.hsv_to_rgb(lc)


def _get_mid_point_angle(x, y):
    distances = np.sqrt(np.diff(x) ** 2 + np.diff(y) ** 2)
    mid_distance = np.sum(distances) / 2
    cumulative_distances = np.cumsum(distances)

    for i, d in enumerate(cumulative_distances):
        if d >= mid_distance:
            t = (mid_distance - (cumulative_distances[i - 1] if i > 0 else 0)) / distances[i]
            x_mid = x[i] + t * (x[i + 1] - x[i])
            y_mid = y[i] + t * (y[i + 1] - y[i])
            dx, dy = x[i + 1] - x[i], y[i + 1] - y[i]
            angle = np.arctan2(dy, dx)
            break
    return x_mid, y_mid, np.degrees(angle)


def add_link_map(ax: plt.Axes, inp: SwmmInput,
                 line_width_default=1,
                 line_width_max=5,
                 make_width_proportional=False,

                 values_dict=None,

                 cmap=None,

                 value_min=None,
                 value_max=None,

                 discrete=False,

                 colorbar_kwargs=None,

                 add_arrows=False,

                 **kwargs):
    complete_vertices(inp)

    if VERTICES not in inp:
        # nothing to plot
        return

    # ---
    # style defaults
    link_style = {
        CONDUITS: {'color': 'yellow'},
        WEIRS: {'color': 'cyan'},
        ORIFICES: {'color': 'lightpink'},
        PUMPS: {'color': 'sienna'},
        OUTLETS: {'color': 'violet'},
    }
    for k, v in link_style.items():
        v['border_color'] = darken_color(v['color'])

    # ---
    kwargs.setdefault('solid_capstyle', 'round')
    kwargs.setdefault('solid_joinstyle', 'round')

    di_links = links_dict(inp)

    if values_dict:
        if discrete:
            values = values_dict.values()
            values_convert = {v: i for i, v in enumerate(sorted(set(values)))}
            values_dict = {k: values_convert[v] for k, v in values_dict.items()}

        values = values_dict.values()

        if value_min is None:
            value_min = min(values)

        if value_max is None:
            value_max = max(values)

        new_width = get_auto_size_function(value_min, value_max, line_width_default, line_width_max)

        if cmap:
            get_color_from_value = custom_color_mapper(cmap, vmin=value_min, vmax=value_max)

    for link, vertices in inp[VERTICES].items():
        x, y = zip(*vertices.vertices)
        section_label = di_links[link]._section_label

        style = {}

        if values_dict and make_width_proportional:
            style['linewidth'] = new_width(values_dict.get(link, np.nan))
        else:
            style['linewidth'] = line_width_default

        if values_dict and cmap:
            style['color'] = get_color_from_value(values_dict.get(link, np.nan))
            line_border_color = darken_color(style['color'])
        else:
            style['color'] = link_style[section_label]['color']
            line_border_color = link_style[section_label]['border_color']

        ax.plot(x, y,
                **{**style, **kwargs},
                path_effects=[pe.Stroke(linewidth=style['linewidth'] + .7, foreground=line_border_color), pe.Normal()])

        if add_arrows:
            x_mid, y_mid, angle = _get_mid_point_angle(x, y)
            ax.plot(x_mid, y_mid, markeredgewidth=0.35, markersize=style['linewidth'] * 4,
                    marker=(3, 0, angle - 90), c=style['color'], markeredgecolor=line_border_color)

    if colorbar_kwargs is not None:
        if discrete:
            get_color_from_value = custom_color_mapper(cmap, vmin=value_min, vmax=value_max)
            if 'label' in colorbar_kwargs:
                colorbar_kwargs['title'] = colorbar_kwargs.pop('label')

            if ax.legend_ is not None:
                ax.add_artist(ax.legend_)

            add_custom_legend(ax, {label: {'color': get_color_from_value(value), 'lw': 1} for label, value in values_convert.items()},
                              **colorbar_kwargs)

        else:
            if 'title' in colorbar_kwargs:
                colorbar_kwargs['label'] = colorbar_kwargs.pop('title')

            colorbar_kwargs.setdefault('location', 'bottom')
            colorbar_kwargs.setdefault('pad', 0)
            colorbar_kwargs.setdefault('shrink', 0.3)
            ax.get_figure().colorbar(cm.ScalarMappable(Normalize(vmin=value_min, vmax=value_max), cmap), ax=ax, **colorbar_kwargs)


def add_subcatchment_map(ax: plt.Axes, inp: SwmmInput,
                         add_center_point=True,
                         center_point_kwargs=None,
                         use_pole_of_inaccessibility_as_center_point=False,

                         add_connector_line=True,
                         connector_line_kwargs=None,
                         add_connector_arrows=False,

                         values_dict=None,

                         cmap='cividis',
                         colorbar_kwargs=None,

                         value_min=None,
                         value_max=None,

                         discrete=False,

                         add_random_hatch=False,
                         **kwargs):
    if POLYGONS not in inp:
        return

    if COORDINATES in inp:
        points = dict(inp[COORDINATES])
    else:
        points = {}

    # all point from nodes and center point of polygons for connector lines
    if use_pole_of_inaccessibility_as_center_point:
        from shapely.algorithms.polylabel import polylabel
        points.update({poly.subcatchment: polylabel(poly.geo) for poly in inp[POLYGONS].values()})
    else:
        points.update({poly.subcatchment: poly.geo.centroid for poly in inp[POLYGONS].values()})

    # ---
    if add_random_hatch:
        hatches = cycle(['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*'])

        reset_hatch = 'hatch' not in kwargs

        import matplotlib as mpl
        mpl.rcParams['hatch.linewidth'] = 0.3

    # ---
    if values_dict:
        values = values_dict.values()

        if discrete:
            values_convert = {v: i for i, v in enumerate(sorted(set(values)))}
            values_dict = {k: values_convert[v] for k, v in values_dict.items()}
            values = values_dict.values()

        if value_min is None:
            value_min = min(values)

        if value_max is None:
            value_max = max(values)

        get_color_from_value = custom_color_mapper(cmap, vmin=value_min, vmax=value_max)

    for label, poly in inp[POLYGONS].items():  # type: Polygon

        # ----------------
        # sub-catchment polygon
        kwargs.setdefault('fill', True)
        kwargs.setdefault('linewidth', 0.5)
        kwargs.setdefault('alpha', 0.5)

        # ---
        if add_random_hatch:
            kwargs.setdefault('hatch', next(hatches) * 2)

        # ---
        if values_dict:
            kwargs['facecolor'] = get_color_from_value(values_dict.get(label, np.nan))
            kwargs['edgecolor'] = darken_color(kwargs['facecolor'])
        else:
            kwargs.setdefault('facecolor', 'lightgray')
            kwargs.setdefault('edgecolor', 'darkgrey')

        # ---
        ax.add_patch(patches.Polygon(poly.polygon, closed=True, **kwargs))

        # ---
        if add_random_hatch and reset_hatch:
            del kwargs['hatch']

        # ----------------
        # center point of sub-catchment
        if add_center_point:

            if center_point_kwargs is None:
                center_point_kwargs = {}

            center_point_kwargs.setdefault('marker', 's')
            center_point_kwargs.setdefault('markersize', 5)
            center_point_kwargs.setdefault('markeredgewidth', 0.5)
            center_point_kwargs.setdefault('fillstyle', 'none')
            center_point_kwargs.setdefault('alpha', 0.5)
            center_point_kwargs.setdefault('color', 'black')

            center = points[poly.subcatchment]
            ax.plot(center.x, center.y, lw=0, **center_point_kwargs)

        # ----------------
        # center connector to sub-catchment
        if add_connector_line:

            if connector_line_kwargs is None:
                connector_line_kwargs = {}
            connector_line_kwargs.setdefault('linestyle', '--')
            connector_line_kwargs.setdefault('color', 'black')
            connector_line_kwargs.setdefault('alpha', 0.5)
            connector_line_kwargs.setdefault('lw', 0.5)

            subcatch = inp[SUBCATCHMENTS][poly.subcatchment]  # type: SubCatchment
            outlet_point = points[subcatch.outlet]
            center = points[poly.subcatchment]
            ax.plot([center.x, outlet_point.x], [center.y, outlet_point.y], **connector_line_kwargs)

            if add_connector_arrows:
                x_mid, y_mid, angle = _get_mid_point_angle([center.x, outlet_point.x], [center.y, outlet_point.y])
                ax.plot(x_mid, y_mid, markeredgewidth=0.4, markersize=4,
                        marker=(3, 0, angle - 90), **connector_line_kwargs)

    if colorbar_kwargs is not None:
        if discrete:
            if 'label' in colorbar_kwargs:
                colorbar_kwargs['title'] = colorbar_kwargs.pop('label')

            if ax.legend_ is not None:
                ax.add_artist(ax.legend_)
            add_custom_legend(ax, {label: {'color': get_color_from_value(value), 'marker': 's', 'lw': 0} for label, value in values_convert.items()},
                              **colorbar_kwargs)

        else:
            if 'title' in colorbar_kwargs:
                colorbar_kwargs['label'] = colorbar_kwargs.pop('title')

            colorbar_kwargs.setdefault('location', 'bottom')
            colorbar_kwargs.setdefault('pad', 0)
            colorbar_kwargs.setdefault('shrink', 0.3)
            ax.get_figure().colorbar(cm.ScalarMappable(Normalize(vmin=value_min, vmax=value_max), cmap), ax=ax, **colorbar_kwargs)


def add_node_map(ax: plt.Axes, inp: SwmmInput,

                 size_default=20,  # = size_min
                 size_max=40,
                 make_size_proportional=False,

                 values_dict=None,

                 cmap=None,  # if set - make color based on values_dict

                 value_min=None,
                 value_max=None,

                 discrete=False,

                 colorbar_kwargs=None,

                 **kwargs):
    """
    Only one marker per scatter possible.
    """
    if COORDINATES not in inp:
        # nothing to plot
        return

    coords = inp[COORDINATES].frame

    # ---
    # style defaults
    node_style = {
        JUNCTIONS: {'marker': 'o', 'c': 'blue'},
        STORAGE: {'marker': 's', 'c': 'lime'},
        OUTFALLS: {'marker': '^', 'c': 'red'},
    }
    for k, v in node_style.items():
        v['edgecolor'] = darken_color(v['c'])

    # ---
    if values_dict:
        if discrete:
            values = values_dict.values()
            values_convert = {v: i for i, v in enumerate(sorted(set(values)))}
            values_dict = {k: values_convert[v] for k, v in values_dict.items()}

        values = values_dict.values()

        if value_min is None:
            value_min = min(values)

        if value_max is None:
            value_max = max(values)

        new_size = get_auto_size_function(value_min, value_max, size_default, size_max)

    # -------------
    kwargs.setdefault('s', size_default)
    kwargs.setdefault('linewidths', 0.5)
    kwargs.setdefault('zorder', 2)

    # -------------
    for section in [JUNCTIONS, STORAGE, OUTFALLS]:
        if section not in inp:
            continue

        coords_in_sec = coords[coords.index.isin(inp[section].keys())]

        if values_dict:
            node_values = [values_dict.get(n, np.nan) for n in coords_in_sec.index]

            # ---
            if make_size_proportional:
                kwargs['s'] = [new_size(i) for i in node_values]

            # ---
            if cmap is not None:
                kwargs.update(
                    dict(
                        c=node_values,
                        cmap=cmap,
                        vmin=value_min,
                        vmax=value_max,
                        edgecolor='black',
                    )
                )

        ax.scatter(x=coords_in_sec.x, y=coords_in_sec.y, **{**node_style[section], **kwargs}, label=section)

    # ---------------------
    if colorbar_kwargs is not None:
        if discrete:
            get_color_from_value = custom_color_mapper(cmap, vmin=value_min, vmax=value_max)
            if 'label' in colorbar_kwargs:
                colorbar_kwargs['title'] = colorbar_kwargs.pop('label')

            if ax.legend_ is not None:
                ax.add_artist(ax.legend_)

            add_custom_legend(ax, {label: {'color': get_color_from_value(value), 'marker': 's', 'lw': 0} for label, value in values_convert.items()},
                              **colorbar_kwargs)

        else:
            if 'title' in colorbar_kwargs:
                colorbar_kwargs['label'] = colorbar_kwargs.pop('title')

            colorbar_kwargs.setdefault('location', 'bottom')
            colorbar_kwargs.setdefault('pad', 0)
            colorbar_kwargs.setdefault('shrink', 0.3)
            ax.get_figure().colorbar(ax.collections[0], ax=ax, **colorbar_kwargs)
    else:
        if ax.legend_ is not None:
            ax.add_artist(ax.legend_)
        ax.legend()


def add_node_labels(ax: plt.Axes, inp: SwmmInput, x_offset=0, y_offset=0, **kwargs):
    """
    Add the labels of the nodes to the map plot as text.

    Works inplace.

    Args:
        ax ():
        inp (swmm_api.SwmmInput): SWMM input-file data.
        x_offset ():
        y_offset ():
        **kwargs ():
    """
    if 'horizontalalignment' not in kwargs or 'ha' not in kwargs:
        kwargs['ha'] = 'center'

    if 'verticalalignment' not in kwargs or 'va' not in kwargs:
        kwargs['va'] = 'baseline'

    for name, node in inp.COORDINATES.items():
        ax.text(node.x + x_offset, node.y + y_offset, name, **kwargs)


def add_custom_legend(ax, lines_dict, **kwargs):
    """
    lines_dict:
    { label in legend: {line_dict ie: color, marker, linewidth, linestyle, ...) }
    kwargs: for legend
    """
    lines = []
    labels = []
    for label, line in lines_dict.items():
        labels.append(label)
        if isinstance(line, Line2D):
            lines.append(line)
        else:
            lines.append(Line2D([0], [0], **line))
    return ax.legend(lines, labels, **kwargs)


def add_backdrop(ax, inp):
    """
    Add the backdrop image to the plot

    Args:
        ax (plt.Axes):
        inp (swmm_api.SwmmInput): SWMM input-file data.
    """
    if SEC.BACKDROP in inp:
        k = BackdropSection.KEYS
        fn = inp.BACKDROP[k.FILE]
        x0, y0, x1, y1 = inp.BACKDROP[k.DIMENSIONS]
        im = plt.imread(fn)
        ax.imshow(im, extent=[x0, x1, y0, y1])


def plot_map(inp):
    """
    Get the map-plot of the system.

    Args:
        inp (swmm_api.SwmmInput): SWMM input-file data.

    Returns:
        (plt.Figure, plt.Axes): figure and axis of the plot
    """
    fig, ax = init_empty_map_plot()
    add_link_map(ax, inp)
    add_subcatchment_map(ax, inp)
    add_node_map(ax, inp)
    add_node_labels(ax, inp)
    return fig, ax
