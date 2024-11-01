import os
import click
from .commands import op_create, op_upload, op_view, op_download
from .constants import MF_CLIENT, MF_UPLOAD_EXECUTABLE, MF_DOWNLOAD_EXECUTABLE, FileType


# ========================== Command-Line Interface (CLI) Entry Point ==========================
@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """OPTIMA Data Management CLI: Easily manage your optimization research data."""

    def _check_required_resource(resource_name: str, resource_path: str) -> None:
        """Check if the specified resource exists and raise an error if it does not."""
        if not os.path.exists(resource_path):
            raise FileNotFoundError(f"Missing resource '{resource_name}', please contact support.")

    def _check_mediaflux_resources():
        """Check essential MediaFlux resources."""
        _check_required_resource("Unimelb MediaFlux Client", MF_CLIENT)
        _check_required_resource("MediaFlux Upload Exectuable", MF_UPLOAD_EXECUTABLE)
        _check_required_resource("MediaFlux Download Exectuable", MF_DOWNLOAD_EXECUTABLE)

    try:
        _check_mediaflux_resources()
        if ctx.invoked_subcommand is None:
            click.echo(ctx.get_help())
    except FileNotFoundError as e:
        click.echo(click.style("ERROR:", fg="red") + f" {str(e)}")
        ctx.exit(1)

# ========================== CLI: View Commands ==========================
@cli.command(help="View a List of Available Problems.")
def view_problems():
    """Display a list of all available problems."""
    op_view.view_problems()

@cli.command(help="View a List of Available Problem Types.")
def view_problem_types():
    """Display a list of all available problem types."""
    op_view.view_problem_types()


# ========================== CLI: Upload Commands ==========================
@cli.command(help="Add Any Research Files to a Selected Problem.")
@click.option("--username", "-u", help="MediaFlux Username")
@click.option("--problem", "-prob", help="Problem Abbreviation")
@click.option("--path", "-p", help="File or Directory Path")
def upload(username, problem, path):
    """Upload any research files to the system."""
    op_upload.upload(file_path=path, username=username, problem_abbr_name=problem)


@cli.command(help="Add Instances Files to a Selected Problem.")
@click.option("--username", "-u", help="MediaFlux Username")
@click.option("--problem", "-prob", help="Problem Abbreviation")
@click.option("--path", "-p", help="File or Directory Path")
def upload_instances(username, problem, path):
    """Upload instance file(s) to the system."""
    op_upload.upload(file_type=FileType.INSTANCE, file_path=path, username=username, problem_abbr_name=problem)


@cli.command(help="Add README File to a Selected Problem.")
@click.option("--username", "-u", help="MediaFlux Username")
@click.option("--problem", "-prob", help="Problem Abbreviation")
@click.option("--path", "-p", help="File or Directory Path")
def upload_readme(username, problem, path):
    """Upload a readme file to the system."""
    op_upload.upload(file_type=FileType.README, file_path=path, username=username, problem_abbr_name=problem)


@cli.command(help="Add Metadata File to a Selected Problem.")
@click.option("--username", "-u", help="MediaFlux Username")
@click.option("--problem", "-prob", help="Problem Abbreviation")
@click.option("--path", "-p", help="File or Directory Path")
def upload_metadata(username, problem, path):
    """Upload a metadata file to the system."""
    op_upload.upload(file_type=FileType.METADATA, file_path=path, username=username, problem_abbr_name=problem)


# ========================== CLI: Create Commands ==========================
@cli.command(help="Set Up a New Research Problem.")
@click.option("--username", "-u", help="MediaFlux Username")
def create(username):
    """Create a new problem in the system."""
    op_create.create_problem(username=username)


# ========================== CLI: Download Commands ==========================
@cli.command(help="Get Research Files from a Selected Problem.")
@click.option("--username", "-u", help="MediaFlux Username")
@click.argument("file_id", required=False)
@click.argument("output_path", required=False, type=click.Path(writable=True))
def download(file_id, output_path):
    """Download any research file(s) from the system."""
    try:
        # result = mediaflux_service.download_from_mediaflux(file_id, output_path)
        result = op_download.download(file_id, output_path)
        click.echo(f"Successfully downloaded file with ID: {file_id}")
        click.echo(f"Download result: {result}")
    except FileNotFoundError:
        click.echo(f"File with ID {file_id} not found in Mediaflux.")
    except PermissionError:
        click.echo(f"Permission denied for output path: {output_path}")
    except Exception as e:
        click.echo(f"Error downloading file: {e}")


if __name__ == "__main__":
    cli()
