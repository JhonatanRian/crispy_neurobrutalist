from django.apps import AppConfig


class CrispyNeurobrutalistConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "crispy_neurobrutalist"
    verbose_name = "Crispy Neurobrutalist"

    def ready(self):
        from django.conf import settings

        if "crispy_forms" not in settings.INSTALLED_APPS:
            import warnings

            warnings.warn(
                "crispy_neurobrutalist requires 'crispy_forms' to be in INSTALLED_APPS. "
                "Please add 'crispy_forms' before 'crispy_neurobrutalist' in your INSTALLED_APPS.",
                UserWarning,
                stacklevel=2,
            )

        template_pack = getattr(settings, "CRISPY_TEMPLATE_PACK", None)
        if template_pack != "neobrutalist":
            import warnings

            warnings.warn(
                "To use crispy_neurobrutalist, set CRISPY_TEMPLATE_PACK = 'neobrutalist' "
                "in your Django settings.",
                UserWarning,
                stacklevel=2,
            )
