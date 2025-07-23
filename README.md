# GBP/USD Range Breakout Strategy - Pine Script

This Pine Script strategy implements a sophisticated range breakout trading system specifically designed for the GBP/USD currency pair on OANDA broker.

## Strategy Overview

### Key Features
- **Timeframe**: 5-minute charts
- **Asset**: GBP/USD (OANDA broker)
- **Trading Sessions**: London (8:00-10:00 GMT) and New York (13:00-15:00 GMT)
- **Range Detection**: Uses first 4 candles of each session
- **Two Entry Scenarios**: Shadow break and body break with Fibonacci retracement
- **Risk Management**: 1:1 risk-to-reward ratio with dynamic stop losses
- **Position Sizing**: Starts with $40 (40% of $100 account), compounds by 20% after each trade

## How It Works

### 1. Range Detection
- At the start of each trading session (London 8:00 GMT or New York 13:00 GMT)
- The strategy analyzes the first 4 five-minute candles
- The highest high and lowest low of these 4 candles define the range ceiling and floor

### 2. Entry Scenarios

#### Shadow Break Scenario
- **Trigger**: First candle breaks range ceiling with its high but closes inside the range
- **Entry**: Sell on the next candle
- **Stop Loss**: Above the high of the shadow candle
- **Take Profit**: 1:1 risk-to-reward ratio

#### Body Break and Retracement Scenario
- **Trigger**: Candle breaks range ceiling with body closing outside the range
- **Wait**: For a candle to close back inside the range
- **Fibonacci**: Draw from range low to breakout high (levels: 0, 0.5, 0.618, 1.0)
- **Entry**: When candle closes below 50% Fibonacci level inside the range
- **Stop Loss**: Above the high of the previous two candles
- **Take Profit**: 1:1 risk-to-reward ratio

### 3. Trading Rules
- Only one trade per day allowed
- Trading only within first 2 hours of each session
- Initial position size: $40 (40% of $100 account)
- Position size increases by 20% after each trade (compounding)

## Setup Instructions

### 1. TradingView Setup
1. Open TradingView and navigate to GBP/USD chart
2. Set timeframe to 5 minutes
3. Click on "Pine Editor" at the bottom of the screen
4. Copy and paste the Pine Script code
5. Click "Add to Chart"

### 2. Strategy Configuration
- **Initial Capital**: $100 (set in strategy settings)
- **Commission**: 0.02% (typical for forex)
- **Timezone**: Ensure your chart is set to GMT for proper session detection

### 3. Optimization Settings
The strategy includes input parameters that can be adjusted:
- London Session Start Hour (default: 8 GMT)
- New York Session Start Hour (default: 13 GMT)
- Show Range Lines (visual aid)
- Show Fibonacci Levels (visual aid)

## Visual Elements

### On-Chart Display
- **Range Lines**: Red line for range high, green line for range low
- **Fibonacci Levels**: Dashed lines showing 0%, 50%, 61.8%, and 100% levels
- **Session Background**: Light blue for London session, light orange for New York session
- **Entry Signals**: 
  - Red triangle down for shadow break signals
  - Purple diamond for body break signals
- **Information Table**: Real-time strategy statistics in top-right corner

### Labels and Information
- Range high/low values displayed on chart
- Strategy information table showing:
  - Current position size
  - Trade status for the day
  - Range definition status
  - Session times

## Risk Management

### Position Sizing
- Starts with 40% of account ($40 from $100)
- Increases by 20% after each trade
- Uses percentage of equity for dynamic scaling

### Stop Loss Strategy
- **Shadow Break**: Above shadow candle high
- **Body Break**: Above highest high of previous two candles
- Always maintains 1:1 risk-to-reward ratio

## Backtesting Considerations

### Optimal Settings
- Use 5-minute timeframe data
- Ensure sufficient historical data (at least 6 months)
- Consider spread costs (built into commission settings)
- Test during different market conditions

### Performance Metrics to Monitor
- Win rate
- Average risk-to-reward ratio
- Maximum drawdown
- Profit factor
- Number of trades per month

## Important Notes

1. **Session Timing**: The strategy is timezone-sensitive. Ensure your TradingView chart is set to GMT.
2. **One Trade Per Day**: The strategy prevents overtrading by limiting to one trade per day.
3. **Session Restrictions**: Trades only occur within the first 2 hours of each session.
4. **Fibonacci Precision**: The strategy uses precise Fibonacci calculations for the retracement scenario.
5. **Compounding**: Position size automatically increases by 20% after each trade.

## Troubleshooting

### Common Issues
- **No Trades Appearing**: Check timezone settings and ensure chart is on 5-minute timeframe
- **Range Not Defined**: Verify session start times and ensure sufficient data
- **Fibonacci Not Showing**: Enable "Show Fibonacci Levels" in strategy inputs

### Strategy Validation
- The information table shows real-time status
- Visual signals appear when conditions are met
- Range lines should appear at session start

This strategy is designed for educational and backtesting purposes. Always test thoroughly before live trading and consider consulting with a financial advisor.
