from prometheus_client import Counter, Histogram

from prometheus.conf import NAMESPACE, PROMETHEUS_LATENCY_BUCKETS

connections_total = Counter(
    "ginger_db_new_connections_total",
    "Counter of created connections by database and by vendor.",
    ["alias", "vendor"],
    namespace=NAMESPACE,
)

connection_errors_total = Counter(
    "ginger_db_new_connection_errors_total",
    "Counter of connection failures by database and by vendor.",
    ["alias", "vendor"],
    namespace=NAMESPACE,
)

execute_total = Counter(
    "ginger_db_execute_total",
    ("Counter of executed statements by database and by vendor, including" " bulk executions."),
    ["alias", "vendor"],
    namespace=NAMESPACE,
)


execute_many_total = Counter(
    "ginger_db_execute_many_total",
    ("Counter of executed statements in bulk operations by database and" " by vendor."),
    ["alias", "vendor"],
    namespace=NAMESPACE,
)


errors_total = Counter(
    "ginger_db_errors_total",
    ("Counter of execution errors by database, vendor and exception type."),
    ["alias", "vendor", "type"],
    namespace=NAMESPACE,
)

query_duration_seconds = Histogram(
    "ginger_db_query_duration_seconds",
    ("Histogram of query duration by database and vendor."),
    ["alias", "vendor"],
    buckets=PROMETHEUS_LATENCY_BUCKETS,
    namespace=NAMESPACE,
)
