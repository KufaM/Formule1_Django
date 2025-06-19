from django.shortcuts import render, get_object_or_404, redirect
from .models import Driver, Team, Track
from .forms import TrackForm

def index(request):
    return render(request, 'html/index.html')

def driver_list_grouped(request):
    teams = Team.objects.prefetch_related('driver_set').all()
    data = []
    for team in teams:
        drivers = list(team.driver_set.all())
        if drivers:
            data.append({'team': team, 'drivers': drivers})
    return render(request, 'html/driver_list_grouped.html', {'data': data})

def driver_detail(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    return render(request, 'html/driver_detail.html', {'driver': driver})


def team_list(request):
    teams = Team.objects.all()
    return render(request, 'html/teams.html', {'teams': teams})

def track_list(request):
    tracks = Track.objects.all()
    return render(request, 'html/tracks.html', {'tracks': tracks})

def track_create(request):
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('track_list')
    else:
        form = TrackForm()
    return render(request, 'html/track_form.html', {'form': form})

def track_edit(request, pk):
    track = get_object_or_404(Track, pk=pk)
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES, instance=track)
        if form.is_valid():
            form.save()
            return redirect('track_list')
    else:
        form = TrackForm(instance=track)
    return render(request, 'html/track_form.html', {'form': form})

def track_delete(request, pk):
    track = get_object_or_404(Track, pk=pk)
    if request.method == 'POST':
        track.delete()
        return redirect('track_list')
    return render(request, 'html/track_confirm_delete.html', {'track': track})
