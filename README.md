# Ji-Li-DigitalWallet-frauddetection

I used Python for this project, and the packages I used were "networkx", "pandas".

The running time for 3 features are all around 220 seconds in a Macbook Pro i7 CPU, 16GB memory, 256GB SSD. 

Note: During the preprocessing data, we found the data in row 377592 of batch_payment.csv, is payback, which should be "trusted".
However, to simplify the fraud detaction, we removed that row directly for testing.
