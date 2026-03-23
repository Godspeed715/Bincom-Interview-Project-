from django.shortcuts import render, get_object_or_404, redirect
from .models import Video

# Create your views here.
def videos_list(request):
    return redirect(videos, page_no=1)

def videos(request, page_no):
    page_count = Video.objects.all().count()
    prev_id = page_no - 1 if page_no > 0 else None
    next_id = page_no + 1 if page_no < page_count else None
    video = get_object_or_404(Video, page_no=page_no)
    print(video.src)
    return render(request,'videos.html', context={'video':video, 'prev_id':prev_id, 'next_id':next_id})