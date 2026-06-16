#!/usr/bin/env python3
"""
Boomi SDK Example: Get Component with Full Analysis
==================================================

This example demonstrates comprehensive component retrieval with both 
user-friendly formatted output and detailed technical analysis.

Features:
- Retrieves component by ID with optional version
- Shows formatted metadata (name, type, version, dates, folder)
- Displays full XML configuration analysis
- Provides detailed structural analysis for debugging
- Handles different component types (process, connector, profile, etc.)
- Command-line interface with usage help
- Comprehensive error handling

Requirements:
- Set environment variables: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET
- Or create a .env file with these variables

Usage:
    python get_component.py COMPONENT_ID [OPTIONS]
    
    Arguments:
    COMPONENT_ID    The component ID to retrieve
    
    Options:
    --version=N     Specific version to retrieve (defaults to latest)
    --detailed      Show detailed structural analysis
    --xml-only      Show only XML configuration
    
    Examples:
    python get_component.py 112b4efe-b173-4258-9492-613ead7d52ce
    python get_component.py 112b4efe-b173-4258-9492-613ead7d52ce --version=1
    python get_component.py 112b4efe-b173-4258-9492-613ead7d52ce --detailed
"""

import os
import sys
import xml.etree.ElementTree as ET
from typing import Optional

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

from boomi import Boomi, extract_component_xml_metadata
from boomi.net.transport.api_error import ApiError


def validate_environment() -> tuple[str, str, str]:
    """Validate required environment variables and return credentials"""
    account_id = os.getenv("BOOMI_ACCOUNT")
    username = os.getenv("BOOMI_USER") 
    password = os.getenv("BOOMI_SECRET")
    
    if not all([account_id, username, password]):
        print("❌ Error: Missing required environment variables")
        print("   Please set: BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET")
        print("   You can also create a .env file with these variables")
        sys.exit(1)
    
    return account_id, username, password

def format_date(date_str):
    """Format ISO date string to readable format"""
    if date_str and 'T' in date_str:
        return date_str.split('T')[0] + ' ' + date_str.split('T')[1].split('.')[0]
    return date_str or 'N/A'

def analyze_object_structure(obj, prefix="", max_depth=3, current_depth=0):
    """Recursively analyze object structure for detailed analysis"""
    if current_depth >= max_depth:
        return f"{prefix}... (max depth reached)"
    
    result = []
    
    if isinstance(obj, dict):
        result.append(f"{prefix}Dict with {len(obj)} keys:")
        for key, value in list(obj.items())[:5]:  # Show first 5 keys
            if isinstance(value, (dict, list)):
                result.append(f"{prefix}  • {key}: {type(value).__name__}")
                if current_depth < max_depth - 1:
                    sub_analysis = analyze_object_structure(value, prefix + "    ", max_depth, current_depth + 1)
                    if sub_analysis:
                        result.append(sub_analysis)
            else:
                value_preview = str(value)[:50] + "..." if len(str(value)) > 50 else str(value)
                result.append(f"{prefix}  • {key}: {type(value).__name__} = {value_preview}")
        
        if len(obj) > 5:
            result.append(f"{prefix}  ... and {len(obj) - 5} more keys")
    
    elif isinstance(obj, list):
        result.append(f"{prefix}List with {len(obj)} items:")
        for i, item in enumerate(obj[:3]):  # Show first 3 items
            if isinstance(item, (dict, list)):
                result.append(f"{prefix}  [{i}]: {type(item).__name__}")
                if current_depth < max_depth - 1:
                    sub_analysis = analyze_object_structure(item, prefix + "    ", max_depth, current_depth + 1)
                    if sub_analysis:
                        result.append(sub_analysis)
            else:
                item_preview = str(item)[:50] + "..." if len(str(item)) > 50 else str(item)
                result.append(f"{prefix}  [{i}]: {type(item).__name__} = {item_preview}")
        
        if len(obj) > 3:
            result.append(f"{prefix}  ... and {len(obj) - 3} more items")
    
    else:
        value_preview = str(obj)[:100] + "..." if len(str(obj)) > 100 else str(obj)
        result.append(f"{prefix}{type(obj).__name__}: {value_preview}")
    
    return "\n".join(result)

def print_component_metadata(metadata):
    """Print formatted component metadata information from the raw XML attributes"""
    print("📋 Component Metadata:")
    print("=" * 50)
    print(f"  Name: {metadata.get('name', 'N/A')}")
    print(f"  Component ID: {metadata.get('componentId', 'N/A')}")
    print(f"  Type: {metadata.get('type', 'N/A')}")
    print(f"  Version: {metadata.get('version', 'N/A')}")

    # Status information
    current_version = metadata.get('currentVersion', 'false')
    deleted = metadata.get('deleted', 'false')
    status_parts = []

    if str(current_version).lower() == 'true':
        status_parts.append("CURRENT")
    if str(deleted).lower() == 'true':
        status_parts.append("DELETED")

    if status_parts:
        print(f"  Status: {' | '.join(status_parts)}")

    print(f"  Created: {format_date(metadata.get('createdDate', 'N/A'))} by {metadata.get('createdBy', 'N/A')}")
    print(f"  Modified: {format_date(metadata.get('modifiedDate', 'N/A'))} by {metadata.get('modifiedBy', 'N/A')}")

    # Folder information
    folder_path = metadata.get('folderFullPath') or metadata.get('folderName')
    if folder_path:
        print(f"  Folder: {folder_path}")

    # Branch information
    branch_name = metadata.get('branchName')
    if branch_name and branch_name != 'main':
        print(f"  Branch: {branch_name}")

def _find_child(element, local_name):
    """Find a direct child by local name, ignoring namespaces."""
    for child in element:
        if child.tag.split('}')[-1] == local_name:
            return child
    return None


def _describe_element(element, prefix="", max_depth=3, current_depth=0):
    """Recursively describe an ElementTree element's structure."""
    if current_depth >= max_depth:
        return f"{prefix}... (max depth reached)"

    result = []
    local_tag = element.tag.split('}')[-1]
    children = list(element)
    attr_note = f" [{len(element.attrib)} attrs]" if element.attrib else ""

    if children:
        result.append(f"{prefix}<{local_tag}>{attr_note} ({len(children)} children)")
        for child in children[:5]:
            sub = _describe_element(child, prefix + "  ", max_depth, current_depth + 1)
            result.append(sub)
        if len(children) > 5:
            result.append(f"{prefix}  ... and {len(children) - 5} more")
    else:
        text_preview = (element.text or '').strip()
        if len(text_preview) > 50:
            text_preview = text_preview[:50] + "..."
        suffix = f" = {text_preview}" if text_preview else ""
        result.append(f"{prefix}<{local_tag}>{attr_note}{suffix}")

    return "\n".join(result)


def print_component_xml(root, detailed=False):
    """Print component XML configuration with optional detailed analysis.

    ``root`` is the parsed ElementTree root of the raw component XML.
    """
    print("\n🔧 Component Configuration:")
    print("=" * 50)

    # Check for the <object> configuration element
    obj = _find_child(root, 'object')
    if obj is not None and len(list(obj)):
        print("📄 Component has XML configuration object")

        if detailed:
            # Detailed structural analysis
            print("\n🔍 Detailed XML Structure Analysis:")
            print("-" * 40)
            print(_describe_element(obj))
        else:
            # Basic structure info
            top_children = list(obj)
            print(f"📊 Configuration contains {len(top_children)} top-level elements")
            print("🔑 Top-level configuration elements:")
            for child in top_children:
                local_tag = child.tag.split('}')[-1]
                count = len(list(child))
                if count:
                    print(f"    • {local_tag}: element ({count} children)")
                else:
                    print(f"    • {local_tag}: element")
    else:
        print("❌ No XML configuration object found")

    # Check for encrypted values
    if _find_child(root, 'encryptedValues') is not None:
        print(f"\n🔒 Component has encrypted values configured")

    # Check for process overrides
    if _find_child(root, 'processOverrides') is not None:
        print(f"\n⚙️ Component has process overrides configured")


def print_raw_response_structure(root):
    """Print raw response structure for debugging (top-level XML elements)"""
    print("\n🔍 Raw Response Structure:")
    print("-" * 40)
    for child in root:
        local_tag = child.tag.split('}')[-1]
        count = len(list(child))
        print(f"  {local_tag}: element ({count} children)")
        if local_tag == 'object' and count:
            print("    📄 XML Configuration Object Found!")

def get_component(component_id, version=None, detailed=False, xml_only=False):
    """Retrieve and display component with specified options"""
    
    # Validate environment variables
    account_id, username, password = validate_environment()
    
    if not xml_only:
        print(f"🏢 Account: {account_id}")
        print(f"👤 User: {username}")
        print(f"🎯 Target Component ID: {component_id}")
        if version:
            print(f"📌 Specific Version: {version}")
        else:
            print(f"📌 Version: Latest")
    
    # Initialize SDK
    try:
        sdk = Boomi(
            account_id=account_id,
            username=username,
            password=password,
            timeout=30000
        )
        if not xml_only:
            print("✅ SDK initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize SDK: {e}")
        return False
    
    if not xml_only:
        print(f"\n🔍 Retrieving component...")
    
    try:
        # Construct component identifier
        if version:
            component_identifier = f"{component_id}~{version}"
        else:
            component_identifier = component_id
        
        # Get the component - response IS the raw XML bytes
        result = sdk.component.get_component(component_id=component_identifier)

        if not xml_only:
            print("✅ Component retrieved successfully!")
            print(f"📊 Response type: {type(result).__name__} ({len(result)} bytes)")

        # Parse the raw XML ourselves (the SDK never parses component XML)
        try:
            root = ET.fromstring(result)
        except ET.ParseError as e:
            print(f"❌ Failed to parse component XML: {e}")
            return False

        # Read root <Component> attributes via the read-only metadata helper
        metadata = extract_component_xml_metadata(result)

        if xml_only:
            # Only show XML configuration
            print_component_xml(root, detailed=detailed)
        else:
            # Show metadata
            print_component_metadata(metadata)

            # Show XML configuration
            print_component_xml(root, detailed=detailed)

            # Show raw structure if detailed mode
            if detailed:
                print_raw_response_structure(root)

            print(f"\n🎉 SUCCESS!")
            print(f"📍 Component '{metadata.get('name', 'N/A')}' retrieved successfully")
            print(f"🔧 Component contains full XML configuration for deployment/analysis")

        return True

    except ApiError as e:
        error_msg = str(e)
        print(f"❌ Component retrieval failed: {error_msg}")
        
        # Provide helpful troubleshooting hints
        if "404" in error_msg or "not found" in error_msg.lower():
            print("🔍 Component not found - check the component ID")
            print("💡 Use list_all_components.py to find valid component IDs")
        elif "403" in error_msg:
            print("🔍 Permission issue - check your API credentials and account permissions")
        elif "400" in error_msg:
            print("🔍 Bad request - check component ID format")
            if version:
                print("💡 Version format should be a number (e.g., 1, 2, 3)")
        elif "401" in error_msg:
            print("🔍 Authentication failed - verify your credentials")
        else:
            print("🔍 Check network connectivity and API endpoint availability")
            
        return False

def main():
    """Main entry point with argument parsing"""
    if len(sys.argv) < 2:
        print("❌ Error: Component ID is required")
        print("\nUsage:")
        print(f"  {sys.argv[0]} COMPONENT_ID [OPTIONS]")
        print("\nOptions:")
        print("  --version=N     Specific version to retrieve")
        print("  --detailed      Show detailed structural analysis")
        print("  --xml-only      Show only XML configuration")
        print("\nExamples:")
        print(f"  {sys.argv[0]} 112b4efe-b173-4258-9492-613ead7d52ce")
        print(f"  {sys.argv[0]} 112b4efe-b173-4258-9492-613ead7d52ce --version=1")
        print(f"  {sys.argv[0]} 112b4efe-b173-4258-9492-613ead7d52ce --detailed")
        print(f"  {sys.argv[0]} 112b4efe-b173-4258-9492-613ead7d52ce --xml-only")
        print("\n💡 Use list_all_components.py to find component IDs")
        return
    
    component_id = sys.argv[1]
    
    # Parse options
    version = None
    detailed = False
    xml_only = False
    
    for arg in sys.argv[2:]:
        if arg.startswith('--version='):
            version = arg.split('=')[1]
        elif arg == '--detailed':
            detailed = True
        elif arg == '--xml-only':
            xml_only = True
        else:
            print(f"❌ Unknown option: {arg}")
            return
    
    if not xml_only:
        print("🚀 Boomi SDK Example: Get Component")
        print("=" * 45)
        if detailed:
            print("🔍 Mode: Detailed Analysis")
        print()
    
    success = get_component(component_id, version, detailed, xml_only)
    
    if not xml_only:
        print(f"\n{'='*45}")
        if success:
            print("🌟 Component retrieval completed successfully!")
        else:
            print("💥 Component retrieval encountered issues")

if __name__ == "__main__":
    main()