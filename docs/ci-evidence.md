# CI evidence snapshot

This is a manually recorded summary of the GitHub Actions push runs for commit [`e680d3ac905651526d562d3a2a40eb235cae77bf`](https://github.com/Caliquende/python-test-automation-training-projects/commit/e680d3ac905651526d562d3a2a40eb235cae77bf), merged on 2 November 2026. It is a historical snapshot, not the current build status or a substitute for the original reports.

| Suite | Result in JUnit reports | Original run |
| --- | --- | --- |
| API Pytest | 17 tests, 0 failures, 0 errors, 0 skipped | [Test Automation](https://github.com/Caliquende/python-test-automation-training-projects/actions/runs/41452532746) |
| Selenium Pytest | 7 tests, 0 failures, 0 errors, 0 skipped | [Test Automation](https://github.com/Caliquende/python-test-automation-training-projects/actions/runs/41452532746) |
| Playwright Pytest | 15 tests, 0 failures, 0 errors, 0 skipped | [Test Automation](https://github.com/Caliquende/python-test-automation-training-projects/actions/runs/41452532746) |
| Newman | 10 requests, 40 assertions, 0 failures | [Newman API Tests](https://github.com/Caliquende/python-test-automation-training-projects/actions/runs/41452532653) |
| CodeQL | Python analysis job completed successfully | [CodeQL Analysis](https://github.com/Caliquende/python-test-automation-training-projects/actions/runs/41452532505) |

The original run pages link the test artifacts and job logs. GitHub requires a signed-in account with repository read access to download artifacts, and artifacts expire. This summary remains in the repository after artifact expiry but cannot replace independent verification of the original XML and HTML reports. A successful CodeQL job does not itself mean that no alerts exist; inspect **Security > Code scanning** for results.

The security scan in this historical run was informational. Its `pip-audit` report listed three entries for `setuptools 79.0.1`: two entries with the same `PYSEC-2026-3447` identifier and one `GHSA-xmj3-9gf7-h52w` entry. These are report entries, not a claim of three distinct vulnerabilities.
