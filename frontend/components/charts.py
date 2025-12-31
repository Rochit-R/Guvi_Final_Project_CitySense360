import plotly.graph_objects as go
import plotly.express as px


def line_chart(x, y, title, y_label):
    """Enhanced line chart with gradient fill and smooth animations"""
    fig = go.Figure()
    
    # Main line with gradient
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode="lines+markers",
        line=dict(
            width=4,
            color='rgba(102, 126, 234, 1)',
        ),
        marker=dict(
            size=10,
            color='rgba(118, 75, 162, 1)',
            line=dict(color='white', width=2)
        ),
        fill='tozeroy',
        fillcolor='rgba(102, 126, 234, 0.2)',
        hovertemplate='<b>%{y:.2f}</b><br>Time: %{x}<extra></extra>'
    ))

    fig.update_layout(
        title=dict(
            text=title,
            font=dict(size=24, color='white', family='Arial Black'),
            x=0.5,
            xanchor='center'
        ),
        xaxis_title=dict(
            text="Time",
            font=dict(size=16, color='rgba(255,255,255,0.8)')
        ),
        yaxis_title=dict(
            text=y_label,
            font=dict(size=16, color='rgba(255,255,255,0.8)')
        ),
        template="plotly_dark",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        hovermode='x unified',
        hoverlabel=dict(
            bgcolor="rgba(15, 23, 42, 0.9)",
            font_size=14,
            font_family="Arial"
        ),
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(255,255,255,0.1)',
            zeroline=False
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(255,255,255,0.1)',
            zeroline=False
        ),
        margin=dict(l=60, r=40, t=80, b=60),
        font=dict(color='white')
    )
    
    # Add animation config
    fig.update_traces(
        marker=dict(
            line=dict(width=2, color='rgba(255,255,255,0.8)')
        )
    )
    
    return fig


def gauge_chart(value, title, max_value=100):
    """Animated gauge chart for metrics"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': title, 'font': {'size': 24, 'color': 'white'}},
        delta={'reference': max_value * 0.7},
        gauge={
            'axis': {'range': [None, max_value], 'tickcolor': "white"},
            'bar': {'color': "rgba(102, 126, 234, 1)"},
            'bgcolor': "rgba(255,255,255,0.1)",
            'borderwidth': 2,
            'bordercolor': "rgba(255,255,255,0.3)",
            'steps': [
                {'range': [0, max_value * 0.33], 'color': 'rgba(76, 175, 80, 0.3)'},
                {'range': [max_value * 0.33, max_value * 0.66], 'color': 'rgba(255, 193, 7, 0.3)'},
                {'range': [max_value * 0.66, max_value], 'color': 'rgba(244, 67, 54, 0.3)'}
            ],
            'threshold': {
                'line': {'color': "white", 'width': 4},
                'thickness': 0.75,
                'value': max_value * 0.9
            }
        }
    ))

    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font={'color': "white", 'family': "Arial"},
        height=400,
        margin=dict(l=40, r=40, t=80, b=40)
    )
    
    return fig


def bar_chart(x, y, title, color_scale='Viridis'):
    """Enhanced bar chart with gradient colors"""
    fig = go.Figure(data=[
        go.Bar(
            x=x,
            y=y,
            marker=dict(
                color=y,
                colorscale='Plasma',
                line=dict(color='rgba(255,255,255,0.3)', width=2),
                showscale=True,
                colorbar=dict(
                    title="Value",
                    titlefont=dict(color='white'),
                    tickfont=dict(color='white')
                )
            ),
            hovertemplate='<b>%{x}</b><br>Value: %{y:.2f}<extra></extra>'
        )
    ])
    
    fig.update_layout(
        title=dict(
            text=title,
            font=dict(size=24, color='white', family='Arial Black'),
            x=0.5,
            xanchor='center'
        ),
        template="plotly_dark",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            showgrid=False,
            title_font=dict(size=16, color='rgba(255,255,255,0.8)')
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(255,255,255,0.1)',
            title_font=dict(size=16, color='rgba(255,255,255,0.8)')
        ),
        hovermode='x',
        hoverlabel=dict(
            bgcolor="rgba(15, 23, 42, 0.9)",
            font_size=14
        ),
        margin=dict(l=60, r=40, t=80, b=60)
    )
    
    return fig


def pie_chart(labels, values, title):
    """Enhanced pie chart with pull effect and custom colors"""
    colors = ['#667eea', '#764ba2', '#f093fb', '#4facfe', '#43e97b']
    
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.4,
        marker=dict(
            colors=colors,
            line=dict(color='rgba(255,255,255,0.3)', width=2)
        ),
        textinfo='label+percent',
        textfont=dict(size=14, color='white', family='Arial'),
        hovertemplate='<b>%{label}</b><br>Value: %{value}<br>Percentage: %{percent}<extra></extra>',
        pull=[0.1, 0, 0, 0, 0]
    )])
    
    fig.update_layout(
        title=dict(
            text=title,
            font=dict(size=24, color='white', family='Arial Black'),
            x=0.5,
            xanchor='center'
        ),
        template="plotly_dark",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=True,
        legend=dict(
            font=dict(color='white', size=12),
            bgcolor='rgba(255,255,255,0.1)',
            bordercolor='rgba(255,255,255,0.3)',
            borderwidth=1
        ),
        margin=dict(l=40, r=40, t=80, b=40),
        height=500
    )
    
    return fig


def area_chart(x, y, title, y_label):
    """Smooth area chart with gradient fill"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        fill='tozeroy',
        mode='lines',
        line=dict(
            width=3,
            color='rgba(102, 126, 234, 1)',
            shape='spline',
            smoothing=1.3
        ),
        fillcolor='rgba(102, 126, 234, 0.3)',
        hovertemplate='<b>%{y:.2f}</b><br>%{x}<extra></extra>'
    ))
    
    fig.update_layout(
        title=dict(
            text=title,
            font=dict(size=24, color='white', family='Arial Black'),
            x=0.5,
            xanchor='center'
        ),
        xaxis_title=dict(
            text="Time",
            font=dict(size=16, color='rgba(255,255,255,0.8)')
        ),
        yaxis_title=dict(
            text=y_label,
            font=dict(size=16, color='rgba(255,255,255,0.8)')
        ),
        template="plotly_dark",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        hovermode='x unified',
        xaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(255,255,255,0.1)'),
        margin=dict(l=60, r=40, t=80, b=60)
    )
    
    return fig