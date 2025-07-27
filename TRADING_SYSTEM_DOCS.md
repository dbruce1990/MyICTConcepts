# ICT Trading System - Developer Documentation

## Table of Contents
1. [System Overview](#system-overview)
2. [Core Concepts](#core-concepts)
3. [Timeframe Hierarchy](#timeframe-hierarchy)
4. [Trade Setup Requirements](#trade-setup-requirements)
5. [Technical Implementation](#technical-implementation)
6. [Development Guidelines](#development-guidelines)
7. [Configuration Defaults](#configuration-defaults)

---

## System Overview

This is a comprehensive mechanical trading system based on ICT (Inner Circle Trader) concepts, combining multiple timeframe analysis with precise entry/exit criteria. The system is designed to eliminate emotion and provide consistent, rule-based trading decisions.

### Core Philosophy
- **Mechanical Approach**: Every decision is rule-based, no discretion
- **Multi-Timeframe Confluence**: Higher timeframes provide direction, lower timeframes provide precision
- **Statistical Backing**: Next Candle Model provides probabilistic edge
- **Risk Management**: CISD provides clear invalidation points

---

## Core Concepts

### 1. The TTrades Fractal Model (Foundation Framework)
**Core Philosophy**: "Price alternates between large and small ranges. Expansion occurs when price moves consistently in one direction with momentum."

**The Framework**:
- **Higher Timeframe Analysis**: Identify bias and structural levels
- **C2 Detection**: Spot potential swing formations via previous high/low tests with inside closes
- **LTF CISD Confirmation**: Change in state of delivery on lower timeframes
- **Expansion Anticipation**: When all align, expect momentum expansion

**Key Insight**: This entire system is built around the fractal nature of markets - the same patterns repeat across all timeframes.

### 1. Next Candle Model (Foundation Concept) - TTrades Implementation
**Definition**: A statistical price action model that predicts the direction of the next candle based on current candle behavior relative to the previous candle.

**TTrades Mechanical Rules** (from actual code):
```
if close[1] > previous_high:
    bias = 1 (target previous high again)
else if close[1] < previous_low:
    bias = -1 (target previous low again)  
else if close[1] < previous_high AND close[1] > previous_low AND current_high > previous_high AND current_low > previous_low:
    bias = -1 (failed to close above previous high, bias previous low)
else if close[1] > previous_low AND close[1] < previous_high AND current_high < previous_high AND current_low < previous_low:
    bias = 1 (failed to close below previous low, bias previous high)
else if current_high <= previous_high AND current_low >= previous_low:
    bias = inherit from previous candle direction (inside bar)
else:
    bias = 0 (outside bar, no bias)
```

**Bias Types**:
- **PDH/PCH (Previous Day/Candle High)**: Close above → Target high again
- **PDL/PCL (Previous Day/Candle Low)**: Close below → Target low again  
- **Failed Close Above**: Swept high but closed inside → Target low
- **Failed Close Below**: Swept low but closed inside → Target high
- **Inside Bar**: Inherit bias from previous candle's close direction
- **Outside Bar**: No specific bias assigned

**Statistical Tracking** (automated in TTrades code):
- Success Rate: How often price hits the targeted level
- Close Through Rate: How often price closes through after hitting
- Sample Size: Number of times each bias was assigned
- Real-time color coding: Blue (active) → Red (hit)

**Key Rule**: "It takes 3 candles to make a swing point. Find me a reversal that didn't form a swing point first - it doesn't exist."

### 2. Candle 2 Closure (C2) - The Core Fractal Pattern
**Definition**: C2 **IS** the Next Candle Model in action. It's the specific pattern that indicates swing formation is beginning.

**The TTrades Fractal Model Logic**:
1. **Candle 1**: Establishes direction (upclose/downclose)
2. **Candle 2**: Tests the previous candle's extremes but closes back inside
3. **Candle 3**: The anticipated swing completion

**Mechanical Rules** (from TTrades):
- **Bullish C2**: Price takes PDH (Previous Day High) but closes back inside previous candle
- **Bearish C2**: Price takes PDL (Previous Day Low) but closes back inside previous candle
- **Inside Bar**: Inherits bias from previous candle's close direction
- **Outside Bar**: No bias assigned

**Critical Understanding**: C2 is not separate from Next Candle Model - it's the visual manifestation of the bias prediction. When C2 forms, we anticipate C3 (swing completion) in the direction opposite to the sweep.

**Multi-Timeframe Application**: 
- HTF C2 formation → Drop to LTF for CISD confirmation
- Allows early entry while HTF swing is still forming

### 3. CISD (Change in State of Delivery) - TTrades Definition
**Definition**: The moment when orderflow changes direction, confirmed by closing through the opening prices of the delivery candles.

**TTrades Methodology**:
- **Series Identification**: Find the consecutive candles that created the high/low
- **Opening Price Levels**: Mark the opening prices of these "delivery" candles  
- **State Change**: When price closes through these openings in opposite direction
- **Confirmation**: This confirms the change from one delivery state to another

**Visual Implementation**: 
- Blue horizontal lines from order block opening prices to trigger points
- Lines extend from the opening price level to the point where CISD triggers

### 5. Fair Value Gaps (FVG)
**Definition**: Price imbalances on the chart where price "gaps" leaving unfilled areas.

**Types**:
- **BISI**: Buy Side Imbalance (bullish FVG)
- **SIBI**: Sell Side Imbalance (bearish FVG)

**Usage**: Higher timeframe FVGs serve as potential target/reversal areas

---

### 4. Order Blocks & Protected Swing Points - The Tightly Coupled Trinity
**Critical Understanding**: CISD, Order Blocks, and Protected Swing Points are the SAME concept viewed from different angles.

**The Relationship**:
- **CISD Occurrence** → **Confirms Order Block Formation** → **Creates Protected Swing Point**
- **Order Block** = The price level series that created the CISD
- **Protected Swing Point** = The swing point that becomes "protected" by the Order Block
- **CISD** = The confirmation mechanism that validates the Order Block

**Mechanical Process**:
1. Swing point gets swept (liquidity grab)
2. Series of candles create the sweep (potential Order Block)
3. Price closes through Order Block opening prices (CISD triggers)
4. CISD confirmation = Order Block validated = Swing Point becomes "protected"

**Why "Protected"**:
- The swing point now has a validated Order Block defending it
- Future price interactions with this level have higher significance
- Provides mechanical invalidation levels for trades

**Visual Implementation**:
- Order Block = Rectangle/box highlighting the sweep candle series
- Protected Swing Point = Enhanced swing line with different color/style
- CISD = Blue horizontal line showing the trigger level

**Integration Notes**:
- Not all swing points become protected (need CISD confirmation)
- Order Blocks without CISD are just potential areas
- Protected status can be revoked if Order Block is fully consumed

---

## Timeframe Hierarchy

### Standard Pairings
```
Weekly → 4hr → 15m → 1m
Daily → 1hr → 5m
1hr → 5m → 1m
30m → 3m
15m → 1m
5m → 15s
```

### Role of Each Timeframe
1. **Higher Timeframe (HTF)**: Provides overall bias and target areas
2. **Structure Timeframe**: Market structure analysis and swing point identification  
3. **Confirmation Timeframe**: CISD detection and setup confirmation
4. **Execution Timeframe**: Precise entry timing

### Primary Focus Pairing: Weekly → 4hr → 15m
- **Weekly**: "Next Week Bias" - overall directional bias
- **4hr**: Market structure, swing point formation, setup identification
- **15m**: CISD confirmation, precise entry timing

---

## Trade Setup Requirements

### ALL Conditions Must Be Met:

1. **HTF Bias Alignment**: Weekly bias must support 4hr direction
2. **4hr Structure**: 
   - Price trades into HTF swing point OR
   - Price is inside 4hr FVG
3. **Swing Point Formation**: 4hr swing forms above old high (for bullish setups)
4. **Candle 2 Closure**: C2 pattern confirms potential swing formation
5. **LTF Confirmation**: 15m CISD provides invalidation level
6. **Next Candle Model**: Bias aligns with trade direction

### Entry Process:
1. Mark HTF swing points and FVGs
2. Monitor for 4hr price action into these levels
3. Wait for C2 closure pattern
4. Drop to 15m for CISD confirmation
5. Execute with clear invalidation level

---

## Technical Implementation

### Current Status:
- ✅ Swing point detection (3-bar pivots)
- ✅ FVG detection and rendering
- ✅ Basic CISD detection (single timeframe)
- ❌ Multi-timeframe analysis
- ❌ Next Candle Model integration
- ❌ C2 detection
- ❌ HTF context awareness

### Required Development:

#### Phase 1: Foundation
- [ ] Multi-timeframe data access
- [ ] Next Candle Model implementation
- [ ] C2 detection algorithm
- [ ] Timeframe configuration system

#### Phase 2: Integration
- [ ] HTF swing point analysis
- [ ] HTF FVG detection
- [ ] Cross-timeframe CISD validation
- [ ] Trade setup validator

#### Phase 3: Dashboard
- [ ] Multi-timeframe status display
- [ ] Setup completion indicators
- [ ] Bias alignment visualization

---

## Development Guidelines

### Code Organization Principles:
1. **Modular Design**: Each concept in separate, well-defined functions
2. **Clear Naming**: Function and variable names reflect trading terminology
3. **Extensive Comments**: Explain the "why" not just the "what"
4. **Performance Conscious**: Limit array sizes, cleanup old data
5. **User Configurable**: Settings for all major parameters

### Pine Script Considerations:
- Use `request.security()` for multi-timeframe data
- Implement proper array capping for performance
- Use time-based coordinates for drawing objects
- Handle bar state properly (confirmed vs real-time)

### Testing Approach:
- Start with single timeframe pair (4hr → 15m)
- Validate each component individually
- Test integration step by step
- Use debug tables for validation

---

## Configuration Defaults

### Timeframe Pairs:
```
Primary: "1W" → "4h" → "15m"
Secondary: "1D" → "1h" → "5m"  
Scalping: "4h" → "15m" → "1m"
```

### Display Settings:
- Max swing points: 100
- Max FVGs: 50
- Max CISDs: 10
- Lookback bars: 500

### Colors:
- Active swings: Black
- Swept swings: Black (dashed)
- FVGs: Blue (#2962FF, 80% transparency)
- CISDs: Blue (#2962FF)

### Next Candle Model:
- Track all bias types (PCH, PCL, Inside PCH, Inside PCL)
- Display success rate statistics
- Update bias on confirmed bars only

---

## Evolution Notes

### Recent Realizations:
- CISD is more complex than initially thought - requires HTF context
- Next Candle Model is foundational to everything
- C2 detection is crucial for early entry timing
- Multi-timeframe integration is essential, not optional
- System is mechanical but highly sophisticated

### Future Enhancements:
- HTF projection system (where swings will form)
- Advanced bias calculation
- Alert system for complete setups
- Performance statistics tracking
- Risk management integration

---

## Decision Framework

When overwhelmed by complexity:
1. **Focus on Foundation**: Next Candle Model first
2. **One Concept at a Time**: Master individually before integration
3. **Test Incrementally**: Small steps, validate each
4. **Document Everything**: Preserve knowledge for future sessions
5. **Stay Mechanical**: Resist discretionary additions

## Brain Dump Section - Additional Concepts

### TTrades Code Analysis Insights:
From the Daily Bias script, we can see the complete mechanical framework:

**Data Structure Pattern**:
```pinescript
type info
    float ph, pl, ch, cl, co  // Previous/Current High/Low/Close/Open
    bool p_up                 // Previous candle direction
    int bias                  // Current bias (-1, 0, 1)
    int bias_ph, bias_pl      // Counters for bias assignments
    int hit_ph, hit_pl        // Counters for successful hits
    int close_ph, close_pl    // Counters for close-throughs
```

**Multi-Timeframe Implementation**:
- Uses `timeframe.change()` to detect new periods
- Separate info objects for Daily and Weekly
- Automatic timeframe validation (`timeframe.in_seconds()`)
- Real-time line drawing with color changes

**Visual Framework**:
- Blue lines before hit → Red lines after hit
- Triangle markers when levels are reached
- Real-time bias display (colored squares)
- Statistics table with success rates
- Customizable colors, positions, sizes

**Alert System**:
- Bias assignment alerts (PDH, PDL, No Bias)
- Level hit alerts (Hit PDH, Hit PDL)
- Frequency control (`alert.freq_once_per_bar`)

---

## Brain Dump Section - User's Complete System

### Core Philosophy:
**"At the end of the day we're just trading swing points lol. It's actually pretty straightforward."**

### System Goal:
Build TTrades Fractal Model functionality (without monthly subscription) + Personal enhancements for rapid chart analysis across watchlist.

### What Makes This Different from TTrades:
- **Free & Customizable**: No monthly fees, full code control
- **Enhanced Context**: Better integration of swing points/liquidity sweeps with C2 detection
- **Personal Projections**: Different projection methodology than TTrades default
- **Scanning Capability**: Proper alerts using `barstate` for trade opportunity detection
- **Watchlist Efficiency**: Quick chart flipping to find MORE trade opportunities

### Visual Requirements (from TTrades Fractal Model):
1. **HTF Candles**: Higher timeframe candle visualization on lower timeframe charts
2. **C2/C3/C4 Labels**: Clear marking of fractal progression 
3. **CISD Detection**: Must occur inside HTF C2 or C3 candle (ignore after C3 closes)
4. **Vertical Time Lines**: Session/period separators (user has existing script for this)
5. **Context Integration**: C2 formations above/below swing points OR inside FVGs
6. **Real-time Updates**: Dynamic color coding and status changes

### Trading Workflow:
1. **C2 Detection**: "Hey we have a potential trade idea"
2. **Context Validation**: Is C2 above/below swing point OR inside FVG?
3. **C3 Hunting**: Begin looking for entry opportunities
4. **C4 Execution**: Execute trades in swing formation
5. **CISD Invalidation**: Clear stop-loss levels from CISD

### Tracking Requirements (PDArrays):
- ✅ **Swing Points**: Pretty solid, can be refined  
- ✅ **Fair Value Gaps**: Fairly flushed out, can be improved
- 🔄 **Order Blocks**: Tightly coupled with CISD and Protected Swing Points (not separate feature)

### Technical Architecture Needs:
- **Object-Oriented Design**: Lots to track across multiple timeframes
- **Multi-Timeframe Integration**: HTF context + LTF execution
- **Performance Optimization**: Handle large datasets efficiently
- **Alert System**: Proper `barstate` handling for scanning alerts

### User's Existing Resources:
- TTrades Daily Bias script (80-90% of Next Candle Model)
- **Period Separator script** (for HTF session visualization and opening price lines)
- Current ICT indicator foundation (swing points, FVGs, basic CISD)

### HTF Implementation Strategy:
**Phase 1: Period Separators & HTF Data Access**
- Integrate existing period separator logic for visual HTF boundaries
- Implement `request.security()` for HTF OHLC data
- Add HTF opening price lines (already in period separator script)

**Phase 2: HTF Candle Visualization**
- Draw HTF candle boxes/outlines on LTF chart
- Implement C2 detection within HTF candle boundaries
- Add C2/C3/C4 labeling system

**Phase 3: Context Integration**
- Validate C2 formations against swing points and FVGs
- Restrict CISD detection to C2/C3 timeframes
- Implement Order Block and Protected Swing Point logic

### Development Priority:
1. **HTF Candle Integration**: Get higher timeframe data display working
2. **C2 Detection Algorithm**: Implement the fractal pattern recognition
3. **Context Validation**: Ensure C2 forms at proper levels (swings/FVGs)
4. **CISD Timing**: Restrict detection to C2/C3 periods only
5. **Order Block Detection**: Complete the PDArray trilogy
6. **Alert System**: Scanning and notification capability

### Key Success Metrics:
- **Speed**: Rapid watchlist analysis (reduce time spent marking charts)
- **Accuracy**: Proper context validation (swing points + FVGs)
- **Completeness**: All TTrades functionality + personal enhancements
- **Automation**: Alert-based opportunity detection

---

*This document serves as the authoritative source for system understanding and development decisions. Update as concepts evolve and new insights emerge.*
