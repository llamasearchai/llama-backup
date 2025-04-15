"""Tests for the llama-backup package."""

import pytest
from typer.testing import CliRunner

# Try importing the package and CLI app
try:
    import llama_backup
    from llama_backup.cli import app as cli_app
except ImportError as e:
    pytest.fail(f"Failed to import llama_backup or cli_app: {e}", pytrace=False)

runner = CliRunner()


def test_import():
    """Test that the main package can be imported."""
    assert llama_backup is not None


def test_version():
    """Test that the package has a version attribute."""
    assert hasattr(llama_backup, "__version__")
    assert isinstance(llama_backup.__version__, str)


def test_cli_version():
    """Test the CLI --version option."""
    result = runner.invoke(cli_app, ["--version"])
    assert result.exit_code == 0
    assert llama_backup.__version__ in result.stdout


def test_cli_run_job_placeholder():
    """Test the placeholder run-job command."""
    result = runner.invoke(cli_app, ["run-job", "my-job", "--config", "dummy.yaml"])
    assert result.exit_code == 0
    assert "Running backup job 'my-job'" in result.stdout
    assert "(Placeholder: Implement actual job execution)" in result.stdout


def test_cli_list_placeholder():
    """Test the placeholder list command."""
    result = runner.invoke(cli_app, ["list", "file:///tmp/backups"])
    assert result.exit_code == 0
    assert "Listing backups at 'file:///tmp/backups'" in result.stdout
    assert "(Placeholder: Implement actual listing logic)" in result.stdout


def test_cli_restore_placeholder():
    """Test the placeholder restore command."""
    result = runner.invoke(
        cli_app,
        [
            "restore",
            "--source",
            "file:///tmp/backups/latest.bak",
            "--output",
            "/tmp/restore_here",
            "--type",
            "files",
        ],
    )
    assert result.exit_code == 0
    assert "Restoring from 'file:///tmp/backups/latest.bak'" in result.stdout
    assert "(Placeholder: Implement actual restore logic)" in result.stdout


# Add more tests later:
# - Test configuration loading
# - Test specific source handlers (e.g., FilesystemSource, PostgresSource) with mocks
# - Test specific destination handlers (e.g., LocalDestination, S3Destination) with mocks/localstack
# - Test compression/decompression
# - Test scheduler integration
# - Test end-to-end backup and restore jobs using temporary files/directories and mocks
