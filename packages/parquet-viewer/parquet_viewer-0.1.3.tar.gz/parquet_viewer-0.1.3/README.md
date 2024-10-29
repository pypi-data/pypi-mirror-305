# Parquet Viewer

A powerful command-line tool for viewing, analyzing, and manipulating Parquet files with ease.

## Features

- 📊 View Parquet files in various table formats
- 📤 Export to different formats (CSV, Excel, JSON, HTML)
- 📈 Display dataset statistics and summaries
- 🔍 Filter and sort data
- 📉 Analyze correlations and missing values
- 🎲 Sample data randomly
- 💾 Memory-efficient handling of large files
- 🎨 Multiple display format options

## Installation

```bash
pip install parquet-viewer
```

## Usage

### Basic Commands

#### View Parquet File
```bash
# Basic viewing
pqview view data.parquet

# Customize display
pqview view data.parquet --max-rows 20 --format github
pqview view data.parquet -n 50 -f pretty --no-stats
```

#### Export to Other Formats
```bash
# Export to CSV
pqview export data.parquet output.csv

# Export to other formats
pqview export data.parquet output.xlsx --format excel
pqview export data.parquet output.json --format json
pqview export data.parquet output.html --format html
```

### Analysis Commands

#### Summary Statistics
```bash
# Show summary statistics for numerical columns
pqview stats data.parquet
```

#### Value Counts
```bash
# Show value counts for a specific column
pqview counts data.parquet column_name
```

#### Missing Values Analysis
```bash
# Show statistics about missing values
pqview missing data.parquet
```

#### Correlation Analysis
```bash
# Show correlation matrix
pqview correlations data.parquet

# Use different correlation methods
pqview correlations data.parquet --method spearman
```

### Data Manipulation Commands

#### Filter Data
```bash
# Filter data using pandas query syntax
pqview filter data.parquet "age > 25 and department == 'IT'"
```

#### Sort Data
```bash
# Sort by single column
pqview sort data.parquet "salary"

# Sort by multiple columns
pqview sort data.parquet "department,salary" --descending
```

#### Sample Data
```bash
# Sample specific number of rows
pqview sample data.parquet --rows 100

# Sample by fraction
pqview sample data.parquet --fraction 0.1 --seed 42
```

## Display Formats

The tool supports various display formats for tables:

| Format  | Description |
|---------|-------------|
| grid    | ASCII grid table |
| pipe    | Markdown-compatible table |
| orgtbl  | Org-mode table |
| github  | GitHub-flavored Markdown table |
| pretty  | Pretty printed table |
| html    | HTML table |
| latex   | LaTeX table |

## Export Formats

Supported export formats:
- CSV
- Excel
- JSON
- HTML

## File Size Limits

By default, the tool has a 5MB file size limit to prevent memory issues. This can be adjusted in the configuration.

## Error Handling

The tool provides clear error messages for common issues:
- File not found
- Invalid file format
- Memory limitations
- Invalid query syntax
- Data type conversion errors

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Author

Ashutosh Bele

## Changelog

### v0.1.0
- Initial release
- Basic viewing and export functionality
- Statistical analysis features
- Data manipulation capabilities