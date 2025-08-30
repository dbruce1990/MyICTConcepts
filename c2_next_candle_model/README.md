# C2 Next Candle Model Statistics Tracker

## Purpose
Track the statistical success rates of **C3 continuations** specifically after **C2 closures**, rather than tracking all Next Candle Model scenarios. This provides focused data on what you actually trade.

## Project Goals
- **Focused Statistics**: Only track C2 → C3 scenarios (not every candle)
- **Actionable Data**: Success rates for the patterns you actually trade
- **Real Trading Metrics**: Does C3 follow Next Candle Model logic after C2?

## Logic Flow

### C2 Detection
**Definition**: A candle that sweeps the high/low of the previous candle but closes back inside the previous candle's range.

**Types**:
- **Bullish C2**: Sweeps C1 low, closes inside C1 range → Bias C1 high  
- **Bearish C2**: Sweeps C1 high, closes inside C1 range → Bias C1 low

### C3 Success Criteria  
**Success**: C3 reaches the biased level (touches C1 high/low)
- Does **NOT** require close beyond
- Just needs to **touch** the target level

### Statistics Tracked
1. **C2 Bull→PCH**: Bullish C2s expecting C3 to take C1 high
2. **C2 Bear→PCL**: Bearish C2s expecting C3 to take C1 low  
3. **Combined Success Rate**: Overall C2 → C3 success rate
4. **Close Through Rates**: When C3 hits target, how often does it close beyond?

## Based On
- **TTrades Daily Bias Logic**: Statistical bias calculation
- **Your Next Candle Model Script**: PCH/PCL methodology adapted for C2s
- **C2 Definition**: From copilot-instructions.md methodology

## Files
- `c2_statistics_tracker.pine`: Main indicator script
- `README.md`: This documentation

## Usage
1. Apply indicator to any timeframe
2. Look for C2 labels: Blue ↑ (bullish) / Red ↓ (bearish)
3. Background shading shows "awaiting C3" periods
4. Statistics table shows success rates in top-right corner

## Key Differences from Standard Next Candle Model
- **Selective Tracking**: Only C2 scenarios (not every candle)
- **Specific Pattern Focus**: C2 closure → C3 continuation
- **Trading-Relevant Data**: Stats for patterns you actually execute
- **Timeout Logic**: Stops tracking after 5 bars if no C3 completion

This gives you the **actual statistics** for the pattern you trade, rather than general market bias data.
