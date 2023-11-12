# python-lucidmotors

Unofficial Python bindings to the Lucid Motors API. No affiliation with Lucid
Motors.

To install dependencies, assuming you have Python development tools already, run:

```
pip install '.[dev]'
```

Try fiddling with `examples/vehicle_info.py`. With no arguments it will prompt
for your Lucid username and password, then print out your user profile and
vehicle information.

It may fail due to validation errors the first few times, because the types in
`lucidmotors/vehicle.py` and `lucidmotors/user.py` need to be extended to understand 
values from all different Lucid trims/styles in all kinds of different states, which 
will take some time.

If you're feeling adventurous, try playing wiht `examples/test_all_actions.py` which
will run through every action we have figured out out thus far. A "stress test" of 
sorts.