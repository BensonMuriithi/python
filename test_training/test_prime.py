import unittest
import prime

class PrimeTestCase(unittest.TestCase):
	
	def test_five_is_prime(self):
		self.assertTrue(prime.isprime(5))
	
	def test_seven_is_prime(self):
		self.assertTrue(prime.isprime(7))
	
	def test_nextprime_seven_iseleven(self):
		self.assertEqual(prime.next_prime(7), 11)
	
	def test_455_not_prime(self):
		self.assertFalse(prime.isprime(452))
	
	def test_zeronot_prime(self):
		self.assertFalse(prime.isprime(0), msg = "Prime numbers must be greater than 1.")
	
	def test_below2_notprime(self):
		for i in xrange(1, -10, -1):
			self.assertFalse(prime.isprime(i), msg = "Prime numbers must be greater than 1.")
	
	def test_nextany_negative_is2(self):
		self.assertEqual(prime.next_prime(-540), 2, msg = "The least prime number is 2!")

if __name__ == "__main__":
	unittest.main()