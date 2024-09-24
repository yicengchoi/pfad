import pandas as pd
import matplotlib.pyplot as plt

# URL
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

# CSV
data = pd.read_csv(url)


print(data.head())

# 选择需要的列：国家/地区和日期
# 将日期列转换为日期格式并计算全球每日新增病例
data_melted = data.melt(id_vars=["Province/State", "Country/Region", "Lat", "Long"],
                         var_name="Date",
                         value_name="Confirmed")

# 将日期转换为日期类型
data_melted["Date"] = pd.to_datetime(data_melted["Date"])

# 计算每日新增病例
daily_data = data_melted.groupby(["Country/Region", "Date"])["Confirmed"].sum().diff().fillna(0)
daily_data = daily_data.reset_index()
daily_data.columns = ["Country/Region", "Date", "Daily Confirmed"]

# 选择某个国家
country_data = daily_data[daily_data["Country/Region"] == "US"]

# 可视化
plt.figure(figsize=(12, 6))
plt.plot(country_data["Date"], country_data["Daily Confirmed"], label="Daily Confirmed Cases", color="blue")
plt.title("Daily Confirmed COVID-19 Cases in the US")
plt.xlabel("Date")
plt.ylabel("Number of Cases")
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
