import logging

from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth import login, logout

from profiles.models import Profile
from traugott.views import Rest

logger = logging.getLogger('app')


class ProfileResource(Rest):

    def get(self, request, profile_id=None):
        if profile_id:
            try:
                profile = Profile.objects.get(pk=profile_id)
                return self.response({'status': 200,
                                      'message': 'OK',
                                      'data': profile.as_dict()})
            except Profile.DoesNotExist:
                return self.response({'status': 404,
                                      'message': 'Profile #%s not found' % profile_id})
            except Exception as e:
                return self.response({'status': 500,
                                      'message': e.message})
        elif request.user.is_authenticated:
            return self.response({'status': 200,
                                  'data': request.user.profile.as_dict()})
        return self.response({'status': 403,
                              'message': 'Invalid profile id or not loggined'})

    def post(self, request):
        if request.user.is_authenticated:
            return self.response({'status': 205,
                                  'message': 'Already loggined'})
        try:
            profile = Profile.get_or_create(request.POST.get('email'),
                                            request.POST.get('password'))
            if not profile:
                return JsonResponse({'status': 401,
                                     'message': 'Invalid password'}, status=401)
            login(request, profile.user)
        except Exception as e:
            return self.response({'status': 500, 'message': e.message})
        return self.response({'status': 200, 'message': 'OK'})

    def delete(self, request):
        logout(request)
        return self.response({'status': 200, 'message': 'OK'})