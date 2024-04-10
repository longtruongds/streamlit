#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

# Create a DataFrame with random integers
df = pd.DataFrame(np.random.randint(0, 100, size=(10, 2)), columns=['Column1', 'Column2'])

# Create a line chart using Plotly Express
fig = px.line(df, x=df.index, y=['Column1', 'Column2'], title='Random Data Line Chart')

# Display the chart in Streamlit
st.plotly_chart(fig)


# In[ ]:





# In[ ]:




