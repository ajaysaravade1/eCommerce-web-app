
import streamlit as st
import math
import pandas as pd

from streamlit_option_menu import option_menu

st. set_page_config(layout="wide")
#Reading file and pre processing
df = pd.read_csv('Ecomm', sep='\t', header=0)
column_names = df.columns.tolist()
result = df.isnull().any()
result = list(result)
col = list(df.columns)
#fill Null to 0
for i in range(len(result)):
  if result[i]==True:
    df[col[i]] = df[col[i]].fillna(0)


df['visit_dt'] = pd.to_datetime(df['visit_dt'],format='%Y%m%d').dt.date
revenue = math.floor(df["order_revenue"].sum())
conversion_rate = (df["order_count"].sum()/df["product_view_plp"].sum()*100).round(2)
average_order_value = (math.floor(df["order_revenue"].sum())/df["order_count"].sum()).round(2)
total_product_sale= df["order_count"].sum()
avg_time_on_site = df["avg_time_on_site"].sum()/df["session_count"].sum()
total_customer = df["user_id"].nunique()

st.title("Dashboard")



col1, col2, col3, col4, col5, col6 = st.columns(6)
col1.metric("Revenue", str(revenue)+' \u20B9')
col2.metric("Conversion Rate", str(conversion_rate)+" %")
col3.metric("Average Order Value ", str(average_order_value)+ " \u20B9")
col4.metric("Total Product Sale ", str(total_product_sale))
col5.metric("Avg time on site", str(avg_time_on_site.round(2))+" sec")
col6.metric("Total Customers", str(total_customer))

st.line_chart(df.groupby('visit_dt').order_revenue.sum())
st.bar_chart(df.groupby('customer_type').order_revenue.sum())
