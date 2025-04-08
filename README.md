# Regisbridge Private School Website

A modern, responsive website for Regisbridge Private School built with Django and Bootstrap.

## Features

- Responsive design optimized for all devices
- Dynamic content management system
- Secure user authentication and authorization
- Online admission application system
- News and events management
- Parent portal
- Contact form with email integration
- SEO optimized
- Performance optimized with caching and lazy loading
- Accessibility compliant

## Tech Stack

- **Backend:** Django 5.0.2
- **Frontend:** Bootstrap 5, JavaScript
- **Database:** PostgreSQL (configurable)
- **Cache:** Redis
- **Task Queue:** Celery
- **Static/Media Storage:** AWS S3 (configurable)
- **Development Tools:** Django Debug Toolbar

## Prerequisites

- Python 3.11+
- PostgreSQL
- Redis (optional, for caching and Celery)
- Node.js and npm (for frontend asset management)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/regisbridge-school.git
   cd regisbridge-school
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

Visit http://127.0.0.1:8000/ to see the website.

## Development

### Code Style

We use:
- Black for Python code formatting
- ESLint for JavaScript linting
- Prettier for JavaScript/CSS formatting

### Running Tests

```bash
python manage.py test
```

### Working with Static Files

During development:
```bash
python manage.py collectstatic
```

### Database Migrations

Create migrations:
```bash
python manage.py makemigrations
```

Apply migrations:
```bash
python manage.py migrate
```

## Deployment

1. Update `.env` with production settings
2. Set `DEBUG=False`
3. Configure your web server (e.g., Nginx)
4. Set up SSL certificates
5. Configure static/media file serving
6. Set up database backups

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, email support@regisbridge.edu or create an issue in the repository.

## Acknowledgments

- Django community
- Bootstrap team
- All contributors

## Project Structure

```
regisbridge/
├── admissions/         # Admissions app
├── main/              # Main app
├── static/            # Static files
│   ├── css/
│   ├── js/
│   ├── images/
│   └── fonts/
├── templates/         # HTML templates
├── media/            # User-uploaded files
├── requirements.txt  # Python dependencies
└── manage.py        # Django management script
```

## Security

- HTTPS enforced
- CSRF protection
- XSS protection
- SQL injection protection
- Secure password hashing
- Rate limiting
- Regular security updates

## Performance

- Static file compression
- Image optimization
- Browser caching
- Database query optimization
- Lazy loading of images
- Minified CSS/JS

## Monitoring

- Error tracking
- Performance monitoring
- User analytics
- Server monitoring
- Security monitoring 