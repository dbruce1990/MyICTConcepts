## 🎯 TTrades Methodology Reference

### Core Foundation
> "My fractal model relies on the foundational understanding that the market cannot reverse without a swing point"

### C2 Detection (HTF Closure Logic)
> "What do I use to determine if the market is likely to reverse I will use candle closures so you can see here price has swept out its previous candle high and then closed back inside the range"

**Implementation**: C2 detection is based exactly on TTrades Daily Bias methodology (Next Candle Model) - inspired by "The Strat" by Rob Smith.

### CISD Logic
> "Do we have a closure through the series of up closed candles that have made this high? Yes, so I consider this High protected"

**Key Understanding**: CISD confirms/validates an order block. Order blocks provide "protected swings" for stop loss placement. Price should NOT return before reaching target.

### Timeframe Pairing System
**Flexible Pairing Structure**:
- Monthly → Daily
- Weekly → 4hr 
- Daily → 1hr
- 4hr → 15m
- 1hr → 5m
- 30m → 3m
- 15m → 1m
- 5m → 15sec

**Chart Compatibility**: System warns when chart timeframe > LTF setting

### C2/C3/C4 Label States
- **Gray**: "Setup has remained valid throughout candle 4"
- **Red**: "Setup fails within the first candle"
- **Orange**: "Setup fails but not the first candle after but the second candle after"

### Visual Components
- **T-Spot**: Gray/green boxes for HTF wick anticipation
- **Formation Liquidity**: Dotted lines marking previous candle highs/lows
- **Projections**: Default [-1, -2, -2.5, -4, -4.5] from CISD bodies
- **Info Table**: Timeframe pairing, countdown timer, bias status

---

## CORRECTED MVP Requirements Analysis

### Core Foundation (Must Have)
1. **HTF Candle Visualization & Period Detection**
   - **Flexible Timeframe Pairing**: Daily→Hourly, Hourly→5min, 1min→15min (not rigid hierarchy)
   - **Period Boundaries**: Vertical lines separating HTF periods 
   - **HTF OHLC Tracking**: Complete OHLC data for each HTF period
   - **Countdown Timer**: Time until next HTF candle close
   - **Chart Compatibility Warnings**: Alert when chart TF > LTF setting

2. **TTrades Daily Bias Integration** 
   - **Mechanical Bias System**: PCH/PCL methodology from open-source Daily Bias indicator
   - **Bias Assignment**: Close above PDH→bias PDH, Close below PDL→bias PDL, etc.
   - **Statistical Foundation**: Success rate tracking and validation
   - **Multi-timeframe Application**: Same logic across all HTF periods

3. **C2/C3/C4 Detection System**
   - **C2**: HTF candle closure beyond previous extreme + reversal back inside
   - **C3**: Anticipated swing completion in opposite direction  
   - **C4**: Continuation or consolidation phase
   - **Label States**: Gray (valid) → Red (failed in first candle) → Orange (failed in second candle)
   - **HTF Context Only**: All detection within current HTF periods

4. **Change in State of Delivery (CISD)**
   - **Delivery Candle Series**: Candles that created the significant high/low
   - **Opening Price Violation**: Close through opening prices of delivery series (NOT swing opening)
   - **HTF Context Integration**: CISD must align with HTF bias direction
   - **Directional Color Coding**: Bullish vs bearish CISD visualization
   - **LTF Confirmation**: Used to confirm HTF bias predictions

### Essential Features (MVP)
5. **T-Spot Implementation**
   - **Wick Formation Areas**: Gray/green boxes where HTF wicks are anticipated
   - **HTF Candle Context**: Based on expected HTF candle development (OHLC pattern)
   - **Entry Zone Marking**: Key areas for LTF setup formations

6. **Projection System**
   - **Default Levels**: [-1, -2, -2.5, -4, -4.5] from CISD bodies
   - **Customizable**: User can add custom projection levels
   - **Target Areas**: Future price delivery and rebalance points

7. **Formation Liquidity**
   - **Previous Candle Levels**: Dotted lines marking previous candle highs/lows
   - **Expansion Targets**: Expected liquidity sweep points
   - **Historical Context**: Previous day/period levels for targeting

8. **Info Table**
   - **Timeframe Pairing**: Current HTF/LTF combination
   - **Asset Information**: Current symbol and timeframe
   - **HTF Timer**: Time until next HTF candle close
   - **Bias Status**: Current mechanical bias (bullish/bearish/neutral)
   - **Active Filters**: Applied time filters and settings

### Advanced Features (Post-MVP)
9. **Time Filter System**
   - **Multiple Kill Zones**: Up to 3 custom time windows
   - **Session Filtering**: Show setups only in specified time ranges
   - **Whole Hour Logic**: Filters apply to entire hour candles
   
10. **Customization & Visual Controls**
    - **History Depth**: 0-40 previous setups display control
    - **Bias Direction**: Bullish/bearish/neutral filtering
    - **Color Schemes**: Customizable visual appearance
    - **Alert System**: Comprehensive notification framework

---

## Technical Architecture - CORRECTED

### Foundation Systems
1. **TTrades Daily Bias Core**: 
   - Complete integration of open-source Daily Bias indicator logic
   - Mechanical PCH/PCL bias assignment algorithm
   - Multi-timeframe bias calculation (Daily, Weekly, etc.)
   - Statistical success rate tracking

2. **Flexible Timeframe Management**:
   - **NOT Rigid Hierarchy**: System supports various pairings (Daily→Hourly, Hourly→5min, 1min→15min)
   - **Automatic Pairing**: Chart timeframe determines recommended HTF pairing
   - **Manual Override**: User can specify custom timeframe combinations
   - **Validation System**: Warns when chart TF is incompatible with LTF setting

3. **HTF Period Detection**:
   - **Period Boundaries**: Vertical separators marking HTF candle opens/closes
   - **OHLC Tracking**: Complete HTF candle data collection and management
   - **Current Focus**: Only concerned with recent HTF periods (not 50+ candles back)

### Core Detection Algorithms

#### 1. C2 Pattern Recognition
- **HTF Closure Logic**: Candle closes beyond previous extreme (high/low)
- **Reversal Confirmation**: Price closes back inside previous range
- **Bias Integration**: Must align with TTrades Daily Bias direction
- **Label Placement**: Gray label on valid C2 formation

#### 2. CISD Detection & Visualization
- **Delivery Series Identification**: Candles that created the swept high/low
- **Opening Price Tracking**: Mark opening prices of delivery candle series
- **Violation Detection**: Close through delivery opening prices (opposite direction)
- **Visual Rendering**: Lines from delivery candles to trigger points

#### 3. T-Spot Calculation
- **HTF Context**: Based on expected HTF candle OHLC development
- **Wick Anticipation**: Areas where HTF wicks likely to form
- **Box Visualization**: Gray/green boxes marking anticipated zones

## 🔧 Implementation Requirements

### Phase 1: TTrades Daily Bias Integration
**Core Engine**: Complete integration of open-source TTrades Daily Bias indicator
- **Reference**: https://www.tradingview.com/script/xdwgV3Fx-TTrades-Daily-Bias-TFO/
- **Mechanical Logic**: PCH/PCL methodology 
- **Bias Assignment**: Close above PDH→bias PDH, Close below PDL→bias PDL, etc.
- **Multi-timeframe**: Same logic applies across all HTF periods

### Phase 2: HTF Framework
**Flexible Timeframe Management**:
- Auto-pairing based on chart timeframe
- Manual override with validation warnings
- Period boundary detection and visualization
- OHLC tracking for each HTF period

### Phase 3: Pattern Detection
**C2 Detection**: Using Daily Bias logic within HTF periods
**CISD Implementation**: 
- Track delivery candle series (candles that created high/low)
- Mark opening prices of delivery series
- Detect violation (close through opening prices)
- Finite line visualization from delivery to trigger

### Phase 4: Visual System
**Components**:
- T-spot boxes for HTF wick anticipation
- Formation liquidity dotted lines  
- Projection lines from CISD bodies
- C2/C3/C4 labels with state progression
- Info table with pairing/bias/countdown

---

## 🎯 Quick Reference

### "How do I implement timeframe pairing?"
- Use flexible pairing structure (not rigid hierarchy)
- Chart TF must be ≤ LTF setting
- Warn when incompatible combination selected

### "How do I detect C2?"
- Use TTrades Daily Bias methodology exactly
- HTF candle closure beyond previous extreme + reversal
- Must occur within HTF periods only

### "How do I implement CISD?"
- Identify delivery candle series that created high/low
- Track opening prices of delivery series (NOT swing opening)
- Detect close through opening prices in opposite direction
- Draw finite lines from delivery to trigger points

### "What are the label states?"
- Gray: Valid setup throughout C4
- Red: Failed in first candle after C2
- Orange: Failed in second candle after C2

---

## Implementation Phases - UPDATED

### Phase 1: Foundation & Bias System ✅ PRIORITY
**Deliverable**: HTF framework with TTrades Daily Bias integration

**Components**:
- [ ] **TTrades Daily Bias Integration**: Complete mechanical bias system
- [ ] **Flexible Timeframe Pairing**: Daily→Hourly, Hourly→5min, 1min→15min support
- [ ] **HTF Period Detection**: Proper period boundaries and OHLC tracking  
- [ ] **Chart Compatibility**: Warning system for incompatible timeframes
- [ ] **Info Table Framework**: Basic table with timeframe pairing and bias status

**Success Criteria**: 
- TTrades Daily Bias logic correctly implemented
- HTF periods detect properly across different timeframe pairings
- Info table shows correct pairing and bias information
- Warning system works for incompatible chart timeframes

### Phase 2: C2 Detection & CISD Foundation 
**Deliverable**: Core pattern recognition with basic labeling

**Components**:
- [ ] **C2 Pattern Detection**: HTF closure beyond previous extreme + reversal
- [ ] **CISD Foundation**: Delivery candle series identification and opening price tracking
- [ ] **Basic Label System**: Gray labels for valid C2 setups
- [ ] **HTF Context Integration**: Ensure all detection within HTF periods
- [ ] **Bias Filtering**: Only show setups aligned with mechanical bias

**Success Criteria**:
- C2 labels appear on valid setups matching video examples
- CISD levels are properly identified and tracked
- Setup detection only occurs within appropriate HTF context
- Bias filtering works correctly

### Phase 3: Complete Label States & CISD Triggers
**Deliverable**: Full C2/C3/C4 system with CISD visualization

**Components**:
- [ ] **C3/C4 Progression**: Anticipation logic and continuation detection
- [ ] **Label State Updates**: Gray→Red→Orange progression based on failure timing
- [ ] **CISD Trigger Detection**: Opening price violation with proper visualization
- [ ] **T-Spot Implementation**: HTF wick anticipation boxes
- [ ] **Formation Liquidity**: Previous candle high/low targeting

**Success Criteria**:
- All three label states function correctly
- CISD triggers display as finite lines (not extending)
- T-spot boxes appear in correct locations
- System behavior matches TTFM video examples

### Phase 4: Advanced Features & Polish
**Deliverable**: Production-ready baseline with full customization

**Components**:
- [ ] **Projection System**: Default and custom projection levels
- [ ] **Time Filters**: Up to 3 custom kill zones
- [ ] **Visual Customization**: Colors, sizes, display options
- [ ] **Alert System**: Comprehensive notification framework
- [ ] **Performance Optimization**: Sub-3 second loading

---

## Key Corrections Made

### ❌ **Previous Errors**:
- Rigid timeframe hierarchy (Weekly→4hr→15m→1m)
- Wrong timeframe pairings (4hr doesn't pair with daily)  
- Misunderstanding of CISD (swing opening vs delivery opening prices)
- Missing TTrades Daily Bias integration
- Incorrect focus (historical vs current price action)

### ✅ **Corrected Understanding**:
- **Flexible Pairing**: Daily→Hourly, Hourly→5min, 1min→15min (based on video evidence)
- **TTrades Daily Bias Foundation**: Complete mechanical bias system integration
- **CISD Clarity**: Opening prices of delivery candle series, not swing opening prices
- **Current Focus**: Model designed around NOW, not historical analysis
- **Fractal Nature**: Same model applies across all timeframes with appropriate pairings

---

*This design document reflects the corrected understanding based on TTrades video analysis and official TTFM documentation. Ready for proper implementation.*
   - Timer/countdown system

2. **C2/C3/C4 Detection System**
   - Gray labels: Valid setups (stable conditions)
   - Red labels: Failed setups (returned to initial levels)
   - Orange labels: Consolidation (didn't fail within next HTF candle)

3. **Change in State of Delivery (CISD)**
   - Series of candles making significant highs/lows
   - Opening price violation detection
   - HTF context integration
   - Bullish/Bearish directional control

4. **Timeframe Pairing System**
   - Automatic HTF/LTF pairing based on chart timeframe
   - Manual override options
   - Validation and warning system

### Essential Features (MVP)
5. **Bias Detection & Control**
   - Bullish, bearish, or neutral bias selection
   - Next Candle Model integration
   - HTF bias context for LTF signals

6. **Basic Visual System**
   - Color-coded labels for setup states
   - Horizontal rays for liquidity levels
   - Clean, professional appearance

7. **Info Table**
   - Current timeframe pairing display
   - Countdown timer
   - Bias status indicator

### Advanced Features (Post-MVP)
8. **Liquidity Systems**
   - Candle 1 liquidity sweep visualization
   - Formation liquidity (previous candle highs/lows)
   - Engineered liquidity pool identification

9. **Equilibrium & Projections**
   - 50% levels of HTF ranges
   - T-Spot identification (wick formation points)
   - Projection targets [-1, -2, -2.5, -4, -4.5]

10. **Customization & Performance**
    - Custom history depth (0-40 setups)
    - Time filters (up to 3 custom windows)
    - Timezone support
    - Alert system

---

## Technical Architecture

### Data Structures
```pine
// HTF Candle tracking
type HTFCandle
    float o, h, l, c
    int startBar, endBar
    bool isComplete
    string bias

// Fractal Model setup
type FractalSetup
    string type        // "C2", "C3", "C4"
    string status      // "gray", "red", "orange"
    int labelBar
    float labelPrice
    string direction   // "bullish", "bearish"
    HTFCandle htfContext

// CISD detection
type CISDLevel
    float price
    int startBar, endBar
    string direction
    bool triggered
```

### Core Systems Architecture

#### 1. HTF Period Detection
- Based on ICT HTF Candles reference implementation
- Period separator visualization
- OHLC tracking across HTF periods
- Timer system for performance optimization

#### 2. Fractal Pattern Recognition
- C2: HTF candle close beyond previous extreme, then reversal
- C3: Anticipated swing completion in opposite direction
- C4: Extended consolidation or failure patterns
- Dynamic status updates based on price action

#### 3. CISD Integration
- Delivery candle series identification
- Opening price violation tracking
- HTF context filtering
- Directional bias alignment

#### 4. Visual Management
- Drawing object pooling and cleanup
- Dynamic color coding system
- Label positioning and management
- Performance optimization

---

## Implementation Phases

### Phase 1: Foundation (Week 1)
**Deliverable**: Basic HTF candle visualization with period boundaries

**Components**:
- [ ] HTF period detection and tracking
- [ ] Basic HTF candle rendering
- [ ] Period separator lines
- [ ] Timer system integration
- [ ] Info table framework

**Success Criteria**: 
- HTF periods display correctly
- Period boundaries are stable and non-repainting
- Basic info table shows timeframe pairing

### Phase 2: Core Detection (Week 2)  
**Deliverable**: C2/C3 detection with basic labeling

**Components**:
- [ ] Next Candle Model bias calculation
- [ ] C2 pattern detection within HTF periods
- [ ] C3 anticipation logic
- [ ] Basic label system (gray/red states)
- [ ] CISD foundation (opening price tracking)

**Success Criteria**:
- C2 labels appear on valid setups
- Labels update to red when setups fail
- Basic CISD levels are tracked

### Phase 3: Advanced States (Week 3)
**Deliverable**: Complete C2/C3/C4 system with all label states

**Components**:
- [ ] C4 consolidation detection
- [ ] Orange label state (slowdown/consolidation)
- [ ] CISD trigger detection and visualization
- [ ] Liquidity sweep basic implementation
- [ ] Enhanced info table with bias status

**Success Criteria**:
- All three label states work correctly
- CISD triggers display properly
- System matches TTFM visual behavior

### Phase 4: Polish & Enhancement (Week 4)
**Deliverable**: Production-ready baseline matching TTFM functionality

**Components**:
- [ ] Performance optimization
- [ ] Alert system implementation  
- [ ] Custom timeframe pairing
- [ ] Time filter integration
- [ ] Visual customization options

**Success Criteria**:
- Indicator performs well on all timeframes
- Visual appearance matches TTFM quality
- Ready for custom enhancements

---

## Success Metrics

### Technical Goals
- **Performance**: Sub-3 second loading (matching TTFM improvements)
- **Stability**: Non-repainting labels and levels
- **Accuracy**: C2/C3 detection matches observable TTFM behavior
- **Reliability**: No runtime errors or memory issues

### Visual Goals
- **Professional Appearance**: Clean, commercial-quality visualization
- **Clear Information**: Intuitive label system and info table
- **Customizable**: User control over visual preferences
- **Responsive**: Smooth updates and transitions

### Functional Goals
- **Complete TTFM Recreation**: All core features implemented
- **Enhanced Foundation**: Ready for custom swing points and FVG integration
- **Extensible Architecture**: Easy to add future enhancements
- **Open Source**: Fully documented and maintainable

---

## Risk Mitigation

### Technical Risks
- **Reverse Engineering Complexity**: Mitigate with systematic observation and testing
- **Performance Issues**: Address with timer systems and object pooling
- **Pine Script Limitations**: Work within v6 constraints, document workarounds

### Implementation Risks  
- **Feature Creep**: Stick to MVP requirements, document future enhancements
- **Time Management**: Phase-based approach with clear deliverables
- **Quality Standards**: Regular testing and validation against TTFM behavior

---

## Next Steps

1. **Environment Setup**: Create project structure and initial Pine Script file
2. **Reference Integration**: Import HTF visualization from ICT HTF Candles
3. **Phase 1 Implementation**: Start with HTF period detection
4. **Iterative Development**: Build, test, validate each component
5. **Documentation**: Maintain comprehensive notes throughout development

---

*This design document will be updated as we learn more about TTFM behavior and refine our implementation approach.*
