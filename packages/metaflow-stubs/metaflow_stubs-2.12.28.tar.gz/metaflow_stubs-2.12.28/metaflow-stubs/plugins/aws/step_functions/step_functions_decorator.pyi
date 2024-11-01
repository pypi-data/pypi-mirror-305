##################################################################################
#                       Auto-generated Metaflow stub file                        #
# MF version: 2.12.28                                                            #
# Generated on 2024-11-01T10:21:04.546868                                        #
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

class DynamoDbClient(object, metaclass=type):
    def __init__(self):
        ...
    def save_foreach_cardinality(self, foreach_split_task_id, foreach_cardinality, ttl):
        ...
    def save_parent_task_id_for_foreach_join(self, foreach_split_task_id, foreach_join_parent_task_id):
        ...
    def get_parent_task_ids_for_foreach_join(self, foreach_split_task_id):
        ...
    ...

class StepFunctionsInternalDecorator(metaflow.decorators.StepDecorator, metaclass=type):
    def task_pre_step(self, step_name, task_datastore, metadata, run_id, task_id, flow, graph, retry_count, max_user_code_retries, ubf_context, inputs):
        ...
    def task_finished(self, step_name, flow, graph, is_task_ok, retry_count, max_user_code_retries):
        ...
    ...

