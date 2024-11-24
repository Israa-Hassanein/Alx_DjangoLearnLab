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

## Security Configuration for HTTPS
- **SECURE_SSL_REDIRECT**: Redirects all HTTP traffic to HTTPS.
- **SECURE_HSTS_SECONDS**: Enforces browsers to use HTTPS for 1 year.
- **SESSION_COOKIE_SECURE**: Ensures session cookies are only sent over HTTPS.
- **CSRF_COOKIE_SECURE**: Ensures CSRF cookies are only sent over HTTPS.
- **X_FRAME_OPTIONS**: Protects against clickjacking.
- **SECURE_CONTENT_TYPE_NOSNIFF**: Prevents MIME type sniffing.
- **SECURE_BROWSER_XSS_FILTER**: Enables browser XSS protection filters.

## Deployment Configuration for HTTPS
1. Install Certbot and obtain SSL certificates:
   ```bash
   sudo apt update
   sudo apt install certbot python3-certbot-nginx
   sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
