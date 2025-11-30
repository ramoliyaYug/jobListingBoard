"""
Script to create sample job data for testing the Job Listing Board.
Run this after migrations: python manage.py shell < scripts/create_sample_data.py
"""

from jobs.models import Job

# Clear existing jobs
Job.objects.all().delete()

# Create sample jobs
jobs_data = [
    {
        'title': 'Senior Python Developer',
        'company': 'TechCorp Inc',
        'description': '''We are looking for an experienced Python developer to join our team.

Requirements:
- 5+ years of Python experience
- Django or FastAPI experience
- PostgreSQL knowledge
- REST API design

Responsibilities:
- Develop backend services
- Optimize database queries
- Code reviews and mentoring
- System architecture planning''',
        'location': 'San Francisco, CA',
        'job_type': 'FT',
        'status': 'PUBLISHED',
    },
    {
        'title': 'Frontend Engineer (React)',
        'company': 'WebFlow Studios',
        'description': '''Join our creative team as a Frontend Engineer!

Requirements:
- 3+ years with React
- TypeScript proficiency
- Responsive design knowledge
- Git workflow experience

Responsibilities:
- Build responsive web interfaces
- Optimize performance
- Collaborate with designers
- Unit testing and debugging''',
        'location': 'Remote',
        'job_type': 'FT',
        'status': 'PUBLISHED',
    },
    {
        'title': 'Data Analyst Intern',
        'company': 'DataViz Solutions',
        'description': '''Great opportunity for a data-driven individual!

Requirements:
- SQL basics
- Excel proficiency
- Analytics interest
- Python or R experience a plus

Responsibilities:
- Data analysis and reporting
- Dashboard creation
- Data cleaning
- Insights presentation''',
        'location': 'New York, NY',
        'job_type': 'INTERN',
        'status': 'PUBLISHED',
    },
    {
        'title': 'DevOps Engineer',
        'company': 'CloudScale Systems',
        'description': '''Help us scale our infrastructure!

Requirements:
- Kubernetes experience
- AWS or GCP knowledge
- CI/CD pipeline expertise
- Linux administration

Responsibilities:
- Infrastructure management
- Deployment automation
- Monitoring and logging setup
- Security implementation''',
        'location': 'Boston, MA',
        'job_type': 'FT',
        'status': 'PUBLISHED',
    },
    {
        'title': 'Part-time Content Writer',
        'company': 'Digital Marketing Pro',
        'description': '''Create engaging content for our clients!

Requirements:
- Excellent writing skills
- SEO knowledge
- Content marketing experience
- Social media familiarity

Responsibilities:
- Blog post creation
- Social content writing
- Proofreading and editing
- Content calendar management''',
        'location': 'Los Angeles, CA',
        'job_type': 'PT',
        'status': 'PUBLISHED',
    },
]

for job_data in jobs_data:
    Job.objects.create(**job_data)

print(f"✓ Created {len(jobs_data)} sample jobs successfully!")
