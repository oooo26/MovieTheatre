from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import timedelta
from .models import Author, Movie, Grade
from .forms import SubscribeForm


# Create your views here.


class IndexView(generic.TemplateView):
    model = Author
    template_name = "about/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["authors"] = Author.objects.all()
        return context


class MovieView(generic.ListView):
    model = Movie
    template_name = "about/movie1.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["movies"] = Movie.objects.order_by("-release_date")
        return context


def add_movie_from_link(gv_link):
    try:
        from pyquery import PyQuery as pq
        from selenium.webdriver import Chrome, ChromeOptions
    except ImportError as e:
        # TODO: error msg?
        return

    opt = ChromeOptions()
    opt.headless = True
    browser = Chrome(options=opt)
    browser.get(gv_link)
    doc = pq(browser.page_source)

    name = doc("meta[property='og:title']").attr("content")
    poster_url = doc("meta[property='og:image']").attr("content")
    duration = int(
        doc("div[ng-show='filminfo.duration>0']").text().split()[-2])
    release_date = doc(
        "p[ng-bind-html='filminfo.formattedReleaseDate']").text()
    grade = doc("small[ng-show]:first-child").text().split()[0][1:]

    grade_id = Grade.objects.filter(level=grade)[0].id
    release_date = release_date[-4:] + release_date[2:-4] + release_date[:2]

    if not name or not poster_url or duration<=0 or not release_date or not grade_id:
        return True


    existing_movies = Movie.objects.values('name')
    existing_movies_names = [list(i.values())[0] for i in existing_movies]
    if name in existing_movies_names:
        return False
    else:
        movie = Movie(
            name=name,
            poster_url=poster_url,
            duration=timedelta(minutes=duration),
            release_date=release_date,
            grade_id=grade_id,
            purchase_url=gv_link
        )
        movie.save()
        return True



def subscribe_movie(request, sub_type):
    if request.method == "POST":
        if sub_type == 1:
            form = SubscribeForm(request.POST)
            if form.is_valid():
                form.instance.duration *= 60
                existing_movies = Movie.objects.values('name')
                existing_movies_names = [list(i.values())[0] for i in existing_movies]
                if form.instance.name in existing_movies_names:
                    from django.contrib import messages
                    messages.error(request, 'The movie already exists')
                    return HttpResponseRedirect(reverse('about:subscribe', args=(sub_type,)))
                else:
                    form.save()
                return HttpResponseRedirect(
                    reverse("about:subscribe", args=(sub_type,)))
        elif sub_type == 2:
            gv_link = request.POST.get("gv_link")
            result = add_movie_from_link(gv_link)
            if not result:
                from django.contrib import messages
                messages.error(request, 'The movie already exists')
            return HttpResponseRedirect(
                reverse("about:subscribe", args=(sub_type,)))

    else:
        form = SubscribeForm()
    return render(request, "about/sub.html", {"form": form})


def unsubscribe_movie(request, pk):
    if request.method == "POST":
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
    context = {
        "movies": Movie.objects.order_by("-release_date")
    }
    return HttpResponseRedirect(reverse('about:movie'))
