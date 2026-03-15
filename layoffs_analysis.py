import pandas as pd

df = pd.read_csv("data_raw/layoffs_raw.csv")

print(df.head())
print(df.columns)

# checking which companies laid off the most people
top_companies = df.groupby("company")["total_laid_off"].sum().sort_values(ascending=False)

print(top_companies.head(10))

# checking which countries were people most laid off in
top_countries = df.groupby("country")["total_laid_off"].sum().sort_values(ascending=False)

print(top_countries.head(10))

# checking in which industries were people mostly laid off
top_industries = df.groupby("industry")["total_laid_off"].sum().sort_values(ascending=False)

print(top_industries.head(10))

df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M")
# calculated layoffs by month
layoffs_by_month = df.groupby("month")["total_laid_off"].sum()

print("\nLayoffs over time:")
print(layoffs_by_month.tail(10))

df.to_csv("data_clean/layoffs_clean.csv", index=False)