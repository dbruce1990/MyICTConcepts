# ICT Concepts Indicator

A Pine Script v6 indicator implementing various ICT (Inner Circle Trader) concepts for market structure analysis on TradingView.

## 🎯 Current Features (Working & Stable)

### ✅ Swing Point Detection & Tracking
- **3-bar pivot detection** for swing highs and lows
- **State tracking**: Active → Swept → Closed-Through
- **Visual differentiation**: Line styles (solid, dashed, dotted) and colors
- **Performance optimized**: Array capping to prevent overflow
- **Configurable display limits**: Max swept/closed swings shown

### ✅ Fair Value Gaps (FVG)
- **BISI** (Bullish Imbalance, Sell-side Inefficiency) detection
- **SIBI** (Sell-side Imbalance, Buy-side Inefficiency) detection
- **Mitigation tracking**: Partial and full gap fills
- **Dynamic sizing**: Option to shrink boxes as gaps get filled
- **Auto-cleanup**: Remove fully mitigated FVGs

### ✅ Color Scheme & Visual Design
- **Black swing lines**: No conflict with other PD arrays
- **Blue FVG boxes**: Distinct from CISD/Order Block indicators
- **Professional appearance**: Clean, minimal color palette

## 🎛️ Settings & Configuration

### Swing Point Settings
- Show/hide different swing states
- Customize colors for each state
- Adjust line styles (solid, dashed, dotted)
- Control memory usage (max swing points stored)
- Set display window (bars to show)

### FVG Settings
- Toggle FVG display
- Adjust to remaining imbalance option
- Remove balanced FVGs option
- Customize FVG color

## 🔧 Technical Implementation

### Performance Optimizations
- **Bulletproof array capping**: Prevents memory overflow
- **Lookback window limiting**: Only processes recent bars
- **Efficient rendering**: Only draws what's needed
- **Memory management**: Automatic cleanup of old objects

### Pine Script v6 Compliance
- Uses proper Pine Script v6 syntax
- Type-safe implementations
- Follows Pine Script best practices

## 🚧 Planned Features (Roadmap)

### 🎯 Priority 1: CISD (Change in State of Delivery)
- **High Priority**: Most important PD array for trading strategy
- **Definition**: Candle(s) that sweep liquidity + close through opening price of sweep candles
- **Logic**: 
  - **Bearish CISD**: Upclose candles sweep swing high → downclose closes below lowest opening price
  - **Bullish CISD**: Downclose candles sweep swing low → upclose closes above highest opening price
- **Components**: CISD level (horizontal line) + Order Block (sweep candle series)
- **Status**: 🚧 Ready to implement core detection

### 🎯 Future CISD Enhancements
- **Secondary Order Blocks**: During distribution/retracement phases
- **Directional Filtering**: User preference for bullish/bearish only
- **Bias Integration**: Daily/session bias for auto-filtering
- **Consolidation Detection**: Distinguish true OBs from false signals

### 🎯 Future Considerations
- Order Blocks detection
- Liquidity voids
- Market structure breaks
- Session-based analysis

## 🛠️ Development Notes

### Issues Overcome
1. **Syntax Errors**: Fixed Pine Script v6 compatibility issues
   - Removed invalid `return` statements in procedures
   - Fixed variable scope issues in `renderSwings` function
   - Resolved color naming conflicts

2. **Array Management**: Implemented robust array overflow prevention
   - Bulletproof capping mechanism
   - Proper memory cleanup
   - Performance optimization

3. **Color Conflicts**: Resolved visual clashing
   - Separated swing lines (black) from other PD arrays (blue)
   - Maintained visual hierarchy

### Code Architecture
- **Modular design**: Separate sections for different features
- **Type-safe**: Uses custom types for swing points and FVGs
- **Extensible**: Easy to add new PD array types

## 🔄 Development Workflow

### Version Control Strategy
- **Main branch**: Stable, working features only
- **Feature branches**: For new implementations (especially CISD)
- **Backup before major changes**: Always commit working state

### Testing Protocol
- Test on multiple timeframes
- Verify performance with large datasets
- Validate against known market structure

## 📖 Context for Future Development

### Key Technical Decisions
1. **3-bar pivot detection**: Simple but effective swing identification
2. **State-based tracking**: Active → Swept → Closed pattern
3. **Memory management**: Proactive array capping vs reactive cleanup
4. **Visual differentiation**: Line styles > color variety

### CISD Implementation Challenges
- **Sweep Detection**: Must detect when price touches/wicks swing levels (stop loss trigger)
- **Series Identification**: Track consecutive same-direction candles using open/close relationship
- **Order Block Storage**: Store entire sweep candle series for future features
- **Performance**: Maintain efficiency while tracking complex relationships
- **Visual Integration**: Blue horizontal lines for CISD levels (matching existing theme)

### CISD Technical Specification
**Core Logic Flow:**
1. **Monitor Swept Swings**: Use existing swing state tracking
2. **Identify Sweep Series**: Group consecutive candles in sweep direction
3. **Calculate CISD Level**: Extreme opening price of sweep series
4. **Detect Trigger**: Opposite direction close through CISD level
5. **Create Order Block**: Store sweep series + CISD level + visual line

**Data Requirements:**
- Reference to swept swing point
- Start/end bars of sweep series
- CISD level (opening price)
- Trigger confirmation
- Visual line object

### For New AI Conversations
When working on this indicator:
1. **Always read this README first** for current context
2. **Review existing code structure** before making changes
3. **Test thoroughly** before committing changes
4. **Update this README** when adding features
5. **Backup working state** before major implementations

## 🎨 Visual Theme
- **Swing Lines**: Black (solid=active, dashed=swept, dotted=closed)
- **FVG Boxes**: Blue with 80% transparency
- **Reserved Colors**: Blue lines reserved for CISD/Order Blocks

## 📝 Current Script State
- **File**: `script.txt`
- **Version**: Pine Script v6
- **Status**: ✅ Stable and functional
- **Last Major Update**: Swing point rendering fixes + FVG cleanup
- **Current Task**: 🚧 Implementing core CISD detection
- **Next Steps**: 
  1. Add CISD type definition
  2. Implement sweep detection logic
  3. Add CISD level calculation
  4. Create visual rendering
  5. Test and validate

---
*This indicator is a work in progress. Current features are stable and tested. Future features will be implemented incrementally with proper version control.*
