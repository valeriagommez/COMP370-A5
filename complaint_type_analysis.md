**Overall must abundant complaint type**

I found this using pandas and the simple command `topComplaint = df["Complaint Type"].value_counts().idxmax()`. This lead me to the conclusion that the most common complaint is "Illegal Parking".

**Illegal parking complaints over first two months of 2024**

As seen in my github repo (https://github.com/valeriagommez/COMP370-A5/blob/main/scripts/task3.ipynb), there were many complaints relating to Illegal Parking on this two month span. February 1st 2024 takes the cake in terms of complaints, as it's the only day that had over 1750 complaints in this span. Furthermore, the daily average of illegal parking complaints was about 1332.

**How does this compare to that same complaint type in June-July of 2024?**

Over this period of time, we can see that the data is a bit more consistent, as there were about 1412 complaints per day, considerably more than during the winter. Furthermore, we can see that once the month of July starts, there is a slight decrease in complaints as compared to the month of June. Nonetheless, there wasn't a day where the number of complaints reached below 1000.
