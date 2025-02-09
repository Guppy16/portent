## Im**portent**

### How our repo is setup

```
portent
├── ai-nlp
│   └── model.py
├── backend
│   └── lambda_function.py
├── flare-hardhat-starter
│   └── FDCExampleJq.ts
├── README.md
└── notes.md
```


**Scripts**

To run the scripts for attesting the data, checkout `flate-hardhat-starter/scripts/FDCExampleJq.ts`. 

To run the AI inference, use the `ai-nlp/label.py` script.

The backend can be run by deploying the lambda function in `backend/lambda_function.py`.
Note that it requires access to the daily price of BTC and LLM predictions. These files are very large so have not been included in the repo.



### How we use Flare

We use the Flare Data Connector (FDC) protocol to attest **both** the data that we fetch from NYT and the our own backend data which would be updated daily based on the news.


```
[
    category: 'U.S. Producer Price Index (PPI) falls',
    date: '2022-08-12'
]
```

Note: to run the attestations in Flare, you must set the environment variables in the `.env` file for:
```
NYT_API_KEY=NewYorkTimesAPIKey
ADAPT_API=LinkToBackend
```

### How our NLP pipeline works

1. Get news data from NYT
2. Label the data with tags
3. Backtest the labels with the price data
4. Agentify the tags + LLMs


Note that the New York Times API key is required to fetch the news data, but is rate limited, so did not work on attestation for the demo. 

Also, note that the NYT API cannot be used for commercial purposes, so we will switch to a plethora of other curated news sources.
