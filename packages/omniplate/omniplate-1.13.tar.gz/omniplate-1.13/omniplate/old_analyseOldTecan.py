import numpy as np


def analyseOldTecan(dfd, rcontents, experiment):
    """
    Parse data from an imported Excel file from older Tecan software.

    Typically the file is from a Tecan F200 or M200 plate reader.

    Parameters
    --
    dfd: dataframe
        Created by importing the data from a file using Panda's read_excel.
    rcontents: dataframe
        Created by analyseContentsofWells.
    experiment: string
        The name of the experiment.

    Returns
    ------
    rdict: list of dictionaries
        Describes the contents of the plate by experiment, condition, strain,
        time, and well.
    datatypes: list of strings
        Delineates all the types of data in the experiment and is minimally
        ['OD'].
    """
    # extract datatypes
    datatypes = [
        dfd[dfd.columns[0]]
        .iloc[
            np.nonzero(
                dfd[dfd.columns[0]]
                .str.startswith("Label", na=False)
                .to_numpy()
            )[0]
        ]
        .to_numpy()[0]
        .split(": ")[1]
    ]
    # extract times of measurements
    t = (
        dfd.loc[
            dfd[dfd.columns[0]].str.startswith("Time [s]", na=False),
            dfd.columns[1] :,
        ]
        .dropna(axis="columns")
        .mean()
        .to_numpy()
        .astype("float")
        / 3600.0
    )
    # deal with overflows
    df = dfd.replace("OVER", np.nan)
    cols = df.columns
    ## extract data
    # add to dataframe
    df.index = df[cols[0]]
    rdict = []
    for x in np.arange(1, 13):
        for y in "ABCDEFGH":
            well = y + str(x)
            if well in df.index:
                data = df.loc[well, cols[1] :].to_numpy(dtype="float")
                if data.ndim == 1:
                    data = data[None, :]
                if (
                    rcontents[well][0] is not None
                    and rcontents[well][1] is not None
                ):
                    for j in range(len(t)):
                        cons = {
                            "experiment": experiment,
                            "condition": rcontents[well][0],
                            "strain": rcontents[well][1],
                            "time": t[j],
                            "well": well,
                        }
                        dats = {
                            datatype: data[i, j]
                            for i, datatype in enumerate(datatypes)
                        }
                        cons.update(dats)
                        rdict.append(cons)
    return rdict, datatypes
