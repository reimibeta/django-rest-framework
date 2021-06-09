class KeyRelatedField:

    def related_field(self, write_only=True):
        return serializers.PrimaryKeyRelatedField(
            queryset=Product.objects.filter(
                is_active=True
            ),
            write_only=write_only
        )


key_related_field = KeyRelatedField()
