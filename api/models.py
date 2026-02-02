from django.db import models


class Resume(models.Model):
    """Basic resume representation for CV matching."""

    candidate_name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField(help_text="Raw text of the CV / resume")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.candidate_name} <{self.email}>"

