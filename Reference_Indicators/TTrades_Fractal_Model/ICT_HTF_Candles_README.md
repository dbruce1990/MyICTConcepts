# ICT HTF Candles - Reference Implementation

## Overview
This is a comprehensive **open-source** HTF (Higher Time Frame) candle visualization system by Fadi Zeidan. This code is **critical for our HTF implementation** and provides the foundation for displaying multiple timeframes, period boundaries, and imbalance detection within ICT concepts.

## Reference Links
- **Official TradingView Page**: https://www.tradingview.com/script/0KTDWTdN-ICT-HTF-Candles-Source-Code-fadi/
- **Author**: Fadi Zeidan (fadizeidan)
- **Social**: X: @fadizeidan
- **Website**: https://www.theicttrader.com/
- **Type**: Open-source script (free to use with attribution)

## Official Description

"Plotting a configurable higher timeframe on current chart's timeframe helps visualize price movement without changing timeframes. It also plots FVG and Volume Imbalance on the higher timeframe for easier visualization."

**ICT Concept Application**: "With ICT concepts, we usually wait for HTF break of structure and then find an entry on a lower timeframe. With this indicator, we can set it to the HTF and watch the development of price action until the break of structure happens. We can then take an entry on the current timeframe."

## Key Architecture Components

### Data Structures
```pinescript
type Candle {
    float o, c, h, l           // OHLC values
    int o_time, o_idx, c_idx   // Time and bar indices
    int h_idx, l_idx           // High/low formation indices
    string dow                 // Day of week / time label
    box body, line wick_up, line wick_down  // Visual elements
    label dow_label            // Time period label
}

type CandleSet {
    array<Candle> candles      // HTF candle collection
    array<Imbalance> imbalances // FVG/VI detection
    CandleSettings settings    // Timeframe configuration
    label tfNameTop/Bottom     // Timeframe labels
    label tfTimerTop/Bottom    // Countdown timers
}
```

## Key Features (Official Settings)

### HTF Configuration
- **HTF Selection**: Configurable higher timeframe to plot on current chart
- **Display Count**: Number of HTF candles to display to the right of current price action
- **Multiple HTF Support**: Up to 6 different higher timeframes simultaneously
- **Limit HTF Display**: Control to show only next 3 HTF candles (or custom amount)

### Visual Customization
- **Body/Border/Wick Colors**: Separate color controls for bullish/bearish candles
- **Positioning Controls**: 
  - Padding from current candles (distance from LTF price action)
  - Space between candles (candle spacing adjustment)
  - Candle width (size of the HTF candles)

### Imbalance Detection
- **Fair Value Gap (FVG)**: Show/Hide FVG detection on the higher timeframe
- **Volume Imbalance**: Show/Hide Volume Imbalance on the higher timeframe  
- **Real-time Updates**: FVGs and V.I. now show on developing candles (Feb 2024 update)

### Advanced Features
- **Trace Lines**: Extend OHLC lines of the higher timeframe with source labeling
- **Price Labels**: Show/Hide price levels of the OHLC values
- **Remaining Time Label**: Countdown timer to next HTF candle close
- **Custom Daily Opens**: Midnight, 8:30, or 9:30 session starts (Nov 2024 update)

### Label System (Nov 2024 Updates)
- **Label Position**: Both above/below candles, above only, or below only
- **Label Alignment**: Align at same level or follow candles (above high/low)
- **Interval Value Display**: Shows time for each candle (except weekly/monthly)

## Critical Methods for Our Implementation

### 1. `Monitor()` - Period Change Detection
```pinescript
HTFBarTime = time(candleSet.settings.htf, 'america/New_York')
isNewHTFCandle = ta.change(HTFBarTime) > 0
```
**Key Learning**: This is how we detect new HTF periods for C2 detection!

### 2. `Update()` - Real-time OHLC Tracking
- Updates current HTF candle with LTF price action
- Tracks high/low formation bar indices (critical for CISD timing)
- Real-time visual updates

### 3. `FindImbalance()` - FVG/VI Detection
- Fair Value Gap detection within HTF periods
- Volume Imbalance identification
- Integration with HTF context

### 4. Visual Management
- **Trace Lines**: OHLC level extensions with labels
- **Positioning**: Dynamic offset calculation for multiple HTFs
- **Timer System**: Countdown to next HTF close

## Integration Strategy for Our System

### Phase 1: HTF Period Framework
```pinescript
// Extract from ICT HTF Candles
- HTF period detection using time() function
- OHLC data collection for each HTF period
- Period boundary visualization
```

### Phase 2: C2 Detection Foundation
```pinescript
// Critical insight from Monitor() method
isNewHTFCandle = ta.change(time(htf_timeframe)) > 0

// Our C2 detection logic
if isNewHTFCandle
    // Start watching for CISD within this HTF period
    // Apply TTrades bias logic from Daily Bias indicator
    // Track order block formations
```

### Phase 3: Multi-Timeframe Architecture
- **Timeframe Pairs**: Weekly→4hr, 4hr→15m, 15m→1m
- **Bias Calculation**: Use TTrades Daily Bias logic across pairs
- **CISD Context**: HTF bias + LTF CISD = Entry signals

## Key Technical Insights

### 1. Time Management
- Uses `time(htf, timezone)` for accurate period detection
- Custom daily opens for different market sessions
- Bar index tracking for precise timing

### 2. Visual Architecture
- Box/line drawing for HTF candles
- Dynamic positioning with offset calculations
- Array management with size limits

### 3. Imbalance Integration
- FVG detection within HTF periods
- Volume imbalance identification
- Box-based visual representation

### 4. Performance Optimization
- Limited display count per timeframe
- Proper object deletion management
- Real-time vs historical calculation handling

## Code Sections We Need

### 1. Period Detection (Lines 550-580)
```pinescript
HTFBarTime = time(candleSet.settings.htf, 'america/New_York')
isNewHTFCandle = ta.change(HTFBarTime) > 0
```

### 2. OHLC Tracking (Lines 570-600)
```pinescript
candle.o := open
candle.c := close  
candle.h := high
candle.l := low
candle.o_idx := bar_index
```

### 3. Visual Management (Lines 440-500)
```pinescript
// Dynamic positioning and offset calculation
// Multiple HTF display management
```

## Implementation Priority

### For Our Main Indicator
1. **Extract HTF Period Detection**: Use the `time()` approach for accurate periods
2. **Adapt OHLC Collection**: Track HTF OHLC within our existing structure
3. **Integrate C2 Logic**: Combine with TTrades bias for C2 detection
4. **Visual Enhancement**: Add period boundaries to our existing system

### Integration Points
- **Period Separator**: Use this approach instead of our current separator
- **CISD Detection**: Apply within HTF period boundaries
- **Order Block Context**: HTF OHLC provides order block reference levels
- **Multi-Timeframe**: Foundation for multiple TF pairs

## Next Development Steps
1. Extract core HTF period detection logic
2. Integrate with our existing swing/CISD system
3. Add multi-timeframe bias calculation using TTrades logic
4. Implement C2 detection within HTF boundaries
5. Create dynamic timeframe pairing system

## Author Information & Updates
- **Creator**: Fadi Zeidan (fadizeidan)  
- **Type**: Open-source script (TradingView House Rules apply)
- **Social**: X: @fadizeidan
- **Website**: https://www.theicttrader.com/
- **Latest Update**: February 2025

### Recent Updates Timeline
- **Feb 22, 2025**: Bug fix for interval label clearing on new candle prints
- **Feb 18, 2025**: Timer display toggle fix, renamed "Day of Week" to "Interval Value"  
- **Nov 28, 2024**: Timer label positioning fix
- **Nov 26, 2024**: Custom Daily Opens, Label Alignment options, Day of Week display
- **Nov 5, 2024**: Offset calculation bug fix
- **Oct 24, 2024**: Timer update fixes
- **Feb 13, 2024**: Major refactor - code cleanup, HTF limits, remaining time labels, trace line improvements

This code provides the **exact foundation** we need for recreating the TTrades Fractal Model's HTF visualization and C2 detection system!
