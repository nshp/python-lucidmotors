# python-lucidmotors

Unofficial Python bindings to the Lucid Motors API. No affiliation with Lucid
Motors.

To install dependencies, assuming you have Python development tools already, run:

```
pip install -r requirements.txt
```

Try fiddling with `examples/vehicle_info.py`. With no arguments it will prompt
for your Lucid username and password, then print out your user profile and
vehicle information.

To generate a test case from your data, visit
[testmycode.cc](https://testmycode.cc). This will log in using your Lucid
account, remove identifying information from the API response, and let you
submit the anonymized data for review.

## Authentication and session lifetime

A successful login or refresh returns three credentials, and they do **not** share a lifetime:

| credential | what it is | lifetime |
|---|---|---|
| `id_token` | the bearer attached to every gRPC call | **5 minutes** (`exp − iat` = 300 s) |
| `gigya_jwt` | stored on the session, not used for calls | 6 hours |
| `refresh_token` | opaque; mints a new session via `authentication_refresh()` | does not rotate; server-side expiry unknown |

`LucidAPI.session_time_remaining` tracks the **id_token**, so it will read as five minutes even though `gigya_jwt` is longer. The server enforces the id_token expiry exactly — a call made 45 seconds past `exp` fails with `UNAUTHENTICATED: token is expired by 45s`, with no grace period.

Two consequences for anything long-running:

- **Refresh before `session_time_remaining` reaches zero, and make your threshold larger than your poll interval.** A client polling every 30 s should refresh at roughly `< 60 s` remaining.
- **Don't refresh more often than that.** Back-to-back calls to `authentication_refresh()` return the *same* session and expiry until it is genuinely near the end, so a threshold that is always true (for example `< 3600` against a 300 s token) just refreshes on every poll for nothing.

`login_with_refresh_token()` lets a service start from a stored refresh token so no password needs to be kept on disk.

If you're feeling adventurous, try playing with `examples/test_all_actions.py` which
will run through every action we have figured out out thus far. A "stress test" of
sorts.
