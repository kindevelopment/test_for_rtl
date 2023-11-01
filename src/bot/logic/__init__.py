from .help import help_router
from .start import start_router
from .payments import payment_router

routers = (start_router, help_router, payment_router)
