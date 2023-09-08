#!/usr/bin/python3

def minOperations(n):
   l = 1
   phrase = 0
   count = 0

   if (n < 1):
      return 0
   
   while (l != n):
      if (n % l == 0):
         phrase = l
         count += 1
      l += phrase
      count += 1

   return count



      
    