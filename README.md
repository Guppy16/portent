# Portent

> _portent_: a sign or warning that a momentous or calamitous event is likely to happen.

_We tell you the effect of real world events on crypto before the market reacts. Enabling you to manage your portfolio with foresight and trade more profitably._

### Why we built this?

* Recent market events led to historic $2.23B in liquidations, surpassing even the FTX and LUNA crash. Real-world events can cause significant market movements that catch traders off guard.

* Understanding which economic events affect crypto and how they impact the market requires deep analysis and expertise.

* Keeping track of global events and their potential impact on crypto markets is a full-time job.

### Our Solution

**Daily Impact Analysis**: We identify and analyze key events that truly affect crypto markets, delivered to you daily.

**Precise Predictions**: Get specific predictions about market impact, including expected percentage changes and time horizons.

**Detailed Analysis**: Understand the reasoning behind each prediction with detailed explanations.

### Demo

Please view the demo below!

https://github.com/user-attachments/assets/a08a53e1-6ef9-45db-b7e5-576d650c4d06


* [Landing Page](https://preview--foresight-crypto-dashboard.lovable.app/)
* [Dashboard](https://preview--foresight-crypto-dashboard.lovable.app/dashboard)

### Next steps

**On-Chain** and **Agent Ecosystem**
  - Reliable and secure price history from _Flare_
  - Curate diverse news sources and store the data on _BNB Greenfield_
  - Integrate this with our conversational agentic AI ecosystem

### Further Reading

We have more detailed notes about our processes and setup in the [notes.md](notes.md) file.

---

### Eth Oxford 2025 Hackathon

This repo is prepared in submission for _eth-Oxford-2025_ hackathon.

We are submitting into the [**AI track**](https://dorahacks.io/hackathon/eth-oxford-2025/ai) with the aim for the **Wildcard** Prize, specifically to tackle this task: _AI for predictive analytics in decentralized markets_. We built our own AI agent to consistently predict the price movement based on key real world events, and have an NLP interface to interact with the agent. Agentic flow is automatic..

We are also submitting for [**Flare**](https://flare-network.notion.site/Flare-Hackathon-Guide-ETH-Oxford-17fd502e6fa6803ab4fefd325eb2395f) Track. As a proof concept, we use the Flare Data Connector (FDC) protocol to attest **both** the data that we fetch from NYT and our own backend data which would be updated daily based on the news. The smart contract is deployed on [coston2](https://coston2-explorer.flare.network/) at [`0xd1F1BE685Fd67F8561BeC1281C714c6a14Eb6baD`](https://coston2-explorer.flare.network/address/0xd1F1BE685Fd67F8561BeC1281C714c6a14Eb6baD#code) example of an attestation submission [here](https://coston2-systems-explorer.flare.rocks/voting-epoch/896247?tab=fdc). 

### Feedback on Using Tools at the Hackathon

- **Flare**
  - ok documentation
    - very easy to setup wallet
    - not many examples that were useful for me (docs were out of date)
  - great helpdesk to understand how the code works
  - tutorial on FDC could be more useful by explaining how the attestation happens under the hood. It was a bit cryptic to me at first to understand all the moving parts.
  - the explorer is very useful to see the data and the attestation
  - `45s` lag on `coston2` was a killer haha
  - `hardhat` tutorial was very useful and a good pre-requisite
- **BNB**
  - Still failing to get token `:(` to migrate from local development to on-chain
- **Torus**
  - Great idea conceptually, but the support was lackluster
- General
  - Why are there no python bindings in general?
  - Some intrductory tutorials on web3 would have been very helpful to do the boiler plate stuff such as
    - deploying frontend / backend to `BNB Greenfield`
    - faucets could have been made more obvious