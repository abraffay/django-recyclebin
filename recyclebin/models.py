from django.db import models
from django.db.models import Manager
from .utils import get_current_request
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

class SoftDeleteManager(models.QuerySet):
    def get(self, **kwargs):
        return super().get(**kwargs,deleted=False)
    def all(self):
        return super().all().filter(deleted=False)

    def get_query_set(self, *args ,**kwargs):
        return super().get_query_set().filter(deleted=False)






class SoftDeleteMixin(models.Model):
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey(User, related_name='%(class)s_requests_created', on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        abstract=True

    objects = SoftDeleteManager.as_manager()
    recycler = Manager()

    def delete(self):
        request = get_current_request()
        self.deleted_at = timezone.now()
        try:
            self.deleted_by = request.user
        except:
            pass
        self.deleted=True
        self.save()

    def permdelete(self):
        return super().delete()
