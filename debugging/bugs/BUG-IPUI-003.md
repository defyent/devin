# BUG-IPUI-003 — Sparse VoiceOver labels and partial Dynamic Type support

- **Module:** iPad app — cross-cutting accessibility
- **Severity:** Low (accessibility)

## Findings
- Source: 23 `accessibilityLabel` uses vs 151 `Image(systemName:)`; no `accessibilityHint/Value/Hidden`. Icon-only toolbar buttons (settings gear, download, tracking, +, ⋯) will mostly be read by SF Symbol name or not at all.
- 87 fixed `.font(.system(size:))` uses. At Accessibility XXL text size, row titles/descriptions scale, but segmented controls (Theme, Time Format, Legs/Forms/Files/Details), section headers, nav titles, Done and Add Leg stay tiny; leg cards keep a fixed ~300pt width so text wraps heavily on a 13" screen.
- Live VoiceOver could not be exercised (simulator AX tree not reachable in this harness).

## Evidence
- evidence/IPUI-014_dyntype_axxxl_config.png
- evidence/IPUI-015_dyntype_flight_list.png
- evidence/IPUI-016_dyntype_flight_detail.png
