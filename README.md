# 1. Installation
### 1.1 Package version
* Python version: 3.11.7
* Poetry version: 1.8.3

### 1.2 Installation
- Create venv:  `python -m venv py3117env`
- Active venv: `source py3117env/bin/activate`
- Install poetry: `poetry install --no-interaction --no-ansi --no-root`


# 2. Layer Architecture
https://paradoxai.atlassian.net/wiki/spaces/OLIVIA/pages/3251601414/Code+Structure+Documentation

# 3. Unit Test example

### STUB example

````python
class BaseOrderServiceTest(BaseTest):
    @pytest.fixture(autouse=True)
    def _setUp(self):
        self.instance_under_test = OrderService

    def _tearDown(self):
        pass

    
class TestGetOrderByUser(BaseOrderServiceTest):
    @patch.object(OrderGetter, "get_orders_by_user", StubOrderGetter.get_orders_by_user_with_new_status)
    def test_get_order_by_user_with_new_status(self):
        # Arrange
        user_id = 1111
        order_status_filter = [OrderStatus.NEW]

        #Act
        orders = self.instance_under_test.get_orders_by_user(user_id, order_status_filter)

        #Assert
        self.assertEqual(2, len(orders))

        # Tear down
        self._tearDown()
````

### MOCK example
We can use mocks to verify the number of calls to a specific dependency. This is useful when checking database queries or third-party API calls.

````python
class BaseGetterTest(BaseTest):
    @pytest.fixture(autouse=True)
    def _setUp(self):
        self.instance_under_test = OrderGetter

    def _tearDown(self):
        pass

class TestGetOrderByUser(BaseGetterTest):
    @patch('order.managers.orders.OrdersManager.get_orders_by_user')
    def test_get_order_by_user_with_no_status_filter_and_return_list_orders(self, order_manager_mock):
        # Arrange
        user_id = 1111
        order_status_filter = []
        order_manager_mock.side_effect = MockOrderManager().mock_get_orders_by_user

        #Act
        orders = self.instance_under_test.get_orders_by_user(user_id, order_status_filter)

        #Assert
        self.assertEqual(len(orders), 3)
        # Check number of call. It will be useful in case we want to check how many times the method is called
        order_manager_mock.assert_called_once_with(user_id, order_status_filter)

        # Tear down
        self._tearDown()
````

### FAKE example

````python
class TestCreateOrderActionWithFakeShippingService(BaseCreateOrderActionTest):
    @patch('order.intergrations.shipping.shipper_factory.ShippingAdapterFactory.get_shipping_adapter')
    @patch('order.managers.orders.OrdersManager.create')
    def test_create_order_with_mock_manager_and_fake_shipping_service_successful(self, order_manager_mock, shipping_factory_mock):
        # Arrange
        order_manager_mock.return_value = Order(id=1111, order_uuid="1234_1111", user_id=1122, status=OrderStatus.NEW)
        shipping_factory_mock.return_value = FakeShippingAdapter()

        # Act
        order_data = self.instance_under_test.create_order(1122, self.shipping_data_input)

        # Assert
        self.assertEqual(1111, order_data.id)
        self.assertEqual(1, shipping_factory_mock.call_count)

        # TODO verify fake shipping order is created
        shipping_provider: int = self.shipping_data_input.get("shipping_data").get("shipping_provider")
        shipping_order = ShippingAdapterFactory.get_shipping_adapter(shipping_provider).get_shipping_order(
            order_data.shipping_order_uuid)
        self.assertEqual(order_data.shipping_order_uuid, shipping_order.shipping_order_uuid)

        # Tear down
        self._tearDown()
````

### Different MOCK and STUB
STUB focus on State Testing while Mock focus on Behavior Testing.

Dive deep into State Testing vs Behavior Testing: https://coderstower.com/2019/09/24/unit-testing-behavior-vs-state/

