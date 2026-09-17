- Use this when asked to calculate compound interest (final amount, total interest, growth over time) for a given principal and rate.
- Tool: `tools/compound_interest.py`.
- Invocation:
  + Run via `python tools/compound_interest.py <principal> <annual_rate> <compounds_per_year> <years>`.
  + `principal` — starting amount, plain number (e.g. `15847`).
  + `annual_rate` — decimal form, not a percentage (e.g. `0.0734` for 7.34%).
  + `compounds_per_year` — integer compounding frequency (e.g. `12` for monthly, `4` for quarterly, `1` for annually).
  + `years` — total duration in years as a decimal; convert months to a fraction of a year first (e.g. 8 years 7 months → `8.5833333`, computed as `years + months/12`).
- Processing:
  + Do not hand-calculate the result — always invoke the script and use its printed output.
  + If the requested duration includes months, convert to decimal years before calling the script; do not pass months separately.
- Output format:
  + Present both printed lines from the script verbatim: `Final amount: $...` and `Total interest: $...`.
  + Do not reformat, round further, or recompute the values shown by the script.
- Constraints:
  + Never fabricate results without running the script.
  + If any input (principal, rate, frequency, years) is missing, ask the user before invoking the script rather than guessing values.
