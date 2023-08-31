import openai, re
import environ
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib import auth, messages
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm
from .models import Chat, Message
from django.utils import timezone
from django.views.generic import ListView, DetailView
from .forms import ApiKeyForm
from django.conf import settings

env = environ.Env()
environ.Env.read_env()

def save_api_key(request, chat_slug):
    chat = get_object_or_404(Chat, user=request.user, slug=chat_slug)
    if request.method == "POST":
        form = ApiKeyForm(request.POST)
        if form.is_valid():
            api_key = form.cleaned_data["api_key"]
            env_file = settings.BASE_DIR / 'chatbot'/'.env'
            try:
                with open(env_file, 'r') as fp:
                    while True:
                        cur_line = fp.readline()
                        if cur_line == 'API_KEY=':
                            with open(env_file, 'a') as file:
                                file.write(api_key)
                            break
            except Exception as e:
                print(f"Error while saving API key: {e}")
            return redirect("chat:chat", chat_slug=chat.slug)  
    else:
        form = ApiKeyForm()

    return render(request, "sidebar.html.html", {"form": form})


openai.api_key = env('API_KEY')

def welcome(request):
    return render(request, 'welcome.html')



def chat_openai(message):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a rogue assistant."},
            {"role": "user", "content": message},
        ]
    )
    answer = response.choices[0].message.content.strip()
    #return answer
    parsed_text = re.sub(r'```(.*?)```', r'<code>\1</code>', answer, flags=re.DOTALL)
    return parsed_text


def process_user_message(message):
    response = chat_openai(message)
    return response


class ChatListView(ListView):
    model = Chat
    template_name='index.html'
    context_object_name = 'chats'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chat_history = []

        for chat in context['chats']:
            recent_message = chat.get_most_recent_message()
            if recent_message:
                chat_history.append(recent_message)

        context['chat_history'] = chat_history
        context['board'] = Chat.objects.filter(user=self.request.user).order_by('-created_at')
        return context
 
 
class ChatDetailView(DetailView):
    model = Chat
    template_name='chat_detail.html'
    
    def get_object(self):
        chat_slug = self.kwargs['chat_slug']
        chat = get_object_or_404(Chat, slug=chat_slug)
        return chat
    
    def post(self, request, *args, **kwargs):
        chat = self.get_object()
        message = request.POST.get('message')  # Assuming your form field is named 'message'
        if message:
            response = process_user_message(message)
            message = Message(chat=chat, message=message, response=response)
            message.save()
            #return JsonResponse({'message': message, 'response': response})
        return redirect('chat:chat', chat_slug=chat.slug)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board'] = Chat.objects.filter(user=self.request.user).order_by('-created_at')
        context['messages'] = Message.objects.filter(chat=self.object)
        return context
    
    
def send_message(request, chat_slug):
    chat = get_object_or_404(Chat, slug=chat_slug, user=request.user)
    
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            response = process_user_message(message)
            message = Message(chat=chat, message=message, response=response, created_at=timezone.now())
            message.save()
            response_data = {
                'response': response,
                'created_at': message.created_at.strftime('%Y-%m-%d %H:%M:%S')  # Format the timestamp
            }
            
            return JsonResponse(response_data)
    return JsonResponse({'error': 'Invalid request'})#return redirect('chat:chat', chat_id=chat_id)

	
def new_chat(request):
    chat = Chat.objects.create(user=request.user)
    return redirect('chat:chat', chat_slug=chat.slug)


def delete_chat(request, chat_slug):
    chat = get_object_or_404(Chat, slug=chat_slug, user=request.user)
    chat.delete_with_messages()
    chats=Chat.objects.filter(user=request.user).all()
    for item in chats:
        if item != None:
            redir_chat =chats[0] 
            return redirect('chat:chat', chat_slug=redir_chat.slug)
        
    new_chat = Chat.objects.create(user=request.user)
    return redirect('chat:chat', chat_slug=new_chat.slug)
    
def login(request):
    form = LoginForm(request.POST)

    if request.method == 'POST':    
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            existing_chats = Chat.objects.filter(user=user)
            if existing_chats.exists():
                chat = Chat.objects.first()#get_object_or_404(Chat, user=request.user)
                return redirect('chat:chat', chat_slug=chat.slug)
            else:
                chat = Chat.objects.create(user=request.user)
                return redirect('chat:chat', chat_slug=chat.slug)
        else:
            error_message = 'Invalid Username or Password'
            context={
                'error_message' : error_message,
                'form' : form,
            }
            return render(request, 'login.html', context)
    else:
        context = {
            'form' : form,
        }
        return render(request, 'login.html', context)



def logout(request):
    auth.logout(request)
    message = 'You have logged out of your account!'

    return render(request, 'logout.html', {'message': message})


def signup(request):
    form = RegisterForm(request.POST)

    if request.method == 'POST':
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                messages.success(request, 'Sign in successful!')
                existing_chats = Chat.objects.filter(user=user)
                if existing_chats.exists():
                    return redirect('chat:index')
                else:
                    chat = Chat.objects.create(user=request.user)
                    return redirect('chat:chat', chat_slug=chat.slug)
                    #return redirect('chat:index' )
            except:
                error_message = 'Error creating account!!'
                context = {
                    'form' : form,
                    'error_message' : error_message,
                }
                return render(request, 'signup.html', context)
        else:
            error_message = 'Passwords do not match'
            context = {
                'form' : form,
                'error_message' : error_message,
            }
            return render(request, 'signup.html', context)
        
    context = {
        'form' : form,
    }
    return render(request, 'signup.html', context)