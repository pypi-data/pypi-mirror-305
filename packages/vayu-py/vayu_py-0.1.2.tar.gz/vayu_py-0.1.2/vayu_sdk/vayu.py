from vayu_sdk.apis.api_webhooks import WebhooksAPI
from .clients.vayu_client import VayuClient
from .apis.api_contracts import ContractsAPI
from .apis.api_customers import CustomersAPI
from .apis.api_events import EventsAPI
from .apis.api_invoices import InvoicesAPI
from .apis.api_meters import MetersAPI
from .apis.api_plans import PlansAPI

class Vayu:
    __api_key: str = None
    __host: str = None
    __client: VayuClient = None

    def __init__(self, api_key: str, host: str = None):
        self.__client = None
        self.__host = host
        self.__api_key = api_key

    @property
    def contracts(self) -> ContractsAPI:
        return ContractsAPI(self.__client)

    @property
    def customers(self) -> CustomersAPI:
        return CustomersAPI(self.__client)

    @property
    def events(self) -> EventsAPI:
        return EventsAPI(self.__client)

    @property
    def invoices(self) -> InvoicesAPI:
        return InvoicesAPI(self.__client)

    @property
    def meters(self) -> MetersAPI:
        return MetersAPI(self.__client)

    @property
    def plans(self) -> PlansAPI:
        return PlansAPI(self.__client)
    
    @property
    def webhooks(self) -> WebhooksAPI:
        return WebhooksAPI(self.__client)
    
    def login(self):
        self.__client = VayuClient(self.__api_key, self.__host)
        self.__client.login()
