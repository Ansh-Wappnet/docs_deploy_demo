# Access & Authentication

Data security and access control are paramount in the Recon AI platform. The Super Admin panel is secured via a robust **Role-Based Access Control (RBAC)** system, ensuring that only authorized personnel can make system-wide configurations.

## Admin URL

All administrative actions are performed through the centralized admin portal:

- **Primary URL:** `https://devapi-recon.dharsi.ai/admin/`

!!! note "Environment Check"
    Please confirm you are accessing the correct environment (**Dev**, **Staging**, or **Prod**) as the URL prefix will vary for each.

---

## Authentication

### Role-Based Access Control (RBAC)
Access to the Super Admin panel is strictly restricted to users with the `superuser` or `superadmin` role. Standard users and client-level administrators cannot access this interface.

- **Authentication Method:** Secure login via email and password (or SSO if configured).
- **Session Management:** Sessions are timed out automatically after periods of inactivity to prevent unauthorized access.

### User Context
Once logged in, the system provides visual indicators of your current session:

- **Sidebar:** Displays the logged-in user's email address at the bottom for quick verification.
- **Profile Menu:** Located in the top-right corner, allowing access to:
    - Account Settings
    - Password Change
    - Logout

!!! warning "Security Best Practice"
    Always log out of your admin session when stepping away from your workstation to maintain system security.
