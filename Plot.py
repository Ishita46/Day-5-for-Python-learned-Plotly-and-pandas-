Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas as pd
>>> df = pd.DataFrame()
>>> print(df)
Empty DataFrame
Columns: []
Index: []
>>> data = [1,2,3,4,5]
>>> df = pd.DataFrame(data)
>>> print(df)
   0
0  1
1  2
2  3
3  4
4  5
>>> import plotly.express as px
>>> df=pd.read_csv("C:/Users/ishit/OneDrive/Desktop/Python/line_chart.csv")
>>> print(df)
    Country  Year  Per capita income
0     Aruba  2002       20436.887129
1     Aruba  2003       20833.761612
2     Aruba  2004       22569.974985
3     Aruba  2005       23300.039558
4     Aruba  2006       24045.272483
..      ...   ...                ...
86  Austria  2004       36821.521468
87  Austria  2005       38403.133877
88  Austria  2006       40635.281816
89  Austria  2007       46855.771745
90  Austria  2008       51708.765754

[91 rows x 3 columns]
>>> fig=px.line(df, x="Year", y="Per capita income", color="Country", title="Per capita income")
>>> fig.show()
>>> fig.show()
