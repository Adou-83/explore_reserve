from .models import Publicite

def publicites_context(request):
    publicites = Publicite.objects.filter(actif=True)
    return {'publicites': publicites}
