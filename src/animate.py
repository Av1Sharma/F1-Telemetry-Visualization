import plotly.graph_objects as go
import pandas as pd

def preprocess_data(data, step=50):
    # Normalize X, Y positions to start from (0,0)
    data['X'] -= data['X'].min()
    data['Y'] -= data['Y'].min()

    data['Z'] = 0  

    return data.iloc[::step].reset_index(drop=True)

def animate_car(data, step=50):
    data = preprocess_data(data, step)

    trace_path = go.Scatter3d(
        x=data['X'], y=data['Y'], z=[0] * len(data),
        mode='lines', line=dict(color='blue', width=4),
        name="Track Path"
    )

    # Moving car marker
    trace_car = go.Scatter3d(
        x=[data['X'][0]], y=[data['Y'][0]], z=[0],
        mode='markers', marker=dict(size=6, color='red'),
        name="Car"
    )

    frames = [
        go.Frame(
            data=[
                go.Scatter3d(
                    x=data['X'][:i+1],  
                    y=data['Y'][:i+1],
                    z=[0] * (i+1),
                    mode='lines+markers',
                    marker=dict(size=6, color='red'),
                    line=dict(color='red', width=2),
                )
            ],
            name=str(i)
        )
        for i in range(1, len(data))
    ]

    # Layout with play/pause/restart controls and interactive rotation
    layout = go.Layout(
        title="F1 Car Telemetry Animation (X-Y Track)",
        scene=dict(
            xaxis_title="X Position",
            yaxis_title="Y Position",
            zaxis_title="Ground Level",
            camera=dict(up=dict(x=0, y=0, z=1)), 
        ),
        updatemenus=[
            dict(
                type="buttons",
                showactive=True,
                buttons=[
                    dict(label="Play", method="animate",
                         args=[None, dict(frame=dict(duration=30, redraw=True), fromcurrent=True)]),
                    dict(label="Pause", method="animate",
                         args=[[None], dict(frame=dict(duration=0, redraw=False), mode="immediate")]),
                    dict(label="Restart", method="animate",
                         args=[None, dict(frame=dict(duration=30, redraw=True), fromcurrent=False)]),
                ]
            )
        ],
        showlegend=True
    )

    fig = go.Figure(data=[trace_path, trace_car], layout=layout, frames=frames)
    fig.show()

if __name__ == '__main__':
    data = pd.read_csv('data/telemetry.csv')

    if 'Time' in data.columns:
        data['Time'] = pd.to_datetime(data['Time'])
        data = data.set_index('Time').resample('100ms').mean().reset_index()

    animate_car(data, step=50)
