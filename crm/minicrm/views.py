from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from minicrm.models import Agent, User, Contact, Message, File
from minicrm.forms import MyUserCreationForm, ContactCreationForm
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def show_logged_in_user(request):
    current_user = request.user
    print(current_user.id)
    print(current_user.username)

def get_logged_in_user(request):
    return request.user


class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = MyUserCreationForm

    def get_success_url(self):
        return reverse('login')

class LandingPageView(TemplateView):
    template_name = 'minicrm/landingpage.html'

class IndexPageView(TemplateView):
    template_name = 'minicrm/index.html'

def login(request):
    if request.method == 'post':
        request.session['agent'] = Agent.objects.get(user = get_logged_in_user(request).pk).pk
    print(request.session['agent'])
    return render(request, 'minicrm/login.html')

def sidebartest(request):
    return render(request, 'minicrm/sidebar.html')

class AgentListView(LoginRequiredMixin, ListView):
    login_url ='/login/'
    redirect_field_name = '/'

    model = Agent

class AgentCreate(LoginRequiredMixin, CreateView):
    model = Agent
    fields ='__all__'
    
    def get_success_url(self):
        return reverse('agents')
    
class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    redirect_field_name = '/'

class ContactCreateView(LoginRequiredMixin, CreateView):
    template_name = 'minicrm/contact_create.html'
    form_class = ContactCreationForm
        
    def get_success_url(self):
        return reverse('minicrm:contacts')

    def form_valid(self, form):
        user = self.request.user
        form.instance.agent = Agent.objects.get(user = user)
        return super(ContactCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ContactCreateView, self).get_context_data(*args,**kwargs)
        currentuser = self.request.user
        context['agent'] = Agent.objects.get(user = currentuser.pk)
        return context
    
class ContactDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'contact'
    model = Contact
    template_name = 'minicrm/contact_detail.html'
   
class ContactUpdateView(LoginRequiredMixin, UpdateView):
    context_object_name = 'contact'
    model = Contact
    template_name = 'minicrm/contact_update.html'
    fields = '__all__'


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    redirect_field_name = '/'

class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    redirect_field_name = '/'

class MessageUpdateView(LoginRequiredMixin, UpdateView):
    context_object_name = 'message'
    model = Message
    template_name = 'minicrm/message_update.html'
    fields = '__all__'

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    template_name = 'minicrm/message_create.html'
    fields = '__all__'

# class FileCreateView(CreateView):
#     model = Agent
#     fields = '__all__'

# class FileListView(ListView):
#     model = File

class AgentDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'agent'
    model = Agent
    template_name = 'minicrm/agent_detail.html'

class UserListView(LoginRequiredMixin, ListView):
    login_url ='/login/'
    redirect_field_name = '/'
    model = User

class UserDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'user'
    model = User
    template_name = 'minicrm/user_detail.html'
