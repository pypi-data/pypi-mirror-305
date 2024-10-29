from django.db.models import CharField
import secrets
from django.db.models import Field

class CustomPrefixUUID(CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 100
        super(CustomPrefixUUID, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = super(CustomPrefixUUID, self).pre_save(model_instance, add)
        if not value:
            self.prefix = getattr(model_instance, "prefix", None)
            if self.prefix is None:
                self.prefix = "base"
            value = self.prefix +"_"+ str(secrets.token_hex(16))
            setattr(model_instance, self.attname, value)
            return value
        else:
            return value

class ListField(Field):
    def __init__(self, seperator=",", *args, **kwargs):
        kwargs['max_length'] = 36
        self.separator = seperator
        super(ListField, self).__init__(*args, **kwargs)

    def from_db_value(self, value, *args):
        if not value:
            return []
        return value.split(self.separator)

    def to_python(self, value):
        if not value:
            return []
        if isinstance(value, list):
            return value
        return value.split(self.separator)
    
    def get_prep_value(self, value):
        if not value:
            return None
        return self.separator.join(value)

    def db_type(self, connection):
        return 'varchar(255)'

    def value_from_object(self, obj):
        test = (super().value_from_object(obj))
        return test

    def pre_save(self, model_instance, add):
        value = super(ListField, self).pre_save(model_instance, add)
        if not value:
            value = []
            setattr(model_instance, self.attname, value)
            return value
        else:
            return value
