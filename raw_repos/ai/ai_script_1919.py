def remove_primes(list):
   modified_list = []
   for idx, num in enumerate(list):
       if is_prime(idx) == False:
           modified_list.append(num)
   return modified_list