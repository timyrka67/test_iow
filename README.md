# test_iow
For test from iponweb.

Term:

Hi Timur  !

1) Plz find test task below.  We expect the task to be done using Python, tests can be written in Python either .

2) Plz reply to confirm that you have seen this email

3) Feel free to ask questions if you have any .

*******************************************************************************************

As an input you have several entities, so called "creatives". Each of them has
   - price
   - id of advertiser
   - country name to serve (optional)

Please implement a function, receiving
   - array of creatives
   - number of winners
   - country name (optional)
and returning number_of_winners creatives, obeying the following rules:

1) all winners must have unique advertiser_id

2) if third argument (country) is provided, then only creatives without country or creatives with same country can be among winners

3*) function should not give preference to any of equal by price creatives, but should return such creatives equiprobable.

Please cover your solution with tests.

* Consider a case with several input creatives equal by price and several function calls with same input, output results may be different.




Usage:
> python3.4 test.py ("Parameters")	           	
> python3.4 test.py 6 "Russia"
