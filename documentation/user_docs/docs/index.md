# Recon AI Overview

Welcome to the **Recon AI** User Guide. This platform allows you to automate the reconciliation of financial transactions, identifying discrepanices and validating data accuracy with powerful rule-based logic.

## Application Workflow
The typical user journey in Recon AI follows a linear flow from data ingestion to analysis.

### 1. Data Connectors

**Goal**: Bring your data into the system.

*   **Ingest**: Upload files via **CSV**, **Excel**, **JSON**, connect to an **SFTP Server**, or integrate via **API**.
*   **Map**: Define how your file columns (e.g., *Date*, *Amount*, *Reference*) correspond to the system's schema.
*   See [Data Connectors](data-connectors/hub.md) for more details.

### 2. Rules Engine

**Goal**: Define "what constitutes a match."

*   **Create Rules**: Use the logic builder to set conditions (e.g., *Amount* must match exactly, *Date* must be within 3 days).
*   **Tolerances**: Configure allowed variances for fuzzy matching.
*   See [Rules Engine](rules-engine/overview.md) for more details.

### 3. Data Pipelines

**Goal**: Automate the processing.

*   **Build Pipeline**: Connect your *Data Sources* to your *Rules*.
*   **Execution**: Trigger pipelines manually to generate results.
*   See [Data Pipelines](data-pipelines/overview.md) for more details.

### 4. Reconciliation & Verification

**Goal**: Review results and handle exceptions.

*   **Dashboard**: Monitor the status of active jobs (Matched vs. Unmatched).
*   **Manual Matching**: Use the workspace to resolve exceptions that the automated rules could not handle.
*   See [Reconciliation](reconciliation/dashboard.md) for more details.

### 5. Analytics

**Goal**: Visualize performance.

*   **Executive Dashboard**: View high-level KPIs, volume trends, and success rates.
*   See [Analytics](analytics/executive-dashboard.md) for more details.

---

## Roles & Permissions

Recon AI uses a secure **Role-Based Access Control (RBAC)** system.

### Admin Users
Administrators have full visibility and control over the platform.

*   **System Settings**: Configure global preferences.
*   **User Management**: Invite users and manage teams.
*   **Audit Logs**: View comprehensive system activity trails.

### Standard Users
Access for non-admin users is determined by their assigned **Role**.

*   **Roles**: Defined by Admins (e.g., *Analyst*, *Reviewer*).
*   **Permissions**: Granularity controls what actions a user can perform (e.g., *View Only*, *Create & Edit*, *Delete*).
