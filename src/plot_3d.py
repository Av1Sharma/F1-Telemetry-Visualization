import plotly.graph_objects as go
import pandas as pd

def create_3d_plot(data):
    trace = go.Scatter3d(
        x=data['X'],
        y=data['Y'],
        z=data['Z'],
        mode='lines+markers',  
        marker=dict(size=4, color=data['Speed'], colorscale='Viridis')  
    )

    layout = go.Layout(
        title="F1 Car Telemetry Visualization",
        scene=dict(
            xaxis_title="X Position",
            yaxis_title="Y Position",
            zaxis_title="Z Position"
        ),
        showlegend=False
    )

    fig = go.Figure(data=[trace], layout=layout)
    fig.show()

if __name__ == '__main__':
    data = pd.read_csv('data/telemetry_data.csv')
    
    create_3d_plot(data)
