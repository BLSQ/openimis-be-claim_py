from claim.reports import claim_percentage_referrals, claims_overview, claim_history, \
    claims_primary_operational_indicators, nhia_claims_paid, nhia_claims_rejected, nhia_claims_pending
from claim.reports.claim_history import claim_history_query
from claim.reports.claim_percentage_referrals import claim_percentage_referrals_query
from claim.reports.claims_overview import claims_overview_query
from claim.reports.claims_primary_operational_indicators import claims_primary_operational_indicators_query
from claim.reports.nhia_claims_paid import nhia_claims_paid_query
from claim.reports.nhia_claims_pending import nhia_claims_pending_query
from claim.reports.nhia_claims_rejected import nhia_claims_rejected_query

report_definitions = [
    {
        "name": "claim_percentage_referrals",
        "engine": 0,
        "default_report": claim_percentage_referrals.template,
        "description": "Percentage of referrals in claims",
        "module": "claim",
        "python_query": claim_percentage_referrals_query,
        "permission": ["131214"],
    },
    {
        "name": "claims_overview",
        "engine": 0,
        "default_report": claims_overview.template,
        "description": "Overview of the processing of claims",
        "module": "claim",
        "python_query": claims_overview_query,
        "permission": ["131213"],
    },
    {
        "name": "claim_history",
        "engine": 0,
        "default_report": claim_history.template,
        "description": "Claim history",
        "module": "claim",
        "python_query": claim_history_query,
        "permission": ["131223"],
    },
    {
        "name": "claims_primary_operational_indicators",
        "engine": 0,
        "default_report": claims_primary_operational_indicators.template,
        "description": "Claims Primary operational indicators",
        "module": "claim",
        "python_query": claims_primary_operational_indicators_query,
        "permission": ["131202"],
    },
    {
        "name": "nhia_claims_paid",
        "engine": 0,
        "default_report": nhia_claims_paid.template,
        "description": "NHIA - Claims Paid",
        "module": "claim",
        "python_query": nhia_claims_paid_query,
        "permission": ["131230"],
    },
    {
        "name": "nhia_claims_rejected",
        "engine": 0,
        "default_report": nhia_claims_rejected.template,
        "description": "NHIA - Claims Rejected",
        "module": "claim",
        "python_query": nhia_claims_rejected_query,
        "permission": ["131231"],
    },
    {
        "name": "nhia_claims_pending",
        "engine": 0,
        "default_report": nhia_claims_pending.template,
        "description": "NHIA - Claims Pending",
        "module": "claim",
        "python_query": nhia_claims_pending_query,
        "permission": ["131232"],
    },
]
