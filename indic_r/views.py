from django.shortcuts import render, get_object_or_404, redirect
from .models import Competition, Workshop, Talk, Proshow, SocialInitiative, EntityComment,Sponsor
from .forms import EntityCommentForm

def home(request):
    competitions = Competition.objects.all()
    workshops = Workshop.objects.all()
    talks = Talk.objects.all()
    proshows = Proshow.objects.all()[:4]
    social_initiatives = SocialInitiative.objects.all()
    sponsor = Sponsor.objects.all()
    context = {
        'competitions': competitions,
        'workshops': workshops,
        'talks': talks,
        'proshows': proshows,
        'social_initiatives': social_initiatives,
        'sponsor':sponsor,
    }
    return render(request, 'indic_r/home.html', context)

def competition_detail(request, pk):
    competition = get_object_or_404(Competition, pk=pk)
    comp = Competition.objects.all()
    comments = competition.entitycomment_set.all()
    form = EntityCommentForm()
    if request.method == 'POST':
        form = EntityCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.competition = competition
            comment.save()
            return redirect('competition_detail', pk=competition.pk)
    context = {
        'entity': competition,
        'comments': comments,
        'form': form,
        'comp':comp,
    }
    return render(request, 'indic_r/competition_detail.html', context)

def workshop_detail(request, pk):
    workshop = get_object_or_404(Workshop, pk=pk)
    comments = workshop.entitycomment_set.all()
    comp = Workshop.objects.all()
    form = EntityCommentForm()
    if request.method == 'POST':
        form = EntityCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.workshop = workshop
            comment.save()
            return redirect('workshop_detail', pk=workshop.pk)
    context = {
        'entity': workshop,
        'comments': comments,
        'form': form,
        'comp':comp,
    }
    return render(request, 'indic_r/workshop_detail.html', context)

def talk_detail(request, pk):
    talk = get_object_or_404(Talk, pk=pk)
    comments = talk.entitycomment_set.all()
    form = EntityCommentForm()
    comp = Talk.objects.all()
    if request.method == 'POST':
        form = EntityCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.talk = talk
            comment.save()
            return redirect('talk_detail', pk=talk.pk)
    context = {
        'entity': talk,
        'comments': comments,
        'form': form,
        'comp':comp,
    }
    return render(request, 'indic_r/talk_detail.html', context)

def proshow_detail(request, pk):
    proshow = get_object_or_404(Proshow, pk=pk)
    comments = proshow.entitycomment_set.all()
    comp = Proshow.objects.all()
    form = EntityCommentForm()
    if request.method == 'POST':
        form = EntityCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.proshow = proshow
            comment.save()
            return redirect('proshow_detail', pk=proshow.pk)
    context = {
        'entity': proshow,
        'comments': comments,
        'comp':comp,
        'form': form,
    }
    return render(request, 'indic_r/proshow_detail.html', context)

def social_initiative_detail(request, pk):
    social_initiative = get_object_or_404(SocialInitiative, pk=pk)
    comments = social_initiative.entitycomment_set.all()
    comp = SocialInitiative.objects.all()
    form = EntityCommentForm()
    if request.method == 'POST':
        form = EntityCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.social_initiative = social_initiative
            comment.save()
            return redirect('social_initiative_detail', pk=social_initiative.pk)
    context = {
        'entity': social_initiative,
        'comments': comments,
        'form': form,
        'comp':comp,
    }
    return render(request, 'indic_r/social_initiative_detail.html', context)
