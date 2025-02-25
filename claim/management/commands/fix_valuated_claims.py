import logging

from claim.models import Claim
from django.core.management.base import BaseCommand


FIELDS_TO_FIX_FOR_CLAIMS = [
    # Main ones that we definitely need to fix
    "submit_stamp",
    "validity_from",
    "status",
    "claimed",

    # Not sure that these need to be fixed, but just to be sure
    "date_from",
    "date_to",
    "approved",
    "reinsured",
    "valuated",
    "date_claimed",
    "date_processed",
    "feedback_available",
    "feedback_status",
    "review_status",
    "approval_status",
    "rejection_reason",
    "audit_user_id",
    "validity_from_review",
    "validity_to_review",
    "audit_user_id_review",
    "audit_user_id_submit",
    "audit_user_id_process",
    "process_stamp",
    "remunerated",
    "guarantee_id",
    "visit_type",
    "category",
    "json_ext",
    "explanation",
    "adjustment",
]
FIELDS_TO_FIX_FOR_SERVICES = [
    # Things we definitely need to fix
    "validity_from",

    # The following fields seem like they stayed the same, but just to be sure
    "status",
    "qty_provided",
    "qty_approved",
    "price_asked",
    "price_adjusted",
    "price_approved",
    "price_valuated",
    "rejection_reason",
    "audit_user_id",
    "validity_from_review",
    "audit_user_id_review",
    "limitation_value",
    "limitation",
    "remunerated_amount",
    "deductable_amount",
    "exceed_ceiling_amount",
    "price_origin",
    "exceed_ceiling_amount_category",
    "json_ext",
    "explanation",
    "justification",
]
FIELDS_TO_FIX_FOR_ITEMS = [
    *FIELDS_TO_FIX_FOR_SERVICES,
    "availability",
]

logger = logging.getLogger(__name__)

HELP_TEXT = ("This command will fix valuated Claims that were mistakenly resubmitted into the system. "
            "It is meant as a one shot, it should not be ran again.")

class Command(BaseCommand):
    help = HELP_TEXT

    def add_arguments(self, parser):
        parser.add_argument(
            '--verbose',
            action='store_true',
            dest='verbose',
            help='Be verbose about what it is doing',
        )

    def handle(self, *args, **options):
        logger.info("*** Processing valuated claims that were mistakenly resubmitted ***")
        total = 0
        error_missing_claim = 0
        error_missing_items = 0
        error_missing_services = 0

        wrong_claims = Claim.objects.filter(validity_to__isnull=True, status=Claim.STATUS_CHECKED, batch_run__isnull=False)
        logger.info(f"Found {len(wrong_claims)} claims to fix")

        for wrong_claim in wrong_claims:
            total += 1
            current_claim_id_to_fix = wrong_claim.id
            logger.info(f"\t Processing claim {total} - ID = {current_claim_id_to_fix} - status = {wrong_claim.status} - code = {wrong_claim.code}")

            claim_to_restore = Claim.objects.filter(legacy_id=current_claim_id_to_fix, status=Claim.STATUS_VALUATED).order_by("-id").first()
            if not claim_to_restore:
                error_missing_claim += 1
                logger.info(f"\t\t ERROR: Claim to restore for claim ID {current_claim_id_to_fix} not found")
                continue

            items_to_restore = {}
            for item in claim_to_restore.items.all().order_by("id"):
                items_to_restore[item.item_id] = item
            services_to_restore = {}
            for service in claim_to_restore.services.all().order_by("id"):
                services_to_restore[service.service_id] = service

            # Fix items
            for wrong_item in wrong_claim.items.all():
                if wrong_item.item_id not in items_to_restore:
                    error_missing_items += 1
                    logger.info(f"\t\t ERROR: Item {wrong_item.item_id} not found in claim {claim_to_restore.id}")
                    continue

                item_to_restore = items_to_restore[wrong_item.item_id]
                for field in FIELDS_TO_FIX_FOR_ITEMS:
                    setattr(wrong_item, field, getattr(item_to_restore, field))
                wrong_item.save()

            # Fix services
            for wrong_service in wrong_claim.services.all():
                if wrong_service.service_id not in services_to_restore:
                    error_missing_services += 1
                    logger.info(f"\t\t ERROR: Service {wrong_service.service_id} not found in claim {claim_to_restore.id}")
                    continue

                service_to_restore = services_to_restore[wrong_service.service_id]
                for field in FIELDS_TO_FIX_FOR_SERVICES:
                    setattr(wrong_service, field, getattr(service_to_restore, field))
                wrong_service.save()

            for field_to_fix in FIELDS_TO_FIX_FOR_CLAIMS:
                setattr(wrong_claim, field_to_fix, getattr(claim_to_restore, field_to_fix))
            wrong_claim.save()

        logger.info("*********************************")
        logger.info(f"Total claims processed: {total}")
        logger.info(f"Total missing claims to restore: {error_missing_claim}")
        logger.info(f"Total missing items to restore: {error_missing_items}")
        logger.info(f"Total missing services to restore: {error_missing_services}")
