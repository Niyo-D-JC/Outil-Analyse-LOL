
class TestUser(TestCase):
    def test_get_coef_damage_type(self):
        # GIVEN


        # WHEN


        # THEN



if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(
        TestLoader().loadTestsFromTestCase(TestUser)
    )
