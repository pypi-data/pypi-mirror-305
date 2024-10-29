from typing import Union, Required, TypedDict, List, Dict


class LwDeleteSearchIssues(TypedDict, total=False):
    """ lw_delete_search_issues. """

    storage_name: Required[str]
    """ Required property """

    rows_to_delete: Required[int]
    """ Required property """

    conditions: Required["_LwDeleteSearchIssuesConditions"]
    """ Required property """

    tenant_ids: Required[Dict[str, "_LwDeleteSearchIssuesTenantIdsAdditionalproperties"]]
    """ Required property """



class _LwDeleteSearchIssuesConditions(TypedDict, total=False):
    project_id: List[int]
    group_id: List[int]


_LwDeleteSearchIssuesTenantIdsAdditionalproperties = Union[str, "_LwDeleteSearchIssuesTenantIdsAdditionalpropertiesAnyof1"]
""" Aggregation type: anyOf """



_LwDeleteSearchIssuesTenantIdsAdditionalpropertiesAnyof1 = int
""" minimum: 1 """

