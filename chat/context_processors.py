from .forms import ApiKeyForm

def api_key_form(request):
    form = ApiKeyForm()
    return {'api_key_form': form}