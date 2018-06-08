In my NLP work, I typically have to ingest huge text files and I've learned to love the reservoir sampling algorithm for being a great tool that allows sampling from data sets that could never be read into memory all at once.

Using the reservoir sampling algorithm on a file is one thing; we know we're reading something in of a fixed size and we'll know when we're done sampling, even if we don't know that size a head of time. We can call the function and simply wait till it returns. 

Reading from a continuous stream like Twitter, for example, is slightly different. The function handling the sampling must be able to update the reservoir when the stream has new input while at the same time keeping it available for inspection at any moment. This is a perfect situation for coroutines! 

The coroutine found in online_reservoir_sampling.py yields both the call count (how many data points it's seen) and the current sample set which may or may not change at every call. 