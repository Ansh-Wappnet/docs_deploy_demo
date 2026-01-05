# Operations

Efficient platform operation requires visibility and governance. The Operations tools provide the necessary oversight for Super Admins.

---

## Recent Actions Timeline

The **Recent Actions** panel is prominently displayed on the right side of the Dashboard as a vertical timeline. It provides a real-time feed of administrative activity.

### Visual Guide
The timeline uses specific visual cues to help you scan information quickly:

- **Icons:**
    - :pencil: **Pencil Icon (Blue Background):** Indicates an edit or change to an existing record.
    - :heavy_plus_sign: **Plus Icon (Green Background):** Indicates a new creation (if applicable).
- **Metadata:**
    - **Relative Time:** e.g., "1 month, 1 week ago".
    - **Entity Name:** The specific object that was modified (e.g., `Match Criteria` or `test company`).
    - **Action Summary:** A brief description of what happened (e.g., `Changed Subscription end date` or `Changed Component json`).

### Purpose
- **Auditability:** Retrace the steps leading to a configuration issue.
- **Accountability:** Identify who made specific changes.
- **Transparency:** Keep the entire ops team aligned on recent system updates.

---

## Common Admin Actions

### The "Add" Operation
Used to instantiate new records in the database.
- **[Clients](clients.md):** Onboarding a new tenant manually.
- **[Domains](domains.md):** Registering a new entry point.
- **[Rule Components](rule-components.md):** Extending the platform's logic library.
- **[Permissions](permissions.md):** Defining new granular access controls.

### The "Change" Operation
Used to modify existing configurations.
- **Updates:** Changing a client's [Subscription Plan](subscription-plans.md).
- **Corrections:** Fixing a typo in a domain name.
- **Status Changes:** Approving or rejecting a client.
- **Configuration:** Enabling or disabling [Modules](modules.md) for a client.

---

## Governance & Best Practices

To maintain a healthy platform environment, adhere to the following guidelines:

1.  **Least Privilege:** Limit the number of users with `superuser` status. Only assign it to those who absolutely need it.
2.  **Validation:** Always test new **Rule Components** in a staging environment before deploying them to production/all clients.
3.  **Subscription Management:** Assign subscription plans *before* enabling a client to ensure they don't access restricted features for free.
4.  **Monitoring:** regularly review the **Recent Actions** timeline to spot unintended or suspicious configuration changes.
