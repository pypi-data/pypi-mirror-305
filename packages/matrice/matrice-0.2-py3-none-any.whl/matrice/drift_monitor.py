import numpy as np
from matrice.utils import handle_response
from datetime import datetime, timedelta

"""Module for interacting with backend API to manage drift monitoring."""


class DriftMonitoring:
    """Class to handle Drift Monitoring-related operations within a project.


    Parameters
    ----------
    session : object
        The session object containing the RPC interface and project ID.

    Attributes
    ----------
    session : object
        The session object for RPC communication.
    project_id : str
        The project ID associated with the session.
    rpc : object
        The RPC interface used to make API calls.

    Example
    -------
    >>> session = Session(account_number="account_number")
    >>> drift_monitoring = DriftMonitoring(session=session_object)
    """

    def __init__(self, session):
        self.session = session
        self.project_id = session.project_id
        self.rpc = session.rpc
        self.last_refresh_time = datetime.now()
        
        
    def refresh(self):
        """
        Refresh the instance by reinstantiating it with the previous values.
        """
        # Check if two minutes have passed since the last refresh
        if datetime.now() - self.last_refresh_time < timedelta(minutes=2):
            raise Exception("Refresh can only be called after two minutes since the last refresh.")

        # Capture the current state
        state = self.__dict__.copy()

        # Prepare the parameters needed for reinitialization
        init_params = {
            'session': self.session,
        }

        # Reinitialize the instance with the captured parameters
        self.__init__(**init_params) 

        # Update last refresh time
        self.last_refresh_time = datetime.now()


    def add_params(
        self,
        _idDeployment,
        deploymentName,
        imageStoreConfidenceThreshold,
        imageStoreCountThreshold,
    ):
        """
        Add drift monitoring parameters.

        Parameters
        ----------
        _idDeployment : str
            The ID of the deployment.
        deploymentName : str
            The name of the deployment.
        imageStoreConfidenceThreshold : float
            Confidence threshold for storing images.
        imageStoreCountThreshold : int
            Count threshold for storing images.

        Returns
        -------
        tuple
            A tuple containing:
            - resp (dict): The API response object.
            - error (str or None): Error message if the API call failed, otherwise None.
            - message (str): Success or error message.

        Example
        -------
        >>> resp, err, msg = drift_monitoring.add_params(_idDeployment, deploymentName, imageStoreConfidenceThreshold, imageStoreCountThreshold)
        >>> if err:
        >>>     print(f"Error: {err}")
        >>> else:
        >>>     print(f"Drift Monitoring detail : {resp}")
        """
        path = "/v1/deployment/drift_monitoring"
        headers = {"Content-Type": "application/json"}
        monitoring_params = {
            "_idDeployment": _idDeployment,
            "deploymentName": deploymentName,
            "imageStoreConfidenceThreshold": imageStoreConfidenceThreshold,
            "imageStoreCountThreshold": imageStoreCountThreshold,
        }
        resp = self.rpc.post(path=path, headers=headers, payload=monitoring_params)

        return handle_response(
            resp,
            "Drift monitoring parameters added successfully",
            "An error occurred while trying to add drift monitoring parameters",
        )

    def update(
        self,
        _idDeployment,
        deploymentName,
        imageStoreConfidenceThreshold,
        imageStoreCountThreshold,
    ):
        """
        Update drift monitoring parameters.

        Parameters
        ----------
        _idDeployment : str
            The ID of the deployment.
        deploymentName : str
            The name of the deployment.
        imageStoreConfidenceThreshold : float
            Confidence threshold for storing images.
        imageStoreCountThreshold : int
            Count threshold for storing images.

        Returns
        -------
        tuple
            A tuple containing:
            - resp (dict): The API response object.
            - error (str or None): Error message if the API call failed, otherwise None.
            - message (str): Success or error message.

        Example
        -------
        >>> resp, err, msg = drift_monitoring.update(_idDeployment, deploymentName, imageStoreConfidenceThreshold, imageStoreCountThreshold)
        >>> if err:
        >>>     print(f"Error: {err}")
        >>> else:
        >>>     print(f"Updated Drift Monitoring detail : {resp}")
        """
        path = "/v1/deployment/update_drift_monitoring"
        headers = {"Content-Type": "application/json"}
        monitoring_params = {
            "_idDeployment": _idDeployment,
            "deploymentName": deploymentName,
            "imageStoreConfidenceThreshold": imageStoreConfidenceThreshold,
            "imageStoreCountThreshold": imageStoreCountThreshold,
        }
        resp = self.rpc.put(path=path, headers=headers, payload=monitoring_params)

        return handle_response(
            resp,
            "Drift monitoring parameters updated successfully",
            "An error occurred while trying to update drift monitoring parameters",
        )
