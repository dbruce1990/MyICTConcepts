# MyTTFM - Higher Timeframe Trading Foundation

## Project Overview

MyTTFM is a progressive implementation of the TTrades Fractal Model, starting with a solid HTF (Higher Timeframe) candle rendering foundation based on Fadi's HTF Candles indicator. This project takes a modular approach, building features incrementally to ensure stability and maintainability.

## Phase 1: HTF Candle Foundation ✅ COMPLETE

### Implemented Features

**Core HTF System:**
- HTF period detection using `request.security`
- Real-time HTF OHLC data access and tracking
- Automatic timeframe pairing (1m→5m, 15m→4H, etc.)
- Manual timeframe selection override
- HTF candle creation, updating, and cleanup

**Visual Rendering:**
- HTF candle bodies with customizable colors
- Upper and lower wicks with proper positioning
- Configurable candle width, spacing, and offset
- HTF timeframe labels and time remaining display
- Clean visual separation from chart candles

**Data Management:**
- Type-safe HTF candle data structures
- Array-based candle set management with bounds checking
- Memory management with automatic cleanup
- Drawing object limits compliance
- Pine Script v6 best practices

**Information Display:**
- Info table showing current HTF OHLC data
- Chart TF vs HTF TF comparison
- HTF candle count tracking
- Real-time time remaining in HTF period

## Technical Architecture

### Type Definitions

```pine
type HTFCandle
    float o, h, l, c        // OHLC prices
    int openTime, openIdx   // Timing data
    int closeIdx, highIdx, lowIdx  // Bar indices
    bool isComplete         // Completion status
    box candleBody          // Visual components
    line wickUp, wickDown

type HTFCandleSet
    array<HTFCandle> candles  // Candle collection
    string timeframe          // HTF timeframe
    int maxDisplay           // Display limit
    label tfLabel, timerLabel // Labels
```

### Key Functions

- `getAutoHTFTimeframe()` - Automatic TF pairing logic
- `getFractalTimeframe()` - Manual/auto TF selection
- `getRemainingTime()` - HTF period countdown
- `safeArrayGet()` - Bounds-safe array access

## Usage Instructions

1. **Add to TradingView:** Copy `MyTTFM.pine` to Pine Editor
2. **Configure Timeframes:** Use "Automatic" for standard pairings or select manually
3. **Customize Display:** Adjust candle colors, sizing, and positioning
4. **Monitor HTF Data:** Use info table to track HTF OHLC values

## Phase 2: TTFMCopilot Integration (Next Steps)

### Planned Features

**Swing Point Detection:**
- 3-bar pivot detection within HTF context
- Swing point state tracking (active, swept, closed-through)
- Visual swing point rendering with customizable colors

**Next Candle Model:**
- TTrades Daily Bias calculation logic
- PCH/PCL methodology implementation
- Statistical success rate tracking
- Real-time bias display and color coding

**Pattern Recognition:**
- C2 closure detection (sweep + close inside)
- C3 closure identification (swing formation)
- C4 continuation pattern tracking
- Pattern progression visualization (Gray→Red→Orange)

**Advanced Systems:**
- CISD (Change in State of Delivery) detection
- T-Spot system for HTF wick anticipation
- Period separators for HTF visualization
- Formation liquidity tracking

## Development Approach

### Incremental Implementation
1. **Phase 1:** HTF Foundation ✅
2. **Phase 2A:** Swing Point Detection
3. **Phase 2B:** Next Candle Model
4. **Phase 2C:** C2/C3/C4 Patterns
5. **Phase 3:** Advanced Features (CISD, T-Spot)

### Code Quality Standards
- Pine Script v6 compliance
- 4-space indentation consistently
- Named parameters for all function calls
- Comprehensive error handling
- Memory management with cleanup
- Type-safe data structures

## Reference Materials

This project builds upon:
- **Fadi HTF Candles:** Core HTF rendering system
- **TTFMCopilot:** Pattern detection and bias calculation
- **TTrades Daily Bias:** Statistical foundation
- **TTrades Fractal Model:** Target commercial system

## File Structure

```
MyTTFM/
├── MyTTFM.pine          # Main indicator file
├── README.md            # This documentation
└── phases/              # Future phase implementations
    ├── phase2a_swings/
    ├── phase2b_bias/
    └── phase2c_patterns/
```

## Contributing

When adding new features:
1. Maintain the modular structure
2. Follow Pine Script v6 best practices
3. Add comprehensive documentation
4. Test thoroughly before integration
5. Update this README with new features

## Status

- ✅ **Phase 1:** HTF Foundation - COMPLETE
- 🚧 **Phase 2A:** Swing Points - READY TO START
- ⏳ **Phase 2B:** Next Candle Model - PENDING
- ⏳ **Phase 2C:** C2/C3/C4 Patterns - PENDING

---

*This project implements the open-source recreation of TTrades Fractal Model concepts while maintaining clean, maintainable code structure for long-term development.*
