
from django.urls import path

# Views 
from .views import (
    # !User - Player - FieldAdmin
    UserPlayerCreateAPIView,
    UserRetriveAPIView,
    UserPartialUpdateAPIView,
    IdRetriveAuthToken,
    PlayerPositionListAPIView,
    UserOrganizedMatchesAPIView,
    UserFielAdminCreateAPIView,

    # !Match
    MatchListAPIView,
    MatchCreationAPIView,
    MatchPlayerRetriveUpdateAPIView,

    # !Field
    FieldListAPIView,
    FieldRetriveAPIView,
)

urlpatterns = [
    # !User
    path('login/', IdRetriveAuthToken.as_view(), name='login'),
    path('signup_player/', UserPlayerCreateAPIView.as_view(), name='signup_player'),
    path('signup_fieldadmin/', UserFielAdminCreateAPIView.as_view(), name='signup_fieldadmin'),

    # !Player
    path('players/<int:pk>/', UserRetriveAPIView.as_view(), name='player' ),
    path('players/update/<int:pk>/', UserPartialUpdateAPIView.as_view(), name='player_update'),
    path('players/position/', PlayerPositionListAPIView.as_view(), name='player_list_position'),
    path('players/organized/<int:pk>/',UserOrganizedMatchesAPIView.as_view(), name='player_organized_list'),

    # !Match
   path('matches/', MatchListAPIView.as_view(), name='match' ),
   path('matches/create/', MatchCreationAPIView.as_view(), name='match_create'),
   path('matches/<int:pk>/',MatchPlayerRetriveUpdateAPIView.as_view(), name='match_retrive'),

   # !Field
   path('fields/', FieldListAPIView.as_view(), name='field_list'),
   path('fields/<int:pk>/', FieldRetriveAPIView.as_view(), name='field_retrive')
]