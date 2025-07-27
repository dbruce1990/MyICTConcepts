# TTrades Fractal Model - Target Implementation

## Overview
This is our target implementation - the commercial indicator we're recreating with our own enhancements. Since we don't have access to the source code, this directory contains our analysis and reverse-engineering notes.

## What We Know (From Official TradingView Description)

### Core Features
- **Custom History**: Control depth of historical setups (0-40 previous setups) - tailor chart to specific style preferences
- **Fractal Timeframe Pairings**: Automatic HTF/LTF pairing based on chart timeframe, with manual override options
- **Bias Selection**: Complete control over bias detection - bullish, bearish, or neutral (both directions)
- **Timeframe Pairing Validation**: Warning system for incompatible timeframe selections
- **Custom Time Filters**: Up to 3 custom time windows for filtering formations
- **Higher Time Frame Candles (PO3)**: Integrates HTF Power of Three framework for critical turning point visualization
- **Info Table**: Customizable display with timeframe pairing, countdown timer, bias status, and time filter preferences

### TTrades Framework Components

#### Label System
- **TTFM Labels (C2/C3/C4)**: 
  - **Gray**: Valid setup, stable conditions
  - **Red**: Failed setup (price returned to initial high/low without forming HTF swing)
  - **Orange**: Consolidation/slowdown (setup didn't fail within next HTF candle)

#### Core Detection Systems
- **Candle 1 Liquidity**: Horizontal rays marking swing points with liquidity sweep visualization
- **Change in State of Delivery (CISD)**: Series of candles making significant highs/lows, close beyond opening price signals trend reversal
- **Candle Equilibrium**: 50% levels of HTF ranges showing discount/premium zones for entries/exits
- **T-Spot Identification**: Anticipated HTF wick formation points based on TTrades methodology
- **Projections**: User-defined future price targets [-1, -2, -2.5, -4, -4.5] for redelivery/rebalance points
- **Formation Liquidity**: Previous candle highs/lows as critical engineered liquidity pools

## Key Insights

### The Fractal Model Logic (Official Description)
1. **Cyclical Nature**: "Rooted in the cyclical nature of price movements, where price alternates between large and small ranges"
2. **Expansion Mechanics**: "Expansion occurs when price moves consistently in one direction with momentum"
3. **HTF + LTF Integration**: "By combining higher Timeframe closures with the confirmation of the change in state of delivery (CISD) on the lower Timeframe, the model reveals moments when expansion is poised to occur"
4. **Stability**: "Remains stable and non-repainting, offering traders reliable, unchanged levels within the given Time period"
5. **Adaptability**: "Seamlessly adjusts to any asset, market condition, or Timeframe"

### Visual System & Automation
- **Color Coding**: Dynamic status indication with specific color meanings for setup progression
- **Label System**: C2/C3/C4 progression tracking with failure/consolidation states
- **Horizontal Rays**: Liquidity sweep visualization with engineered liquidity pools
- **Projection Lines**: Future price target areas based on delivery shifts
- **Fully Automated Framework**: All components customizable to match visual preferences and model timeframes

## Our Implementation Goals

### What We're Replicating
- [ ] HTF candle visualization with period boundaries
- [ ] C2/C3/C4 detection and labeling
- [ ] CISD detection within HTF context
- [ ] Liquidity sweep identification
- [ ] Dynamic color coding system
- [ ] Customizable timeframe pairings
- [ ] Statistical tracking and info table

### Our Enhancements
- [ ] Better swing point integration (our existing system)
- [ ] Enhanced FVG detection and context
- [ ] Improved alert system with proper barstate handling
- [ ] Custom projection methodology
- [ ] Free and open source with full customization

## Development Strategy

### Phase 1: Foundation
- Integrate period separator for HTF visualization
- Add HTF OHLC data collection
- Implement basic C2 detection within HTF periods

### Phase 2: Core Features
- Add C2/C3/C4 labeling system
- Implement CISD detection with HTF context
- Create dynamic color coding

### Phase 3: Advanced Features
- Add projection system
- Implement liquidity sweep detection
- Create comprehensive info table

### Phase 4: Polish
- Alert system optimization
- Performance tuning
- Visual customization options

## Missing Information
Since this is a paid indicator, we need to reverse-engineer:
- Exact C2 detection algorithm
- Precise CISD timing rules
- T-Spot calculation methodology
- Projection formula
- Alert conditions

## Reference Links
- **Official TradingView Page**: https://www.tradingview.com/script/XdwK9qQQ-Fractal-Model-Pro-TTrades/
- **Author**: TooDegreesofficial (toodegrees) 
- **Website**: https://www.toodegrees.trade/ttfm
- **Social**: X: @toodegrees, YouTube, Instagram channels
- **Type**: Invite-only commercial indicator (paid access required)
- **ICT_HTF_Candles_(fadi).pine**: Complete HTF visualization system with period detection, OHLC tracking, and imbalance detection
- **ICT_HTF_Candles_README.md**: Detailed analysis of HTF implementation approach

## Implementation Status
- **Indicator Type**: Invite-only commercial indicator (paid access required)
- **Latest Updates**: February 2025 - Performance optimizations, custom model timeframes, wick projections
- **Key Improvements**: 10x speed improvement, timezone support, floating drawings removal
