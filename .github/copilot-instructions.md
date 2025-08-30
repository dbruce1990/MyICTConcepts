# GitHub Copilot Repository Instructions

## Project Context
I am developing an ICT (Inner Circle Trader) concepts indicator in Pine Script v6 that recreates the commercial TTrades Fractal Model with personal enhancements. The project is based on multi-timeframe analysis using swing points, Fair Value Gaps (FVGs), and Change in State of Delivery (CISD) detection in addition to TTrades' Daily Bias (or I call it Next Candle Model) for statistical validation. The goal is to create a reliable, non-repainting indicator that integrates seamlessly with the TTrades methodology while providing a solid foundation for future enhancements. The project is structured to allow for easy reference to existing indicators and methodologies, with a focus on maintaining high code quality and comprehensive documentation. Every trade setup is based on the Next Candle Model, which is a statistical bias system with a 63-67% success rate. Once we identify a C2 (Candle 2) closure, we anticipate a C3 (Candle 3) continuation. We can also trade C4 (Candle 4) based on C3 closures as the point is to trade the next candle in a swing point formation (also known as a pivot point or williams fractal...simply a 3-candle pattern with a high/low in the middle). 

## Key Concepts & Definitions

### ICT Trading Terminology
- **Order Block**: The candle or series of candles that sweep liquidity (a swing high or low)
- **Swing Point**: A 3-candle pattern with a high/low in the middle that indicates a potential reversal point in the market
- **Protected Swing Point**: Derived from how TTrades defines OB (Order Block). It is a swing point that has swept another swing point's liquidity and formed an OB.
- **CISD (Change in State of Delivery)**: A candle closure beyond the lowest/highest opening price of thecandle or series of candles that swept liquidity. A CISD validates an order block and creates a protected swing point.
- **HTF (Higher Time Frame)**: The timeframe that provides bias and target levels for lower time frame execution. Any higher timeframe than the one we are looking at.
- **LTF (Lower Time Frame)**: Any timeframe lower than the current time frame we are discussing.
- **FVG (Fair Value Gap)**: 3-candle pattern with gap between high/low of outer candles. For example a bullish FVG is where there is no overlap between the high of the first candle and the low of the third candle. Reverse for bearish FVG.
- **Imbalance**: Represents an inefficiency in price delivery. There are different kinds of imbalances, such as FVG's and Volume Imbalances (VI's). There are also others such as New Day Opening Gaps (NDOG's) and New Week Opening Gaps (NWOG's), which are a kind of volume imbalance in my opinion. Any gap between candles is considered an imbalance.
- **BISI**: A type of FVG. BISI stands for Buyside Imbalance, Sellside Inefficiency.
- **SIBI**: A type of FVG. SIBI stands for Sellside Imbalance, Buyside Inefficiency.
- **C2 Closure**: A C2 closure is a candle that sweeps the high or low of the previous candle and closes back inside the previous candle's range. This is a critical part of the TTrades Fractal Model.
- **C3 Closure**: A specific pattern where a swing point formation (3-candle pattern) aligns with Next Candle Model logic. Occurs when: (1) A swing point forms (high[1] > high[2] AND high < high[1] for swing high, or low[1] < low[2] AND low > low[1] for swing low), AND (2) The current candle's close aligns with the swing direction (close < low[1] for bearish swing high, close > high[1] for bullish swing low). This creates a bias for C4 in the direction of the swing.
- **C4**: The fourth candle in a swing formation that can be traded based on the C3 closure. Requires C3 to close beyond C2's high/low as per the next candle model rules. 
- **Next Candle Model**: Statistical system for setting a bias for the next candle using the sweep of PCH/PCL and candle closure logic. The core logic is simple: if price takes and closes (displaces) directionaly beyond the previous candle's high or low, we expect the next candle to continue in that same direction. However, if price takes the high/low of the previous candle but fails to displace, the bias shifts for the next candle, anticipating the opposing bias to play out for the next candle and form a swing high/low. To better explain, if next candle bias is PCH, and takes it, but fails to displace above the PCH, then the next candle model dictates the bias becomes PCL, allowing us to build a narrative to anticipate price to take PCL. This is a candle-by-candle way we get to "read the story" that price action is telling us based on candle closures. A continuous bias system, helping us read and follow current order flow. **CRITICAL**: C3 closure is NOT a failure of the Next Candle Model - it's a specific alignment pattern where swing point formation coincides with Next Candle Model directional bias. **Bias Hierarchy**: When multiple patterns conflict, the priority is: Swing Points > FVG context > Basic Next Candle Model logic. Where swing points have the highest priority, then FVG context can override mechanical bias, and finally basic Next Candle Model logic applies when no other patterns are present. We only care about FVG's the first time price forms a swing point from it. So if it's a BISI (bullish fvg or more specifically a Buyside Imbalance, Sellside Inefficiency (BISI)) and price trades low into the FVG and forms a swing point out of it, that means it leaves a swing point so we can "forget" about it, because now a swing formation is present at that level, which would override the FVG. If price retraces back to the FVG later, we don't care about it anymore because a swing point is now present at that level. We only care about FVG's the first time price trades into them and forms a swing point from them. After that, we can "forget" about them because a swing point is now present at that level, which overrides the FVG. If price doesn't form a swing point, meaning it just trades through the fvg and closes beyond it, that "inverses" the FVG (iFVG - Inversion FVG) and now the FVG is bearish instead of bullish (or vice versa). This is a more advanced nuance, but the key point is that swing points have the highest priority, then FVG context, then basic Next Candle Model logic. I don't want to overcomplicate the logic, but this is a critical understanding of how the patterns interact. We won't be using iFVG's in this implementation, but it's good to understand the concept. 
- **PCH**: Previous Candle High
- **PCL**: Previous Candle Low
- **PDH**: Previous Day High
- **PDL**: Previous Day Low
- **PCH/PCL Methodology**: The statistical bias calculation system used in TTrades Daily Bias and Next Candle Model. It is a simple logic that determines the bias for the next candle based on the previous candle's high and low.
- **Time Frame Pairings**: When discussing TTrades' Fractal Model or honestly ICT concepts in general, we use a set of time frame pairings for multiple time frame analysis. Here are the time frame pairings we use (you'll often see minute time frames short-handed as m15 or 15m for 15 minutes. Most traders tend to prefix the time frame with the letter, but not critical to anything, just be consistent with your use):
    - Monthly → Daily
    - Weekly → 4hr
    - Daily → 1hr
    - 4hr → 15m
    - 1hr → 5m
    - 30m → 3m
    - 15m → 1m
    - 5m → 15sec


### Technical Architecture
- **Main Script**: `script.pine` (495 lines) with swing points, FVGs, CISD detection. We're not currently touching this file as it's broken but it does contain core logic for FVG's, Swing Points, HTF Candle support. The CISD logic is incorrect and needs fixed. We seemed to have a bug where the lines are extending infinitely instead of being finite from the delivery candle to the trigger candle and struggle to identify the proper opening price to use to validate the CISD/OB formation.
- **HTF Integration**: While I execute using 3 time frames typically (HTF, ITF, LTF), the indicator only needs to support 2 time frames for bias and structure. So I use the HTF for bias and narrative and even targets/POIs, the ITF for structure and verification of the HTF bias. You don't NEED to use the LTF for the entry function, but you can repeat the process on the LTF fractal of the intermediate time frame (ITF) to get an even more precise entry. The LTF is not required for the indicator to function, but it is useful for improved risk management and entry precision. So, if we're wanting to refine from the Monthly > Daily we can look at the Daily > 1hr to get a more precise entry. If we want to refine it further, we can look at the 1hr > 5m to get an even more precise entry. The LTF is not required, but it is useful for improved risk management and entry precision.At some point we just need to get into the trade. You can try to refine entries too much and end up lost or just missing the move cause you're waiting for perfection
- **Reference Indicators**: Organized in `Reference_Indicators/` with comprehensive READMEs. Not all have script files, some are just reference materials. The ones that do have scripts are open source and can be borrowed/inspired from in our indicator's implementation


## Pine Script v6 Requirements

### Critical Rules (ALWAYS FOLLOW)
1. **Indentation**: ALWAYS use 4 spaces (never tabs) - this prevents 90% of syntax errors
2. **Multi-line Function Calls**: NEVER mix positional and named parameters in multi-line calls - use single line with all named parameters instead. There is a bug when copying the script into the Pine Editor that causes the multi-line calls to break. Easier to just keep parameters on a single line.
3. **Drawing Limits**: Set max_boxes_count, max_lines_count, max_labels_count in indicator declaration
4. **Array Bounds**: Check array.size() before array.get() calls
5. **Barstate Handling**: Wrap logic that relies on candle closures in `barstate.isconfirmed` checks
6. **Object Cleanup**: Implement cleanup methods for drawing objects to prevent exceeding limits and improving performance.
7. **Error Handling**: Always check for common errors like "Cannot call 'array.get' with argument 'id'=na" and handle them gracefully

### Common Error Prevention
- "Cannot call 'array.get' with argument 'id'=na" → Always initialize arrays and check bounds
- "Index out of bounds" → Add if array.size() > index checks before access
- Drawing object limits → Implement cleanup methods and object pooling
- Indentation errors → Always verify 4-space indentation consistency
- "Mismatched input" in multi-line calls → Use single line with named parameters: `line.new(x1=val, y1=val, x2=val, y2=val, color=col)`

### Logic Error Prevention & Methodology Insights
- **C3 Closure Logic**: C3 closure = Swing Point Formation. Meaning when the candle closes we can check to see if the current candles high/low is greater than the previous candle's high/low and the previous candle's high/low is greater than the candle's high/low before it. This is a 3-candle pattern that indicates a swing or pivot point formation. This is a critical part of the TTrades Fractal Model and Next Candle Model logic. We are trading continuations of swing points.
- **Pattern Priority**: When multiple patterns occur on same candle, prioritize: C3 Closure > C2 Closure > Outside Bar C2
- **Bias Conflicts**: POI context overrides basic next candle model mechanical bias (e.g., a c3 closure may indicate a PCL bias from a next candle model mechanical perspective, but context of it being inside a BISI FVG with it being a reversal candle could indicate a PCH bias instead even if we don't get a c2 closure out of it! This is where the nuances lay!)
- **Pattern Detection**: Apply Next Candle Model to every candle, filter them based on context (swing points, FVG's) to refine bias. Multi-timeframe analysis after filtering the HTF (remember we're thinking top down analysis, meaning: next candle model gives us our mechanical bias, filtering based on swing points and FVG's, as well as candle types (see candle type section) helps build a narrative. The LTF adds further confirmations to our bias.
- **Swing Point Filtering**: Not all swings are tradeable - require Point of Interest (POI) context for higher probability setups which are old swing highs/lows, FVGs, or Order Blocks. We only trade swing points that occur at significant POIs. We don't trade random swings. We likely won't be implementing OB detection for POI's in this version, but it's a good concept to understand. We will be using FVG's and Swing Points for POI's.

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

## Indicator Components

### Next Phases 🎯
1. **Period Separators**: Visualize the start and end of each HTF period (e.g., Weekly, Daily). The `Period_Separator/` in `Reference_Indicators/` can be heavily borrowed from for inspiration.
2. **HTF Candle Rendering**: We can use either the logic from the root directory `script.pine` or the `ICT HTF Candles` reference implementation to render HTF candles. This will provide the foundation for our HTF bias and target levels. We can essentially run HTF swing point, FVG, and next candle model detection with it and then apply the same logic across multiple timeframes.
3. **C2/C3/C4 Detection**: Within HTF periods with progression tracking
4. **Next Candle Model**: Statistical bias calculation across timeframes
5. **Setup Filtering**: Later implementation after HTF foundation is solid

### Implementation Priorities (UPDATED)
1. **Period Separators** - Critical foundation for HTF detection
2. **HTF Integration** - Using ICT HTF Candles reference implementation  
3. **C2 Detection** - Within HTF context, not standalone
4. **Statistical Layer** - Next Candle Model implementation
5. **Filtering System** - Save for later, after core functionality is complete

### Implementation Insights
- **Multi-timeframe Hierarchy (My Preferred TFs)**: Weekly→4hr→15m→1m. Find weekly bias. Wait for 4hr swings in the direction of weekly bias. Drop to m15 to confirm 4hr swing formations in direction of weekly bias. Fine-tune entry with 1m if desired (not a requirement). 
- **HTF Integration**: Higher timeframe provides bias/targets, lower timeframe provides execution signals
- **Statistical Foundation**: TTrades Daily Bias provides mechanical bias calculation (PCH/PCL methodology)
- **Label Progression**: Gray (valid) → Red (failed) → Orange (consolidation) from TTrades Fractal Model

## TTrades Methodology Foundation

### The Fractal Model Logic (Core Framework)
**Philosophy**: "Price moves between liquidity pools (internal and external liquidity). Price cannot reverse without forming a swing point. Expansion occurs when time frames align."

**Framework Components**:
1. **HTF Bias Detection**: Daily/4hr directional bias (C3/C4 continuation days ideal), though the model can be applied to all timeframe pairings.
2. **Point of Interest Requirement**: High/Low > FVG > 0.5 Order Block (we don't trade random swings)
3. **C2 Detection**: Sweep + close back inside the previous candle at a POI (high/low, FVG, OB)
4. **C2 Validation**: Must form an IC-CISD to be tradeable (long wicks are preferred but not required)
5. **Trade within C3**: If no OB formed in C2, wait for C3 to validate the OB before trading.
6. **Fallback C4**: Once C3 closure is confirmed, we can trade the continuation of C4 if targets aren't met.
7. **T-Spot**: HTF wick anticipation areas (optimization nuance exists). T-Spot is the opening price of the current HTF candle period, to 50% of the previous HTF candle. If previous candle is a reversal candle with a long wick, we want 50% of the wick to be respected. Ideally it doesn't test it, but we don't want candle closures beyond 50% of the HTF candle or wick (if using). 

**Key Insight**: We only trade swing formations that occur at significant Points of Interest with CISD validation - not every swing point qualifies.

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

**Required Elements**:
- **Sweep**: C2 must take the high/low of C1
- **Close Inside**: C2 must close within C1's range
- **Point of Interest**: Must occur at High/Low > FVG > 0.5 Order Block
- **Long Wick Preferred**: Improves probability but not required

**Critical Understanding**: C2 is not separate from Next Candle Model - it's the visual manifestation of bias prediction. When C2 forms, we anticipate C3 (swing completion) in direction opposite to the sweep.

### CISD (Change in State of Delivery)
**CORRECT Definition**: CISD (Change in State of Delivery) occurs when a series of candles sweep liquidity (take out a prior swing high or low), and then price reverses and an opposing candle closes beyond the opening price of the first candle in the series that performed the sweep. This validates the order block and creates a protected swing point.

**Implementation**:
- **Delivery Candles**: The candle(s) that created the high/low (swept the liquidity)
- **Opening Price Level**: Mark opening price of the first candle in the series that swept liquidity. For bearish CISD, this is the opening price of the first bullish candle in the series that swept the prior swing low. For bullish CISD, this is the opening price of the first bearish candle in the series that swept the prior swing high.
- **CISD Trigger**: When price closes through this opening price in opposite direction
- **IC-CISD**: Same concept but within current HTF fractal candle period only
- **Line Drawing**: FINITE lines from delivery candle opening price to trigger candle (NOT extending)

**Critical Note**: CISD is about the opening price of the candle that DID THE SWEEPING - not the swing point's opening price.

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