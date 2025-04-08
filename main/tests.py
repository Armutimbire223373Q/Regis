from django.test import TestCase, Client
from django.urls import reverse
from .models import (
    AboutPage, AcademicsPage, CurriculumPage,
    StudentLifePage, ContactPage, FAQ
)

class MainAppTests(TestCase):
    def setUp(self):
        """Set up test data."""
        self.client = Client()
        
        # Create test pages
        self.about_page = AboutPage.objects.create(
            title="About Us",
            content="Test content",
            mission_statement="Test mission",
            vision_statement="Test vision",
            values="Test values",
            history="Test history"
        )
        
        self.academics_page = AcademicsPage.objects.create(
            title="Academics",
            content="Test content",
            programs_overview="Test programs",
            curriculum_overview="Test curriculum",
            faculty_highlight="Test faculty"
        )
        
        self.curriculum_page = CurriculumPage.objects.create(
            title="Grade 1 Curriculum",
            content="Test content",
            grade_level="Grade 1",
            subjects="Test subjects",
            learning_outcomes="Test outcomes"
        )
        
        self.student_life_page = StudentLifePage.objects.create(
            title="Student Life",
            content="Test content",
            activities="Test activities",
            clubs="Test clubs",
            sports="Test sports"
        )
        
        self.contact_page = ContactPage.objects.create(
            title="Contact Us",
            content="Test content",
            address="Test address",
            phone="1234567890",
            email="test@example.com",
            office_hours="9-5"
        )
        
        self.faq = FAQ.objects.create(
            question="Test Question?",
            answer="Test Answer",
            category="General"
        )

    def test_about_page_view(self):
        """Test about page view."""
        response = self.client.get(reverse('main:about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.about_page.title)

    def test_academics_page_view(self):
        """Test academics page view."""
        response = self.client.get(reverse('main:academics'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.academics_page.title)

    def test_curriculum_page_view(self):
        """Test curriculum page view."""
        response = self.client.get(reverse('main:curriculum'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.curriculum_page.title)

    def test_student_life_page_view(self):
        """Test student life page view."""
        response = self.client.get(reverse('main:student_life'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.student_life_page.title)

    def test_contact_page_view(self):
        """Test contact page view."""
        response = self.client.get(reverse('main:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.contact_page.title)

    def test_parents_page_view(self):
        """Test parents page view."""
        response = self.client.get(reverse('main:parents'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.faq.question)

    def test_home_page_view(self):
        """Test home page view."""
        response = self.client.get(reverse('main:home'))
        self.assertEqual(response.status_code, 200)

    def test_page_model_str(self):
        """Test page model string representation."""
        self.assertEqual(str(self.about_page), self.about_page.title)
        self.assertEqual(str(self.academics_page), self.academics_page.title)
        self.assertEqual(str(self.curriculum_page), f"{self.curriculum_page.title} - {self.curriculum_page.grade_level}")
        self.assertEqual(str(self.student_life_page), self.student_life_page.title)
        self.assertEqual(str(self.contact_page), self.contact_page.title)

    def test_faq_model_str(self):
        """Test FAQ model string representation."""
        self.assertEqual(str(self.faq), self.faq.question)
