import pandas as pd
from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure

monthly_df = pd.read_csv("../data/monthly_averages_all.csv", parse_dates=["Month"])
monthly_zip_df = pd.read_csv("../data/monthly_by_zip.csv", parse_dates=["Month"], dtype={"Zip": str})

# extract months and zip codes
months = monthly_df["Month"]
zips = sorted(monthly_zip_df["Zip"].dropna().unique())

def getChartByZip(z) : 
    s = monthly_zip_df[monthly_zip_df["Zip"] == z].set_index("Month")["Average Closing Time"].dropna()
    return s.reindex(months).to_numpy()   

src_all = ColumnDataSource(dict(month=months, hours=monthly_df["Average Closing Time"].to_numpy()))
src_1 = ColumnDataSource(dict(month=months, hours=getChartByZip(zips[0])))
src_2 = ColumnDataSource(dict(month=months, hours=getChartByZip(zips[1])))

sel1 = Select(title="Zipcode 1", value=zips[0], options=zips)
sel2 = Select(title="Zipcode 2", value=zips[1], options=zips)

p = figure(x_axis_type="datetime", width=800, height=400, x_axis_label="Month", y_axis_label="Average time to close (hours)")
p.line("month", "hours", source=src_all, color="black", legend_label="All zipcodes")
p.line("month", "hours", source=src_1, color="blue", legend_label="Zipcode 1")
p.line("month", "hours", source=src_2, color="red", legend_label="Zipcode 2")
p.scatter("month", "hours", source=src_1, color="blue", size=7)
p.scatter("month", "hours", source=src_2, color="red", size=7)

def update(attr, old, new):
    src_1.data = dict(month=months, hours=getChartByZip(sel1.value))
    src_2.data = dict(month=months, hours=getChartByZip(sel2.value))
    # src_1.data = getChartByZip(sel1.value)
    # src_2.data = getChartByZip(sel2.value)

sel1.on_change("value", update)
sel2.on_change("value", update)

curdoc().add_root(column(sel1, sel2, p))
