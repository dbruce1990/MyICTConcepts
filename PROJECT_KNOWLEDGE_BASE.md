# Project Knowledge Base - Quick Reference

## 🎯 Project Goal
Recreate the commercial TTrades Fractal Model indicator in Pine Script v6 with personal enhancements, focusing on multi-timeframe CISD detection and C2 closure identification.

## 📁 Project Structure
```
ictconcepts_cursor/
├── script.pine                          # Main indicator (495 lines, functional)
├── COPILOT_CUSTOM_INSTRUCTIONS.md       # GitHub Copilot persistent instructions
├── DEVELOPMENT_GUIDELINES.md            # Technical best practices & bug prevention
├── TRADING_SYSTEM_DOCS.md              # Complete methodology documentation  
└── Reference_Indicators/
    ├── TTrades_Daily_Bias/
    │   ├── script.pine                  # Mechanical bias calculation (open source)
    │   └── README.md                    # Analysis with TradingView link
    ├── Period_Separator/
    │   ├── script.pine                  # HTF visualization framework
    │   └── README.md                    # Period boundary implementation
    └── TTrades_Fractal_Model/
        ├── ICT_HTF_Candles.pine         # HTF period detection system (open source)
        ├── ICT_HTF_Candles_README.md    # Technical analysis & integration guide
        └── README.md                    # Target system analysis (commercial)
```

## 🔗 Official Reference Links
- **TTrades Fractal Model**: https://www.tradingview.com/script/XdwK9qQQ-Fractal-Model-Pro-TTrades/
- **TTrades Daily Bias**: https://www.tradingview.com/script/xdwgV3Fx-TTrades-Daily-Bias-TFO/
- **ICT HTF Candles**: https://www.tradingview.com/script/0KTDWTdN-ICT-HTF-Candles-Source-Code-fadi/

## 🧠 Core Concepts (No Re-explanation Needed)
- **CISD = Order Block = Protected Swing Point** (same concept, different names)
- **C2 Closure**: HTF candle close triggering expansion in TTrades methodology
- **Next Candle Model**: 63-67% success rate bias system (PCH/PCL statistics)
- **Multi-timeframe Hierarchy**: Weekly→4hr→15m→1m with bias inheritance
- **Label Progression**: Gray (valid) → Red (failed) → Orange (consolidation)

## ⚡ Technical Standards
- **Pine Script v6**: 4-space indentation (NEVER tabs)
- **Drawing Limits**: Always set max counts and implement cleanup
- **Array Safety**: Bounds checking before array.get() calls
- **Time Coordinates**: xloc.bar_time for persistence
- **Documentation**: Comprehensive READMEs with official links

## 🚀 Development Status
- ✅ **Core Foundation**: Swing points, FVGs, CISD detection functional
- ✅ **Reference System**: Complete documentation with TradingView links
- ✅ **Development Framework**: Guidelines and custom instructions established
- 🚧 **HTF Integration**: Next phase using ICT HTF Candles methodology
- 🎯 **Target**: Automated C2/C3/C4 detection with TTrades Fractal Model features

## 💡 Key Implementation Insights
1. **HTF Period Detection**: Use `time()` function from ICT HTF Candles for accurate boundaries
2. **Bias Calculation**: Extract mechanical rules from TTrades Daily Bias for C2 detection
3. **Statistical Foundation**: Built-in success rate tracking validates methodology
4. **Non-repainting**: Stable levels within time periods ensure reliability
5. **Universal Application**: System adapts to any asset/market/timeframe

This knowledge base ensures new conversations can start with full context without re-explaining fundamentals.
