from django.contrib.contenttypes.models import ContentType
from .serializers import RecycleSerializer




def get_deleted_items(models):
    qs_li = []
    for model in models:
        qs = model.objects.filter(deleted=True).order_by('deleted_at')
        qs_li.append(qs)
    serializer = RecycleSerializer(qs_li, many=True)
    return serializer.data



def restore(model, id):
    ct = ContentType.objects.get(model=model)
    model = ct.model_class()
    model.recycler.filter(pk=id).update(deleted=False)



def permanent_delete(model, id):
    ct = ContentType.objects.get(model=model)
    model = ct.model_class()
    obj = model.recycler.get(pk=id)
    obj.permdelete()

