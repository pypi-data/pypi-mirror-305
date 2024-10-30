import pathlib
from importlib_resources import files

BASE_DIR = "exasol_advanced_analytics_framework"
TEMPLATES_DIR = pathlib.Path("resources", "templates")
OUTPUTS_DIR = pathlib.Path("resources", "outputs")
SOURCE_DIR = files(f"{BASE_DIR}.udf_framework")

UDF_CALL_TEMPLATES = {
    "query_handler_runner_udf_call.py": "create_query_handler.jinja.sql"
}
LUA_SCRIPT_TEMPLATE = "create_query_loop.jinja.sql"
LUA_SCRIPT_OUTPUT = pathlib.Path(BASE_DIR, OUTPUTS_DIR, "create_query_loop.sql")
