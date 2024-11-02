# Bigeye Airflow Operators for Airflow Versions 2.x

## Operators
### Create Metric Operator (bigeye_airflow.operators.create_metric_operator)

The CreateMetricOperator creates metrics from a list of metric configurations provided to the operator.
This operator will fill in reasonable defaults like setting thresholds.  It authenticates through an Airflow connection 
ID and offers the option to run the metrics after those metrics have been created.  Please review the link below to 
understand the structure of the configurations.

[Create or Update Metric Swagger](https://docs.bigeye.com/reference/createmetric)

#### Parameters
1. connection_id: str - The Airfow connection ID used to store the required Bigeye credential.
2. warehouse_id: int - The Bigeye source/warehouse id to which the metric configurations will be deployed.
3. configuration: List[dict] - A list of metric configurations conforming to the following schema.
    ```
    schema_name: str
    table_name: str
    column_name: str
    metric_template_id: uuid.UUID
    metric_name: str
    description: str
    notifications: List[str]
    thresholds: List[dict]
    filters: List[str]
    group_by: List[str]
    user_defined_metric_name: str
    metric_type: SimpleMetricCategory
    default_check_frequency_hours: int
    update_schedule: str
    delay_at_update: str
    timezone: str
    should_backfill: bool
    lookback_type: str
    lookback_days: int
    window_size: str
    _window_size_seconds
    ```
4. run_after_upsert: bool - If true it will run the metrics after creation.  Defaults to False.
5. workspace_id: Optional[int] - The ID of the workspace where metrics should be created. 
If only 1 workspace configured, then will default to that else this will be required.

### Run Metrics Operator (bigeye_airflow.operators.run_metrics_operator)

The RunMetricsOperator will run metrics in Bigeye based on the following:

1. All metrics for a given table, by providing warehouse ID, schema name and table name.
2. All metrics for a given collection, by providing the collection ID.
3. Any and all metrics, given a list of metric IDs.  

Currently, if a list of metric IDs is provided these will be run instead of metrics provided for
warehouse_id, schema_name, table_name, and collection_id

#### Parameters
1. connection_id: str - The Airfow connection ID used to store the required Bigeye credential.
2. warehouse_id: int - The Bigeye source/warehouse id for which metrics will be run.
3. schema_name: str - The schema name for which metrics will be run.
4. table_name: str - The table name for which metrics will be run.
5. collection_id: int - The ID of the collection where the operator will run the metrics.
6. metric_ids: List[int] - The metric ids to run.
7. workspace_id: Optional[int] - The ID of the workspace where metrics should be run. 
If only 1 workspace configured, then will default to that else this will be required.
8. circuit_breaker_mode: bool - Whether dag should raise an exception if metrics result in alerting state, default False.

### Create Delta Operator (bigeye_airflow.operators.create_delta_operator)

The CreateDeltaOperator creates deltas from a list of delta configurations provided to the operator.
This operator will fill in reasonable defaults like column mappings.  It authenticates through an Airflow connection 
ID and offers the option to run the deltas after those deltas have been created.  Please review the link below to 
understand the structure of the configurations.

#### Parameters
1. connection_id: str - The Airfow connection ID used to store the required Bigeye credential.
2. warehouse_id: int - The Bigeye source/warehouse id to which the metric configurations will be deployed.
3. configuration: List[dict] - A list of delta configurations conforming to the following schema.
    ```
    delta_name: str
    fq_source_table_name: str
    target_table_comparisons: dict
    - example: {"target_table_comparisons": [{"fq_target_table_name": "Snowflake.TOOY_DEMO_DB.PROD_REPL.ORDERS"}]
    tolerance: Optional[float]
    - default = 0.0
    cron_schedule: Optional[dict] 
    - default = None 
    - example: {"cron_schedule": {"name": "Midnight UTC", "cron": "0 0 * * *"}}
    notification_channels: Optional[List[dict]]
    - default = None
    - example: {"notification_channels: [{"slack": "#data-alerts"}]
    ```
4. run_after_upsert: bool - If true it will run the deltas after creation.  Defaults to False.
5. workspace_id: Optional[int] - The ID of the workspace where deltas should be created. 
If only 1 workspace configured, then will default to that else this will be required.

### Run Deltas Operator (bigeye_airflow.operators.run_deltas_operator)

The RunDeltasOperator will run deltas in Bigeye based on the following:

1. All deltas for a given table, by providing warehouse ID, schema name and table name.
2. Any and all deltas, given a list of delta IDs.  

Currently, if a list of delta IDs is provided these will be run instead of metrics provided for
warehouse_id, schema_name, table_name.

#### Parameters
1. connection_id: str - The Airfow connection ID used to store the required Bigeye credential.
2. warehouse_id: int - The Bigeye source/warehouse id for which metrics will be run.
3. schema_name: str - The schema name for which metrics will be run.
4. table_name: str - The table name for which metrics will be run.
5. delta_ids: List[int] - The delta ids to run.
6. workspace_id: Optional[int] - The ID of the workspace where deltas should be run. 
If only 1 workspace configured, then will default to that else this will be required.
7. circuit_breaker_mode: bool - Whether dag should raise an exception if deltas result in alerting state, default False.
