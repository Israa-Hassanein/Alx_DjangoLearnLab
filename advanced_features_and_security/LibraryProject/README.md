# Django Application Security Measures

## Secure Settings
- `DEBUG = False` to prevent debug information leaks.
- `SECURE_BROWSER_XSS_FILTER` and `SECURE_CONTENT_TYPE_NOSNIFF` enabled to protect against XSS and MIME attacks.
- Cookies (`CSRF_COOKIE_SECURE`, `SESSION_COOKIE_SECURE`) configured for HTTPS.

## CSRF Protection
- All forms include `{% csrf_token %}` in templates.

## SQL Injection Prevention
- Used Django ORM to safely parameterize queries.
- Validated user inputs with Django forms.

## Content Security Policy (CSP)
- Configured CSP headers using `django-csp` to prevent XSS.

## Testing
- Tested forms for CSRF and XSS.
- Checked input fields to ensure no raw SQL vulnerabilities.
