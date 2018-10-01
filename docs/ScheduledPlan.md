# ScheduledPlan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Id | [optional] 
**name** | **str** | Name | [optional] 
**created_at** | **datetime** | Date and time when ScheduledPlan was created | [optional] 
**updated_at** | **datetime** | Date and time when ScheduledPlan was last updated | [optional] 
**title** | **str** | Title | [optional] 
**user_id** | **int** | User Id which owns this ScheduledPlan | [optional] 
**user** | [**UserPublic**](UserPublic.md) | User who owns this ScheduledPlan | [optional] 
**run_as_recipient** | **bool** | Whether schedule is ran as recipient (only applicable for email recipients) | [optional] 
**enabled** | **bool** | Whether the ScheduledPlan is enabled | [optional] 
**next_run_at** | **datetime** | When the ScheduledPlan will next run (null if running once) | [optional] 
**last_run_at** | **datetime** | When the ScheduledPlan was last run | [optional] 
**look_id** | **int** | Id of a look | [optional] 
**dashboard_id** | **int** | Id of a dashboard | [optional] 
**lookml_dashboard_id** | **str** | Id of a LookML dashboard | [optional] 
**filters_string** | **str** | Query string to run look or dashboard with | [optional] 
**dashboard_filters** | **str** | (DEPRECATED) Alias for filters_string field | [optional] 
**require_results** | **bool** | Delivery should occur if running the dashboard or look returns results | [optional] 
**require_no_results** | **bool** | Delivery should occur if the dashboard look does not return results | [optional] 
**require_change** | **bool** | Delivery should occur if data have changed since the last run | [optional] 
**send_all_results** | **bool** | Will run an unlimited query and send all results. | [optional] 
**crontab** | **str** | Vixie-Style crontab specification when to run | [optional] 
**datagroup** | **str** | Name of a datagroup; if specified will run when datagroup triggered (can&#39;t be used with cron string) | [optional] 
**timezone** | **str** | Timezone for interpreting the specified crontab (default is Looker instance timezone) | [optional] 
**query_id** | **str** | Query id | [optional] 
**scheduled_plan_destination** | [**list[ScheduledPlanDestination]**](ScheduledPlanDestination.md) | Scheduled plan destinations | [optional] 
**run_once** | **bool** | Whether the plan in question should only be run once (usually for testing) | [optional] 
**include_links** | **bool** | Whether links back to Looker should be included in this ScheduledPlan | [optional] 
**can** | **dict(str, bool)** | Operations the current user is able to perform on this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


