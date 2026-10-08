import argparse
from datetime import datetime
import pandas as pd

def main() :
    parser = argparse.ArgumentParser(description="Count complaint types per borough within a specified date range.")
    parser.add_argument("-i", "--input", required=True,
        help="Path to the input CSV file")
    
    parser.add_argument("-s", "--start", required=True,
        help="Start date of the specified window")
    
    parser.add_argument("-e", "--end", required=True,
        help="End date of the specified window")
    
    parser.add_argument("-o", "--output", required=False, action='store_true',
        help="Output file for the results")

    args = parser.parse_args()

    start_date = datetime.strptime(args.start, "%d-%m-%Y")
    end_date = datetime.strptime(args.end, "%d-%m-%Y")

    # drop uneccessary columns
    data = pd.read_csv(args.input, usecols=["Created Date", "Complaint Type", "Borough"])
    data["Created Date"] = pd.to_datetime(data["Created Date"], format="%Y-%m-%d %H:%M:%S", errors="coerce")

    filtered_data = data[data["Created Date"].between(start_date, end_date)]
    # print(filtered_data.head(10)) # works

    counts = (filtered_data.groupby(["Complaint Type", "Borough"]).size().reset_index(name="count"))

    header = ["complaint type, borough, count"]
    for count in counts.itertuples(index=False) : 
        header.append(f"{count[0].lower()}, {count[1].capitalize()}, {count[2]}")

    csvFile = "\n".join(header) + "\n"

    if args.output:
        with open(args.output, "w") as f:
            f.write(csvFile)
    else:
        print(csvFile, end="")

if __name__ == "__main__" : 
    main()
