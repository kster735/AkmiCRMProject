from django.urls import path
from minicrm.views import (sidebartest, AgentListView,
 AgentDetailView, ContactListView, AgentCreate,
   MessageListView, MessageCreateView, MessageDetailView, MessageUpdateView, IndexPageView, ContactDetailView, 
   ContactCreateView, UserListView, UserDetailView, ContactUpdateView)

app_name = 'minicrm'

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('agents/', AgentListView.as_view(), name='agents'),
    path('detail_agent/<int:pk>', AgentDetailView.as_view(), name='detail_agent'),
    path('agents/create', AgentCreate.as_view(), name='create_agent'),
    path('contacts/', ContactListView.as_view(), name='contacts'),
    path('detail_contact/<int:pk>', ContactDetailView.as_view(), name='detail_contact'),
    path('create_contact/', ContactCreateView.as_view(), name='create_contact'),
    path('update_contact/<int:pk>', ContactUpdateView.as_view(), name='update_contact'),
    path('create_message/', MessageCreateView.as_view(), name='create_message'),
    path('messages/', MessageListView.as_view(), name='messages'),
    path('detail_message/<int:pk>', MessageDetailView.as_view(), name='detail_message'),
    path('update_message/<int:pk>', MessageUpdateView.as_view(), name='update_message'),
    path('users/', UserListView.as_view(), name='users'),
    path('detail_user/<int:pk>', UserDetailView.as_view(), name='detail_user'),
    path('sidebartest/', sidebartest, name='sidebartest'),
]
