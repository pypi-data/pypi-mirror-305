##################################################################################
#                       Auto-generated Metaflow stub file                        #
# MF version: 2.12.28                                                            #
# Generated on 2024-11-01T10:21:04.502360                                        #
##################################################################################

from __future__ import annotations

import typing
if typing.TYPE_CHECKING:
    import metaflow.decorators

class MetaDatum(tuple, metaclass=type):
    """
    MetaDatum(field, value, type, tags)
    """
    @staticmethod
    def __new__(_cls, field, value, type, tags):
        """
        Create new instance of MetaDatum(field, value, type, tags)
        """
        ...
    def __repr__(self):
        """
        Return a nicely formatted representation string
        """
        ...
    def __getnewargs__(self):
        """
        Return self as a plain tuple.  Used by copy and pickle.
        """
        ...
    ...

TASK_ID_XCOM_KEY: str

FOREACH_CARDINALITY_XCOM_KEY: str

K8S_XCOM_DIR_PATH: str

def safe_mkdir(dir):
    ...

def push_xcom_values(xcom_dict):
    ...

class AirflowInternalDecorator(metaflow.decorators.StepDecorator, metaclass=type):
    def task_pre_step(self, step_name, task_datastore, metadata, run_id, task_id, flow, graph, retry_count, max_user_code_retries, ubf_context, inputs):
        ...
    def task_finished(self, step_name, flow, graph, is_task_ok, retry_count, max_user_code_retries):
        ...
    ...

