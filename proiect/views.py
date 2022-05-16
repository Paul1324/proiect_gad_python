from msilib.schema import ListView
from django.shortcuts import render
from requests import request
from . import get_page
from .get_page import Profile as PROFILE
from .get_page import Repo as REPO
import sys
from .models import Profile, Repo
from .svd import RegisterProfile
# Create your views here.
# view that uses get_page to return an user profile


def search_view(request):
    all_profiles = Profile.objects.all()
    all_repos = Repo.objects.all()
    if request.method == 'GET':
        return render(request, 'search.html', {'profiles': all_profiles, 'search_placeholder' : "github username"})
    else:
        username = request.POST.get('search')
        if username:
            username = username.strip()
            profile = get_page.get_page(username)
            if(profile != None):
                return render(request, 'profile.html', {'profile': profile, 'from_db': False, 'from_save': False})
            else:
                return render(request, 'search.html', {'profiles': all_profiles, 'search_placeholder' : "profile not found"})
        else:
            username = request.POST.get('go_to_profile')
            if username:
                profile_db = all_profiles.filter(username=username)[0]
                profile_id = profile_db.id
                repos_db = all_repos.filter(profile_id=profile_id)
                repos_list = []
                for rep in repos_db:
                    aux = REPO(rep.name, rep.url,
                               rep.language, rep.description)
                    repos_list.append(aux)
                profile = PROFILE(profile_db.image, profile_db.fullname, profile_db.username,
                                  profile_db.bio, profile_db.followers, profile_db.following, repos_list)
                if(profile != None):
                    return render(request, 'profile.html', {'profile': profile, 'from_db': True, 'from_save': False})
            else:
                username = request.POST.get('save_profile')
                if username:
                    try: 
                        all_profiles.get(username=username)
                    except:
                        profile = get_page.get_page(username)

                        if profile:
                            reg_prof = Profile(image=profile.image, fullname=profile.fullname, username=profile.username,
                                            bio=profile.bio, followers=profile.followers, following=profile.following)
                            reg_prof.save()
                            prof_db = all_profiles.filter(username=username)[0]
                            prof_id = prof_db.id
                            for i in profile.public_repos:
                                repo = Repo(name=i.name, url=i.url, language=i.language,
                                            description=i.description, profile_id=prof_id)
                                repo.save()
                else:
                    username = request.POST.get('delete_profile')
                    if username:
                        all_profiles.filter(username=username).delete()
        return render(request, 'search.html', {'profiles': all_profiles, 'search_placeholder' : "github username"})
