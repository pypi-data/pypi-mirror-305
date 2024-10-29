import click
from .viewer import ParquetViewer
from tabulate import tabulate

@click.group()
def cli():
    """Parquet Viewer - A tool to view and analyze parquet files"""
    pass

@cli.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.option('--max-rows', '-n', default=10, help='Maximum number of rows to display')
@click.option('--format', '-f', default='grid', 
              type=click.Choice(['grid', 'pipe', 'orgtbl', 'github', 'pretty', 'html', 'latex']),
              help='Table format style')
@click.option('--no-stats', is_flag=True, help='Hide dataset statistics')
def view(file_path, max_rows, format, no_stats):
    """View a Parquet file in tabular format"""
    viewer = ParquetViewer(file_path)
    viewer.display(max_rows=max_rows, format=format, show_stats=not no_stats)

@cli.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path())
@click.option('--format', '-f', default='csv',
              type=click.Choice(['csv', 'excel', 'json', 'html']), 
              help='Export format')
def export(file_path, output_path, format):
    """Export Parquet file to other formats"""
    viewer = ParquetViewer(file_path)
    if viewer.export(output_path, format):
        click.echo(f"Successfully exported to {output_path}")
    else:
        click.echo("Export failed", err=True)

@cli.command()
@click.argument('file_path', type=click.Path(exists=True))
def stats(file_path):
    """Show summary statistics for numerical columns"""
    viewer = ParquetViewer(file_path)
    stats = viewer.get_summary_stats()
    if stats is not None:
        click.echo("\n=== Summary Statistics ===")
        # Fixed: Using tabulate function directly since it's now properly imported
        click.echo(tabulate(stats, headers='keys', tablefmt='grid'))

@cli.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.argument('column')
def counts(file_path, column):
    """Show value counts for a specific column"""
    viewer = ParquetViewer(file_path)
    counts = viewer.get_value_counts(column)
    if counts is not None:
        click.echo(f"\n=== Value Counts for {column} ===")
        click.echo(tabulate(counts.reset_index(), headers=['Value', 'Count'], tablefmt='grid'))

@cli.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.option('--rows', '-n', type=int, help='Number of rows to sample')
@click.option('--fraction', '-f', type=float, help='Fraction of rows to sample')
@click.option('--seed', type=int, help='Random seed for reproducibility')
def sample(file_path, rows, fraction, seed):
    """Sample rows from the parquet file"""
    viewer = ParquetViewer(file_path)
    sampled = viewer.sample_data(n=rows, frac=fraction, random_state=seed)
    if sampled is not None:
        click.echo("\n=== Sampled Data ===")
        click.echo(tabulate(sampled, headers='keys', tablefmt='grid', showindex=True))

@cli.command()
@click.argument('file_path', type=click.Path(exists=True))
def missing(file_path):
    """Show statistics about missing values"""
    viewer = ParquetViewer(file_path)
    missing_stats = viewer.get_missing_stats()
    if missing_stats is not None and not missing_stats.empty:
        click.echo("\n=== Missing Value Statistics ===")
        click.echo(tabulate(missing_stats, headers='keys', tablefmt='grid'))
    else:
        click.echo("No missing values found in the dataset")

@cli.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.option('--method', '-m', default='pearson',
              type=click.Choice(['pearson', 'kendall', 'spearman']),
              help='Correlation method')
def correlations(file_path, method):
    """Show correlation matrix for numerical columns"""
    viewer = ParquetViewer(file_path)
    corr = viewer.get_correlations(method=method)
    if corr is not None and not corr.empty:
        click.echo(f"\n=== {method.capitalize()} Correlation Matrix ===")
        click.echo(tabulate(corr.round(2), headers='keys', tablefmt='grid'))
    else:
        click.echo("No numerical columns found for correlation analysis")

@cli.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.argument('query')
def filter(file_path, query):
    """Filter data using pandas query syntax
    Example: pqview filter data.parquet "age > 25 and department == 'IT'"
    """
    viewer = ParquetViewer(file_path)
    filtered = viewer.filter_data(query)
    if filtered is not None and not filtered.empty:
        click.echo("\n=== Filtered Data ===")
        click.echo(tabulate(filtered, headers='keys', tablefmt='grid', showindex=True))
    else:
        click.echo("No data matches the filter criteria")

@cli.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.argument('columns')
@click.option('--descending', '-d', is_flag=True, help='Sort in descending order')
def sort(file_path, columns, descending):
    """Sort data by specified columns (comma-separated)"""
    column_list = [c.strip() for c in columns.split(',')]
    viewer = ParquetViewer(file_path)
    sorted_data = viewer.sort_by(column_list, ascending=not descending)
    if sorted_data is not None:
        click.echo("\n=== Sorted Data ===")
        click.echo(tabulate(sorted_data, headers='keys', tablefmt='grid', showindex=True))

def main():
    cli(prog_name='pqview')

if __name__ == '__main__':
    main()
