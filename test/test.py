import culqipy
import unittest
import uuid

culqipy.COD_COMMERCE = 'pk_test_vzMuTHoueOMlgUPj'
culqipy.API_KEY = 'sk_test_UTCQSGcXW8bCyU59'


class TestStringMethods(unittest.TestCase):
    def token(self):

        dir_token = {'card_number': '4111111111111111', 'cvv': '123',
                     'currency_code': 'PEN', 'first_name': 'will',
                     'last_name': 'Muro', 'email': 'wmuro@me.com',
                     'expiration_month': 9, 'expiration_year': 2020,
                     'fingerprint': 'q352454534'}

        token = culqipy.Token.create(dir_token)
        return token

    def charge(self):
        dir_charge = {'address': 'Avenida Lima 1232', 'address_city': 'LIMA',
                      'amount': 1000, 'country_code': 'PE', 'currency_code': 'PEN',
                      'email': 'wmuro@me.com', 'first_name': 'William', 'installments':0,
                      'last_name': 'Muro', 'metadata': '', 'phone_number': 3333339,
                      'product_description': 'Venta de prueba', 'token_id': self.token()["id"]}

        charge = culqipy.Charge.create(dir_charge)
        return charge

    def plan(self):
        dir_plan = {'alias': 'plan-test-' + str(uuid.uuid1()), 'amount': 1000,
                    'currency_code': 'PEN', 'interval': 'day', 'interval_count': 2,
                    'limit': 10, 'name': 'Plan de Prueba ' + str(uuid.uuid1()),
                    'trial_days': 50}

        plan = culqipy.Plan.create(dir_plan)
        return plan

    def subscription(self):
        dir_subscription = {'address': 'Avenida Lima 123213', 'address_city': 'LIMA',
                            'country_code': 'PE', 'email': 'wmuro@me.com', 'last_name': 'Muro',
                            'first_name': 'William', 'phone_number': 1234567789,
                            'plan_alias': self.plan()["alias"], 'token_id': self.token()["id"]}

        subscription = culqipy.Subscription.create(dir_subscription)
        return subscription

    def refund(self):
        dir_refund = {'amount': 500, 'charge_id': self.charge()["id"], 'reason': 'give me money back'}
        refund = culqipy.Refund.create(dir_refund)
        return refund

    def test_token(self):
        print(self.token())
        self.assertEqual("token", str(self.token()["object"]))

    def test_find_token(self):
        id = self.token()["id"]
        token = culqipy.Token.get(id)
        self.assertEqual("token", str(token["object"]))

    def test_charge(self):
        self.assertEqual("charge", str(self.charge()["object"]))

    def test_list_charge(self):
        params = {'min_amount': 500, 'max_amount': 1000}
        charge_list = culqipy.Charge.list(params)
        data = False
        print(charge_list)
        if len(charge_list) > 0:
            data = True
        self.assertTrue(data)

    def test_plan(self):
        self.assertEqual("plan", str(self.plan()["object"]))

    def test_subscription(self):
        self.assertEqual("subscription", str(self.subscription()["object"]))

    def test_refund(self):
        self.assertEqual("refund", str(self.refund()["object"]))


if __name__ == '__main__':
    unittest.main()
