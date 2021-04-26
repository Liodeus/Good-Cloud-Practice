# cloudsql_maintenance

## Background

Cloud SQL instances need occasional updates to fix bugs, prevent security exploits, and perform upgrades. After applying updates, Cloud SQL restarts the instances, which can cause a disruption in service. During maintenance, HA primary instances do not fail over to standby instances.

Maintenance windows are blocks of time when Cloud SQL schedules this maintenance to take place.

If you do not specify a preferred window, disruptive updates can happen at any time.

CloudSQL Instances must have a maintenance schedule.

## Fix

```shell
gcloud sql instances patch instance-id --maintenance-window-day=day --maintenance-window-hour=hour
```

## References

- [Overview of maintenance on Cloud SQL instances](https://cloud.google.com/sql/docs/mysql/maintenance)
- [Setting a preferred window for maintenance on an instance](https://cloud.google.com/sql/docs/mysql/set-maintenance-window#set-maintenance)
