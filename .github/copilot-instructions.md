# GitHub Copilot Repository Instructions

## Project Context
I am developing an ICT (Inner Circle Trader) concepts indicator in Pine Script v6 that recreates the commercial TTrades Fractal Model with personal enhancements. The project is based on multi-timeframe analysis using swing points, Fair Value Gaps (FVGs), and Change in State of Delivery (CISD) detection.

## Key Concepts & Definitions

### ICT Trading Terminology
- **Order Block**: Same as CISD - opening price violation of a swing point that creates liquidity
- **Protected Swing Point**: Same as Order Block - these terms are interchangeable in our system
- **CISD (Change in State of Delivery)**: The most critical component - represents order block formation when swing point opening price is violated
- **FVG (Fair Value Gap)**: 3-candle pattern with gap between high/low of outer candles
- **BISI**: Bearish FVG (Bearish Institutional Support/Resistance Imbalance) 
- **SIBI**: Bullish FVG (Support/Resistance Institutional Bearish Imbalance)
- **C2 Closure**: HTF candle close that triggers expansion moments in TTrades methodology
- **Next Candle Model**: Statistical bias system with 63-67% success rates using PCH/PCL logic

### Technical Architecture
- **Main Script**: `script.pine` (495 lines) with swing points, FVGs, CISD detection
- **Multi-timeframe Hierarchy**: Weekly→4hr→15m→1m with HTF bias providing LTF confirmation
- **HTF Integration**: Higher timeframe provides bias/targets, lower timeframe provides execution signals
- **Statistical Foundation**: TTrades Daily Bias provides mechanical bias calculation (PCH/PCL methodology)

## Pine Script v6 Requirements

### Critical Rules (ALWAYS FOLLOW)
1. **Indentation**: ALWAYS use 4 spaces (never tabs) - this prevents 90% of syntax errors
2. **Drawing Limits**: Set max_boxes_count, max_lines_count, max_labels_count in indicator declaration
3. **Array Bounds**: Check array.size() before array.get() calls
4. **Time Coordinates**: Use xloc.bar_time for persistent drawings, xloc.bar_index for temporary
5. **Barstate Handling**: Use barstate.isconfirmed for final calculations, barstate.islast for updates

### Common Error Prevention
- "Cannot call 'array.get' with argument 'id'=na" → Always initialize arrays and check bounds
- "Index out of bounds" → Add if array.size() > index checks before access
- Drawing object limits → Implement cleanup methods and object pooling
- Indentation errors → Always verify 4-space indentation consistency

## Project Structure & References

### Reference Indicators (All documented with TradingView links)
1. **TTrades Daily Bias** (Open Source): Mechanical bias calculation system
   - Link: https://www.tradingview.com/script/xdwgV3Fx-TTrades-Daily-Bias-TFO/
   - Purpose: Foundation for C2 detection and statistical validation
   
2. **ICT HTF Candles** (Open Source): Multi-timeframe visualization system  
   - Link: https://www.tradingview.com/script/0KTDWTdN-ICT-HTF-Candles-Source-Code-fadi/
   - Purpose: HTF period detection and OHLC tracking for our implementation
   
3. **TTrades Fractal Model** (Commercial): Target system we're recreating
   - Link: https://www.tradingview.com/script/XdwK9qQQ-Fractal-Model-Pro-TTrades/
   - Purpose: Complete automated system with C2/C3/C4 labeling (Gray→Red→Orange)

### File Organization
- `script.pine`: Main indicator implementation
- `Reference_Indicators/`: Organized reference materials with comprehensive READMEs
- `DEVELOPMENT_GUIDELINES.md`: Technical best practices and recurring issue solutions
- `TRADING_SYSTEM_DOCS.md`: Complete methodology documentation

## Development Status & Current Implementation

### Completed ✅
- **Core Foundation**: Swing points, FVGs, CISD detection functional (495 lines in script.pine)
- **Reference System**: Complete documentation with official TradingView links
- **Development Framework**: Guidelines and custom instructions established
- **Swing Point Detection**: State tracking with proper identification
- **FVG Detection**: BISI/SIBI patterns with mitigation tracking
- **CISD Detection**: Watching most recent swept swing only
- **Documentation**: Comprehensive reference materials with official sources

### Current Focus 🚧
- HTF integration using ICT HTF Candles methodology
- Multi-timeframe bias calculation using TTrades Daily Bias logic
- C2 detection within HTF period boundaries  
- Statistical tracking and validation systems

### Next Phases 🎯
- C2/C3/C4 labeling system with progression tracking
- Dynamic color coding (Gray→Red→Orange) for setup states
- Projection system for future price targets
- Complete automation with customizable timeframe pairings

### Implementation Insights
- **Multi-timeframe Hierarchy**: Weekly→4hr→15m→1m with HTF bias providing LTF confirmation
- **HTF Integration**: Higher timeframe provides bias/targets, lower timeframe provides execution signals
- **Statistical Foundation**: TTrades Daily Bias provides mechanical bias calculation (PCH/PCL methodology)
- **Label Progression**: Gray (valid) → Red (failed) → Orange (consolidation) from TTrades Fractal Model

## TTrades Methodology Foundation

### The Fractal Model Logic (Core Framework)
**Philosophy**: "Price alternates between large and small ranges. Expansion occurs when price moves consistently in one direction with momentum."

**Framework Components**:
1. **Cyclical Nature**: Price alternates between large and small ranges
2. **Expansion Mechanics**: Occurs with directional momentum 
3. **HTF + LTF Integration**: HTF closures + LTF CISD = Expansion moments
4. **Non-repainting**: Stable levels within time periods
5. **Universal Application**: Works across assets, markets, timeframes

**Key Insight**: This entire system is built around the fractal nature of markets - the same patterns repeat across all timeframes.

### Next Candle Model (Statistical Foundation)
**Definition**: Statistical price action model predicting next candle direction based on current behavior relative to previous candle.

**TTrades Mechanical Rules** (from actual implementation):
```
if close[1] > previous_high:
    bias = 1 (target previous high again)
else if close[1] < previous_low:
    bias = -1 (target previous low again)  
else if failed_to_close_above_previous_high:
    bias = -1 (bias previous low)
else if failed_to_close_below_previous_low:
    bias = 1 (bias previous high)
else if inside_bar:
    bias = inherit from previous candle direction
else:
    bias = 0 (outside bar, no bias)
```

**Statistical Tracking** (automated in TTrades code):
- Success Rate: How often price hits targeted level (63-67% success rates)
- Close Through Rate: How often price closes through after hitting
- Sample Size: Number of times each bias was assigned
- Real-time color coding: Blue (active) → Red (hit)

### Candle 2 Closure (C2) - Core Fractal Pattern
**Definition**: C2 IS the Next Candle Model in action - the specific pattern indicating swing formation beginning.

**TTrades C2 Logic**:
1. **Candle 1**: Establishes direction (upclose/downclose)
2. **Candle 2**: Tests previous candle's extremes but closes back inside
3. **Candle 3**: Anticipated swing completion

**Critical Understanding**: C2 is not separate from Next Candle Model - it's the visual manifestation of bias prediction. When C2 forms, we anticipate C3 (swing completion) in direction opposite to the sweep.

### CISD (Change in State of Delivery)
**TTrades Definition**: The moment when orderflow changes direction, confirmed by closing through opening prices of delivery candles.

**Implementation**:
- **Series Identification**: Find consecutive candles that created the high/low
- **Opening Price Levels**: Mark opening prices of these "delivery" candles  
- **State Change**: When price closes through these openings in opposite direction
- **Order Block Formation**: CISD creates order blocks and protected swing points

### Bias Assignment Rules (Mechanical)
- Close Above PDH → Bias PDH
- Close Below PDL → Bias PDL
- Failed to Close Above PDH → Bias PDL  
- Failed to Close Below PDL → Bias PDH
- Inside Bar → Previous session direction bias
- Outside Bar (closes inside) → No bias

## Communication Preferences

### When Providing Code
- Always use 4-space indentation
- Include drawing object limit considerations
- Add array bounds checking where needed
- Explain complex algorithms in comments
- Reference our existing type definitions (SwingPoint, FVG, CISD)

### When Discussing Features
- Connect to TTrades methodology and our reference implementations
- Consider multi-timeframe implications
- Discuss statistical validation approaches
- Reference our organized documentation structure

### Context Assumptions
- Assume familiarity with our complete reference system
- No need to re-explain ICT concepts, order blocks, or swing points
- Focus on implementation details and integration strategies
- Reference existing documentation rather than recreating explanations

## Knowledge Base Integration
All technical context, reference materials, and methodology documentation is preserved in organized README files with official TradingView links. New conversations should leverage this existing knowledge base rather than starting from scratch.

## Development Philosophy
Focus on recreating the TTrades Fractal Model with enhancements while maintaining the mechanical, statistical foundation. Prioritize reliability, performance, and comprehensive documentation for future development sessions.

## Knowledge Base Maintenance Instructions

### When Discovering New Recurring Issues
1. **Document Immediately**: Add to `DEVELOPMENT_GUIDELINES.md` with problem/solution format
2. **Update This File**: Add critical issues to the Pine Script v6 Requirements section
3. **Update Knowledge Base**: Reflect changes in `PROJECT_KNOWLEDGE_BASE.md`
4. **Version Control**: Commit changes to preserve solutions for future sessions

### When Learning New Methodology Insights  
1. **Document in Trading System Docs**: Add to methodology explanations
2. **Update Reference READMEs**: Enhance understanding in relevant indicator documentation
3. **Cross-reference**: Ensure all related files are updated consistently
4. **Preserve Context**: Maintain comprehensive documentation for context switching

### Knowledge Base File Hierarchy
- `.github/copilot-instructions.md` ← Primary instructions (this file)
- `PROJECT_KNOWLEDGE_BASE.md` ← Quick reference for new conversations
- `DEVELOPMENT_GUIDELINES.md` ← Technical best practices and recurring solutions
- `TRADING_SYSTEM_DOCS.md` ← Complete methodology documentation
- `Reference_Indicators/*/README.md` ← Specific implementation guidance

**Critical**: Always update multiple files when discovering new insights to ensure knowledge persistence across all future development sessions.