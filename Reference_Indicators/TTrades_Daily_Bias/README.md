# TTrades Daily Bias - Reference Implementation

## Overview
This is the complete **open-source** implementation of the TTrades Daily Bias indicator by TradeForOpp. This indicator provides the **mechanical bias system** that forms the foundation of the TTrades methodology and is integrated into the commercial Fractal Model.

## Reference Links
- **Official TradingView Page**: https://www.tradingview.com/script/xdwgV3Fx-TTrades-Daily-Bias-TFO/
- **Author**: TradeForOpp (tradeforopp)
- **Social**: X: @TradeForOpp, YouTube: @tradeforopp, Instagram: @tradeforopp
- **Website**: https://stratalerts.com/tfo/
- **Type**: Open-source script (free to use with attribution)

## Official Description

Inspired by TTrades_edu video on daily bias, this indicator develops a higher timeframe bias and collects statistical data on its success rate. While TTrades introduced multiple concepts, this indicator focuses on one specific method utilizing previous highs and lows.

### Bias Assignment Logic (Official Rules)

#### Daily Timeframe Scenarios:
1. **Close Above PDH**: Following day's bias targets PDH
2. **Trade Above PDH but Close Below**: Following day's bias targets PDL  
3. **Close Below PDL**: Following day's bias targets PDL
4. **Trade Below PDL but Close Above**: Following day's bias targets PDH
5. **Inside Bar (No PDH/PDL Touch)**: Refer to previous candle direction
   - Previous day closed above open → Target PDH
   - Previous day closed below open → Target PDL
6. **Outside Bar (Takes Both PDH/PDL but Closes Inside)**: No bias assigned

**Note**: Weekly timeframe functions identically with PWH/PWL (Previous Week High/Low)

## Key Components

### Statistical Analysis Features

#### Visual Components
- **Previous High/Low Lines**: Blue (before hit) → Red (after hit) with customizable colors
- **Period Separators**: Daily and weekly boundary visualization  
- **Triangular Markers**: Plotted when PDH/PDL levels are traded through
- **Bias Indicators**: Color-coded squares showing current bias direction (customizable top/bottom placement)

#### Statistics Table (Comprehensive Data)
1. **Success Rate**: Percentage of times price successfully reached the assigned target
2. **Close-Through Rate**: From successful hits, percentage that actually closed through the level
3. **Sample Size**: Total instances where each bias type was assigned
4. **Color Coding**: Blue (current target not hit) → Red (target reached)

**Example Interpretation**: 
- PDH row shows 279 sample size
- 76.7% success rate reaching PDH
- 53.7% close-through rate after hitting PDH

#### Alert System
- **Bias Assignment**: New period bias determination alerts
- **Liquidity Raids**: PDH/PDL hit notifications  
- **Session Changes**: Daily/weekly period transitions
- **Configurable Options**: Specific alert types or "Any alert() function call"

## Critical Integration Points

### For Our Main Indicator
1. **CISD Detection**: Uses this bias logic as foundation
2. **HTF Integration**: Multi-timeframe bias calculation
3. **Order Block Context**: Bias determines order block significance
4. **Protected Swing Points**: Bias influences protection status

### TTrades Fractal Model Connection
- This bias system is the **core engine** driving C2 detection
- HTF bias + LTF CISD = Expansion moments
- Statistical foundation provides confidence levels
- Mechanical nature ensures consistency

## Code Analysis & Technical Implementation

### Data Structures
- `info` type: Tracks OHLC data, bias states, hit counters, statistical metrics
- `lines` type: Manages previous high/low visualization with hit detection
- Multi-timeframe support (Daily and Weekly with extensibility)

### Key Functions  
- `handle_bias()`: Core mechanical bias assignment algorithm
- `update_info()`: Session management and OHLC data collection
- `update_lines()`: Visual line management with hit detection and color changes
- Statistics tracking with comprehensive success rate calculations

### Alert Infrastructure
- Bias assignment alerts with mechanical reasoning
- Liquidity raid notifications for PDH/PDL hits
- Session change notifications for period transitions
- Configurable alert types with specific conditions

## Implementation Notes

### For Our System Integration
- ✅ **Open Source**: Complete code available for analysis and adaptation
- ✅ **Mechanical Foundation**: Exact algorithmic rules for bias calculation
- ✅ **Multi-timeframe Support**: Daily and Weekly patterns with extensibility
- ✅ **Statistical Validation**: Built-in success rate tracking and analysis
- ✅ **Alert Infrastructure**: Comprehensive notification system
- 🚧 **Integration Needed**: Connect with our swing/CISD detection systems

### Performance Considerations
- Multi-timeframe line management with hit detection
- Array management for historical data collection
- Real-time vs historical calculation optimization
- Drawing object limits and cleanup procedures

## Author Information
- **Creator**: TradeForOpp (tradeforopp)
- **Type**: Open-source script (TradingView House Rules apply)
- **Social**: X: @TradeForOpp, YouTube: @tradeforopp, Instagram: @tradeforopp
- **Website**: https://stratalerts.com/tfo/
- **License**: Open-source with attribution requirements

## Usage in Our Development
This code provides the **exact mechanical foundation** for:
1. Understanding how bias drives CISD detection
2. Implementing multi-timeframe bias calculation
3. Creating statistical tracking systems
4. Building proper alert mechanisms

## Next Steps
1. Extract bias calculation logic for our main indicator
2. Adapt for multiple timeframe pairs (not just Daily/Weekly)
3. Integrate with our existing swing point detection
4. Connect bias states to CISD and order block systems
