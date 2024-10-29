import pandas as pd
from tabulate import tabulate
import os

class ParquetViewer:
    def __init__(self, file_path):
        self.file_path = file_path
        self._df = None
        self.MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB in bytes
        self.available_formats = {
            'grid': 'ASCII grid table',
            'pipe': 'Markdown-compatible table',
            'orgtbl': 'Org-mode table',
            'github': 'GitHub-flavored Markdown table',
            'pretty': 'Pretty printed table',
            'html': 'HTML table',
            'latex': 'LaTeX table'
        }

    def load_file(self):
        """Load the parquet file into a pandas DataFrame"""
        try:
            # Check file size before loading
            file_size = os.path.getsize(self.file_path)
            if file_size > self.MAX_FILE_SIZE:
                print(f"File size ({file_size / 1024 / 1024:.2f} MB) exceeds maximum allowed size (5 MB)")
                return False
                
            self._df = pd.read_parquet(self.file_path)
            return True
        except Exception as e:
            print(f"Error loading parquet file: {e}")
            return False

    def display(self, max_rows=50, format="grid", show_stats=True, columns=None):
        """Display the parquet file contents in tabular format with optional statistics"""
        if self._df is None:
            if not self.load_file():
                return
            
        # Filter columns if specified
        display_df = self._df[columns] if columns else self._df
        
        # Get basic information about the DataFrame
        total_rows = len(display_df)
        total_cols = len(display_df.columns)
        memory_usage = display_df.memory_usage(deep=True).sum() / 1024 / 1024  # MB
        
        if show_stats:
            print("\n=== Dataset Statistics ===")
            print(f"Total rows: {total_rows:,}")
            print(f"Total columns: {total_cols}")
            print(f"Memory usage: {memory_usage:.2f} MB")
            print(f"\nColumn types:")
            for col, dtype in display_df.dtypes.items():
                print(f"  - {col}: {dtype}")
            print("\n=== Data Preview ===")
        
        # Show the data in tabular format
        if max_rows and max_rows < total_rows:
            half_rows = max_rows // 2
            ellipsis_row = pd.DataFrame(
                {col: ['...'] for col in display_df.columns},
                index=['...']
            )
            display_df = pd.concat([
                display_df.head(half_rows),
                ellipsis_row,
                display_df.tail(half_rows)
            ])
        else:
            display_df = self._df

        print(tabulate(display_df, headers='keys', tablefmt=format, showindex=True))

    def export(self, output_path, format='csv'):
        """Export the data to various formats"""
        if self._df is None:
            if not self.load_file():
                return False

        try:
            format = format.lower()
            if format == 'csv':
                self._df.to_csv(output_path, index=False)
            elif format == 'excel':
                self._df.to_excel(output_path, index=False)
            elif format == 'json':
                self._df.to_json(output_path, orient='records')
            elif format == 'html':
                self._df.to_html(output_path, index=False)
            else:
                raise ValueError(f"Unsupported export format: {format}")
            return True
        except Exception as e:
            print(f"Error exporting file: {e}")
            return False

    def get_summary_stats(self):
        """Get summary statistics for numerical columns"""
        if self._df is None:
            if not self.load_file():
                return None
        return self._df.describe()

    def get_dataframe(self):
        """Return the underlying pandas DataFrame"""
        if self._df is None:
            self.load_file()
        return self._df

    def filter_data(self, conditions):
        """Filter data based on conditions
        Example: viewer.filter_data("age > 25 and country == 'USA'")
        """
        if self._df is None:
            if not self.load_file():
                return None
        try:
            return self._df.query(conditions)
        except Exception as e:
            print(f"Error applying filter: {e}")
            return None

    def sort_by(self, columns, ascending=True):
        """Sort data by specified columns"""
        if self._df is None:
            if not self.load_file():
                return None
        try:
            return self._df.sort_values(columns, ascending=ascending)
        except Exception as e:
            print(f"Error sorting data: {e}")
            return None

    def get_value_counts(self, column):
        """Get unique values and their counts for a specific column"""
        if self._df is None:
            if not self.load_file():
                return None
        try:
            return self._df[column].value_counts()
        except Exception as e:
            print(f"Error getting value counts: {e}")
            return None

    def sample_data(self, n=None, frac=None, random_state=None):
        """Return a random sample of rows"""
        if self._df is None:
            if not self.load_file():
                return None
        try:
            return self._df.sample(n=n, frac=frac, random_state=random_state)
        except Exception as e:
            print(f"Error sampling data: {e}")
            return None

    def get_missing_stats(self):
        """Get statistics about missing values in each column"""
        if self._df is None:
            if not self.load_file():
                return None
        try:
            missing_stats = pd.DataFrame({
                'missing_count': self._df.isnull().sum(),
                'missing_percentage': (self._df.isnull().sum() / len(self._df) * 100).round(2)
            })
            return missing_stats[missing_stats['missing_count'] > 0]
        except Exception as e:
            print(f"Error calculating missing stats: {e}")
            return None

    def convert_column_type(self, column, dtype):
        """Convert data type of a specific column"""
        if self._df is None:
            if not self.load_file():
                return False
        try:
            self._df[column] = self._df[column].astype(dtype)
            return True
        except Exception as e:
            print(f"Error converting column type: {e}")
            return False

    def get_correlations(self, method='pearson'):
        """Get correlation matrix for numerical columns"""
        if self._df is None:
            if not self.load_file():
                return None
        try:
            numeric_cols = self._df.select_dtypes(include=['int64', 'float64']).columns
            return self._df[numeric_cols].corr(method=method)
        except Exception as e:
            print(f"Error calculating correlations: {e}")
            return None
