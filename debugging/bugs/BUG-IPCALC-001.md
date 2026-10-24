# BUG-IPCALC-001 — Unit Converter: NM <-> Statute Miles conversion inverted; large values shown in scientific notation

- **Module:** iPad app — Calculator > Unit Converter (Distance)
- **Severity:** High (wrong navigation figure, ~25% error, no warning)
- **App:** DataHangar Flight 1.0.13 (46), iPad Pro 13" Simulator iOS 26.5
- **Found:** 2026-10-24, iPad Swift audit row 76

## Steps
1. Calculator > Unit Converter > Distance, Convert From = Nautical Miles (NM).
2. Enter 100.

## Expected
Statute Miles = 115.08 mi (1 NM = 1.15078 mi). Meters 185,200 m; Feet 607,612 ft shown as plain numbers.

## Actual
Statute Miles = **86.8974 mi** (that is the mi->NM figure). Meters shows `1.852e+05 m`, Feet `6.076e+05 ft`.
Reverse direction (100 mi -> NM) is also inverted per source (gives 115.08 NM instead of 86.90 NM).

## Cause
`Views/Calculator/UnitConverterView.swift`, distance units:
```swift
ConvUnit(name: "Statute Miles", abbrev: "mi", toBase: { $0 * 1.852 / 1.60934 }, fromBase: { $0 * 1.60934 / 1.852 }),
```
Base unit is NM; the factors are swapped. Fix: `toBase: { $0 * 1.60934 / 1.852 }, fromBase: { $0 * 1.852 / 1.60934 }`.
Scientific notation comes from the result formatter (likely `%g`); use a grouped decimal format for large values.

## Evidence
- screenshots/IPCALC-010_unit_nm_to_mi_wrong.png

## Notes
Other converter factors (speed mph/km/h/m/s/fpm, altitude m/FL, weight, volume, temp, pressure) checked in source: correct. No website counterpart.
