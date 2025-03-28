import plotly.graph_objects as go
import pandas as pd

def animate_car(data):
    frames = [go.Frame(
        data=[go.Scatter3d(
            x=data['X'][:i],
            y=data['Y'][:i],
            z=data['Z'][:i],
            mode='lines+markers',
            marker=dict(size=4, color=data['Speed'][:i], colorscale='Viridis'),
        )],
        name=str(i)
    ) for i in range(1, len(data))]

    trace = go.Scatter3d(
        x=data['X'][:1],
        y=data['Y'][:1],
        z=data['Z'][:1],
        mode='lines+markers',
        marker=dict(size=4, color=data['Speed'][:1], colorscale='Viridis'),
    )

    layout = go.Layout(
        title="F1 Car Telemetry Animation",
        scene=dict(
            xaxis_title="X Position",
            yaxis_title="Y Position",
            zaxis_title="Z Position"
        ),
        updatemenus=[dict(
            type="buttons",
            showactive=False,
            buttons=[dict(label="Play", method="animate", args=[None, dict(frame=dict(duration=50, redraw=True), fromcurrent=True)])]
        )],
        showlegend=False
    )

    fig = go.Figure(data=[trace], layout=layout, frames=frames)
    fig.show()

if __name__ == '__main__':
    # Load the telemetry data from CSV
    data = pd.read_csv('data/telemetry_data.csv')
    
    # Animate the car's movement based on the telemetry data
    animate_car(data)
