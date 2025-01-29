# stock-simulator
📈 AI Stock Simulator

Welcome to the AI Stock Simulator, a Streamlit-based web application that allows users to simulate stock trading using real-time data and AI-driven price predictions. Whether you're a beginner looking to understand the stock market or an enthusiast aiming to test your trading strategies, this simulator provides an interactive and educational experience.

Table of Contents

📈 AI Stock Simulator
Table of Contents
🔍 Overview
🚀 Features
🛠️ Installation
💻 Usage
🎨 User Interface
🔧 Technologies Used
🤝 Contributing
📜 License
📫 Contact
🔍 Overview

The AI Stock Simulator is designed to provide users with a realistic stock trading experience without the financial risk. It integrates real-time stock data fetching, basic AI predictions using linear regression, and a simulated trading environment where users can buy and sell stocks to manage a virtual portfolio.

🚀 Features

Real-Time Stock Data: Fetches up-to-date stock prices and historical data using the yfinance library.
AI-Based Predictions: Utilizes a simple linear regression model to predict future stock prices.
Virtual Trading: Simulate buying and selling stocks with a virtual balance.
Portfolio Management: Track your holdings, current portfolio value, and net worth.
Dark Theme UI: Enhanced user experience with a custom dark-themed interface.
Interactive Charts: Visualize stock price history with dynamic charts.
Responsive Layout: Organized layout with sidebars and columns for seamless navigation.
🛠️ Installation

Follow these steps to set up the AI Stock Simulator on your local machine.

1. Clone the Repository
git clone https://github.com/yourusername/ai-stock-simulator.git
cd ai-stock-simulator
2. Create a Virtual Environment (Optional but Recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
Ensure you have Python 3.7+ installed.

pip install -r requirements.txt
If a requirements.txt file is not provided, you can install the necessary packages manually:

pip install streamlit yfinance numpy pandas matplotlib scikit-learn
4. Run the Application
streamlit run app.py
Replace app.py with the name of your main Python file if different.

5. Access the App
Once the server starts, open your web browser and navigate to http://localhost:8501 to interact with the AI Stock Simulator.

💻 Usage

Enter Stock Symbol:
Use the sidebar to input the stock ticker symbol (e.g., AAPL for Apple Inc.).
Select View History:
Choose the number of days of historical data to view (ranging from 30 to 365 days).
Set Investment Amount:
Specify the amount you wish to invest per transaction (between $10 and $1,000).
View Stock Chart:
The main section displays the selected stock's price history in a line chart.
Trading Panel:
See the current stock price and AI 7-day forecast.
Buy Shares: Purchase shares based on your investment amount.
Sell Shares: Sell shares based on your investment amount.
Portfolio Overview:
Monitor your holdings, including the number of shares, current value, total portfolio value, and net worth.
Balance Management:
Start with an initial balance of $10,000. Buy and sell stocks to manage and grow your virtual balance.
🎨 User Interface

The application features a dark-themed interface with the following components:

Sidebar: Contains controls for stock selection, historical data range, and investment amount.
Main Area:
Stock Chart: Visual representation of the stock's price history.
Trading Panel: Interactive section for buying and selling stocks with AI predictions.
Portfolio Display: Tabular view of your current holdings and financial summaries.

Replace with actual screenshot if available.

🔧 Technologies Used

Streamlit: For building the interactive web application.
yfinance: To fetch real-time and historical stock data.
NumPy: For numerical operations.
Pandas: For data manipulation and analysis.
Matplotlib: For plotting charts.
Scikit-learn: For implementing the linear regression model.
🤝 Contributing

Contributions are welcome! If you'd like to enhance the AI Stock Simulator, follow these steps:

Fork the Repository
Create a Feature Branch
git checkout -b feature/YourFeature
Commit Your Changes
git commit -m "Add some feature"
Push to the Branch
git push origin feature/YourFeature
Open a Pull Request
Please ensure your code adheres to the existing style and includes appropriate documentation.



📫 Contact

For any questions, suggestions, or feedback, feel free to reach out:

Email: reswanth.rejipillai@mail.mcgill.ca
GitHub: @jumpman786

