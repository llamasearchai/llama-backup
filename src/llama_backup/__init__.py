"""
llama_backup: Advanced secure backup management system with ML capabilities.

This package provides tools for creating, managing, and verifying backups
with advanced security, ML-powered deduplication, and lifecycle management.
"""

# Imports for missing files commented out/removed:
# from .backup import BackupJob, BackupMetadata, BackupVault, RetentionPolicy, StorageTier
# from .ml import AnomalyDetector, MLXCompressor, NeuralDeduplication

from .security import BlockchainVerifier, SecurityManager
from .storage import FileSystemStorage, StorageBackend

__version__ = "0.1.0"
__all__ = [
    # Removed due to missing files:
    # "BackupVault",
    # "BackupMetadata",
    # "BackupJob",
    # "StorageTier",
    # "RetentionPolicy",
    # "MLXCompressor",
    # "NeuralDeduplication",
    # "AnomalyDetector",
    "StorageBackend",
    "FileSystemStorage",
    "SecurityManager",
    "BlockchainVerifier",
]
