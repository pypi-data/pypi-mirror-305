from .logger import Logger, LakeHouseLogger

def get_logger(dd_api_key, dd_customer, environment, workspace_name, log_level):
    return Logger(dd_api_key, dd_customer, environment, workspace_name, log_level)

def get_lakehouse_logger(environment, location, spark_structure):
    return LakeHouseLogger(environment, location, spark_structure)
