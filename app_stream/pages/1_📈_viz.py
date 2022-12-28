import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px 
import plotly.graph_objects as go

from plotly.subplots import make_subplots



DATA = "get_around_delay_analysis.xlsx"

@st.cache
def load_data():
    data = pd.read_excel(DATA)
    return data



data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("")

#ratio en % des type de location
ratio_checking_type = data["checkin_type"].value_counts(normalize=True).round(3)

ratio_state = data["state"].value_counts(normalize=True).round(3)

# ratio d'annulation selon type de location
mobile = data[data["checkin_type"] == "mobile"]
mobile_ratio_state = mobile["state"].value_counts(normalize=True).round(3)

connect = data[data["checkin_type"] == "connect"]
connect_ratio_state = connect["state"].value_counts(normalize=True).round(3)

#





st.markdown("<h1 style='text-align: center; color: white;'>Dashbord GetAround</h1>", unsafe_allow_html=True)
st.markdown("###")

pie = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "pie"}]],shared_yaxes = True, 
                    x_title="proportion des type de location et % d'annulation",
                    subplot_titles=["Distribution de type de location", "proportion des annulation"])

pie.add_trace(go.Pie( 
    values=ratio_checking_type,
    labels=['Mobile', 'Connect '],
    marker_colors = ['#202EBD','#13E7E3'],                      
    ),
    row=1, col=1)

pie.add_trace(go.Pie(
    values=ratio_state,
    labels=['Non annulée', 'Annulée '],
    marker_colors = ['#20BD2E','#FF3333'],
    ),
    row=1, col=2)

pie.update_layout(
    width=1500,
    legend=dict(
        font=dict(
            size=16
        )))

st.plotly_chart(pie)

fig_pie = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "pie"}]],shared_yaxes = True,
                        x_title='proportion des annulation par type de location',subplot_titles=["Mobile", "Connect"])

fig_pie.add_trace(go.Pie( 
    values=mobile_ratio_state,
    labels=['Non annulée', 'Annulée '],
    marker_colors = ['#20BD2E','#FF3333'],                      
    ),
    row=1, col=1)

fig_pie.add_trace(go.Pie(
    values=connect_ratio_state,
    labels=['Non annulée', 'Annulée '],
    marker_colors = ['#20BD2E','#FF3333'],
    ),
    row=1, col=2)

fig_pie.update_layout(
    width=1500,
    legend=dict(
        font=dict(
            size=16
        )))

st.plotly_chart(fig_pie)