from django.db.models import (
    Model,
    CharField,
    TextField,
)

class JobPosting(Model):
    title = TextField(null=True, blank=True)
    description = TextField(null=True, blank=True)

    def __str__(self):
        return self.title