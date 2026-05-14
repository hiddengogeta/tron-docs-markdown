

* [Advanced](/docu/docs/category/advanced)
* Governance & Voting
Version: 6.3.0

On this page

# Governance & Voting Guide

TRON uses a Delegated Proof of Stake (DPoS) governance model. TRX holders can vote for Super Representatives (SRs) and participate in network governance through proposals.

## Super Representatives[​](#super-representatives "Direct link to Super Representatives")

Super Representatives produce blocks and participate in governance. There are 27 SRs and 100+ SR Partners (candidates).

### Apply to Become a Super Representative[​](#apply-to-become-a-super-representative "Direct link to Apply to Become a Super Representative")

```
const tx = await tronWeb.transactionBuilder.applyForSR(  
    'TOwnerAddress',              // applicant address  
    'https://your-website.com',   // official website URL  
);  
const signedTx = await tronWeb.trx.sign(tx);  
const receipt = await tronWeb.trx.sendRawTransaction(signedTx);
```

note

Applying for SR requires burning 9,999 TRX.

## Voting for Super Representatives[​](#voting-for-super-representatives "Direct link to Voting for Super Representatives")

### Vote for SRs[​](#vote-for-srs "Direct link to Vote for SRs")

```
// Vote for multiple SRs  
const votes = {  
    'TSR1Address': 1000,  // 1000 votes for SR1  
    'TSR2Address': 500,   // 500 votes for SR2  
    'TSR3Address': 200,   // 200 votes for SR3  
};  
  
const tx = await tronWeb.transactionBuilder.vote(  
    votes,            // votes object: { address: voteCount }  
    'TVoterAddress',  // voter address (optional, uses default)  
);  
const signedTx = await tronWeb.trx.sign(tx);  
const receipt = await tronWeb.trx.sendRawTransaction(signedTx);
```

tip

Your voting power equals the total TRX you have staked (frozen). You must freeze TRX before voting.

### List Super Representatives[​](#list-super-representatives "Direct link to List Super Representatives")

```
const srList = await tronWeb.trx.listSuperRepresentatives();  
srList.forEach(sr => {  
    console.log(`${sr.address}: ${sr.voteCount} votes`);  
});
```

## Governance Proposals[​](#governance-proposals "Direct link to Governance Proposals")

SRs can create proposals to modify TRON network parameters.

### Create a Proposal[​](#create-a-proposal "Direct link to Create a Proposal")

```
// Propose to change network parameter #0 (maintenance interval) to 10000  
const parameters = [{ key: 0, value: 10000 }];  
  
const tx = await tronWeb.transactionBuilder.createProposal(  
    parameters,       // array of { key, value } pairs  
    'TSRAddress',     // issuer address (must be an SR)  
);  
const signedTx = await tronWeb.trx.sign(tx);  
const receipt = await tronWeb.trx.sendRawTransaction(signedTx);
```

### Vote on a Proposal[​](#vote-on-a-proposal "Direct link to Vote on a Proposal")

```
const tx = await tronWeb.transactionBuilder.voteProposal(  
    1,              // proposal ID  
    true,           // true = approve, false = disapprove  
    'TSRAddress',   // voter address (must be an SR)  
);  
const signedTx = await tronWeb.trx.sign(tx);  
const receipt = await tronWeb.trx.sendRawTransaction(signedTx);
```

### Delete a Proposal[​](#delete-a-proposal "Direct link to Delete a Proposal")

Only the proposer can delete their own pending proposal:

```
const tx = await tronWeb.transactionBuilder.deleteProposal(  
    1,            // proposal ID  
    'TSRAddress', // issuer address (must be the original proposer)  
);  
const signedTx = await tronWeb.trx.sign(tx);  
const receipt = await tronWeb.trx.sendRawTransaction(signedTx);
```

### Query Proposals[​](#query-proposals "Direct link to Query Proposals")

```
// List all proposals  
const proposals = await tronWeb.trx.listProposals();  
  
// Get specific proposal by ID  
const proposal = await tronWeb.trx.getProposal(1);  
console.log('Proposal:', proposal);  
// {  
//   proposal_id: 1,  
//   proposer_address: '...',  
//   parameters: [{ key: 0, value: 10000 }],  
//   expiration_time: ...,  
//   state: 'PENDING' | 'APPROVED' | 'DISAPPROVED' | 'CANCELLED',  
//   approvals: ['TSR1', 'TSR2', ...]  
// }
```

## Common Network Parameters[​](#common-network-parameters "Direct link to Common Network Parameters")

| Key | Parameter | Description |
| --- | --- | --- |
| 0 | MaintenanceTimeInterval | Time between maintenance periods |
| 1 | AccountUpgradeCost | Cost to apply for SR (in SUN) |
| 2 | CreateAccountFee | Fee for creating a new account |
| 3 | TransactionFee | Bandwidth unit price |
| 4 | AssetIssueFee | TRC-10 token creation fee |
| 5 | WitnessPayPerBlock | SR block reward |
| 11 | EnergyFee | Energy unit price |
| 12 | TotalEnergyCurrentLimit | Total energy limit |

## Related API References[​](#related-api-references "Direct link to Related API References")

* [transactionBuilder.applyForSR](/docu/docs/API List/transactionBuilder/applyForSR)
* [transactionBuilder.vote](/docu/docs/API List/transactionBuilder/vote)
* [transactionBuilder.createProposal](/docu/docs/API List/transactionBuilder/createProposal)
* [transactionBuilder.deleteProposal](/docu/docs/API List/transactionBuilder/deleteProposal)
* [transactionBuilder.voteProposal](/docu/docs/API List/transactionBuilder/voteProposal)