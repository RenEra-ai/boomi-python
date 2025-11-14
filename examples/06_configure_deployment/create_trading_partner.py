#!/usr/bin/env python3
"""
Boomi SDK Example: Trading Partner Component Management
========================================================

This example demonstrates:
1. Creating X12 trading partner components
2. Retrieving trading partners by ID
3. Querying trading partners
4. Managing trading partner settings

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Account must have B2B/EDI feature enabled for trading partner creation
- Account must have permissions for trading partner operations
- Python 3.7+

Note:
- If your account doesn't have B2B/EDI, creation will fail
- You can still test get/query operations if trading partners already exist
- Use --query to check existing trading partners first

Usage:
    # Create a simple X12 trading partner
    python3 create_trading_partner.py --create

    # Create with custom name and folder
    python3 create_trading_partner.py --create --name "My Partner" --folder "MyFolder"

    # Get an existing trading partner by ID
    python3 create_trading_partner.py --get TRADING_PARTNER_ID

    # Query all trading partners
    python3 create_trading_partner.py --query

    # Create, then get to verify
    python3 create_trading_partner.py --create --verify
"""

import os
import sys
import argparse
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from boomi import Boomi
from boomi.models import (
    TradingPartnerComponentQueryConfig,
    TradingPartnerComponentQueryConfigQueryFilter,
    TradingPartnerComponentSimpleExpression,
    TradingPartnerComponentSimpleExpressionOperator,
    TradingPartnerComponentSimpleExpressionProperty
)


def build_trading_partner_xml(name, folder_name, description):
    """Build X12 trading partner component XML"""
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<bns:Component xmlns:bns="http://api.platform.boomi.com/"
               name="{name}"
               type="tradingpartner"
               folderName="{folder_name}">
    <bns:encryptedValues />
    <bns:description>{description}</bns:description>
    <bns:object>
        <TradingPartner classification="mytradingpartner" standard="x12">
            <ContactInfo />
            <PartnerInfo>
                <X12PartnerInfo>
                    <X12Options
                        acknowledgementoption="donotackitem"
                        envelopeoption="groupall"
                        fileDelimiter="stardelimited"
                        filteracknowledgements="false"
                        outboundInterchangeValidation="false"
                        outboundValidationOption="filterError"
                        rejectDuplicateInterchange="false"
                        segmentchar="newline" />
                    <X12ControlInfo>
                        <ISAControlInfo
                            ackrequested="false"
                            authorinfoqual="00"
                            interchangeid=""
                            interchangeidqual="01"
                            securityinfoqual="00"
                            testindicator="P" />
                        <GSControlInfo respagencycode="T" />
                    </X12ControlInfo>
                </X12PartnerInfo>
            </PartnerInfo>
            <PartnerCommunication>
                <X12PartnerCommunication>
                    <CommunicationOptions />
                </X12PartnerCommunication>
            </PartnerCommunication>
            <DocumentTypes />
            <Archiving />
        </TradingPartner>
    </bns:object>
    <bns:processOverrides />
</bns:Component>'''


def create_trading_partner(sdk, name="SDK Created Trading Partner", folder_name="Home", description="Trading partner created via Boomi Python SDK"):
    """Create a simple X12 trading partner component"""
    print("\n" + "="*70)
    print("🏗️  CREATING TRADING PARTNER")
    print("="*70)

    print("\n📋 Trading Partner Details:")
    print(f"  Name: {name}")
    print("  Standard: X12")
    print("  Classification: mytradingpartner")
    print("  Communication: X12")
    print(f"  Folder: {folder_name}")

    print("\n🔄 Creating via Component API...")

    try:
        xml_body = build_trading_partner_xml(name, folder_name, description)
        result = sdk.component.create_component(request_body=xml_body)

        print("✅ Trading partner created successfully!")
        print(f"   Type: {type(result).__name__}")

        # Extract component ID
        component_id = None
        if hasattr(result, 'id_'):
            component_id = result.id_
            print(f"   ID: {component_id}")
        elif hasattr(result, 'component_id'):
            component_id = result.component_id
            print(f"   Component ID: {component_id}")

        if hasattr(result, 'name'):
            print(f"   Name: {result.name}")

        if hasattr(result, 'standard'):
            print(f"   Standard: {result.standard}")

        print("\n🎉 SUCCESS!")

        return component_id

    except Exception as e:
        print(f"❌ Trading partner creation failed: {e}")
        return None


def get_trading_partner(sdk, trading_partner_id):
    """Retrieve a trading partner by ID"""
    print("\n" + "="*70)
    print(f"🔍 GETTING TRADING PARTNER: {trading_partner_id}")
    print("="*70)

    try:
        result = sdk.trading_partner_component.get_trading_partner_component(
            id_=trading_partner_id
        )

        print("✅ Trading partner retrieved successfully!")
        print(f"   Type: {type(result).__name__}")

        # Display key information
        if hasattr(result, 'name'):
            print(f"   Name: {result.name}")
        if hasattr(result, 'id_'):
            print(f"   ID: {result.id_}")
        if hasattr(result, 'standard'):
            print(f"   Standard: {result.standard}")
        if hasattr(result, 'classification'):
            print(f"   Classification: {result.classification}")
        if hasattr(result, 'folder_name'):
            print(f"   Folder: {result.folder_name}")

        # Show contact info if available
        if hasattr(result, 'contact_info') and result.contact_info:
            contact = result.contact_info
            if hasattr(contact, 'contact_name'):
                print(f"   Contact: {contact.contact_name}")
            if hasattr(contact, 'email'):
                print(f"   Email: {contact.email}")

        print("\n🎉 GET operation successful!")

        return result

    except Exception as e:
        print(f"❌ Get trading partner failed: {e}")
        return None


def query_trading_partners(sdk, name_pattern=None):
    """Query trading partners"""
    print("\n" + "="*70)
    print("🔍 QUERYING TRADING PARTNERS")
    print("="*70)

    try:
        # Build query expression
        if name_pattern:
            print(f"   Filter: Name LIKE '{name_pattern}'")
            expression = TradingPartnerComponentSimpleExpression(
                operator=TradingPartnerComponentSimpleExpressionOperator.LIKE,
                property=TradingPartnerComponentSimpleExpressionProperty.NAME,
                argument=[name_pattern]
            )
        else:
            print("   Filter: All trading partners")
            expression = TradingPartnerComponentSimpleExpression(
                operator=TradingPartnerComponentSimpleExpressionOperator.LIKE,
                property=TradingPartnerComponentSimpleExpressionProperty.NAME,
                argument=['%']
            )

        query_filter = TradingPartnerComponentQueryConfigQueryFilter(expression=expression)
        query_config = TradingPartnerComponentQueryConfig(query_filter=query_filter)

        result = sdk.trading_partner_component.query_trading_partner_component(
            request_body=query_config
        )

        if result and hasattr(result, 'result') and result.result:
            count = len(result.result)
            print(f"\n✅ Found {count} trading partner(s):")

            for i, tp in enumerate(result.result, 1):
                tp_id = getattr(tp, 'id_', getattr(tp, 'id', 'N/A'))
                tp_name = getattr(tp, 'name', 'Unnamed')
                tp_standard = getattr(tp, 'standard', 'N/A')
                print(f"\n   {i}. {tp_name}")
                print(f"      ID: {tp_id}")
                print(f"      Standard: {tp_standard}")

            print("\n🎉 QUERY operation successful!")
            return result.result
        else:
            print("\n✅ Query successful - 0 trading partners found")
            return []

    except Exception as e:
        print(f"❌ Query trading partners failed: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Create and test Boomi trading partner components"
    )
    parser.add_argument(
        "--create",
        action="store_true",
        help="Create a new trading partner"
    )
    parser.add_argument(
        "--name",
        default="SDK Created Trading Partner",
        help="Trading partner name (default: SDK Created Trading Partner)"
    )
    parser.add_argument(
        "--folder",
        default="Home",
        help="Folder name (default: Home)"
    )
    parser.add_argument(
        "--description",
        default="Trading partner created via Boomi Python SDK",
        help="Trading partner description"
    )
    parser.add_argument(
        "--get",
        metavar="ID",
        help="Get trading partner by ID"
    )
    parser.add_argument(
        "--query",
        action="store_true",
        help="Query all trading partners"
    )
    parser.add_argument(
        "--query-name",
        metavar="PATTERN",
        help="Query trading partners by name pattern (e.g., 'SDK%%')"
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="After creating, verify by getting it back"
    )

    args = parser.parse_args()

    # Print header
    print("🚀 Boomi SDK - Trading Partner Component Example")
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

    created_id = None

    if args.create:
        created_id = create_trading_partner(sdk, args.name, args.folder, args.description)
        if created_id and args.verify:
            print("\n" + "="*70)
            print("🔄 VERIFYING CREATION...")
            print("="*70)
            get_trading_partner(sdk, created_id)

    if args.get:
        get_trading_partner(sdk, args.get)

    if args.query:
        query_trading_partners(sdk)

    if args.query_name:
        query_trading_partners(sdk, args.query_name)

    if not any([args.create, args.get, args.query, args.query_name]):
        parser.print_help()
        return 0

    print("\n" + "="*70)
    print("✅ Trading Partner Example Complete!")
    print("="*70)
    print("\n📚 This example demonstrates:")
    print("   • Creating X12 trading partner components")
    print("   • Retrieving trading partners by ID")
    print("   • Querying trading partner components")
    print("   • Working with trading partner settings")

    return 0


if __name__ == "__main__":
    sys.exit(main())
