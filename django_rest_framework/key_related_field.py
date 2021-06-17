from rest_framework import serializers


class KeyRelatedField:

    def related_field(self, queryset, write_only=True):
        return serializers.PrimaryKeyRelatedField(
            queryset=queryset,
            write_only=write_only
        )


key_related_field = KeyRelatedField()
