# from .errors import dp
from .users import dp
# from .event.events import dp
# from .event.events_callback import dp
# from .event.events_add import dp
from .accident.accident import dp
from .accident.acident_add import dp
from .accident.accident_callback import dp
from .nlp.nlp import dp

# from .order.order_add import dp
# from .order.order_remove import dp
# from .order.orders import dp
# from .order.order_callback import dp
__all__ = ["dp"]
