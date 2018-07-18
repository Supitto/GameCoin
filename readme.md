


     _______  _______  __   __  _______           _______  _______  ___   __    _ 
    |       ||   _   ||  |_|  ||       |         |       ||       ||   | |  |  | |
    |    ___||  |_|  ||       ||    ___|         |       ||   _   ||   | |   |_| |
    |   | __ |       ||       ||   |___          |       ||  | |  ||   | |       |
    |   ||  ||       ||       ||    ___|         |      _||  |_|  ||   | |  _    |
    |   |_| ||   _   || ||_|| ||   |___          |     |_ |       ||   | | | |   |
    |_______||__| |__||_|   |_||_______|         |_______||_______||___| |_|  |__|


                            LLLLLLLLLLLLLLLLLLLLMMMMMMMM
                            LLLLLLLLLLLLLLLLLLLLMMMMMMMM
                        LLLLLLLLLLLLLLLLLLLLLLLLLLLLMMMMMMMM
                        LLLLLLLLLLLLLLLLLLLLLLLLLLLLMMMMMMMM
                        LLLLLLLLMMMMMMMMLLLLLLLLLLLLMMMMMMMM
                        LLLLLLLLMMMMMMMMLLLLLLLLLLLLMMMMMMMM
                    LLLLLLLLKKKKLLLLLLLLMMMMLLLLLLLLLLLLMMMMMMMM
                    LLLLLLLLKKKKLLLLLLLLMMMMLLLLLLLLLLLLMMMMMMMM
                    LLLLLLLLKKKKLLLLLLLLMMMMLLLLLLLLLLLLMMMMMMMM
                    LLLLLLLLKKKKLLLLLLLLMMMMLLLLLLLLLLLLMMMMMMMM
                    LLLLLLLLKKKKLLLLLLLLMMMMLLLLLLLLLLLLMMMMMMMM
                    LLLLLLLLKKKKLLLLLLLLMMMMLLLLLLLLLLLLMMMMMMMM
                    LLLLLLLLKKKKLLLLLLLLMMMMLLLLLLLLLLLLMMMMMMMM
                    LLLLLLLLKKKKLLLLLLLLMMMMLLLLLLLLLLLLMMMMMMMM
                    LLLLLLLLKKKKLLLLLLLLMMMMLLLLLLLLLLLLMMMMMMMM
                    LLLLLLLLKKKKLLLLLLLLMMMMLLLLLLLLLLLLMMMMMMMM
                    LLLLLLLLKKKKLLLLLLLLMMMMLLLLLLLLLLLLMMMMMMMM
                    LLLLLLLLKKKKLLLLLLLLMMMMLLLLLLLLLLLLMMMMMMMM
                    LLLLLLLLKKKKLLLLLLLLMMMMLLLLLLLLLLLLMMMMMMMM
                    LLLLLLLLKKKKLLLLLLLLMMMMLLLLLLLLLLLLMMMMMMMM
                    LLLLLLLLKKKKLLLLLLLLMMMMLLLLLLLLLLLLMMMMMMMM
                    LLLLLLLLKKKKLLLLLLLLMMMMLLLLLLLLLLLLMMMMMMMM
                    LLLLLLLLKKKKLLLLLLLLMMMMLLLLLLLLLLLLMMMMMMMM
                    LLLLLLLLKKKKLLLLLLLLMMMMLLLLLLLLLLLLMMMMMMMM
                    LLLLLLLLKKKKLLLLLLLLMMMMLLLLLLLLLLLLMMMMMMMM
                        LLLLLLLLMMMMMMMMLLLLLLLLLLLLMMMMMMMM
                        LLLLLLLLMMMMMMMMLLLLLLLLLLLLMMMMMMMM
                        LLLLLLLLLLLLLLLLLLLLLLLLLLLLMMMMMMMM
                        LLLLLLLLLLLLLLLLLLLLLLLLLLLLMMMMMMMM
                            LLLLLLLLLLLLLLLLLLLLMMMMMMMM
                            LLLLLLLLLLLLLLLLLLLLMMMMMMMM
    
    
    
    
                       A (not really) cryptocurrency for gamified systems

# What is it

GC aims to be a system that everyone that have a gamefied system (a city maybe) can use to control and sustain a simple economy

# Why is it

For the hell of it

# How it works

Game coin works assuming atomic coins (1 GC), it also assumes a central unity that controls the whole thing. We still don't have byzantine fault tolerance, but we are working on it.
The central unity validate the transactions and generate new coins.
There are rounds every n seconds, the transactions are validated on the end of the round. If there is any transaction approved it generates a new block, otherwise it will not.

Every game coin is a tuple of:
- The hash of the coin
- The last block where the coin was mentioned

Every block consist in a set of transactions, the time of the round in unix epoch, an OTPT value (based in the epoch) encrypted with the public signature of the central unity, a hash map of the coins in the block, and the hash of the last block.
The OTPT private key is also held by the central unity (this guarantees the authenticity of the block)

Every transaction consists in the tuple:
- Last owner public key
- New owner public key
- Coin hash

To perform a transaction, the owner of the coin have to answer a riddle encrypted with his public key.
To check the ownership of the coin the central unity run through the blocks and go until it finds the hash of the block. If it finds the coin before the specified block, or it cannot assure the ownership of the coin, it will drop the entire transaction.
(It will be later changed to another checking system probably)

#Want to help

Don't be shy, send me a message and let's talk.
