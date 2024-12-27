from django.shortcuts import render

# Create your views here.
import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot

# CSV ?? ??
CSV_PATH = 'graph/dataset.csv'

def load_data():
    df = pd.read_csv(CSV_PATH)
    df['time'] = pd.to_datetime(df['time'])  # time ?? datetime ???? ??
    return df

def index(request):
    # ??? ??
    df = load_data()

    # ?? ? ??? ??? ?? ?? ??
    columns = [
        {'key': 'temperature', 'name': 'Temperature'},
        {'key': 'humidity', 'name': 'Humidity'},
        {'key': 'VPD', 'name': 'VPD'},
        {'key': 'height', 'name': 'Height'}
    ]

    # ??? ?? POST ???? ??? (????? ?? ? ??)
    selected_keys = request.POST.getlist('columns') or [col['key'] for col in columns]

    # Plotly ??? ??
    traces = []
    colors = {'temperature': 'red', 'humidity': 'blue', 'VPD': 'green', 'height': 'purple'}

    for key in selected_keys:
        traces.append(go.Scatter(x=df['time'], y=df[key], mode='lines', name=key.capitalize(), line=dict(color=colors[key])))

    layout = go.Layout(
        title='Plant Data Visualization',
        xaxis={'title': 'Time'},
        yaxis={'title': 'Values'},
        template='plotly_dark'
    )

    fig = go.Figure(data=traces, layout=layout)
    graph = plot(fig, output_type='div')

    # ???? ???? ??? ??
    context = {
        'graph': graph,
        'columns': columns,
        'selected_keys': selected_keys,
    }
    return render(request, 'graphs/index.html', context)