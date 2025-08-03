# ProFleet - Fleet Management System

A comprehensive Django-based fleet management system with role-based authentication and user management.

## 🚀 Features

- **Custom User Authentication** with role-based access control
- **Four User Roles**: Client, Driver, Clearance Agent, and Admin
- **Role-specific Dashboards** with tailored functionality
- **Responsive Design** using Bootstrap 5
- **Admin Panel** with advanced user management
- **Deployment Ready** for platforms like Render, Railway, or Heroku

## 👥 User Roles

### 🏢 Client
- Track shipments and manage orders
- View delivery status and history
- Access invoices and billing information
- Contact support and view notifications

### 🚛 Driver
- View daily delivery schedules
- Update delivery status in real-time
- Access route optimization
- Report issues and contact dispatch

### 📋 Clearance Agent
- Handle customs documentation
- Process import/export clearances
- Manage document workflows
- Track clearance status

### ⚙️ Admin
- Complete system management
- User administration and analytics
- System monitoring and configuration
- Access to Django admin panel

## 🛠️ Technology Stack

- **Backend**: Django 5.2.4
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Authentication**: Django's built-in auth with custom user model
- **Deployment**: Gunicorn, WhiteNoise for static files

## 📁 Project Structure

```
pro_fleet/
├── manage.py
├── requirements.txt
├── README.md
├── .env.example
├── pro_fleet/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── users/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
├── templates/
│   ├── base.html
│   └── users/
│       ├── landing.html
│       ├── login.html
│       ├── register.html
│       ├── client_dashboard.html
│       ├── driver_dashboard.html
│       ├── clearance_agent_dashboard.html
│       └── admin_dashboard.html
└── static/
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- pip or pipenv

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd pro_fleet
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser (Admin)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 🔧 Configuration

### Environment Variables

Create a `.env` file based on `.env.example`:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgresql://username:password@localhost:5432/profleet_db
```

### Database Configuration

**Development (SQLite)**
- Default configuration uses SQLite
- No additional setup required

**Production (PostgreSQL)**
- Set `DATABASE_URL` environment variable
- Install `psycopg2-binary` (included in requirements.txt)

## 📱 Usage

### User Registration

1. Visit the homepage
2. Click "Register" 
3. Fill out the form and select your role:
   - **Client**: For businesses shipping goods
   - **Driver**: For delivery personnel
   - **Clearance Agent**: For customs processing
   - **Admin**: For system administration

### Dashboard Access

After login, users are automatically redirected to their role-specific dashboard:

- **Clients**: Order management, shipment tracking
- **Drivers**: Delivery schedules, route information
- **Clearance Agents**: Documentation, clearance processing
- **Admins**: System overview, user management

## 🎨 Key Components

### Custom User Model (`users/models.py`)

```python
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('client', 'Client'),
        ('driver', 'Driver'),
        ('clearance_agent', 'Clearance Agent'),
        ('admin', 'Admin'),
    ]
    
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default='client'
    )
```

### Role-Based Views (`users/views.py`)

- Automatic dashboard routing based on user role
- Permission checks for role-specific pages
- Custom registration with role selection

### Admin Interface (`users/admin.py`)

- Enhanced user management
- Bulk actions for user operations
- Advanced filtering and search

## 🚀 Deployment

### For Render/Railway

1. **Push to GitHub**
2. **Connect your repository**
3. **Set environment variables**:
   - `SECRET_KEY`
   - `DEBUG=False`
   - `ALLOWED_HOSTS=your-domain.com`
   - `DATABASE_URL` (PostgreSQL)

4. **Build command**: `pip install -r requirements.txt`
5. **Start command**: `gunicorn pro_fleet.wsgi:application`

### Static Files

For production, uncomment WhiteNoise in `settings.py`:
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Uncomment this
    # ... other middleware
]
```

## 🔒 Security Features

- CSRF protection enabled
- Secure password validation
- Role-based access control
- Environment-based configuration
- Production-ready security settings

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🧪 Testing

### Manual Testing

1. **Test User Registration**:
   ```bash
   # Visit http://127.0.0.1:8000/register/
   # Create users with different roles
   ```

2. **Test Role-Based Access**:
   - Login as different user types
   - Verify dashboard content matches role
   - Test navigation and permissions

3. **Test Admin Panel**:
   ```bash
   # Visit http://127.0.0.1:8000/admin/
   # Login with superuser credentials
   # Test user management features
   ```

### Sample Test Users

After running the server, you can create test users:

| Role | Username | Purpose |
|------|----------|---------|
| Client | `test_client` | Test client dashboard |
| Driver | `test_driver` | Test driver dashboard |
| Agent | `test_agent` | Test clearance agent dashboard |
| Admin | `test_admin` | Test admin dashboard |

## 🐛 Troubleshooting

### Common Issues

**1. Migration Errors**
```bash
# Reset migrations if needed
python manage.py migrate --fake users zero
python manage.py makemigrations users
python manage.py migrate
```

**2. Static Files Not Loading**
```bash
# Collect static files
python manage.py collectstatic
```

**3. Permission Denied Errors**
- Ensure proper user roles are assigned
- Check if user is logged in
- Verify dashboard URL matches user role

**4. Database Connection Issues**
- Check DATABASE_URL format
- Ensure PostgreSQL is running (production)
- Verify database credentials

## 📊 Database Schema

### CustomUser Model Fields

| Field | Type | Description |
|-------|------|-------------|
| `username` | CharField | Unique username |
| `email` | EmailField | User email address |
| `first_name` | CharField | User's first name |
| `last_name` | CharField | User's last name |
| `user_type` | CharField | Role (client/driver/clearance_agent/admin) |
| `phone_number` | CharField | Contact phone (optional) |
| `is_active` | BooleanField | Account status |
| `date_joined` | DateTimeField | Registration date |

## 🔄 Development Workflow

### Adding New Features

1. **Create a new branch**
   ```bash
   git checkout -b feature/new-feature
   ```

2. **Make changes**
   - Update models if needed
   - Create/update views
   - Add/modify templates
   - Update URLs

3. **Test changes**
   ```bash
   python manage.py runserver
   # Test functionality manually
   ```

4. **Create migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to classes and functions
- Keep templates organized and well-commented

## 📈 Future Enhancements

### Planned Features

- [ ] Real-time notifications
- [ ] GPS tracking integration
- [ ] Advanced reporting and analytics
- [ ] Mobile app support
- [ ] API endpoints for third-party integration
- [ ] Document upload and management
- [ ] Email notifications
- [ ] Multi-language support

### Technical Improvements

- [ ] Add comprehensive test suite
- [ ] Implement caching (Redis)
- [ ] Add logging and monitoring
- [ ] Performance optimization
- [ ] Security enhancements
- [ ] Docker containerization

## 📞 Support

For support and questions:
- Email: support@profleet.com
- Phone: +1 (555) 123-4567
- Documentation: [Project Wiki](link-to-wiki)
- Issues: [GitHub Issues](link-to-issues)

## 📝 Changelog

### Version 1.0.0 (Current)
- Initial release
- Custom user authentication
- Role-based dashboards
- Admin panel integration
- Responsive design
- Deployment ready

---

**Built with ❤️ using Django and Bootstrap**

*ProFleet - Streamlining fleet management operations*
