from prometheus_client import Counter, Histogram

users_created_total = Counter(
    "users_created_total",
    "Total created users"
)

api_request_duration_seconds = Histogram(
    "api_request_duration_seconds",
    "API request duration",
    ["method"]
)
