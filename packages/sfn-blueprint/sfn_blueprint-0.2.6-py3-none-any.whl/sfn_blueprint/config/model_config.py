MODEL_CONFIG = {
    "code_generator": {
        "model": "gpt-3.5-turbo",
        "temperature": 0.7,
        "max_tokens": 500
    },
    "feature_suggester": {
        "model": "gpt-3.5-turbo",
        "temperature": 0.7,
        "max_tokens": 1000,
        "n": 1,
        "stop": None
    }
}