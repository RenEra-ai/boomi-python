#!/usr/bin/env python3
"""
Full Document Retrieval Chain Example

Demonstrates the complete 4-step workflow for retrieving document payloads
from Boomi process executions, mirroring the Process Reporting UI experience:

  Step 1: Query ExecutionRecord — find recent process executions
  Step 2: Query ExecutionConnector — list connector shapes per execution
  Step 3: Query GenericConnectorRecord — list documents per connector
  Step 4: Download ConnectorDocument — fetch actual document content

Usage:
  # Run the full chain for the most recent execution
  python full_document_retrieval_chain.py

  # Specify an execution ID
  python full_document_retrieval_chain.py --execution-id EXECUTION_ID

  # Save downloaded documents to a directory
  python full_document_retrieval_chain.py --output-dir ./downloads

Environment Variables Required:
  BOOMI_ACCOUNT - Boomi account ID
  BOOMI_USER    - Boomi username
  BOOMI_SECRET  - Boomi password/token
"""

import os
import sys
import argparse
from datetime import datetime, timedelta

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'src'))

from boomi import Boomi
from boomi.models import (
    ConnectorDocument,
    ExecutionRecordQueryConfig,
    ExecutionRecordQueryConfigQueryFilter,
    ExecutionRecordSimpleExpression,
    ExecutionRecordSimpleExpressionOperator,
    ExecutionRecordSimpleExpressionProperty,
    ExecutionConnectorQueryConfig,
    ExecutionConnectorQueryConfigQueryFilter,
    ExecutionConnectorSimpleExpression,
    ExecutionConnectorSimpleExpressionOperator,
    ExecutionConnectorSimpleExpressionProperty,
    GenericConnectorRecordQueryConfig,
    GenericConnectorRecordQueryConfigQueryFilter,
    GenericConnectorRecordSimpleExpression,
    GenericConnectorRecordSimpleExpressionOperator,
    GenericConnectorRecordSimpleExpressionProperty,
)


class DocumentRetrievalChain:
    """Walks through the full 4-step document retrieval chain."""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.sdk = Boomi(
            account_id=os.environ.get('BOOMI_ACCOUNT'),
            username=os.environ.get('BOOMI_USER'),
            password=os.environ.get('BOOMI_SECRET'),
            timeout=30000,
        )

    def step1_find_executions(self, days: int = 7, limit: int = 5):
        """Step 1: Query ExecutionRecord to find recent executions."""
        print(f"\n--- Step 1: Finding executions from last {days} days ---")

        query_expression = ExecutionRecordSimpleExpression(
            operator=ExecutionRecordSimpleExpressionOperator.GREATERTHAN,
            property=ExecutionRecordSimpleExpressionProperty.EXECUTIONTIME,
            argument=[(datetime.now() - timedelta(days=days)).strftime('%Y-%m-%dT%H:%M:%SZ')],
        )
        query_config = ExecutionRecordQueryConfig(
            query_filter=ExecutionRecordQueryConfigQueryFilter(expression=query_expression)
        )

        result = self.sdk.execution_record.query_execution_record(request_body=query_config)

        executions = []
        if result and hasattr(result, 'result') and result.result:
            for rec in result.result[:limit]:
                info = {
                    'execution_id': getattr(rec, 'execution_id', None),
                    'process_name': getattr(rec, 'process_name', 'N/A'),
                    'status': getattr(rec, 'status', 'N/A'),
                    'execution_time': getattr(rec, 'execution_time', 'N/A'),
                }
                executions.append(info)
                if self.verbose:
                    print(f"  {info['process_name']} | {info['status']} | {info['execution_id']}")

        print(f"Found {len(executions)} execution(s)")
        return executions

    def step2_list_connectors(self, execution_id: str):
        """Step 2: Query ExecutionConnector to list connector shapes."""
        print(f"\n--- Step 2: Listing connectors for execution {execution_id} ---")

        query_expression = ExecutionConnectorSimpleExpression(
            operator=ExecutionConnectorSimpleExpressionOperator.EQUALS,
            property=ExecutionConnectorSimpleExpressionProperty.EXECUTIONID,
            argument=[execution_id],
        )
        query_config = ExecutionConnectorQueryConfig(
            query_filter=ExecutionConnectorQueryConfigQueryFilter(expression=query_expression)
        )

        result = self.sdk.execution_connector.query_execution_connector(request_body=query_config)

        connectors = []
        if result and hasattr(result, 'result') and result.result:
            for conn in result.result:
                info = {
                    'id': getattr(conn, 'id_', None),
                    'connector_type': getattr(conn, 'connector_type', 'N/A'),
                    'action_type': getattr(conn, 'action_type', 'N/A'),
                    'success_count': getattr(conn, 'success_count', 0),
                    'error_count': getattr(conn, 'error_count', 0),
                }
                connectors.append(info)
                if self.verbose:
                    print(f"  {info['connector_type']} {info['action_type']} "
                          f"| ok={info['success_count']} err={info['error_count']}")

        print(f"Found {len(connectors)} connector(s)")
        return connectors

    def step3_list_documents(self, execution_id: str, limit: int = 10):
        """Step 3: Query GenericConnectorRecord to list individual documents."""
        print(f"\n--- Step 3: Listing document records for execution {execution_id} ---")

        query_expression = GenericConnectorRecordSimpleExpression(
            operator=GenericConnectorRecordSimpleExpressionOperator.EQUALS,
            property=GenericConnectorRecordSimpleExpressionProperty.EXECUTIONID,
            argument=[execution_id],
        )
        query_config = GenericConnectorRecordQueryConfig(
            query_filter=GenericConnectorRecordQueryConfigQueryFilter(expression=query_expression)
        )

        result = self.sdk.generic_connector_record.query_generic_connector_record(
            request_body=query_config
        )

        records = []
        if result and hasattr(result, 'result') and result.result:
            for rec in result.result[:limit]:
                info = {
                    'id': getattr(rec, 'id_', None),
                    'connection_name': getattr(rec, 'connection_name', 'N/A'),
                    'operation_name': getattr(rec, 'operation_name', 'N/A'),
                    'status': getattr(rec, 'status', 'N/A'),
                    'size': getattr(rec, 'size', 0),
                }
                records.append(info)
                if self.verbose:
                    print(f"  {info['connection_name']} / {info['operation_name']} "
                          f"| {info['status']} | {info['size']} KB | {info['id']}")

        print(f"Found {len(records)} document record(s)")
        return records

    def step4_download_document(self, record_id: str, output_path: str = None) -> bytes:
        """Step 4: Download actual document content via ConnectorDocument."""
        print(f"\n--- Step 4: Downloading document {record_id} ---")

        document = ConnectorDocument(generic_connector_record_id=record_id)
        content = self.sdk.connector_document.download_connector_document(
            request_body=document
        )

        print(f"Downloaded {len(content)} bytes")

        if output_path:
            with open(output_path, 'wb') as f:
                f.write(content)
            print(f"Saved to: {output_path}")

        # Show preview for text content
        try:
            text = content.decode('utf-8')
            preview = text[:300]
            if len(text) > 300:
                preview += '...'
            print(f"Preview:\n{preview}")
        except UnicodeDecodeError:
            print(f"(Binary content, {len(content)} bytes)")

        return content

    def run_full_chain(self, execution_id: str = None, output_dir: str = None,
                       days: int = 7, max_documents: int = 3):
        """Run the complete 4-step retrieval chain."""
        # Step 1: Find an execution
        if not execution_id:
            executions = self.step1_find_executions(days=days)
            if not executions:
                print("No executions found.")
                return
            execution_id = executions[0]['execution_id']
            print(f"Using execution: {executions[0]['process_name']} ({execution_id})")

        # Step 2: List connector shapes
        connectors = self.step2_list_connectors(execution_id)

        # Step 3: List document records
        records = self.step3_list_documents(execution_id, limit=max_documents)
        if not records:
            print("No document records found for this execution.")
            return

        # Step 4: Download documents
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        for i, record in enumerate(records[:max_documents]):
            output_path = None
            if output_dir:
                output_path = os.path.join(output_dir, f"document_{i+1}_{record['id']}")

            try:
                self.step4_download_document(record['id'], output_path=output_path)
            except Exception as e:
                print(f"Failed to download {record['id']}: {e}")

        print(f"\nChain complete. Processed {len(records)} document(s).")


def main():
    parser = argparse.ArgumentParser(
        description='Full 4-step document retrieval chain for Boomi executions',
    )
    parser.add_argument('--execution-id', help='Specific execution ID (skips Step 1)')
    parser.add_argument('--output-dir', help='Directory to save downloaded documents')
    parser.add_argument('--days', type=int, default=7, help='Days to look back (default: 7)')
    parser.add_argument('--max-documents', type=int, default=3,
                        help='Max documents to download (default: 3)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')

    args = parser.parse_args()

    chain = DocumentRetrievalChain(verbose=args.verbose)
    chain.run_full_chain(
        execution_id=args.execution_id,
        output_dir=args.output_dir,
        days=args.days,
        max_documents=args.max_documents,
    )


if __name__ == '__main__':
    main()
