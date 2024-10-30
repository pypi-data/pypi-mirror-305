import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import xarray as xr
from matplotlib.dates import DateFormatter
from pandas import DataFrame
from scipy import stats
from skyfield import almanac
from skyfield import api
from tqdm import tqdm


def grid2d(x, y, v, xi=1, yi=1):
    """
    Function to grid data
    
    Parameters
    ----------
    x: data with data for the x dimension
    y: data with data for the y dimension
    v: data with data for the z dimension
    xi: Horizontal resolution for the gridding
    yi: Vertical resolution for the gridding
                
    Returns
    -------
    grid: z data gridded in x and y space with xi and yi resolution
    XI: x data gridded in x and y space with xi and yi resolution
    YI: y data gridded in x and y space with xi and yi resolution

    """
    if np.size(xi) == 1:
        xi = np.arange(np.nanmin(x), np.nanmax(x) + xi, xi)
    if np.size(yi) == 1:
        yi = np.arange(np.nanmin(y), np.nanmax(y) + yi, yi)
    raw = pd.DataFrame({'x': x, 'y': y, 'v': v}).dropna()
    grid = np.full([np.size(xi), np.size(yi)], np.nan)
    raw['xbins'], xbin_iter = pd.cut(raw.x, xi, retbins=True, labels=False)
    raw['ybins'], ybin_iter = pd.cut(raw.y, yi, retbins=True, labels=False)
    _tmp = raw.groupby(['xbins', 'ybins'])['v'].agg('median')
    grid[_tmp.index.get_level_values(0).astype(int), _tmp.index.get_level_values(1).astype(int)] = _tmp.values
    YI, XI = np.meshgrid(yi, xi)
    return grid, XI, YI


def updown_bias(ds, var='PSAL', v_res=1):
    """
    This function computes up and downcast averages for a specific variable

    Parameters
    ----------
    ds: xarray on OG1 format containing at least time, depth, latitude, longitude and the selected variable. 
        Data should not be gridded.
    var: Selected variable
    v_res: Vertical resolution for the gridding
                
    Returns
    -------
    df: pandas dataframe containing dc (Dive - Climb average), cd (Climb - Dive average) and depth

    """
    p = 1  # Horizontal resolution
    z = v_res  # Vertical resolution
    varG, profG, depthG = grid2d(ds.PROFILE_NUMBER, ds.DEPTH, ds[var], p, z)

    grad = np.diff(varG, axis=0)  # Horizontal gradients

    dc = np.nanmean(grad[0::2, :], axis=0)  # Dive - CLimb
    cd = np.nanmean(grad[1::2, :], axis=0)  # Climb - Dive

    df = pd.DataFrame(data={'dc': dc, 'cd': cd, 'depth': depthG[0, :]})
    return df


def plot_updown_bias(df: pd.DataFrame, ax: plt.Axes = None, xlabel='Temperature [C]', **kw: dict, ) -> tuple({plt.Figure, plt.Axes}):
    """
    This function can be used to plot the up and downcast differences computed with the updown_bias function
    
    Parameters
    ----------
    df: pandas dataframe containing dc (Dive - Climb average), cd (Climb - Dive average) and depth
    ax: axis to plot the data
    xlabel: label for the x-axis
    
    Returns
    -------
    A line plot comparing the day and night average over depth for the selected day
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(5, 5))
    else:
        fig = plt.gcf()

    ax.plot(df.dc, df.depth, label='Dive-Climb')
    ax.plot(df.cd, df.depth, label='Climb-Dive')
    ax.legend(loc=3)
    lims = np.abs(df.dc)
    ax.set_xlim(-np.nanpercentile(lims, 99.5), np.nanpercentile(lims, 99.5))
    ax.set_xlabel(xlabel)
    ax.set_ylim(df.depth.max() + 10, -df.depth.max() / 30)
    ax.grid()
    return fig, ax


def find_cline(var, depth_array):
    """
    Find the depth of the maximum vertical difference for a specified variables
    Input data has to be gridded
    """
    clin = np.where(np.abs(np.diff(np.nanmean(var, axis=0))) == np.nanmax(np.abs(np.diff(np.nanmean(var, axis=0)))))
    return np.round(depth_array[0, clin[0]], 1)


def plot_basic_vars(ds, v_res=1, start_prof=0, end_prof=-1):
    """
    This function plots the basic oceanographic variables temperature, salinity and density. A second plot is created and filled with oxygen and 
    chlorophyll data if available.
    
    Parameters
    ----------
    ds: xarray in OG1 format containing at least temperature, salinity and density and depth
    v_res: vertical resolution for the gridding. Horizontal resolution (by profile) is assumed to be 1
    start_prof: start profile used to compute the means that will be plotted. This can vary in case the dataset spread over a large timescale
                or region and subsections want to be plotted-1     
    end_prof: end profile used to compute the means that will be plotted. This can vary in case the dataset spread over a large timescale
              or region and subsections want to be plotted-1          
    
    Returns
    -------
    Line plots for the averages of the different variables. 
    Thermo, halo and pycnocline are computed and plotted. A sentence stating the depth of the clines is printed too
    """
    p = 1
    z = v_res
    tempG, profG, depthG = grid2d(ds.PROFILE_NUMBER, ds.DEPTH, ds.TEMP, p, z)
    salG, profG, depthG = grid2d(ds.PROFILE_NUMBER, ds.DEPTH, ds.PSAL, p, z)
    denG, profG, depthG = grid2d(ds.PROFILE_NUMBER, ds.DEPTH, ds.DENSITY, p, z)

    tempG = tempG[start_prof:end_prof, :]
    salG = salG[start_prof:end_prof, :]
    denG = denG[start_prof:end_prof, :]
    depthG = depthG[start_prof:end_prof, :]

    halo = find_cline(salG, depthG)
    thermo = find_cline(tempG, depthG)
    pycno = find_cline(denG, depthG)
    print(
        f'The thermocline, halocline and pycnocline are located at respectively {thermo}, {halo} and {pycno}m as shown in the plots as well')

    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    ax1 = ax[0].twiny()
    ax2 = ax[0].twiny()
    ax2.spines["top"].set_position(("axes", 1.2))
    ax[0].plot(np.nanmean(tempG, axis=0), depthG[0, :], c='blue')
    ax1.plot(np.nanmean(salG, axis=0), depthG[0, :], c='red')
    ax2.plot(np.nanmean(denG, axis=0), depthG[0, :], c='black')
    ax[0].axhline(thermo, linestyle='dashed', c='blue')
    ax1.axhline(halo, linestyle='dashed', c='red')
    ax2.axhline(pycno, linestyle='dashed', c='black')

    ax[0].set(xlabel=f'Average Temperature [C] \nbetween profile {start_prof} and {end_prof}', ylabel='Depth (m)')
    ax[0].tick_params(axis='x', colors='blue')
    ax[0].xaxis.label.set_color('blue')
    ax1.spines['bottom'].set_color('blue')
    ax1.set(xlabel=f'Average Salinity [PSU] \nbetween profile {start_prof} and {end_prof}')
    ax1.xaxis.label.set_color('red')
    ax1.spines['top'].set_color('red')
    ax1.tick_params(axis='x', colors='red')
    ax2.spines['bottom'].set_color('black')
    ax2.set(xlabel=f'Average Density [kg m-3] \nbetween profile {start_prof} and {end_prof}')
    ax2.xaxis.label.set_color('black')
    ax2.spines['top'].set_color('black')
    ax2.tick_params(axis='x', colors='black')

    if 'CHLA' in ds.variables:
        chlaG, profG, depthG = grid2d(ds.PROFILE_NUMBER, ds.DEPTH, ds.CHLA, p, z)
        chlaG = chlaG[start_prof:end_prof, :]
        ax2_1 = ax[1].twiny()
        ax2_1.plot(np.nanmean(chlaG, axis=0), depthG[0, :], c='green')
        ax2_1.set(xlabel=f'Average Chlorophyll-a [mg m-3] \nbetween profile {start_prof} and {end_prof}')
        ax2_1.xaxis.label.set_color('green')
        ax2_1.spines['top'].set_color('green')
        ax2_1.tick_params(axis='x', colors='green')
    else:
        ax[1].text(0.3, 0.7, 'Chlorophyll data unavailable', va='top', transform=ax[1].transAxes)

    if 'DOXY' in ds.variables:
        oxyG, profG, depthG = grid2d(ds.PROFILE_NUMBER, ds.DEPTH, ds.DOXY, p, z)
        oxyG = oxyG[start_prof:end_prof, :]
        ax[1].plot(np.nanmean(oxyG, axis=0), depthG[0, :], c='orange')
        ax[1].set(xlabel=f'Average Oxygen [mmol m-3] \nbetween profile {start_prof} and {end_prof}')
        ax[1].xaxis.label.set_color('orange')
        ax[1].spines['top'].set_color('orange')
        ax[1].tick_params(axis='x', colors='orange')
        ax[1].spines['bottom'].set_color('orange')
    else:
        ax[1].text(0.3, 0.5, 'Oxygen data unavailable', va='top', transform=ax[1].transAxes)

    [a.set_ylim(depthG.max() + 10, -5) for a in ax]
    [a.grid() for a in ax]
    return fig, ax


def optics_first_check(ds, var='CHLA'):
    """
    Function to assess any drift in deep optics data and the presence of any possible negative data
    This function returns plots and text
    """
    if var not in ds.variables:
        print(
            f"{var} does not exist in the dataset. Make sure the spelling is correct or add this variable to your dataset")
        return
    # Check how much negative data there is
    neg_chl = np.round((len(np.where(ds[var] < 0)[0]) * 100) / len(ds[var]), 1)
    if neg_chl > 0:
        print(f'{neg_chl}% of scaled {var} data is negative, consider recalibrating data')
        # Check where the negative values occur and if we just see them at specific time of the mission or not
        start = ds.TIME[np.where(ds[var] < 0)][0]
        end = ds.TIME[np.where(ds[var] < 0)][-1]
        min_z = ds.DEPTH[np.where(ds[var] < 0)].min().values
        max_z = ds.DEPTH[np.where(ds[var] < 0)].max().values
        print(f'Negative data in present from {str(start.values)[:16]} to {str(end.values)[:16]}')
        print(f'Negative data is present between {"%.1f" % np.round(min_z, 1)} and {"%.1f" % np.round(max_z, 1)} ')
    else:
        print(f'There is no negative scaled {var} data, recalibration and further checks are still recommended ')
    # Check if there is any missing data throughout the mission
    if len(ds.TIME) != len(ds[var].dropna(dim='N_MEASUREMENTS').TIME):
        print(f'{var} data is missing for part of the mission')  # Add to specify where the gaps are
    else:
        print(f'{var} data is present for the entire mission duration')
    # Check bottom dark count and any drift there
    bottom_opt_data = ds[var].where(ds[var].DEPTH > ds.DEPTH.max() - (ds.DEPTH.max() * 0.1)).dropna(
        dim='N_MEASUREMENTS')
    slope, intercept, r_value, p_value, std_err = stats.linregress(np.arange(0, len(bottom_opt_data)), bottom_opt_data)
    ax = sns.regplot(data=ds, x=np.arange(0, len(bottom_opt_data)), y=bottom_opt_data,
                     scatter_kws={"color": "grey"},
                     line_kws={"color": "red", "label": "y={0:.8f}x+{1:.5f}".format(slope, intercept)},
                     )
    ax.legend(loc=2)
    ax.grid()
    ax.set(ylim=(np.nanpercentile(bottom_opt_data, 0.5), np.nanpercentile(bottom_opt_data, 99.5)),
           xlabel='Measurements',
           ylabel=var)
    percentage_change = (((slope * len(bottom_opt_data) + intercept) - intercept) / abs(intercept)) * 100

    if abs(percentage_change) >= 1:
        print(
            'Data from the deepest 10% of data has been analysed and data does not seem perfectly stable. An alternative solution for dark counts has to be considered. \nMoreover, it is recommended to check the sensor has this may suggest issues with the sensor (i.e water inside the sensor, temporal drift etc)')
        print(
            f'Data changed (increased or decreased) by {"%.1f" % np.round(percentage_change, 1)}% from the beginning to the end of the mission')
    else:
        print(
            f'Data from the deepest 10% of data has been analysed and data seems stable. These deep values can be used to re-assess the dark count if the no {var} at depth assumption is valid in this site and this depth')
    return ax


def sunset_sunrise(time, lat, lon):
    """
    Calculates the local sunrise/sunset of the glider location from GliderTools.
    [https://github.com/GliderToolsCommunity/GliderTools/blob/master/glidertools/optics.py]

    The function uses the Skyfield package to calculate the sunrise and sunset
    times using the date, latitude and longitude. The times are returned
    rather than day or night indices, as it is more flexible for the quenching
    correction.


    Parameters
    ----------
    time: numpy.ndarray or pandas.Series
        The date & time array in a numpy.datetime64 format.
    lat: numpy.ndarray or pandas.Series
        The latitude of the glider position.
    lon: numpy.ndarray or pandas.Series
        The longitude of the glider position.

    Returns
    -------
    sunrise: numpy.ndarray
        An array of the sunrise times.
    sunset: numpy.ndarray
        An array of the sunset times.

    """

    ts = api.load.timescale()
    eph = api.load("de421.bsp")

    df = DataFrame.from_dict(dict([("time", time), ("lat", lat), ("lon", lon)]))

    # set days as index
    df = df.set_index(df.time.values.astype("datetime64[D]"))

    # groupby days and find sunrise/sunset for unique days
    grp_avg = df.groupby(df.index).mean(numeric_only=False)
    date = grp_avg.index

    time_utc = ts.utc(date.year, date.month, date.day, date.hour)
    time_utc_offset = ts.utc(
        date.year, date.month, date.day + 1, date.hour
    )  # add one day for each unique day to compute sunrise and sunset pairs

    bluffton = []
    for i in range(len(grp_avg.lat)):
        bluffton.append(api.wgs84.latlon(grp_avg.lat[i], grp_avg.lon[i]))
    bluffton = np.array(bluffton)

    sunrise = []
    sunset = []
    for n in tqdm(range(len(bluffton))):

        f = almanac.sunrise_sunset(eph, bluffton[n])
        t, y = almanac.find_discrete(time_utc[n], time_utc_offset[n], f)

        if not t:
            if f(time_utc[n]):  # polar day
                sunrise.append(
                    pd.Timestamp(
                        date[n].year, date[n].month, date[n].day, 0, 1
                    ).to_datetime64()
                )
                sunset.append(
                    pd.Timestamp(
                        date[n].year, date[n].month, date[n].day, 23, 59
                    ).to_datetime64()
                )
            else:  # polar night
                sunrise.append(
                    pd.Timestamp(
                        date[n].year, date[n].month, date[n].day, 11, 59
                    ).to_datetime64()
                )
                sunset.append(
                    pd.Timestamp(
                        date[n].year, date[n].month, date[n].day, 12, 1
                    ).to_datetime64()
                )

        else:
            sr = t[y == 1]  # y=1 sunrise
            sn = t[y == 0]  # y=0 sunset

            sunup = pd.to_datetime(sr.utc_iso()).tz_localize(None)
            sundown = pd.to_datetime(sn.utc_iso()).tz_localize(None)

            # this doesn't look very efficient at the moment, but I was having issues with getting the datetime64
            # to be compatible with the above code to handle polar day and polar night

            su = pd.Timestamp(
                sunup.year[0],
                sunup.month[0],
                sunup.day[0],
                sunup.hour[0],
                sunup.minute[0],
            ).to_datetime64()

            sd = pd.Timestamp(
                sundown.year[0],
                sundown.month[0],
                sundown.day[0],
                sundown.hour[0],
                sundown.minute[0],
            ).to_datetime64()

            sunrise.append(su)
            sunset.append(sd)

    sunrise = np.array(sunrise).squeeze()
    sunset = np.array(sunset).squeeze()

    grp_avg["sunrise"] = sunrise
    grp_avg["sunset"] = sunset

    # reindex days to original dataframe as night
    df_reidx = grp_avg.reindex(df.index)
    sunrise, sunset = df_reidx[["sunrise", "sunset"]].values.T

    return sunrise, sunset


def day_night_avg(ds, sel_var='CHLA', start_time='2024-04-18', end_time='2024-04-20'):
    """
    This function computes night and day averages for a selected variable over a specific period of time
    Data in divided into day and night using the sunset and sunrise time as described in the above function sunset_sunrise from GliderTools
    Parameters
    ----------
    ds: xarray on OG1 format containing at least time, depth, latitude, longitude and the selected variable. 
        Data should not be gridded.
    sel_var: variable to use to compute the day night averages
    start_time: Start date of the data selection. As missions can be long and can make it hard to visualise NPQ effect,
                we recommend end selecting small section of few days to few weeks.
    end_time: End date of the data selection. As missions can be long and can make it hard to visualise NPQ effect,
                we recommend selecting small section of few days to few weeks.
                
    Returns
    -------
    day_av: pandas.Dataframe
        A dataframe with the day averages of the selected variable with the following columns:
            batch: Number representing the grouping for each day. This number can represent the number of the day in chronological order
            depth: Depth values for the average
            dat: Average value for the selected variable
            day: Actual date for the batch 
    night_av: pandas.Dataframe
        A dataframe with the night averages of the selected variable with the following columns:
            batch: Number representing the grouping for each day. This number can represent the number of the day in chronological order
            depth: Depth values for the average
            dat: Average value for the selected variable
            day: Actual date for the batch 

    """
    if "TIME" in ds.indexes.keys():
        pass
    else:
        ds = ds.set_xindex('TIME')
    ds_sel = ds.sel(TIME=slice(start_time, end_time))
    sunrise, sunset = sunset_sunrise(ds_sel.TIME, ds_sel.LATITUDE, ds_sel.LONGITUDE)

    # creating batches where one batch is a night and the following day
    day = (ds_sel.TIME > sunrise) & (ds_sel.TIME < sunset)
    # find day and night transitions
    daynight_transitions = np.abs(np.diff(day.astype(int)))
    # get the cumulative sum of daynight to generate separate batches for day and night
    daynight_batches = daynight_transitions.cumsum()
    batch = np.r_[0, daynight_batches // 2]

    # Create day and night averages to then have easy to plot
    df = pd.DataFrame(np.c_[ds_sel[sel_var], day, batch, ds_sel['DEPTH']], columns=['dat', 'day', 'batch', 'depth'])
    ave = df.dat.groupby([df.day, df.batch, np.around(df.depth)]).mean()
    day_av = ave[1].to_frame().reset_index()
    night_av = ave[0].to_frame().reset_index()
    #Assign date value

    for i in np.unique(day_av.batch):
        date_val = str(ds_sel.TIME.where(batch == i).dropna(dim='N_MEASUREMENTS')[-1].values)[:10]
        day_av.loc[np.where(day_av.batch == i)[0], 'date'] = date_val
        night_av.loc[np.where(night_av.batch == i)[0], 'date'] = date_val
    return day_av, night_av


def plot_daynight_avg(day: pd.DataFrame, night: pd.DataFrame, ax: plt.Axes = None, sel_day='2023-09-09',
                      xlabel='Chlorophyll [mg m-3]', **kw: dict, ) -> tuple({plt.Figure, plt.Axes}):
    """
    This function can be used to plot the day and night averages computed with the day_night_avg function
    
    Parameters
    ----------
    day: pandas dataframe containing the day averages
    night: pandas dataframe containing the night averages
    ax: axis to plot the data
    sel_day: selected day to plot
    xlabel: label for the x-axis
    
    Returns
    -------
    A line plot comparing the day and night average over depth for the selected day

    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(5, 5))
    else:
        fig = plt.gcf()
    ax.plot(night.where(night.date == sel_day).dropna().dat, night.where(night.date == sel_day).dropna().depth,
            label='Night time average')
    ax.plot(day.where(day.date == sel_day).dropna().dat, day.where(day.date == sel_day).dropna().depth,
            label='Daytime average')
    ax.legend()
    ax.invert_yaxis()
    ax.grid()
    ax.set(xlabel=xlabel, ylabel='Depth [m]')
    ax.set_title(sel_day)
    return fig, ax


def plot_section_with_srss(ds: xr.Dataset, sel_var: str, ax: plt.Axes = None, start_time='2023-09-06',
                           end_time='2023-09-10', ylim=45, **kw: dict, ) -> tuple({plt.Figure, plt.Axes}):
    """
    This function can be used to plot sections for any variable with the sunrise and sunset plotted over
    
    Parameters
    ----------
    ds: xarray on OG1 format containing at least time, depth, latitude, longitude and the selected variable. 
        Data should not be gridded.
    sel_var: selected variable to plot
    ax: axis to plot the data
    start_time: Start date of the data selection. As missions can be long and came make it hard to visualise NPQ effect,
    end_time: End date of the data selection. As missions can be long and came make it hard to visualise NPQ effect,
    ylim: specified limit for the maximum y-axis value. The minimum is computed as ylim/30
    
    Returns
    -------
    A section showing the variability of the selected data over time and depth
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(5, 5))
    else:
        fig = plt.gcf()

    if "TIME" not in ds.indexes.keys():
        ds = ds.set_xindex('TIME')
    ds_sel = ds.sel(TIME=slice(start_time, end_time))
    sunrise, sunset = sunset_sunrise(ds_sel.TIME, ds_sel.LATITUDE, ds_sel.LONGITUDE)

    c = ax.scatter(ds_sel.TIME, ds_sel.DEPTH, c=ds_sel[sel_var], s=10, vmin=np.nanpercentile(ds_sel[sel_var], 0.5),
                   vmax=np.nanpercentile(ds_sel[sel_var], 99.5))
    ax.set_ylim(ylim, -ylim / 30)
    for n in np.unique(sunset):
        ax.axvline(np.unique(n), c='blue')
    for m in np.unique(sunrise):
        ax.axvline(np.unique(m), c='orange')
    ax.set_ylabel('Depth [m]')
    plt.colorbar(c, label=f'{sel_var} [{ds[sel_var].units}]')
    return fig, ax


def check_temporal_drift(ds: xr.Dataset, var: str, ax: plt.Axes = None, **kw: dict, ) -> tuple({plt.Figure, plt.Axes}):
    if ax is None:
        fig, ax = plt.subplots(1, 2, figsize=(14, 6))
    else:
        fig = plt.gcf()

    ax[0].scatter(mdates.date2num(ds.TIME), ds[var], s=10)
    ax[0].xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    ax[0].set(ylim=(np.nanpercentile(ds[var], 0.01), np.nanpercentile(ds[var], 99.99)), ylabel=var)

    c = ax[1].scatter(ds[var], ds.DEPTH, c=mdates.date2num(ds.TIME), s=10)
    ax[1].set(xlim=(np.nanpercentile(ds[var], 0.01), np.nanpercentile(ds[var], 99.99)), ylabel='Depth (m)', xlabel=var)
    ax[1].invert_yaxis()

    [a.grid() for a in ax]
    plt.colorbar(c, format=DateFormatter('%b %d'))
    return fig, ax


def check_monotony(da):
    """
    This function check weather the selected variable over the mission is monotonically increasing or not. This is developed in particular for profile number.
    If the profile number is not monotonically increasing, this may mean that whatever function was used to assign the profile number may have misassigned some points.
    
    Parameters
    ----------
    da: xarray.DataArray on OG1 format. Data should not be gridded.

    Returns
    -------
    It will print a sentence stating whether data is

    """
    if not pd.Series(da).is_monotonic_increasing:
        print(f'{da.name} is not always monotonically increasing')
    else:
        print(f'{da.name} is always monotonically increasing')


def plot_profIncrease(ds: xr.DataArray, ax: plt.Axes = None, **kw: dict, ) -> tuple({plt.Figure, plt.Axes}):
    """
    This function can be used to plot the profile number and check for any possible issues with the profile index assigned.

    Parameters
    ----------
    ds: xarray in OG1 format with at least PROFILE_NUMBER, TIME, DEPTH. Data should not be gridded
    ax: axis to plot the data

    Returns -------
    Two plots, one line plot with the profile number over time (expected to be always increasing). A
    second plot which is a scatter plot showing at which depth over time there was a profile index where the
    difference was neither 0 nor 1 (meaning there are possibly issues with how the profile index was assigned)

    """
    if ax is None:
        fig, ax = plt.subplots(2, 1, figsize=(10, 5), sharex=True)
    else:
        fig = plt.gcf()

    ax[0].plot(ds.TIME, ds.PROFILE_NUMBER)
    ax[0].set(ylabel='Profile_Number')
    if len(np.where((np.diff(ds.PROFILE_NUMBER) != 0) & (np.diff(ds.PROFILE_NUMBER) != 1))[0]) == 0:
        ax[1].text(0.2, 0.5, 'Data in monotonically increasing and no issues can be observed',
                   transform=ax[1].transAxes)
    else:
        ax[1].scatter(ds.TIME[np.where((np.diff(ds.PROFILE_NUMBER) != 0) & (np.diff(ds.PROFILE_NUMBER) != 1))],
                      ds.DEPTH[np.where((np.diff(ds.PROFILE_NUMBER) != 0) & (np.diff(ds.PROFILE_NUMBER) != 1))],
                      s=10, c='red', label='Depth at which we have issues \n with the profile number assigned')
    ax[1].set(ylabel='Depth')
    ax[1].invert_yaxis()
    ax[1].legend()
    ax[1].xaxis.set_major_locator(plt.MaxNLocator(8))
    [a.grid() for a in ax]
    return fig, ax
