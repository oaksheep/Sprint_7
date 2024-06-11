import allure
import requests
from endpoints import Endpoints
from urls import Urls


class TestReturnOrderList:
    @allure.title('В тело ответа возвращается список заказов')
    def test_list_order(self):
        response = requests.get(f'{Urls.URL}{Endpoints.CREATE_ORDER}')
        assert len(response.json()) > 0
