from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Post, Category, Comment, NewsletterSubscriber
from .forms import CommentForm, PostSearchForm, SearchForm
from django.db.models import Count, Prefetch
from django.utils import timezone

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_queryset(self):
        cache_key = 'published_posts'
        posts = cache.get(cache_key)
        if posts is None:
            posts = Post.objects.filter(status='published').select_related('author').prefetch_related('categories')
            cache.set(cache_key, posts, 60 * 15)  # Cache for 15 minutes
        return posts
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cache_key = 'all_categories'
        categories = cache.get(cache_key)
        if categories is None:
            categories = Category.objects.all()
            cache.set(cache_key, categories, 60 * 60)  # Cache for 1 hour
        context['categories'] = categories
        context['search_form'] = PostSearchForm()
        context['search_form'].fields['category'].queryset = categories
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    
    def get_queryset(self):
        return Post.objects.select_related('author').prefetch_related(
            Prefetch('comments', queryset=Comment.objects.filter(active=True))
        )
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.increase_views()
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        
        # Get similar posts
        post = self.object
        cache_key = f'similar_posts_{post.id}'
        similar_posts = cache.get(cache_key)
        if similar_posts is None:
            post_tags_ids = post.categories.values_list('id', flat=True)
            similar_posts = Post.objects.filter(
                categories__in=post_tags_ids,
                status='published'
            ).exclude(id=post.id).annotate(
                same_tags=Count('categories')
            ).order_by('-same_tags', '-publish')[:3]
            cache.set(cache_key, similar_posts, 60 * 60)  # Cache for 1 hour
        context['similar_posts'] = similar_posts
        
        return context

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                            slug=post,
                            status='published',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    
    # Increment view count
    post.views += 1
    post.save()
    
    # Get similar posts
    post_tags_ids = post.categories.values_list('id', flat=True)
    similar_posts = Post.published.filter(categories__in=post_tags_ids)\
                                .exclude(id=post.id)\
                                .annotate(same_tags=Count('categories'))\
                                .order_by('-same_tags', '-publish')[:3]
    
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    
    return render(request,
                 'blog/post_detail.html',
                 {'post': post,
                  'comments': comments,
                  'comment_form': comment_form,
                  'similar_posts': similar_posts})

def category_posts(request, slug):
    cache_key = f'category_{slug}_posts'
    category_data = cache.get(cache_key)
    
    if category_data is None:
        category = get_object_or_404(Category, slug=slug)
        posts = Post.objects.filter(
            categories=category,
            status='published'
        ).select_related('author').prefetch_related('categories')
        
        category_data = {
            'category': category,
            'posts': posts,
            'categories': Category.objects.all()
        }
        cache.set(cache_key, category_data, 60 * 15)  # Cache for 15 minutes
    else:
        category = category_data['category']
        posts = category_data['posts']
    
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    return render(request, 'blog/category_posts.html', {
        'category': category,
        'posts': posts,
        'categories': category_data['categories']
    })

@cache_page(60 * 15)  # Cache for 15 minutes
def post_search(request):
    form = SearchForm(request.GET)
    posts = Post.published.all()
    query = request.GET.get('query')
    category_id = request.GET.get('category')
    date_filter = request.GET.get('date')
    
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(excerpt__icontains=query)
        )
    
    if category_id:
        posts = posts.filter(categories__id=category_id)
    
    if date_filter:
        today = timezone.now().date()
        if date_filter == 'today':
            posts = posts.filter(publish__date=today)
        elif date_filter == 'week':
            posts = posts.filter(publish__date__gte=today - timezone.timedelta(days=7))
        elif date_filter == 'month':
            posts = posts.filter(publish__date__gte=today - timezone.timedelta(days=30))
        elif date_filter == 'year':
            posts = posts.filter(publish__date__gte=today - timezone.timedelta(days=365))
    
    # Annotate categories with post count
    categories = Category.objects.annotate(post_count=Count('post'))
    
    # Pagination
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    context = {
        'posts': posts,
        'categories': categories,
        'search_form': form,
        'query': query,
        'category_id': category_id,
        'date_filter': date_filter,
    }
    
    return render(request, 'blog/post_list.html', context)

def newsletter_subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            subscriber, created = NewsletterSubscriber.objects.get_or_create(
                email=email,
                defaults={'is_active': True}
            )
            if created:
                messages.success(request, 'Thank you for subscribing to our newsletter!')
            else:
                if not subscriber.is_active:
                    subscriber.is_active = True
                    subscriber.save()
                    messages.success(request, 'Welcome back! You have been resubscribed to our newsletter.')
                else:
                    messages.info(request, 'You are already subscribed to our newsletter.')
        except Exception as e:
            messages.error(request, 'An error occurred. Please try again later.')
            # Log the error for debugging
            print(f"Newsletter subscription error: {str(e)}")
        
        return redirect(request.META.get('HTTP_REFERER', '/'))
