# Ji-Li-DigitalWallet-frauddetection

I used Python for this project, and the packages I used were "networkx", "pandas".

The running time for 3 features are all around 220 seconds in a Macbook Pro i7 CPU, 16GB memory, 256GB SSD. 

Note: During the preprocessing data, we found the data in row 377592 of batch_payment.csv, is payback, which should be "trusted".
However, to simplify the fraud detaction, we removed that row directly for testing.

We could also add features list below:

1) When anyone makes a payment to another user, they'll be notified if the amount of transaction become a outlier. (>1.5IQR or >3IQR)

"unverified: This amount of transaction is too high. Are you sure you would like to proceed with this payment?"

2) When anyone makes a payment to another user, they'll be notified if it is a foreigh transaction.

"unverified: This transaction is a foreign transation. Are you sure you would like to proceed with this payment?"

3) When anyone makes a payment to another user,  they'll be notified if they've already made at least one same amount of transaction with that user in a short time (10 min, 1 h, or 1 day).

"unverified: You've had several/one similar transactions with this user in a short time. Are you sure you would like to proceed with this payment?"
