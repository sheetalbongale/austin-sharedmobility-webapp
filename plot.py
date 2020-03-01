import pandas as pd
import os
import plotly
import plotly.graph_objects as go
import json
import plotly.express as px

def load_agg_data():

    csv_path = os.path.join("data", "311data.csv")
    df = pd.read_csv(csv_path)
    return df

def plot():

    df = load_agg_data()
    fig = px.scatter_mapbox(
        df,
        lat="SR Location Lat",
        lon="SR Location Long",
        hover_name="SR Method Received Desc",
        hover_data=["SR Location", "SR Type Desc"],
        color_discrete_sequence=["red"],
        zoom=12,
        height=700,
    )
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


if __name__ == "__main__":
    print(plot())


