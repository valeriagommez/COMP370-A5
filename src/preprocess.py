import pandas as pd

df_full = pd.read_csv("../data/data_2024.csv", on_bad_lines="skip")
df = df_full[["Created Date", "Closed Date", "Incident Zip"]]

df["Created Date"] = pd.to_datetime(df["Created Date"], format="%Y-%m-%d %H:%M:%S", errors="coerce")
df["Closed Date"] = pd.to_datetime(df["Closed Date"], format="%Y-%m-%d %H:%M:%S", errors="coerce")
df = df.dropna(subset=["Created Date", "Closed Date"])  # drop if not closed

# finding create to close time
df["Create-Close Time"] = (df["Closed Date"] - df["Created Date"]).dt.total_seconds() / 3600
# classifying data per month
df["Month"] = df["Created Date"].dt.to_period("M").dt.to_timestamp()

# get average for ALL data 
df_monthly = df.groupby("Month")["Create-Close Time"].mean().rename("Average Closing Time").reset_index() 
df_monthly.to_csv("../data/monthly_averages_all.csv", index=False)

# get monthly average for data per zipcode
df_per_zip = df.groupby(["Incident Zip", "Month"])["Create-Close Time"].mean().rename("Average Closing Time").reset_index() 
df_per_zip.rename(columns={"Incident Zip": "Zip"}).to_csv("../data/monthly_by_zip.csv", index=False)

print(df.head(5))
