import streamlit as st
import matplotlib.pyplot as pit
import numpy as np

# bar chart
rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)
