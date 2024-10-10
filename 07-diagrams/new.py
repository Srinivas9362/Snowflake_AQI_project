try:
    import snowflake.snowpark
    print("Snowpark is installed.")
except ImportError:
    print("Snowpark is not installed.")
