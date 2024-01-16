import yfinance as yf;
import plotly.io as pio;
import plotly.graph_objects as go;

# Setting the colour of the plot
pio.templates.default = "plotly_dark"

# Initializing the Stock names and the start/end date for comparison
amd_ticker = 'AMD'
nvidia_ticker = 'NVDA'
start_date = '2023-10-01'
end_date = '2024-12-31'

# Fetching the data from the internet
amd_data = yf.download(amd_ticker, start= start_date, end = end_date)
nvidia_data = yf.download(nvidia_ticker , start = start_date, end = end_date)


amd_data['Daily_Return'] = amd_data['Adj Close'].pct_change()
nvidia_data['Daily_Return'] = nvidia_data['Adj Close'].pct_change()

# Figure creation for the visualization
fig = go.Figure()
fig.add_trace(go.Scatter( x=amd_data.index, y=amd_data['Daily_Return'], mode= 'lines', name='AMD', line= dict(color='blue')))
fig.add_trace(go.Scatter( x=nvidia_data.index, y=nvidia_data['Daily_Return'], mode= 'lines', name='Nvidia', line= dict(color='red')))

fig.update_layout(title= 'Daily Returns for AMD and Nvidia (Q4)', 
                  xaxis_title='Date', yaxis_title= 'Daily Return', legend= dict(x=0.02, y=0.95))
fig.show()
