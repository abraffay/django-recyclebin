from rest_framework import serializers


class RecycleSerializer(serializers.Serializer):
    model_name          = serializers.SerializerMethodField(read_only=True)
    name                = serializers.SerializerMethodField(read_only=True)
    pk                  = serializers.SerializerMethodField(read_only=True)
    deleted_by          = serializers.SerializerMethodField(read_only=True)
    deleted_at          = serializers.SerializerMethodField(read_only=True)

    def get_model_name(self, obj):
        try:
            return obj._meta.verbose_name.replace(" ", "")
        except:
            return None
    def get_name(self, obj):
        try:
            return obj.name
        except:
            return None        
    def get_pk(self, obj):
        try:
            return obj.id
        except:
            return None

    def get_deleted_by(self, obj):
        try:
            return str(obj.deleted_by)
        except:
            return None

    def get_deleted_at(self, obj):
        try:
            return obj.deleted_at
        except:
            return None