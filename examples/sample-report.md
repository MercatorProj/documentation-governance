# Sample drift report (illustrative only)

| Source change | Documentation | Evidence | Finding type | Confidence | Recommendation | Status |
|---|---|---|---|---|---|---|
| `src/domain/order-schema.ts`: field renamed | `docs/architecture/order-data-model.md` | Type declaration changed from `packageCount` to `cartonCount` | mechanical | high | Update field table and search related examples | proposed |
| Packing workflow branch changed | `docs/guide/packing-workflow.md` | Implementation and tests differ from prose, but requirement authority is unclear | conflict | medium | Ask product owner whether behavior or requirement should change | needs-review |
