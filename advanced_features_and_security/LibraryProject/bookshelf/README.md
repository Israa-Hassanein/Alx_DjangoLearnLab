# Permissions and Groups Setup

## Permissions
- `can_view`: Allows users to view books.
- `can_create`: Allows users to create new books.
- `can_edit`: Allows users to edit books.
- `can_delete`: Allows users to delete books.

## Groups
- `Viewers`: Assigned `can_view`.
- `Editors`: Assigned `can_view`, `can_create`, `can_edit`.
- `Admins`: Assigned `can_view`, `can_create`, `can_edit`, `can_delete`.

## How to Test
1. Create test users in the admin site or using `create_groups.py`.
2. Assign them to groups: `Viewers`, `Editors`, or `Admins`.
3. Verify access to book-related views based on their permissions.

## Notes
- Use `@permission_required` decorators to protect views.
- Permissions are defined in the `Book` model's `Meta` class.
