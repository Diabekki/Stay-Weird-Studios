from django.apps import AppConfig


class CartCheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cart_checkout'

    def ready(self):
        import cart_checkout.signals