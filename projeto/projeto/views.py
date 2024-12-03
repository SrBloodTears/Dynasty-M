from django.conf import settings
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class Login(View):
    """
    Class Based View para autenticação de usúarios.
    """

    def get(self, request):
        contexto = {'mensagem': ''}
        if request.user.is_authenticated:
            return redirect("/persona")
        else:
         return render(request, 'autenticacao.html', contexto)
    
    def post(self, request):

        # obtém as credenciais de autenticação do formulário

        usuario = request.POST.get('usuario', None)
        senha = request.POST.get('senha', None)

        # Verifica as credenciais de autenticação fornecidas
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:

            # Verifica se o usuario ainda está ativo no sistema
            if user.is_active:
                login(request, user)
                return redirect("/persona")
            
            return render(request, 'autenticacao.html', {'mensagem': 'Usuário inativos.'})
        
        return render(request, 'autenticacao.html', {'mensagem': 'Usuário ou senha inválidos'})
    
class Logout(View):
    """
    Class Based View para realizar logout de usuários.
    """

    def get(self, request):
        logout(request)
        return redirect(settings.LOGIN_URL)

class LoginAPI(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={
                'request': request
            }
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'id': user.id,
            'nome': user.first_name,
            'email': user.email,
            'token': token.key
        })