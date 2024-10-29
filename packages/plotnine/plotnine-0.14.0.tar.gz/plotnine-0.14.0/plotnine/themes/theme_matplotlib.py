from ..options import get_option
from .elements import element_blank, element_line, element_rect, element_text
from .theme import theme


class theme_matplotlib(theme):
    """
    The default matplotlib look and feel.

    The theme can be used (and has the same parameter
    to customize) like a [](`matplotlib.rc_context`) manager.

    Parameters
    ----------
    rc : dict
        rcParams which should be applied on top of mathplotlib default.
    fname : str
        Filename to a matplotlibrc file
    use_defaults : bool
        If `True` (the default) resets the plot setting
        to the (current) `matplotlib.rcParams` values
    """

    def __init__(self, rc=None, fname=None, use_defaults=True):
        import matplotlib as mpl

        m = get_option("base_margin")
        base_size = mpl.rcParams.get("font.size", 11)
        linewidth = mpl.rcParams.get("grid.linewidth", 0.8)

        super().__init__(
            line=element_line(size=linewidth),
            rect=element_rect(size=linewidth),
            text=element_text(
                size=base_size,
                linespacing=1,
                rotation=0,
                margin={},
            ),
            aspect_ratio=get_option("aspect_ratio"),
            axis_text=element_text(margin={"t": 2.4, "r": 2.4, "units": "pt"}),
            axis_title_x=element_text(
                va="bottom", ha="center", margin={"t": m, "units": "fig"}
            ),
            axis_line=element_blank(),
            axis_title_y=element_text(
                angle=90,
                va="center",
                ha="left",
                margin={"r": m, "units": "fig"},
            ),
            dpi=get_option("dpi"),
            figure_size=get_option("figure_size"),
            legend_background=element_rect(color="none"),
            legend_box_margin=0,
            legend_box_spacing=m * 3,
            legend_key_spacing_x=6,
            legend_key_spacing_y=2,
            legend_frame=element_rect(color="black"),
            legend_key=element_blank(),
            legend_key_size=16,
            legend_ticks_length=0.2,
            legend_margin=0,
            legend_position="right",
            legend_spacing=10,
            legend_text=element_text(
                margin={
                    "t": m / 2,
                    "b": m / 2,
                    "l": m / 2,
                    "r": m / 2,
                    "units": "fig",
                }
            ),
            legend_ticks=element_line(color="black"),
            legend_title=element_text(
                ha="left",
                margin={
                    "t": m,
                    "b": m / 2,
                    "l": m * 2,
                    "r": m * 2,
                    "units": "fig",
                },
            ),
            panel_border=element_rect(color="black"),
            panel_grid=element_blank(),
            panel_spacing=m,
            plot_caption=element_text(
                ha="right",
                va="bottom",
                ma="left",
                margin={"t": m, "units": "fig"},
            ),
            plot_margin=m,
            plot_subtitle=element_text(
                size=base_size * 0.9,
                va="top",
                ma="left",
                margin={"b": m, "units": "fig"},
            ),
            plot_title=element_text(
                va="top",
                ma="left",
                margin={"b": m, "units": "fig"},
            ),
            strip_align=0,
            strip_background=element_rect(
                fill="#D9D9D9", color="black", size=linewidth
            ),
            strip_text=element_text(
                margin={
                    "t": 1 / 3,
                    "b": 1 / 3,
                    "l": 1 / 3,
                    "r": 1 / 3,
                    "units": "lines",
                },
            ),
            strip_text_y=element_text(rotation=-90),
            complete=True,
        )

        if use_defaults:
            _copy = mpl.rcParams.copy()
            if "tk.pythoninspect" in _copy:
                del _copy["tk.pythoninspect"]
            self._rcParams.update(_copy)

        if fname:
            self._rcParams.update(mpl.rc_params_from_file(fname))
        if rc:
            self._rcParams.update(rc)
