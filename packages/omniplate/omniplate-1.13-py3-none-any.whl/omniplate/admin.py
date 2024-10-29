"""Functions for general administration, mostly of data frames."""

import pandas as pd

import omniplate.omgenutils as gu


def initialiseprogress(self, experiment):
    """Initialise progress dictionary."""
    self.progress["ignoredwells"][experiment] = []
    self.progress["negativevalues"][experiment] = False


def makewellsdf(df_r):
    """Make a dataframe with the contents of the wells."""
    df = df_r[["experiment", "condition", "strain", "well"]].drop_duplicates()
    df = df.reset_index(drop=True)
    return df


def make_s(self, tmin=None, tmax=None, rdf=None):
    """
    Generate s dataframe.

    Calculates means and variances of all data types from raw data.

    Drop "original_experiment" and "experiment_id" because there should
    be one OD_mean for all experiment_ids.
    """
    if rdf is None:
        # restrict time
        if tmin and not tmax:
            rdf = self.r[self.r.time >= tmin]
        elif tmax and not tmin:
            rdf = self.r[self.r.time <= tmax]
        elif tmin and tmax:
            rdf = self.r[(self.r.time >= tmin) & (self.r.time <= tmax)]
        else:
            rdf = self.r
    # classify columns
    groupby_columns = ["experiment", "condition", "strain", "time"]
    good_columns = (
        groupby_columns
        + ["well"]
        + list(
            set([dtype for e in self.datatypes for dtype in self.datatypes[e]])
        )
    )
    # for common variables
    good_columns += [field for field in rdf.columns if "common_" in field]
    # find and drop remaining columns
    bad_columns = [col for col in rdf.columns if col not in good_columns]
    if bad_columns:
        rdf = rdf.drop(columns=bad_columns)
    # find means
    df1 = rdf.groupby(groupby_columns).mean(numeric_only=True).reset_index()
    for exp in self.allexperiments:
        for dtype in self.datatypes[exp]:
            df1 = df1.rename(columns={dtype: dtype + "_mean"})
    # find std
    df2 = rdf.groupby(groupby_columns).std(numeric_only=True).reset_index()
    for exp in self.allexperiments:
        for dtype in self.datatypes[exp]:
            df2 = df2.rename(columns={dtype: dtype + "_err"})
    return pd.merge(df1, df2)


def update_s(self):
    """Update means and errors of all datatypes from raw data."""
    # find tmin and tmax in case restrict_time has been called
    tmin = self.s.time.min()
    tmax = self.s.time.max()
    # recalculate s dataframe
    self.s = make_s(self, tmin, tmax)


def add_to_s(self, derivname, outdf):
    """
    Add dataframe of time series to s dataframe.

    Parameters
    ----------
    derivname: str
        Root name for statistic described by dataframe, such as "gr".
    outdf: dataframe
        Data to add.
    """
    gu.merge_df_into(
        self.s, outdf, ["experiment", "condition", "strain", "time"]
    )
    # to prevent fragmentation
    self.s = self.s.copy()


def add_dict_to_sc(self, statsdict):
    """Add one-line dict to sc dataframe."""
    statsdf = pd.DataFrame(statsdict, index=pd.RangeIndex(0, 1, 1))
    gu.merge_df_into(self.sc, statsdf, ["experiment", "condition", "strain"])
    # to prevent fragmentation
    self.sc = self.sc.copy()


def check_kwargs(kwargs):
    """Stop if final s missing from experiments, conditions, or strains."""
    if "condition" in kwargs:
        raise SystemExit("Use conditions not condition as an argument.")
    elif "strain" in kwargs:
        raise SystemExit("Use strains not strain as an argument.")
    elif "experiment" in kwargs:
        raise SystemExit("Use experiments not experiment as an argument.")


@property
def cols_to_underscore(self):
    """Replace spaces in column names of all dataframes with underscores."""
    for df in [self.r, self.s, self.sc]:
        df.columns = df.columns.str.replace(" ", "_")
