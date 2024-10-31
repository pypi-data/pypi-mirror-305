# README.md
# botrun_litellm

A wrapper for litellm with TAIDE configuration support.

## Installation

```bash
pip install botrun_litellm
```

## Usage

```python
from botrun_litellm import botrun_litellm_completion

response = botrun_litellm_completion(
    messages=[{"role": "user", "content": "Hello!"}],
    model="openai/gpt-4"
)
```

## Environment Variables

The following environment variables are required:

- `TAIDE_BASE_URL`: Base URL for TAIDE API
- `TAIDE_API_KEY`: API key for TAIDE
- `DEFAULT_MODEL`: (Optional) Default model to use

## License

MIT License