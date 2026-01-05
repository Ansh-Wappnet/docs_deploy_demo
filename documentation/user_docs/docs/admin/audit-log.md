# Audit Log

The **Audit Log** provides a comprehensive trail of all system activities and security events. It is an essential tool for monitoring compliance, investigating incidents, and tracking user actions.

## Overview

The main interface displays a timeline of events alongside summary metrics.

![Audit Log Interface](../assets/admin_audit_log.png)

### Summary Metrics
*   **Total Events**: The total number of logged activities.
*   **Errors**: The count of failed operations or system errors.
*   **Warnings**: The number of non-critical alerts.
*   **Unique Users**: The count of distinct users who generated activity.

## Search and Filter

You can use the controls at the top to narrow down the log entries:

*   **Search**: Enter an email address to find logs related to a specific user.
*   **Date Range**: Select a *Start Date* and *End Date* to view events within a specific window.
*   **Severity**: Filter by *All Severity*, *Info*, *Warning*, or *Error* to focus on critical issues.

## Exporting Logs

Administrators can export audit logs for external analysis or archiving.

1.  Apply any desired filters (Date, Severity, etc.).
2.  Click the **Export** button.
3.  The system will generate a downloadable file containing the visible logs.

> **Constraint**: You can export a maximum of **7 days** of logs at a time. If you need data for a longer period, please perform multiple exports in 7-day chunks.
