from django.contrib.syndication.feeds import Feed

from belleville.entry.models import Post, PostCategory

class LatestDjangoEntries(Feed):
    title = "Djangrrl.com | Django"
    link = "http://www.djangrrl.com/"
    description = "Latest posts about Django"

    def items(self):
        return Post.objects.filter(postcategory__category=3, publish=True).order_by('-created_at')[:5]

class LatestEntries(Feed):
    title = "Djangrrl"
    link = "http://www.djangrrl.com/"
    description = "Latest posts on Djangrrl"

    def items(self):
        return Post.objects.filter(publish=True).order_by('-created_at')[:5]

