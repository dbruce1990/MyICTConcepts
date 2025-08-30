# Swing Point Tracker - Standalone Indicator

## Overview
A comprehensive swing point detection and visualization system designed for ICT-style trading analysis. This indicator tracks 3-bar pivot points through their complete lifecycle: formation → sweep → closure.

## Key Features

### 🎯 **Smart State Management**
- **Active Swings**: Newly formed pivots that haven't been touched
- **Swept Swings**: Pivots that have been wicked through but not closed through  
- **Closed Swings**: Pivots that have been definitively broken (close through)

### 📊 **Point of Interest (POI) Tracking**
- Automatically identifies the most recent swept swing high/low
- Shows POI age (bars since sweep) for timing analysis
- Clean, focused info table showing only what matters

### 🎨 **Professional Visualization**
- Theme-friendly default colors (works on light/dark backgrounds)
- Customizable line styles (solid/dashed/dotted)
- Optional swing labels for new formations
- Adjustable display limits for performance

## How to Use

### 1. **Basic Setup**
- Add to chart alongside price action
- Default settings work well for most timeframes
- Adjust colors to match your chart theme

### 2. **Reading the Display**
- **Blue Lines**: Active swings (untouched pivots)
- **Orange Lines**: Swept swings (current POIs) 
- **Gray Lines**: Closed swings (broken structure)

### 3. **Info Table (Top Right)**
Shows the most important information:
- **Swept High**: Current bullish POI level and age
- **Swept Low**: Current bearish POI level and age  
- **Quick Stats**: Total active and swept swing counts

### 4. **Integration with Other Indicators**
The indicator outputs data that other indicators can reference:

**Data Window Outputs:**
- `Active Swept High Level` - Exact price level
- `Active Swept Low Level` - Exact price level
- `Has Active Swept High` - Boolean (1 = yes, 0 = no)
- `Has Active Swept Low` - Boolean (-1 = yes, 0 = no)

## Settings Guide

### **Display Settings**
- **Show Active/Swept/Closed Swings**: Control visibility by state
- **Max Swept/Closed Swings**: Limit display for clean charts
- **Show Swing Labels**: Optional SH/SL labels on formation
- **Show Info Table**: Toggle the POI summary table

### **Styling Settings**  
- **Colors**: Customize for each swing state (active/swept/closed)
- **Line Styles**: Choose solid, dashed, or dotted lines
- **Table Position**: Move info table to preferred location

### **Performance Settings**
- **Max Swing Points**: Memory limit (100 default)
- **Bars to Display**: Lookback window (500 default)
- **Show Debug Info**: Extra data window information

## Trading Applications

### **ICT Methodology**
- **Order Block Analysis**: Swept swings mark potential reversal zones
- **Liquidity Mapping**: Track where stops have been taken
- **Structure Analysis**: Identify break of structure vs. sweep and reverse

### **Multi-Timeframe Analysis**
- Use on higher timeframes for bias/targets
- Use on lower timeframes for entry confirmation  
- POI age helps assess setup quality (fresher = better)

### **Pattern Recognition**
- **Failed Breakouts**: Swept swings that reverse quickly
- **Liquidity Grabs**: Multiple sweeps before reversal
- **Structure Breaks**: Closed swings confirm trend changes

## Technical Notes

### **Detection Logic**
- **3-Bar Pivots**: `high[1] > high[0] AND high[1] > high[2]` (swing high)
- **State Updates**: Real-time tracking of wick vs. close through  
- **Performance**: Automatic cleanup of old swings for efficiency

### **Data Output Format**
Perfect for building composite indicators:
```pinescript
// Example: Reference in another indicator
swept_high = request.security(syminfo.tickerid, "", "Active Swept High Level")
has_poi = request.security(syminfo.tickerid, "", "Has Active Swept High")
```

## Best Practices

### **Settings Optimization**
- **Day Trading**: Lower lookback (200-300 bars)
- **Swing Trading**: Higher lookback (500-1000 bars)
- **Scalping**: Enable swing labels for immediate feedback

### **Performance Tips**
- Reduce max swing points on slower devices
- Turn off closed swings display if not needed
- Use debug info only when troubleshooting

### **Visual Clarity**
- Keep swept swing limit low (3-5) for clean charts
- Use contrasting colors for active vs swept states
- Position info table where it doesn't block price action

## Version History
- **v1.0**: Initial release with full state management and POI tracking
- Based on battle-tested logic from C2 Statistics Tracker development

## Support
This indicator was developed as part of the MyICTConcepts project for recreating TTrades Fractal Model functionality with custom enhancements.
