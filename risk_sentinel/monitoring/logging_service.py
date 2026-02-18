import logging
from typing import Any

logger = logging.getLogger(__name__)

class LoggingService:
    """Handles centralized logging for the Risk Sentinel system.

    Attributes:
        log_level: The current logging level.
    """
    
    def __init__(self, log_level: str = 'INFO'):
        self.log_level = log_level
        # Initialize logger with basic configuration
        logging.basicConfig(
            level=self.log_level,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

    def log_event(self, event_name: str, message: str, metadata: Optional[Dict[str, Any]] = None) -> None:
        """Logs an event with optional metadata.

        Args:
            event_name: Name of the event.
            message: Description of the event.
            metadata: Additional information about the event.
        """
        log_message = f"{event_name}: {message}"
        if metadata:
            log_message += f" - Metadata: {metadata}"
        
        logger.log(self._get_log_level(), log_message)

    def _get_log_level(self) -> int:
        """Converts string log level to its corresponding integer value."""
        levels = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }
        return levels.get(self.log_level, logging.INFO)

    def set_log_level(self, new_level: str) -> None:
        """Sets the log level to a new value.

        Args:
            new_level: New logging level.
        """
        self.log_level = new_level
        # Reconfigure logger with new level
        logging.basicConfig(
            level=self.log_level,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'