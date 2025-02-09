## Im**portent**

### How our repo is setup




Note: to run the attestations in Flare, you must set the environment variables in the `.env` file for:
```
NYT_API_KEY=NewYorkTimesAPIKey
ADAPT_API=LinkToBackend
```

Note that the New York Times API key is required to fetch the news data, but is rate limited, so did not work on attestation for the demo. 

### How we use Flare

We use the Flare Data Connector (FDC) protocol to attest **both** the data that we fetch from NYT and the our own backend data which would be updated daily based on the news.

In our pipeline


```
[
    category: 'U.S. Producer Price Index (PPI) falls',
    date: '2022-08-12'
]
```

### How our NLP pipeline works

1. Get news data from NYT
2. Label the data
3. Backtest the labels with the price data
4. Agentify the data