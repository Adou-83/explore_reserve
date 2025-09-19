from .models import Publicite

def publicites_context(request):
    return {
        'publicites': Publicite.objects.filter(actif=True)
    }
