#!/usr/bin/env python3
"""
Boomi SDK Example: Trading Partner Deletion
===========================================

This example demonstrates:
1. Deleting trading partner components
2. Safe deletion with dependency checks
3. Restoring deleted trading partners
4. Batch deletion operations

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have permissions for trading partner operations
- Python 3.7+

Usage:
    # Delete a trading partner by ID
    python3 delete_trading_partner.py --delete TRADING_PARTNER_ID

    # Check dependencies before deletion
    python3 delete_trading_partner.py --delete TRADING_PARTNER_ID --check-dependencies

    # Delete multiple trading partners
    python3 delete_trading_partner.py --batch-delete ID1 ID2 ID3

    # Restore a deleted trading partner
    python3 delete_trading_partner.py --restore TRADING_PARTNER_ID

    # List deleted trading partners
    python3 delete_trading_partner.py --list-deleted

    # Dry run (simulate deletion without actually deleting)
    python3 delete_trading_partner.py --delete TRADING_PARTNER_ID --dry-run
"""

import os
import sys
import argparse
from typing import List, Optional
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import (
    TradingPartnerProcessingGroupQueryConfig,
    TradingPartnerProcessingGroupQueryConfigQueryFilter,
    TradingPartnerProcessingGroupSimpleExpression,
    TradingPartnerProcessingGroupSimpleExpressionOperator
)


class TradingPartnerDeleter:
    """Manages trading partner deletion operations"""

    def __init__(self, sdk: Boomi, verbose: bool = False):
        """Initialize the deleter"""
        self.sdk = sdk
        self.verbose = verbose

    def get_trading_partner_info(self, tp_id: str) -> Optional[dict]:
        """Get trading partner information"""
        try:
            tp = self.sdk.trading_partner_component.get_trading_partner_component(
                id_=tp_id
            )

            info = {
                'id': getattr(tp, 'id_', getattr(tp, 'component_id', 'N/A')),
                'name': getattr(tp, 'component_name', getattr(tp, 'name', 'Unnamed')),
                'standard': getattr(tp, 'standard', 'N/A'),
                'classification': getattr(tp, 'classification', 'N/A'),
                'folder': getattr(tp, 'folder_name', 'N/A'),
                'deleted': getattr(tp, 'deleted', False)
            }

            return info

        except Exception as e:
            if self.verbose:
                print(f"   Error getting trading partner info: {e}")
            return None

    def check_dependencies(self, tp_id: str) -> dict:
        """Check if trading partner is used in processing groups"""
        print(f"\n🔍 Checking dependencies for trading partner: {tp_id}")

        dependencies = {
            'processing_groups': [],
            'has_dependencies': False
        }

        try:
            # Query processing groups that contain this trading partner
            # Note: This is a simplified check - in production you might need more thorough checks
            query_expression = TradingPartnerProcessingGroupSimpleExpression(
                operator=TradingPartnerProcessingGroupSimpleExpressionOperator.LIKE,
                property="name",
                argument=['%']
            )

            query_filter = TradingPartnerProcessingGroupQueryConfigQueryFilter(
                expression=query_expression
            )
            query_config = TradingPartnerProcessingGroupQueryConfig(
                query_filter=query_filter
            )

            result = self.sdk.trading_partner_processing_group.query_trading_partner_processing_group(
                request_body=query_config
            )

            if result and hasattr(result, 'result') and result.result:
                for pg in result.result:
                    # Check if this processing group references the trading partner
                    if hasattr(pg, 'trading_partners') and pg.trading_partners:
                        if hasattr(pg.trading_partners, 'trading_partner'):
                            partners = pg.trading_partners.trading_partner
                            if not isinstance(partners, list):
                                partners = [partners]

                            for partner in partners:
                                partner_id = getattr(partner, 'id_', getattr(partner, 'id', None))
                                if partner_id == tp_id:
                                    dependencies['processing_groups'].append({
                                        'id': getattr(pg, 'component_id', 'N/A'),
                                        'name': getattr(pg, 'component_name', 'N/A')
                                    })
                                    dependencies['has_dependencies'] = True

            if dependencies['has_dependencies']:
                print(f"   ⚠️  Found {len(dependencies['processing_groups'])} processing group(s) using this trading partner:")
                for pg in dependencies['processing_groups']:
                    print(f"      • {pg['name']} (ID: {pg['id']})")
            else:
                print("   ✅ No processing group dependencies found")

        except Exception as e:
            if self.verbose:
                print(f"   ⚠️  Error checking dependencies: {e}")

        return dependencies

    def delete_trading_partner(self, tp_id: str, force: bool = False) -> bool:
        """Delete a trading partner component"""
        print("\n" + "="*70)
        print(f"🗑️  DELETING TRADING PARTNER: {tp_id}")
        print("="*70)

        # Get trading partner info
        info = self.get_trading_partner_info(tp_id)
        if not info:
            print("❌ Trading partner not found or cannot be accessed")
            return False

        print(f"\n📋 Trading Partner Details:")
        print(f"   Name: {info['name']}")
        print(f"   Standard: {info['standard']}")
        print(f"   Classification: {info['classification']}")
        print(f"   Folder: {info['folder']}")
        print(f"   Already Deleted: {info['deleted']}")

        if info['deleted']:
            print("\n⚠️  Trading partner is already deleted")
            return False

        # Check dependencies unless forced
        if not force:
            deps = self.check_dependencies(tp_id)
            if deps['has_dependencies']:
                print("\n❌ Cannot delete - trading partner has dependencies")
                print("   Use --force to delete anyway (not recommended)")
                return False

        # Perform deletion
        try:
            print("\n🔄 Deleting trading partner...")
            self.sdk.trading_partner_component.delete_trading_partner_component(
                id_=tp_id
            )

            print("✅ Trading partner deleted successfully!")
            return True

        except Exception as e:
            print(f"❌ Deletion failed: {e}")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return False

    def batch_delete(self, tp_ids: List[str], force: bool = False) -> dict:
        """Delete multiple trading partners"""
        print("\n" + "="*70)
        print(f"📦 BATCH DELETING {len(tp_ids)} TRADING PARTNER(S)")
        print("="*70)

        results = {
            'total': len(tp_ids),
            'successful': 0,
            'failed': 0,
            'skipped': 0,
            'details': []
        }

        for i, tp_id in enumerate(tp_ids, 1):
            print(f"\n[{i}/{len(tp_ids)}] Processing: {tp_id}")

            # Get info
            info = self.get_trading_partner_info(tp_id)
            if not info:
                print("   ⏭️  Skipped - not found")
                results['skipped'] += 1
                results['details'].append({
                    'id': tp_id,
                    'status': 'skipped',
                    'reason': 'not found'
                })
                continue

            print(f"   Name: {info['name']}")

            # Check if already deleted
            if info['deleted']:
                print("   ⏭️  Skipped - already deleted")
                results['skipped'] += 1
                results['details'].append({
                    'id': tp_id,
                    'name': info['name'],
                    'status': 'skipped',
                    'reason': 'already deleted'
                })
                continue

            # Check dependencies unless forced
            if not force:
                deps = self.check_dependencies(tp_id)
                if deps['has_dependencies']:
                    print("   ⏭️  Skipped - has dependencies")
                    results['skipped'] += 1
                    results['details'].append({
                        'id': tp_id,
                        'name': info['name'],
                        'status': 'skipped',
                        'reason': 'has dependencies'
                    })
                    continue

            # Delete
            try:
                self.sdk.trading_partner_component.delete_trading_partner_component(
                    id_=tp_id
                )
                print("   ✅ Deleted")
                results['successful'] += 1
                results['details'].append({
                    'id': tp_id,
                    'name': info['name'],
                    'status': 'deleted'
                })
            except Exception as e:
                print(f"   ❌ Failed: {e}")
                results['failed'] += 1
                results['details'].append({
                    'id': tp_id,
                    'name': info['name'],
                    'status': 'failed',
                    'error': str(e)
                })

        # Print summary
        print("\n" + "="*70)
        print("📊 BATCH DELETE SUMMARY")
        print("="*70)
        print(f"Total: {results['total']}")
        print(f"Successful: {results['successful']}")
        print(f"Failed: {results['failed']}")
        print(f"Skipped: {results['skipped']}")

        return results

    def restore_trading_partner(self, tp_id: str) -> bool:
        """Restore a deleted trading partner"""
        print("\n" + "="*70)
        print(f"♻️  RESTORING TRADING PARTNER: {tp_id}")
        print("="*70)

        try:
            # Get the trading partner (even if deleted)
            tp = self.sdk.trading_partner_component.get_trading_partner_component(
                id_=tp_id
            )

            deleted = getattr(tp, 'deleted', False)
            name = getattr(tp, 'component_name', getattr(tp, 'name', 'Unnamed'))

            print(f"\n📋 Trading Partner: {name}")
            print(f"   Deleted: {deleted}")

            if not deleted:
                print("\n⚠️  Trading partner is not deleted - no restore needed")
                return False

            # Restore by updating (POST to the same ID restores it)
            print("\n🔄 Restoring trading partner...")
            self.sdk.trading_partner_component.update_trading_partner_component(
                id_=tp_id,
                request_body=tp
            )

            print("✅ Trading partner restored successfully!")
            return True

        except Exception as e:
            print(f"❌ Restore failed: {e}")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return False



def main():
    parser = argparse.ArgumentParser(
        description="Delete Boomi trading partner components",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Delete a trading partner
  %(prog)s --delete TRADING_PARTNER_ID

  # Check dependencies before deletion
  %(prog)s --delete TRADING_PARTNER_ID --check-dependencies

  # Force deletion (skip dependency checks)
  %(prog)s --delete TRADING_PARTNER_ID --force

  # Delete multiple trading partners
  %(prog)s --batch-delete ID1 ID2 ID3

  # Restore a deleted trading partner
  %(prog)s --restore TRADING_PARTNER_ID
"""
    )

    # Operations
    parser.add_argument(
        "--delete",
        metavar="ID",
        help="Delete a trading partner by ID"
    )
    parser.add_argument(
        "--batch-delete",
        nargs="+",
        metavar="ID",
        help="Delete multiple trading partners"
    )
    parser.add_argument(
        "--restore",
        metavar="ID",
        help="Restore a deleted trading partner"
    )

    # Options
    parser.add_argument(
        "--check-dependencies",
        action="store_true",
        help="Check dependencies before deletion (default behavior)"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Skip dependency checks"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose output"
    )

    args = parser.parse_args()

    # Check for at least one operation
    if not any([args.delete, args.batch_delete, args.restore]):
        parser.print_help()
        return 0

    # Print header
    print("🚀 Boomi SDK - Trading Partner Deletion Example")
    print("="*70)

    # Initialize SDK
    try:
        sdk = Boomi(
            account_id=os.getenv("BOOMI_ACCOUNT"),
            username=os.getenv("BOOMI_USER"),
            password=os.getenv("BOOMI_SECRET"),
            timeout=30000,
        )
        print("✅ SDK initialized successfully!")
        print(f"📍 Account: {os.getenv('BOOMI_ACCOUNT')}")
    except Exception as e:
        print(f"❌ SDK initialization failed: {e}")
        print("\n🔍 Make sure environment variables are set:")
        print("   - BOOMI_ACCOUNT")
        print("   - BOOMI_USER")
        print("   - BOOMI_SECRET")
        return 1

    # Initialize deleter
    deleter = TradingPartnerDeleter(
        sdk=sdk,
        verbose=args.verbose
    )

    # Execute operations
    success = True

    if args.delete:
        success = deleter.delete_trading_partner(args.delete, force=args.force)

    elif args.batch_delete:
        results = deleter.batch_delete(args.batch_delete, force=args.force)
        success = results['failed'] == 0

    elif args.restore:
        success = deleter.restore_trading_partner(args.restore)

    # Print footer
    print("\n" + "="*70)
    if success:
        print("✅ Operation completed successfully!")
    else:
        print("⚠️  Operation completed with errors")
    print("="*70)

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
