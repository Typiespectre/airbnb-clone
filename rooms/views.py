# from django.core.paginator import Paginator, EmptyPage
# from django.shortcuts import render, redirect
# from django.urls import reverse
# from django.http import Http404
from django.views.generic import ListView, DetailView
from django.utils import timezone
from . import models

"""
# vanilla paginator
def all_rooms(request):
    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]
    page_count = models.Room.objects.count() // page_size
    return render(
        request,
        "rooms/home.html",
        context={
            "rooms": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count),
        },
    )
"""

"""
# using django paginator
def all_rooms(request):
    page = request.GET.get("page")
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.get_page(page)
        return render(request, "rooms/home.html", {"page": rooms})
    except EmptyPage:
        return redirect("/")
        # 한꺼번에 Exception 처리하는 것보단 각 오류에 맞는 대응을 하는 것이 더 좋다.
"""


# using class based views
# using ListView abstraction / 참고: ccbv.com
class HomeView(ListView):

    """ homeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


"""
def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        raise Http404()
"""


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room
