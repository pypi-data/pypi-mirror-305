
from numpy import linspace, interp
from collections.abc import Iterable

def h_index(x,y):
    last_a = x[0]
    for a,b in zip(x,y):
        assert b >= 0, f"Negative sample value {b=}"
        if a > b:
            break
        last_a = a
    return last_a

def hirsch(
    samples: Iterable[float],
    populations: Iterable[float] | None = None,
    continuous: bool = False,
    sort: bool = True,
    plot: bool = False,
    sample_frequency: int = 100,
) -> float:

    """Takes a list of populations and returns the continuous Hirsch-index. 
    
    :param samples: Iterable of samples
    :param continuous: Calculate the continuous hirsch index
    :sample_frequency: number of interpolation points between data points
    :sort: sort the populations, set to False if populations is already sorted
    :plot: return a `plotly.graph_objects.Figure` together with the h-index for debugging
    """
    
    # :param populations: Iterable of populations (maximum value for each sample)

    assert sample_frequency > 1
    assert samples, "Must pass non-empty samples"

    if populations:
        assert len(samples) == len(populations)
        continuous = True
        samples = [s/p for s,p in zip(samples, populations)]

    if sort:
        y = sorted(samples, reverse=True)
    else:
        y = samples

    n = len(samples)

    ### DISCRETE

    if not continuous:
        # x-coordinates
        x = linspace(1, n, n)
        
        # calculate h-index
        h = h_index(x,y)

    ### CONTINUOUS

    else:
        # interpolate
        x = linspace(0.0, 1.0, n)
        q = linspace(0.0, 1.0, n*sample_frequency+1)
        y_smooth = interp(q, x, y)

        # calculate h-index
        h = h_index(q,y_smooth)

    if plot:
        import plotly.graph_objects as go
        fig = go.Figure()
        
        trace = go.Scatter(mode="text", x=[0,0,h,h,0], y=[0,h,h,0,0], name="h_box", fill="toself")
        fig.add_trace(trace)
        
        if continuous:
            line_shape = None
        else:
            line_shape = "vh"

        trace = go.Scatter(x=x, y=y, name="samples", mode="markers+lines", line_shape=line_shape)
        fig.add_trace(trace)

        trace = go.Scatter(mode="markers", x=[0], y=[0], name="origin")
        fig.add_trace(trace)

        if continuous:
            trace = go.Scatter(x=q, y=y_smooth, name="interpolated")
            fig.add_trace(trace)

        fig.update_xaxes(zeroline=True, zerolinecolor="black")
        fig.update_yaxes(zeroline=True, zerolinecolor="black")

        return fig, h

    return h
