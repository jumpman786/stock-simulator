import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Configure page settings
st.set_page_config(
    page_title="Stock Simulator",
    page_icon="📈",
    layout="wide"
)

# Custom CSS for dark theme
st.markdown("""
<style>
    .main {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    .stButton>button {
        background-color: #1F77B4;
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: #262730;
        color: white;
    }
    .stSelectbox>div>div>div>div>div {
        background-color: #262730;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'portfolio' not in st.session_state:
    st.session_state.portfolio = {}
if 'balance' not in st.session_state:
    st.session_state.balance = 10000

# AI Prediction Function
def predict_stock_price(ticker):
    try:
        data = yf.download(ticker, period="1y")
        if len(data) < 30:
            return "Not enough data"
        
        # Create features
        data['Days'] = np.arange(len(data))
        X = data[['Days']]
        y = data['Close']
        
        # Train model
        model = LinearRegression()
        model.fit(X, y)
        
        # Predict next 7 days
        future_days = np.array([[len(data) + i] for i in range(7)])
        predictions = model.predict(future_days)
        
        return float(predictions[-1])  # Explicit conversion to float
    except Exception as e:
        return f"Prediction error: {str(e)}"

# Main App
st.title("💰 AI Stock Simulator")
st.write(f"Current Balance: ${st.session_state.balance:,.2f}")

# Sidebar Controls
with st.sidebar:
    st.header("Controls")
    ticker = st.text_input("Enter Stock Symbol (e.g., AAPL)", "AAPL").upper()
    days = st.slider("View History (Days)", 30, 365, 90)
    investment = st.number_input("Investment Amount", 10, 1000, 100)

try:
    stock_data = yf.download(ticker, period=f"{days}d")
    if stock_data.empty:
        raise ValueError("No data returned for this symbol")
    
    # Main columns
    col1, col2 = st.columns([2, 1])

    with col1:
        # Stock Chart
        st.subheader(f"{ticker} Price History")
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(stock_data['Close'], color='#00FFAA')
        ax.set_facecolor('#0E1117')
        fig.set_facecolor('#0E1117')
        ax.tick_params(colors='white')
        st.pyplot(fig)

    with col2:
        # Trading Panel
        st.subheader("Trading")
        current_price = float(stock_data['Close'].iloc[-1])  # Explicit float conversion
        st.write(f"Current Price: ${current_price:.2f}")
        
        # AI Prediction
        prediction = predict_stock_price(ticker)
        if isinstance(prediction, float):
            st.write(f"AI 7-Day Forecast: ${prediction:.2f}")
            if prediction > current_price:
                st.success("AI Suggests: Potential Growth")
            else:
                st.error("AI Suggests: Possible Decline")
        else:
            st.warning(prediction)
        
        col_buy, col_sell = st.columns(2)
        with col_buy:
            if st.button(f"Buy {ticker}"):
                shares = investment / current_price
                if investment <= st.session_state.balance:
                    st.session_state.portfolio[ticker] = st.session_state.portfolio.get(ticker, 0) + shares
                    st.session_state.balance -= investment
                    st.success(f"Bought {shares:.2f} shares of {ticker}")
                else:
                    st.error("Insufficient funds")
        
        with col_sell:
            if st.button(f"Sell {ticker}"):
                owned_shares = st.session_state.portfolio.get(ticker, 0)
                if owned_shares > 0:
                    shares = investment / current_price
                    if shares <= owned_shares:
                        st.session_state.portfolio[ticker] = owned_shares - shares
                        st.session_state.balance += investment
                        st.success(f"Sold {shares:.2f} shares of {ticker}")
                    else:
                        st.error("Not enough shares to sell")
                else:
                    st.error("No shares to sell")

    # Portfolio Display
    st.subheader("Your Portfolio")
    portfolio_cols = st.columns(3)
    portfolio_cols[0].write("**Stock**")
    portfolio_cols[1].write("**Shares**")
    portfolio_cols[2].write("**Current Value**")
    
    total_value = 0.0
    for stock, shares in st.session_state.portfolio.items():
        if shares > 0:
            try:
                price_data = yf.download(stock, period='1d')
                if not price_data.empty:
                    price = float(price_data['Close'].iloc[-1])  # Explicit float conversion
                    value = shares * price
                    total_value += value
                    portfolio_cols[0].write(stock)
                    portfolio_cols[1].write(f"{shares:.2f}")
                    portfolio_cols[2].write(f"${value:.2f}")
            except Exception as e:
                st.error(f"Error loading {stock} data: {str(e)}")
    
    if total_value == 0:
        st.write("Your portfolio is empty")
    else:
        st.write(f"**Total Portfolio Value: ${total_value:,.2f}**")
        st.write(f"**Net Worth: ${(st.session_state.balance + total_value):,.2f}**")

except Exception as e:
    st.error(f"Could not retrieve stock data: {str(e)}")

st.caption("Note: This is a simulation for educational purposes. AI predictions are not financial advice.")