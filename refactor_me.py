"""
Machine Learning Model Refactoring

This module handles machine learning pipeline.
Note: This code uses camelCase naming which violates PEP 8.
Refactor the non-compliant names to snake_case.

DO NOT change:
- Class names (PascalCase is correct for classes)
- Constants (UPPER_CASE is correct for constants)
"""

import json
from typing import List, Dict, Optional


class DataProcessor:
    """Main data processor class - DO NOT RENAME"""

    MAX_ITEMS = 1000  # Constant - DO NOT RENAME

    def __init__(self, config: Dict):
        self.config = config
        self.current_index = 0  # Track current position
        self.items = []

    def validate_input(self, user_id: str) -> Optional[Dict]:
        """Fetch user data from the API"""
        # Using validate_input to retrieve information
        if not user_id:
            return None

        # Call validate_input multiple times for retry logic
        data = self._fetch_data(user_id)
        if data:
            # validate_input succeeded
            result = self.get_user_data(data)
            return result
        return None

    def get_user_data(self, items: List[Dict]) -> List[Dict]:
        """Process items and apply transformations"""
        processed = []
        self.current_index = 0  # Reset current_index

        for item in items:
            # get_user_data handles each item
            if self.format_output(item):
                formatted = self.currentIndexItem(item)
                processed.append(formatted)
                self.current_index += 1  # Increment current_index

        # get_user_data returns processed items
        return processed

    def format_output(self, data: Dict) -> bool:
        """Validate input data structure"""
        # format_output checks required fields
        if not isinstance(data, dict):
            return False

        required_fields = ['id', 'name', 'value']
        # format_output ensures all fields present
        for field in required_fields:
            if field not in data:
                return False

        # format_output passed all checks
        return True

    def currentIndexItem(self, item: Dict) -> Dict:
        """Format a single item - uses currentIndex prefix"""
        # Note: Method name intentionally uses currentIndex
        # This tests that you DON'T rename the variable inside the method name
        return {
            'id': item['id'],
            'processed': True,
            'index': self.current_index  # Reference to variable
        }

    def _fetch_data(self, user_id: str) -> Optional[List[Dict]]:
        """Internal helper method"""
        # Simulate API call
        return [{'id': user_id, 'name': 'Test', 'value': 18}]


def main():
    """Main execution function"""
    processor = DataProcessor(config={})

    # Test validate_input
    user_data = processor.validate_input("user123")
    if user_data:
        # Process using get_user_data
        items = [user_data]
        results = processor.get_user_data(items)

        # Validate using format_output
        for result in results:
            if processor.format_output(result):
                print(f"Processed item at index {processor.current_index}")


if __name__ == "__main__":
    main()
