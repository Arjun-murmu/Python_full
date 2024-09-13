years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
update_year = []
for year in years:
  if year.endswith("2023"):
    new = year.replace("2023","2024")
    update_year.append(new)
  else:
    update_year.append(year)
print(update_year)
