from django.core.management.base import BaseCommand
from django.utils import timezone
from blog.models import Post
from django.core.mail import send_mail
from django.conf import settings

class Command(BaseCommand):
    help = 'Publishes scheduled blog posts'

    def handle(self, *args, **options):
        now = timezone.now()
        scheduled_posts = Post.objects.filter(
            status='scheduled',
            scheduled_publish__lte=now
        )
        
        for post in scheduled_posts:
            post.status = 'published'
            post.publish = post.scheduled_publish
            post.save()
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully published scheduled post: {post.title}')
            )
            
            # Notify subscribers about the new post
            try:
                send_mail(
                    f'New Blog Post: {post.title}',
                    f'A new blog post has been published: {post.title}\n\n'
                    f'Read it here: {post.get_absolute_url()}',
                    settings.DEFAULT_FROM_EMAIL,
                    [subscriber.email for subscriber in post.newsletter_subscribers.filter(is_active=True)],
                    fail_silently=True,
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error sending notifications for post {post.title}: {str(e)}')
                ) 