
# Requirements
- Python 3.10
- `pytest` (if running tests)

# Running the code
To run, change INPUT variable to the string of your choice and run transcribe_string.py.

As a default, the INPUT variable is set to the following:

```python
INPUT = """Patient presents today with several issues. Number one BMI has increased by 10%
since their last visit number next patient reports experiencing dizziness several times
in the last two weeks. Number next patient has a persistent cough that hasn’t
improved for last 4 weeks Number next patient is taking drug number five several
times a week"""
```
```
python transcribe_string.py
```


# Running Tests

`pytest` is required.

Installing `pytest`...

```
pip install pytest
```

Run the tests...

```
pytest transcribe_string.py
```