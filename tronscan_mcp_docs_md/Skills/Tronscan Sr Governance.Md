

# Super Representatives

**Skill ID**: `tronscan-sr-governance`  
**ClawHub**: [clawhub.ai/sshnii/tronscan-sr-governance](https://clawhub.ai/sshnii/tronscan-sr-governance)

Query TRON Super Representatives (SR), witness rankings, candidate lists, account vote destinations, chain parameter configuration, and governance proposals.

This skill is intended for **SR / witness / chain governance** queries. For account asset profiling, use **tronscan-account-profiler**. To look up who voted for a specific SR, use the `getVoteList` endpoint in **tronscan-account-profiler**.

---

## Use Cases

### Query Super Representative List

* `getWitnessList` — Retrieve the SR / witness list, filterable by type (Super Representative / Partner / Candidate)

Example prompts:

```
"Who are the top SRs?"
"What is the current Super Representative ranking?"
"How many SR candidates does TRON have?"
"Show me the list of SR partners."
"How many active witnesses are there on TRON?"
```

---

### Query Network Vote Statistics

* `getWitnessGeneralInfo` — Retrieve network aggregate stats: total votes, block production statistics, witness count

Example prompts:

```
"What is the total number of votes on the TRON network?"
"How many blocks have Super Representatives produced?"
"How many witnesses are there currently?"
"What does the network voting overview look like?"
"What are the overall block production stats?"
```

---

### Query Account Vote Records

* `getAccountVotes` — Retrieve the vote records for a given address: which SRs it voted for and the vote amounts

Use `getAccountVotes` to find out who an address voted for. To find out who voted for a specific SR, use `getVoteList` in **tronscan-account-profiler**, passing in the SR address.

Example prompts:

```
"Which SRs did this address vote for?"
"Where are my votes going?"
"Who did address TXxx... cast their votes to?"
"How many votes did this wallet allocate to Super Representatives?"
"Show me the vote destinations for this address."
```

---

### Query SR Vote Metrics and History

* `getWitnessVoteInfo` — Retrieve vote metrics and ranking change history for a specified witness

Example prompts:

```
"How many votes does SR X currently have?"
"How has this Super Representative's ranking changed over time?"
"What is the historical vote data for witness TXxx...?"
"What is the recent vote trend for this SR?"
"Show me the ranking history of this Super Representative."
```

---

### Query Chain Parameters and Governance Proposals

* `getChainParameters` — Retrieve all current TRON network configuration parameters: transaction fees, energy price, bandwidth price, etc.
* `getProposals` — Retrieve the governance proposal list, including proposal content, vote information, and participant details

Example prompts:

```
"What is the current energy price on TRON?"
"How is the bandwidth fee calculated?"
"What governance proposals are currently active?"
"What was the result of the latest proposal vote?"
"What are the current network configuration parameters?"
```

---

## Installation

### Confirm TronScan MCP is Connected

See [Getting Started](/en/skills/getting-started).

### Install from ClawHub

> [Open on ClawHub](https://clawhub.ai/sshnii/tronscan-sr-governance)

Copy the link to this page and send it to your AI Agent:

```
Please install this skill: https://clawhub.ai/sshnii/tronscan-sr-governance
```