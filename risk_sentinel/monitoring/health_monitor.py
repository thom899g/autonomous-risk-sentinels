import logging
from datetime import datetime
from typing import Dict, Optional

logger = logging.getLogger(__name__)

class HealthMonitor:
    """Monitors the health of Risk Sentinel components and provides status updates.

    Attributes:
        component_status: Dictionary mapping component names to their current status.
        last_checked: Timestamp of the last health check.
    """
    
    def __init__(self):
        self.component_status: Dict[str, str] = {}
        self.last_checked: Optional[datetime] = None

    def update_component_status(self, component_name: str, status: str) -> None:
        """Updates the status of a specific component.

        Args:
            component_name: Name of the component.
            status: New status of the component (e.g., 'healthy', 'degraded', 'down').
        """
        self.component_status[component_name] = status
        logger.info(f"Updated status for {component_name} to {status}")

    def get_component_status(self, component_name: str) -> Optional[str]:
        """Retrieves the current status of a specific component.

        Args:
            component_name: Name of the component.

        Returns:
            Current status if exists, else None.
        """
        return self.component_status.get(component_name)

    def perform_health_check(self) -> Dict[str, str]:
        """Performs a comprehensive health check of all components and returns their statuses."""
        timestamp = datetime.now()
        logger.info("Performing health check...")
        
        # This is a placeholder; in reality, it would communicate with each component
        # to get their status.
        self.component_status = {
            'data_feeder': 'healthy',
            'data_processing_engine': 'healthy',
            'risk_identification_engine': 'healthy',
            'risk_quantifier': 'healthy',
            'risk_mitigator': 'healthy'
        }
        
        self.last_checked = timestamp
        return self.component_status

    def get_overall_health(self) -> str:
        """Determines the overall health based on component statuses."""
        unhealthy_components = [status for status in self.component_status.values() if status != 'healthy']
        
        if unhealthy_components:
            return 'degraded'
        else:
            return 'healthy'