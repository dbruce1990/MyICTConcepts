# Development Guidelines & Best Practices

This document captures recurring issues, solutions, and best practices to prevent wasting time on the same problems repeatedly.

## Pine Script Specific Issues

### 1. Indentation Requirements
**Problem**: Pine Script v6 has strict indentation rules that cause syntax errors
**Solution**: 
- Use **4 spaces** (not tabs) for indentation
- Nested structures must maintain consistent indentation levels
- Method definitions and if/for/while blocks require proper indentation
- Array/object access within methods needs proper spacing

**Example**:
```pinescript
// ✅ CORRECT
if condition
    for i = 0 to array.size(myArray) - 1
        element = array.get(myArray, i)
        if element.someProperty > value
            // Do something
            element.otherProperty := newValue

// ❌ INCORRECT (mixed tabs/spaces or wrong indentation)
if condition
	for i = 0 to array.size(myArray) - 1
	element = array.get(myArray, i)
		if element.someProperty > value
		element.otherProperty := newValue
```

### 2. Drawing Object Limits
**Problem**: Runtime errors from hitting max drawing objects (500 boxes, 500 lines, etc.)
**Solution**:
- Always set `max_boxes_count`, `max_lines_count`, `max_labels_count` in indicator declaration
- Implement cleanup methods to delete old objects
- Use arrays to track objects and limit array sizes
- For arrays: Use `array.size() > maxCount` checks and `array.shift()` or `array.pop()`

### 3. Time-based vs Bar-based Coordinates
**Problem**: Drawing objects disappearing or not rendering correctly
**Solution**: 
- Use `time` coordinates for persistent drawings: `xloc.bar_time`
- Use `bar_index` for temporary/current session drawings: `xloc.bar_index`
- For historical analysis, prefer time-based coordinates

### 4. Barstate Handling
**Problem**: Calculations running on every tick causing performance issues
**Solution**:
- Use `barstate.isconfirmed` for final calculations
- Use `barstate.islast` for current bar updates
- Use `barstate.isrealtime` for live trading scenarios (but note: limited execution frequency)
- Avoid heavy calculations on every tick

### 5. Real-Time Update Limitations (NEW)
**Problem**: Timers and real-time displays lag or "stick" at certain values
**Solution**: 
- Pine Script only executes when market activity occurs (ticks)
- Cannot force execution every second - limited by market data flow
- For maximum update frequency: Remove `barstate` conditions and execute every cycle
- Accept that some lag during quiet market periods is unavoidable

### 6. Drawing Coordinate System (NEW)
**Problem**: Wick centering issues with odd-width candle bodies
**Solution**:
- Use even numbers for candle widths (2, 4, 6, 8) for better centering
- For mathematical centering: `wickCenterX = leftX + math.floor(width / 2)`
- Pine Script's box coordinates work differently than expected for width calculations
- Test centering visually for each use case

### 7. Label Cleanup (NEW) 
**Problem**: Timer labels persist after candles complete, causing visual clutter
**Solution**:
- Implement comprehensive cleanup that affects ALL objects, not just current ones
- Delete and recreate labels every cycle rather than trying to update in place
- Separate timer logic from main rendering to avoid interference

## Code Organization Best Practices

### 1. Type Definitions
- Define all custom types at the top of the script
- Use clear, descriptive names
- Group related properties together
- Add comments explaining the purpose

### 2. Variable Declarations
- Use `var` for variables that should persist between bars
- Group related variables together
- Initialize arrays and objects with proper sizing
- Use meaningful variable names

### 3. Function/Method Organization
- Define helper functions before main logic
- Use methods for custom types when possible
- Keep functions focused on single responsibilities
- Add parameter validation where needed

## Performance Optimization

### 1. Array Management
- Set maximum sizes for arrays to prevent memory issues
- Use `array.clear()` instead of creating new arrays when possible
- Prefer `array.unshift()` and `array.pop()` for FIFO operations
- Cap array sizes with regular cleanup

### 2. Drawing Object Management
- Implement object pools for frequently created/destroyed objects
- Delete objects that are no longer needed
- Use conditional rendering based on user settings
- Batch drawing operations when possible

## Trading System Constraints

### 1. Timeframe Limitations (Critical for HTF Integration)
**Pine Script Constraint**: Can only request HIGHER timeframe data, not lower
- From 15m chart: Can get 4hr/daily/weekly data, but NOT 1m data
- From 4hr chart: Can get daily/weekly data, but NOT 1hr/15m data
- **Impact**: Shapes our HTF integration approach - must design around this limitation
- **Solution**: Design flexible timeframe pairing where HTF is always higher than current chart

### 2. User Trading Preferences (Design Requirements)
**Setup Preferences**: 
- Primary: Setups after swept swing points (highest priority)
- Secondary: Setups inside Fair Value Gaps
- Avoid: Random setups without key level context

**Timeframe Usage Patterns**:
- Standard hierarchy: Weekly→4hr→15m→1m
- Alternative for noisy conditions: 30m→3m
- HTF provides bias/targets, LTF provides execution signals
- Period separators are essential (not optional) for workflow

**Quality Requirements**:
- Filter out noise, focus only on high-probability setups
- Statistical validation required (like TTrades provides with 63-67% success rates)
- Mechanical approach preferred over discretionary

### 3. Drawing Object Management

## Debugging Strategies

### 1. Common Error Messages
- **"Cannot call 'array.get' with argument 'id'=na"** → Check array initialization and ensure array exists
- **"Index 'X' is out of bounds"** → Add bounds checking: `if array.size(myArray) > index`
- **"line.new() cannot be called in local scope"** → Move to global scope or use var declaration
- **"Lookahead is not allowed"** → Remove historical references in real-time calculations
- **Array bounds errors** → Always use: `if array.size(myArray) > 0 and index < array.size(myArray)`

### 2. Array Bounds Checking Pattern (CRITICAL)
```pinescript
// ✅ ALWAYS use this pattern before array access
if array.size(myArray) > 0 and index >= 0 and index < array.size(myArray)
    element = array.get(myArray, index)
    // Process element safely

// ✅ For last element access
if array.size(myArray) > 0
    lastElement = array.get(myArray, array.size(myArray) - 1)

// ❌ NEVER do direct access without checking
element = array.get(myArray, index)  // Can cause runtime errors
```

### 2. Debugging Tools
- Use `log.info()` for debugging (limit usage for performance)
- Use `plotchar()` for boolean debugging
- Use `bgcolor()` for condition highlighting
- Comment out sections to isolate issues

## Integration Patterns

### 1. Multi-timeframe Data
- Use `request.security()` for HTF data collection
- Handle `na` values from HTF requests
- Cache HTF data to avoid repeated requests
- Use `timeframe.change()` for period detection

### 2. Alert System
- Use `alert()` with `alert.freq_once_per_bar` for single alerts
- Validate conditions before triggering alerts
- Include relevant context in alert messages
- Test alerts in paper trading first

## File Organization

### 1. Project Structure
- Keep reference indicators in `Reference_Indicators/`
- Use `.pine` extensions for syntax highlighting
- Maintain comprehensive READMEs with links and context
- Version control all changes

### 2. Documentation
- Include TradingView links in READMEs
- Document all custom types and their purposes
- Explain complex algorithms with comments
- Maintain change logs for major updates

## Testing & Validation

### 1. Before Deploying
- Test on multiple timeframes
- Verify with different market conditions
- Check performance on long historical data
- Validate alert conditions work correctly

### 2. Code Review Checklist
- ✅ Proper indentation (4 spaces, no tabs)
- ✅ Drawing object limits set in indicator declaration
- ✅ Array bounds checking before ALL array.get() calls
- ✅ Array initialization verification (not na)
- ✅ Barstate handling appropriate for calculations
- ✅ Performance considerations addressed
- ✅ Documentation updated in multiple knowledge base files
- ✅ New recurring issues documented in guidelines

## Future AI Instructions

When working on Pine Script code:
1. **Always use 4-space indentation** (never tabs)
2. **Check drawing object limits** before adding new visual elements
3. **Validate array access** with bounds checking
4. **Consider barstate** for calculations and updates
5. **Reference this document** for recurring issues

This document should be updated whenever new recurring issues are discovered and solved.
