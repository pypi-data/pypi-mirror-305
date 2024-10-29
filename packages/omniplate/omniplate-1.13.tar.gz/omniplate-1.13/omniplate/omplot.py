"""Functions to plot from the data frames."""

import colorcet
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

import omniplate.admin as admin
import omniplate.clogger as clogger
import omniplate.omerrors as errors
import omniplate.omgenutils as gu
import omniplate.sunder as sunder


@clogger.log
def plot(
    self,
    x="time",
    y="OD",
    hue="strain",
    style="condition",
    size=None,
    kind="line",
    col=None,
    row=None,
    height=5,
    aspect=1,
    xlim=None,
    ylim=None,
    figsize=False,
    returnfacetgrid=False,
    title=None,
    plate=False,
    wells=False,
    nonull=False,
    messages=False,
    sortby=False,
    distinct_colours=False,
    tmin=None,
    tmax=None,
    prettify_dict=None,
    experiments="all",
    conditions="all",
    strains="all",
    experimentincludes=False,
    experimentexcludes=False,
    conditionincludes=False,
    conditionexcludes=False,
    strainincludes=False,
    strainexcludes=False,
    **kwargs,
):
    """
    Plot from the underlying dataframes (chosen automatically).

    Seaborn's relplot is used, which is described at
    https://seaborn.pydata.org/generated/seaborn.relplot.html

    Parameters
    ----------
    x: string
        The variable - column of the dataframe - for the x-axis.
    y: string
        The variable - column of the dataframe - for y-axis.
    hue: string
        The variable whose variation will determine the colours of the
        lines plotted. From Seaborn.
    style: string
        The variable whose variation will determine the style of each line.
        From Seaborn.
    size: string
        The variable whose vairation will determine the size of each
        marker. From Seaborn.
    kind: string
        Either 'line' or 'scatter', which determines the type of plot.
        From Seaborn.
    col: string, optional
        The variable that varies over the columns in a multipanel plot.
        From Seaborn.
    row: string, optional
        The variable that varies over the rows in a multipanel plot.
        From Seaborn.
    height: float, optional
        The height of the individual panels in a multipanel plot.
        From Seaborn.
    aspect: float, optional
        The aspect ratio of the individual panels in a multipanel plot.
        From Seaborn.
    xlim: list of two floats, optional
        The minimal and maximal x-value, such as [0, None]
    ylim: list of two floats, optional
        The minimal and maximal y-value, such as [0, None]
    figsize: tuple, optional
        A tuple of (width, height) for the size of figure.
        Ignored if wells= True or plate= True.
    returnfacetgrid: boolean, optional
        If True, return Seaborn's facetgrid object created by relplot
    title: float, optional
        The title of the plot (overwrites any default titles).
    plate: boolean, optional
        If True, data for each well for a whole plate are plotted in one
        figure.
    wells: boolean, optional
        If True, data for the individual wells is shown.
    nonull: boolean, optional
        If True, 'Null' strains are not plotted.
    sortby: list of strings, optional
        A list of columns to sort the data in the dataframe and passed to
        pandas sort_values.
    messsages: boolean, optional
        If True, print warnings for any data requested but not found.
    distinct_colours: boolean, optional
        If True, try to make neighbouring colours in the plot distinct
        rather than graded.
    tmin: float, optional
        If specifed, restrict the data to times greater than tmin.
    tmax: float, optional
        If specifed, restrict the data to times less than tmax.
    prettify_dict: dict, optional
        To replace the x- and y-axis labels:
            e.g., {"time": "time (h)", "OD": "optical density"}
    experiments: string or list of strings
        The experiments to include.
    conditions: string or list of strings
        The conditions to include.
    strains: string or list of strings
        The strains to include.
    experimentincludes: string, optional
        Selects only experiments that include the specified string in
        their name.
    experimentexcludes: string, optional
        Ignores experiments that include the specified string in their
        name.
    conditionincludes: string, optional
        Selects only conditions that include the specified string in their
        name.
    conditionexcludes: string, optional
        Ignores conditions that include the specified string in their name.
    strainincludes: string, optional
        Selects only strains that include the specified string in their
        name.
    strainexcludes: string, optional
        Ignores strains that include the specified string in their name.
    kwargs: for Seaborn's relplot
        https://seaborn.pydata.org/generated/seaborn.relplot.html

    Returns
    -------
    sfig: Seaborn's facetgrid object generated by relplot if
    returnfacetgrid= True

    Examples
    --------
    >>> p.plot(y= 'OD', plate= True)
    >>> p.plot(y= 'OD', wells= True, strainincludes= 'Gal10:GFP')
    >>> p.plot(y= 'OD')
    >>> p.plot(x= 'OD', y= 'gr')
    >>> p.plot(y= 'cGFPperOD', nonull= True, ymin= 0)
    >>> p.plot(y= 'cGFPperOD', conditionincludes= '2% Mal',
    ...        hue= 'strain')
    >>> p.plot(y= 'cmCherryperOD', conditions= ['0.5% Mal',
    ...        '1% Mal'], hue= 'strain', style= 'condition',
    ...         nonull= True, strainincludes= 'mCherry')
    >>> p.plot(y= 'cGFPperOD', col= 'experiment')
    >>> p.plot(y= 'max gr')
    """
    admin.check_kwargs(kwargs)
    # choose the correct dataframe
    basedf, dfname = plotfinddf(self, x, y, tmin, tmax)
    # get experiments, conditions and strains
    exps, cons, strs = sunder.getall(
        self,
        experiments,
        experimentincludes,
        experimentexcludes,
        conditions,
        conditionincludes,
        conditionexcludes,
        strains,
        strainincludes,
        strainexcludes,
        nonull,
    )
    # choose the right type of plot
    if plate:
        dtype = y if x == "time" else x
        plotplate(self, basedf, exps, dtype)
    elif wells:
        plot_wells(
            x,
            y,
            basedf,
            exps,
            cons,
            strs,
            style=style,
            size=size,
            kind=kind,
            col=col,
            row=row,
            xlim=xlim,
            ylim=ylim,
            title=title,
            figsize=figsize,
            messages=messages,
            distinct_colours=distinct_colours,
            prettify_dict=prettify_dict,
            **kwargs,
        )
    elif dfname == "s" or dfname == "r":
        sfig = plot_rs(
            x,
            y,
            basedf,
            exps,
            cons,
            strs,
            hue=hue,
            style=style,
            size=size,
            kind=kind,
            col=col,
            row=row,
            height=height,
            aspect=aspect,
            xlim=xlim,
            ylim=ylim,
            title=title,
            figsize=figsize,
            sortby=sortby,
            returnfacetgrid=returnfacetgrid,
            distinct_colours=distinct_colours,
            prettify_dict=prettify_dict,
            **kwargs,
        )
        if returnfacetgrid:
            return sfig
    elif dfname == "sc":
        plot_sc(
            x,
            y,
            basedf,
            exps,
            cons,
            strs,
            hue=hue,
            style=style,
            size=size,
            kind=kind,
            col=col,
            row=row,
            height=height,
            aspect=aspect,
            xlim=xlim,
            ylim=ylim,
            figsize=figsize,
            title=title,
            sortby=sortby,
            distinct_colours=distinct_colours,
            prettify_dict=prettify_dict,
            **kwargs,
        )
    else:
        raise errors.PlotError("No data found")


def plotplate(self, basedf, exps, dtype):
    """
    Plot the data for each well following the layout of a 96-well plate.

    Parameters
    ----------
    self: platereader object
    basedf: DataFrame
        The r dataframe.
    exps: float
        The name of the experiments.
    dtype: float
        The data type to be plotted: 'OD', 'GFP', etc.
    """
    if exps == ["__combined__"]:
        exps = list(self.experiment_map.keys())
        experiment_column = "original_experiment"
    else:
        experiment_column = "experiment"
    for e in exps:
        plt.figure()
        # first create an empty plate - in case of missing wells
        ax = []
        for rowl in range(8):
            for coll in np.arange(1, 13):
                sindex = coll + 12 * rowl
                axi = plt.subplot(8, 12, sindex)
                ax.append(axi)
                plt.tick_params(labelbottom=False, labelleft=False)
                # label well locations
                for j in range(12):
                    if sindex == j + 1:
                        plt.title(j + 1)
                for j, k in enumerate(np.arange(1, 96, 12)):
                    if sindex == k:
                        plt.ylabel("ABCDEFGH"[j] + " ", rotation=0)
        # fill in the wells that have been measured
        for pl in basedf.query(f"{experiment_column} == @e")["well"].unique():
            if experiment_column == "experiment":
                well_loc = pl
            else:
                well_loc = pl.split("_")[1]
            rowl = "ABCDEFGH".index(well_loc[0])
            coll = int(well_loc[1:])
            sindex = coll + 12 * rowl
            wd = basedf.query(f"{experiment_column} == @e and well == @pl")
            ax[sindex - 1].plot(
                wd["time"].to_numpy(), wd[dtype].to_numpy(), "-"
            )
        plt.suptitle(e + ": " + dtype)
        plt.show(block=False)


def plot_wells(
    x,
    y,
    basedf,
    exps,
    cons,
    strs,
    style="condition",
    size=None,
    kind="line",
    col=None,
    row=None,
    xlim=None,
    ylim=None,
    title=None,
    figsize=None,
    messages=False,
    distinct_colours=False,
    prettify_dict=None,
    **kwargs,
):
    """
    Plot data from the individual wells.

    Data for each experiment, condition, and strain are plotted in
    a separate figure unless row and col are specified.
    """
    for e in exps:
        if row and col:
            # use facetgrid to show multiple plots simultaneously
            df = basedf.query(
                "experiment == @e and condition == @cons and strain == @strs"
            )
            sfig = sns.FacetGrid(df, row=row, col=col)
            for (row_var, col_var), facet_df in df.groupby([row, col]):
                ax = sfig.axes[
                    sfig.row_names.index(row_var),
                    sfig.col_names.index(col_var),
                ]
                sns.lineplot(x=x, y=y, hue="well", data=facet_df, ax=ax)
                ax.set(xlabel="", ylabel="")
            if prettify_dict is not None:
                sfig.set_axis_labels(
                    prettify_dict.get(x, x), prettify_dict.get(y, y)
                )
            else:
                sfig.set_axis_labels(x, y)
            sfig.set_titles()
            if title:
                sfig.fig.suptitle(title)
            else:
                sfig.fig.suptitle(e)
            if xlim is not None:
                plt.xlim(xlim)
            if ylim is not None:
                plt.ylim(ylim)
            if figsize and len(figsize) == 2:
                sfig.fig.set_figwidth(figsize[0])
                sfig.fig.set_figheight(figsize[1])
            plt.tight_layout()
            plt.show(block=False)
        else:
            # create one plot for each strain and condition
            for c in cons:
                for s in strs:
                    df = basedf.query(
                        "experiment == @e and condition == @c and strain == @s"
                    )
                    if df.empty:
                        if messages:
                            print(e + ":", "No data found for", s, "in", c)
                    else:
                        if distinct_colours:
                            palette = sns.color_palette(
                                colorcet.glasbey, df.well.unique().size
                            )
                        else:
                            palette = None
                        sfig = sns.relplot(
                            x=x,
                            y=y,
                            data=df,
                            hue="well",
                            kind=kind,
                            style=style,
                            size=size,
                            palette=palette,
                            **kwargs,
                        )
                        if prettify_dict is not None:
                            sfig.set_xlabels(prettify_dict.get(x, x))
                            sfig.set_ylabels(prettify_dict.get(y, y))
                        if title:
                            sfig.fig.suptitle(title)
                        else:
                            sfig.fig.suptitle(e + ": " + s + " in " + c)
                        if xlim is not None:
                            plt.xlim(xlim)
                        if ylim is not None:
                            plt.ylim(ylim)
                        plt.show(block=False)


def plot_rs(
    x,
    y,
    basedf,
    exps,
    cons,
    strs,
    hue="strain",
    style="condition",
    size=None,
    kind="line",
    col=None,
    row=None,
    height=5,
    aspect=1,
    xlim=None,
    ylim=None,
    title=None,
    figsize=None,
    sortby=False,
    returnfacetgrid=False,
    distinct_colours=False,
    prettify_dict=None,
    **kwargs,
):
    """Plot time-series data from the .r or .s dataframes."""
    # plot time series
    df = basedf.query(
        "experiment == @exps and condition == @cons and strain == @strs"
    )
    if df.empty or df.isnull().all().all():
        # no data or data all NaN
        print("No data found.")
    else:
        if sortby:
            df = df.sort_values(by=gu.makelist(sortby))
        # add warnings for poor choice of seaborn's parameters - may cause
        # inadvertent averaging
        if hue == style:
            print(
                f'Warning: "hue" and "style" have both been set to {hue}"'
                '" and there may be unintended averaging.'
            )
        if (
            x != "commontime"
            and len(df["experiment"].unique()) > 1
            and hue != "experiment"
            and size != "experiment"
            and style != "experiment"
            and col != "experiment"
        ):
            print(
                "Warning: there are multiple experiments, but neither "
                '"hue", "style", nor "size" is set to "experiment" and there'
                " may be averaging over experiments."
            )

        if "units" not in kwargs:
            # try to augment df to allow seaborn to estimate errors
            df = augmentdf(df, y)
        # plot
        if distinct_colours:
            palette = sns.color_palette(
                colorcet.glasbey, df[hue].unique().size
            )
            kwargs["palette"] = palette
        # remove conditions and strains that are all nan
        cdf = (
            df.groupby(["experiment", "condition", "strain"])[y]
            .apply(np.nanmean)
            .reset_index()
        )
        keep_conditions = list(cdf.dropna().condition.values)
        keep_strains = list(cdf.dropna().strain.values)
        # use seaborn to plot
        tdf = df[
            df.condition.isin(keep_conditions) & df.strain.isin(keep_strains)
        ]
        if not tdf.empty:
            sfig = sns.relplot(
                x=x,
                y=y,
                data=tdf,
                hue=hue,
                kind=kind,
                style=style,
                errorbar="sd",
                size=size,
                col=col,
                row=row,
                aspect=aspect,
                height=height,
                **kwargs,
            )
            if prettify_dict is not None:
                sfig.set_xlabels(prettify_dict.get(x, x))
                sfig.set_ylabels(prettify_dict.get(y, y))
            if title:
                sfig.fig.suptitle(title)
            if xlim is not None:
                sfig.set(xlim=xlim)
            if ylim is not None:
                sfig.set(ylim=ylim)
            if figsize and len(figsize) == 2:
                sfig.fig.set_figwidth(figsize[0])
                sfig.fig.set_figheight(figsize[1])
            plt.show(block=False)
            if returnfacetgrid:
                return sfig
            else:
                return None
        else:
            print("No data found.")


def plot_sc(
    x,
    y,
    basedf,
    exps,
    cons,
    strs,
    hue="strain",
    style="condition",
    size=None,
    kind="line",
    col=None,
    row=None,
    height=5,
    aspect=1,
    xlim=None,
    ylim=None,
    figsize=None,
    title=None,
    sortby=False,
    distinct_colours=False,
    prettify_dict=None,
    **kwargs,
):
    """Plot summary statistics from the .sc dataframe."""
    # plot summary stats
    df = basedf.query(
        "experiment == @exps and condition == @cons and strain == @strs"
    )
    xcols = df.columns[df.columns.str.startswith(x)]
    ycols = df.columns[df.columns.str.startswith(y)]
    cols_to_keep = (
        ["experiment", "condition", "strain"] + list(xcols) + list(ycols)
    )
    for field in [hue, style, size]:
        if isinstance(field, str):
            cols_to_keep += [field]
    df = df[np.unique(cols_to_keep)].dropna()
    if df.empty or df.isnull().all().all():
        # no data or data all NaN:
        print("No data found.")
    else:
        if sortby:
            df = df.sort_values(by=gu.makelist(sortby))
        if distinct_colours:
            palette = sns.color_palette(
                colorcet.glasbey, df[hue].unique().size
            )
        else:
            palette = None
        sfig = sns.relplot(
            x=x,
            y=y,
            data=df,
            hue=hue,
            kind="scatter",
            style=style,
            size=size,
            col=col,
            row=row,
            aspect=aspect,
            height=height,
            palette=palette,
            **kwargs,
        )
        if prettify_dict is not None:
            sfig.set_xlabels(prettify_dict.get(x, x))
            sfig.set_ylabels(prettify_dict.get(y, y))
        if xlim is not None:
            sfig.set(xlim=xlim)
        if ylim is not None:
            sfig.set(ylim=ylim)
        if row is None and col is None:
            # add error bars
            # find coordinates of points in relplot
            xc, yc = [], []
            for point_pair in sfig.ax.collections:
                for xp, yp in point_pair.get_offsets():
                    xc.append(xp)
                    yc.append(yp)
            # add error bars
            xerr = df[x + "_err"] if x + "_err" in df.columns else None
            yerr = df[y + "_err"] if y + "_err" in df.columns else None
            sfig.ax.errorbar(
                xc,
                yc,
                xerr=xerr,
                yerr=yerr,
                fmt=" ",
                ecolor="dimgray",
                alpha=0.5,
            )
        if title is not None:
            sfig.fig.suptitle(title)
        plt.show(block=False)


def plotfinddf(self, x, y, tmin, tmax):
    """
    Find the correct dataframe for plotting y versus x.

    Parameters
    ----------
    self: a platereader instance
    x: string
        Name of x-variable.
    y: string
        Name of y-variable.
    tmin: float
        If specifed, restrict the data to times greater than tmin.
    tmax: float
        If specifed, restrict the data to times less than tmax.

    Returns
    -------
    basedf: dataframe
        The dataframe that contains the x and y variables.
    dfname: string
        The name of the dataframe.
    """
    # choose the correct dataframe
    if hasattr(self, "r") and x in self.r.columns and y in self.r.columns:
        # raw data (with wells)
        basedf = self.r
        dfname = "r"
    elif x in self.s.columns and y in self.s.columns:
        # processed data (no wells)
        basedf = self.s
        dfname = "s"
    elif x in self.sc.columns and y in self.sc.columns:
        # summary stats
        basedf = self.sc
        dfname = "sc"
    else:
        raise errors.PlotError(
            f"The variables x= {x}"
            + f" and y= {y}"
            + " cannot be plotted against each other because they are not in "
            + " the same dataframe"
        )
    if (tmin or tmax) and "time" in basedf.columns:
        if tmin is not None and tmax is None:
            basedf = basedf[basedf.time >= tmin]
        elif tmin is None and tmax is not None:
            basedf = basedf[basedf.time <= tmax]
        elif tmin is not None and tmax is not None:
            basedf = basedf[(basedf.time >= tmin) & (basedf.time <= tmax)]
    return basedf, dfname


def augmentdf(df, datatype):
    """
    Augment dataframe to allow Seaborn to errors.

    Use 'err' (if present in the dataframe) to allow Seaborn to generate
    errors in relplot, otherwise returns original dataframe.

    Note we call seaborn with errorbar = "sd" and so use sqrt(3/2) * error
    because seaborn calculates the standard deviation from the augmented data
    (the mean, the mean + std, and the mean - std) and so gets
    std/sqrt(3/2) otherwise because there are three data points.
    """
    if datatype + "_err" in df:
        derr = datatype + "_err"
    elif "mean" in datatype and datatype.split("_mean")[0] + "_err" in df:
        derr = datatype.split("_mean")[0] + "_err"
    else:
        derr = False
        # returned if df is df_r
        return df
    if derr:
        df.insert(0, "augtype", "mean")
        mn = df[datatype].to_numpy()
        err = df[derr].to_numpy()
        # add std
        dfp = df.copy()
        dfp[datatype] = mn + np.sqrt(3 / 2) * err
        dfp["augtype"] = "+err"
        # minus std
        dfm = df.copy()
        dfm[datatype] = mn - np.sqrt(3 / 2) * err
        dfm["augtype"] = "-err"
        # concat
        df = pd.concat([df, dfp, dfm], ignore_index=True)
    return df


def savefigs(self, fname=None, onefile=True):
    """
    Save all current figures to PDF.

    Either all figures save to one file or each to a separate one.

    Parameters
    ----------
    fname: string, optional
        Name of file. If unspecified, the name of the experiment is used.
    onefile: boolean, optional
        If False, each figures is save to its own PDF file.

    Example
    -------
    >>> p.savefigs()
    >>> p.savefigs('figures.pdf')
    """
    if fname:
        if ".pdf" not in fname:
            fname += ".pdf"
        fname = str(self.wdirpath / fname)
    else:
        fname = str(self.wdirpath / ("".join(self.allexperiments) + ".pdf"))
    if onefile:
        gu.figs2pdf(fname)
    else:
        for i in plt.get_fignums():
            plt.figure(i)
            savename = str(plt.getp(plt.gcf(), "axes")[0].title).split("'")[1]
            savename = savename.replace(" ", "_")
            if savename == "":
                savename = "Whole_plate_Figure_" + str(i)
            print("Saving", savename)
            plt.savefig(str(self.wdirpath / (savename + ".pdf")))


@property
def close(self):
    """
    Close all figures.

    Example
    -------
    >>> p.close
    """
    plt.close("all")
