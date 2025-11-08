# welcome-cli

**Goal:** Fix small cross-file issues so `python main.py` prints:

Welcome to GDG Dev Nest, explorer!

css
Copy code

**Run**
```bash
python main.py
```

Slight hint:

Check that variable names match across files and be careful with spaces and punctuation when composing the final string.

Deliverable:

Exact output match is required (including punctuation).



```bash
### `welcome-cli-plus/messages.py`
```python
# messages.py

WELCOME_PREFIX = "Welcome to GDG Dev Nest"
WELCOME_NAME = "explorer"
