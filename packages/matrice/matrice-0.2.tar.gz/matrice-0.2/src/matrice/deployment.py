import sys
from matrice.utils import handle_response , get_summary  
from datetime import datetime, timedelta

class Deployment:
    """
    Initialize Deployment instance with the given session and optional deployment_id.

    Parameters
    ----------
    session : object
        The session object containing project and RPC information.
    deployment_id : str, optional
        The ID of the deployment to be managed. Default is None.
    deployment_name : str, optional
        The name of the deployment. Default is an empty string.

    Example
    -------
    >>> session = Session(account_number="account_number")
    >>> deployment = Deployment(session=session_object,deployment_id=deployment_id,deployment_name=deployment_name)
    """

    def __init__(self, session, deployment_id=None, deployment_name=None):
        self.project_id = session.project_id
        self.last_refresh_time = datetime.now()
        assert deployment_id or deployment_name, "Either deployment_id or deployment_name must be provided"
        self.deployment_id = deployment_id #TODO get deployment id with name and check if id maps to the name or not
        self.deployment_name = deployment_name
        self.session=session
        self.rpc = session.rpc
        self.details, err, message = self._get_details()
        
        # Deployment details
        self.deployment_id = self.details.get("_id")
        self.deployment_name = self.details.get("deploymentName")
        self.project_id = self.details.get("_idProject")
        self.model_id = self.details.get("_idModel")
        self.user_id = self.details.get("_idUser")
        self.user_name = self.details.get("userName")
        self.action_id = self.details.get("_idAction")
        self.auth_keys = self.details.get("authKeys", [])
        self.runtime_framework = self.details.get("runtimeFramework")
        self.model_input = self.details.get("modelInput")
        self.model_type = self.details.get("modelType")
        self.model_output = self.details.get("modelOutput")
        self.deployment_type = self.details.get("deploymentType")
        self.suggested_classes = self.details.get("suggestedClasses", [])
        self.running_instances = self.details.get("runningInstances", [])
        self.auto_shutdown = self.details.get("autoShutdown")
        self.auto_scale = self.details.get("autoScale")
        self.gpu_required = self.details.get("gpuRequired")
        self.status = self.details.get("status")
        self.hibernation_threshold = self.details.get("shutdownThreshold")
        self.image_store_confidence_threshold = self.details.get("imageStoreConfidenceThreshold")
        self.image_store_count_threshold = self.details.get("imageStoreCountThreshold")
        self.images_stored_count = self.details.get("imagesStoredCount")
        self.bucket_alias = self.details.get("bucketAlias")
        self.credential_alias = self.details.get("credentialAlias")
        self.created_at = self.details.get("createdAt")
        self.updated_at = self.details.get("updatedAt")
        self.compute_alias = self.details.get("computeAlias")
        self.is_optimized=self.details.get("isOptimized")
        # Get and store deployment status cards
        self.status_cards = self._get_deployment_status_cards()
        
        # Get and store summary information
        summary_response, err, message = get_summary(self.session, self.project_id, "deployments")
        if summary_response:
            summary_data = summary_response
            self.total_deployments = summary_data.get("TotalDeployments")
            self.active_deployments = summary_data.get("ActiveDeployments")
            self.total_running_instances_count = summary_data.get("TotalRunningInstancesCount")
            self.hibernated_deployments = summary_data.get("hibernatedDeployments")
            self.error_deployments = summary_data.get("errorDeployments")
        else:
            self.total_deployments = None
            self.active_deployments = None
            self.total_running_instances_count = None
            self.hibernated_deployments = None
            self.error_deployments = None
        
    
    def refresh(self):
        """
        Refresh the instance by reinstantiating it with the previous values.
        """
        # Check if two minutes have passed since the last refresh
        if datetime.now() - self.last_refresh_time < timedelta(minutes=2):
            raise Exception("Refresh can only be called after two minutes since the last refresh.")

        # Prepare initialization parameters
        init_params = {
            'session': self.session,
            'deployment_id': self.deployment_id,
            'deployment_name': self.deployment_name
        }

        # Reinitialize the instance
        self.__init__(**init_params)

        # Update the last refresh time
        self.last_refresh_time = datetime.now()


    def _get_details(self):
        """
        Fetch deployment details based on either the deployment ID or deployment name.

        This method tries to fetch deployment details by ID if available;
        otherwise, it tries to fetch by name. It raises a ValueError if neither
        identifier is provided.

        Returns
        -------
        dict
            A dictionary containing the deployment details.

        Raises
        ------
        ValueError
            If neither deployment ID nor deployment name is provided.

        Example
        -------
        >>> deployment_details = deployment.get_details()
        >>> if isinstance(deployment_details, dict):
        >>>     print("deployment Details:", deployment_details)
        >>> else:
        >>>     print("Failed to retrieve deployment details.")
        """
        id = self.deployment_id
        name = self.deployment_name
        

        if id:
            try:
                return self._get_deployment_by_id()
            except Exception as e:
                print(f"Error retrieving deployment by id: {e}")
        elif name:
            try:
                return self._get_deployment_by_name()
            except Exception as e:
                print(f"Error retrieving deployment by name: {e}")
        else:
            raise ValueError(
                "At least one of 'deployment_id' or 'deployment_name' must be provided."
            )

        

    def _get_deployment_by_id(self):
        """
        Fetch details of the specified deployment.

        Returns
        -------
        tuple
            A tuple containing three elements:
            - API response (dict): The raw response from the API.
            - error_message (str or None): Error message if an error occurred, None otherwise.
            - status_message (str): A status message indicating success or failure.

        Examples
        --------
        >>> deployment = Deployment(session, deployment_id="1234")
        >>> deployment._get_deployment_by_id()
        """
        path = f"/v1/deployment/{self.deployment_id}"
        resp = self.rpc.get(path=path)

        return handle_response(
            resp,
            "Deployment fetched successfully",
            "An error occurred while trying to fetch deployment.",
        )

    def _get_deployment_by_name(self):
        """
        Fetch deployment details using the deployment name.

        Returns
        -------
        tuple
            A tuple containing three elements:
            - API response (dict): The raw response from the API.
            - error_message (str or None): Error message if an error occurred, None otherwise.
            - status_message (str): A status message indicating success or failure.

        Raises
        ------
        SystemExit
            If the deployment name is not set.

        Examples
        --------
        >>> deployment = Deployment(session, deployment_name="MyDeployment")
        >>> resp, err, msg = deployment.get_deployment_by_name()
        >>> if err:
        >>>     print(f"Error: {err}")
        >>> else:
        >>>     print(f"Deployment details : {resp}")
        """
        if self.deployment_name == "":
            print(
                "Deployment name not set for this Deployment. Cannot perform the operation for Deployment without deployment name"
            )
            sys.exit(0)
        path = f"/v1/deployment/get_deployment_by_name?deploymentName={self.deployment_name}"
        resp = self.rpc.get(path=path)

        return handle_response(
            resp,
            "Deployment by name fetched successfully",
            "Could not fetch Deployment by name",
        )

    def rename(self, updated_name):
        """
        Update the deployment name for the current deployment.

        Parameters
        ----------
        updated_name : str
            The new name for the deployment.

        Returns
        -------
        tuple
            A tuple containing three elements:
            - API response (dict): The raw response from the API.
            - error_message (str or None): Error message if an error occurred, None otherwise.
            - status_message (str): A status message indicating success or failure.

        Raises
        ------
        SystemExit
            If the deployment ID is not set.

        Examples
        --------
        >>> deployment = Deployment(session, deployment_id="1234")
        >>> resp, err, msg = deployment.rename_deployment("NewDeploymentName")
        >>> if err:
        >>>     print(f"Error: {err}")
        >>> else:
        >>>     print(f"Response : {resp}")
        """
        if self.deployment_id is None:
            print("Deployment id not set for this model.")
            sys.exit(0)

        body = {"deploymentName": updated_name}

        headers = {"Content-Type": "application/json"}
        path = f"/v1/deployment/update_deployment_name/{self.deployment_id}"
        resp = self.rpc.put(path=path, headers=headers, payload=body)

        return handle_response(
            resp,
            f"Deployment name updated to {updated_name}",
            "Could not update the deployment name",
        )

    def delete(self):
        """
        Delete the specified deployment.

        Parameters
        ----------
        deployment_id : str
            The ID of the deployment to be deleted.

        Returns
        -------
        tuple
            A tuple containing three elements:
            - API response (dict): The raw response from the API.
            - error_message (str or None): Error message if an error occurred, None otherwise.
            - status_message (str): A status message indicating success or failure.

        Examples
        --------
        >>> deployment = Deployment(session)
        >>> resp, err, msg = deployment.delete_deployment("1234")
        >>> if err:
        >>>     print(f"Error: {err}")
        >>> else:
        >>>     print(f"Response : {resp}")
        """
        path = f"/v1/deployment/delete_deployment/{self.deployment_id}"

        resp = self.rpc.delete(path=path)
        return handle_response(
            resp,
            "Deployment deleted successfully.",
            "An error occurred while trying to delete the deployment.",
        )


    def get_deployment_server(self, model_train_id, model_type):
        """
        Fetch information about the deployment server for a specific model.

        Parameters
        ----------
        model_train_id : str
            The ID of the model training instance.
        model_type : str
            The type of model (e.g., 'trained', 'exported').

        Returns
        -------
        tuple
            A tuple containing three elements:
            - API response (dict): The raw response from the API.
            - error_message (str or None): Error message if an error occurred, None otherwise.
            - status_message (str): A status message indicating success or failure.

        Examples
        --------
        >>> deployment = Deployment(session)
        >>> resp, err, msg = deployment.get_deployment_server("train123", "trained")
        >>> if err:
        >>>     print(f"Error: {err}")
        >>> else:
        >>>     print(f"Deployment server details : {resp}")
        """
        path = f"/v1/deployment/get_deploy_server/{model_train_id}/{model_type}"
        resp = self.rpc.get(path=path)
        return handle_response(
            resp,
            "Deployment server fetched successfully",
            "An error occurred while trying to fetch deployment server.",
        )

    def wakeup_deployment_server(self):
        """
        Wake up the deployment server associated with the current deployment. The deployment ID is set during initialization.

        Returns
        -------
        tuple
            A tuple containing three elements:
            - API response (dict): The raw response from the API.
            - error_message (str or None): Error message if an error occurred, None otherwise.
            - status_message (str): A status message indicating success or failure.

        Examples
        --------
        >>> deployment = Deployment(session, deployment_id="1234")
        >>> resp, err, msg = deployment.wakeup_deployment_server()
        >>> if err:
        >>>     print(f"Error: {err}")
        >>> else:
        >>>     print(f"Response : {resp}")
        """
        path = f"/v1/deployment/wake_up_deploy_server/{self.deployment_id}"
        resp = self.rpc.get(path=path)
        return handle_response(
            resp,
            "Deployment server has been successfully awakened",
            "An error occurred while attempting to wake up the deployment server.",
        )

    def _get_deployment_status_cards(self):
        """
        Fetch status cards for the current project's deployments. The project ID is set during initialization.

        Returns
        -------
        tuple
            A tuple containing three elements:
            - API response (dict): The raw response from the API.
            - error_message (str or None): Error message if an error occurred, None otherwise.
            - status_message (str): A status message indicating success or failure.

        Examples
        --------
        >>> deployment = Deployment(session)
        >>> resp, err, msg = deployment.get_deployment_status_cards()
        >>> if err:
        >>>     print(f"Error: {err}")
        >>> else:
        >>>     print(f"Response : {resp}")
        """
        path = f"/v1/deployment/status_cards?projectId={self.project_id}"
        resp = self.rpc.get(path=path)
        return handle_response(
            resp,
            "Deployment status cards fetched successfully.",
            "An error occurred while trying to fetch deployment status cards.",
        )

    def create_auth_key(self, expiry_days):
        """
        Create a new authentication key for the deployment that is valid for the specified number of days. The deployment ID is set during initialization.

        Parameters
        ----------
        expiry_days : int
            The number of days before the authentication key expires.

        Returns
        -------
        tuple
            A tuple containing three elements:
            - API response (dict): The raw response from the API.
            - error_message (str or None): Error message if an error occurred, None otherwise.
            - status_message (str): A status message indicating success or failure.

        Examples
        --------
        >>> deployment = Deployment(session, deployment_id="1234")
        >>> resp, err, msg = deployment.create_auth_key(30)
        """
        body = {"expiryDays": expiry_days, "authType": "external"}

        headers = {"Content-Type": "application/json"}
        path = f"/v1/deployment/add_auth_key/{self.deployment_id}?projectId={self.project_id}"

        resp = self.rpc.post(path=path, headers=headers, payload=body)
        return handle_response(
            resp,
            "Auth Key created successfully.",
            "An error occurred while trying to create auth key.",
        )

    
    def delete_auth_key(self, auth_key):
        """
        Delete the specified authentication key.

        Parameters
        ----------
        auth_key : str
            The authentication key to be deleted.

        Returns
        -------
        tuple
            A tuple containing three elements:
            - API response (dict): The raw response from the API.
            - error_message (str or None): Error message if an error occurred, None otherwise.
            - status_message (str): A status message indicating success or failure.

        Raises
        ------
        SystemExit
            If the deployment ID is not set.

        Examples
        --------
        >>> deployment = Deployment(session, deployment_id="1234")
        >>> resp, err, msg = deployment.delete_auth_key("abcd1234")
        >>> if err:
        >>>     print(f"Error: {err}")
        >>> else:
        >>>     print(f"Response : {resp}")
        """
        if self.deployment_id is None:
            print("Deployment id not set for this deployment.")
            sys.exit(0)

        path = f"/v1/deployment/delete_auth_key/{self.deployment_id}/{auth_key}"

        resp = self.rpc.delete(path=path)
        return handle_response(
            resp,
            "Auth key deleted successfully.",
            "An error occurred while trying to delete the auth key.",
        )
        
    def request_total_monitor(self):
        """
        Monitors the total number of requests for a given deployment.

        Returns:
        --------
        tuple:
            A tuple consisting of (result, error, message) containing the total number of requests.

        Example:
        --------
        >>> result, error, message = model_prediction.request_total_monitor()
        >>> print(result)
        {'total_requests': 1000}
        """
        # Check if deployment_id exists
        if self.deployment_id:
            deployment_id_url = self.deployment_id
        # If not, check if deployment_name exists and fetch deployment_id
        elif self.deployment_name:
            _, error, _ = self._get_deployment_by_name()
            if error:
                return None, error, "Failed to fetch deployment ID using the deployment name."
            deployment_id_url = self.deployment_id  # Assuming _get_deployment_by_name sets self.deployment_id
        else:
            return None, "Deployment ID and name are not set.", "Cannot perform operation without a deployment ID or name."

        path = f"/v1/model_prediction/monitor/req_total/{deployment_id_url}?projectId={self.project_id}"
        headers = {"Content-Type": "application/json"}
        body = {}

        resp = self.rpc.post(path=path, headers=headers, payload=body)
        return handle_response(
            resp,
            "Request total monitored successfully",
            "An error occurred while monitoring the request total.",
        )


    def request_count_monitor(self, start_date, end_date, granularity="second"):
        """
        Monitors the count of requests for a specific time range and granularity.

        Parameters:
        -----------
        start_date : str
            The start date of the monitoring period in ISO format.
        end_date : str
            The end date of the monitoring period in ISO format.
        granularity : str, optional
            The time granularity for the count (e.g., second, minute). Default is "second".
        deployment_id : str, optional
            The ID of the deployment to monitor.

        Returns:
        --------
        tuple:
            A tuple consisting of (result, error, message) containing request counts.

        Example:
        --------
        >>> start = "2024-01-28T18:30:00.000Z"
        >>> end = "2024-02-29T10:11:27.000Z"
        >>> result, error, message = deployment.request_count_monitor(start, end)
        >>> print(result)
        {'counts': [{'timestamp': '2024-01-28T18:30:00Z', 'count': 50}, ...]}
        """
        path = f"/v1/model_prediction/monitor/request_count"
        headers = {"Content-Type": "application/json"}
        body = {
            "granularity": granularity,
            "startDate": start_date,
            "endDate": end_date,
            "status": "REQ. COUNT",
            "deploymentId": self.deployment_id,
        }
        resp = self.rpc.post(path=path, headers=headers, payload=body)

        return handle_response(
            resp,
            "Request count monitored successfully",
            "An error occurred while monitoring the request count.",
        )

    def request_latency_monitor(self, start_date, end_date, granularity="second"):
        """
        Monitors the request latency for a specific time range and granularity.

        Parameters:
        -----------
        start_date : str
            The start date of the monitoring period in ISO format.
        end_date : str
            The end date of the monitoring period in ISO format.
        granularity : str, optional
            The time granularity for latency tracking (e.g., second, minute). Default is "second".
        deployment_id : str, optional
            The ID of the deployment to monitor.

        Returns:
        --------
        tuple:
            A tuple consisting of (result, error, message) containing latency information.

        Example:
        --------
        >>> start = "2024-01-28T18:30:00.000Z"
        >>> end = "2024-02-29T10:11:27.000Z"
        >>> result, error, message = deployment.request_latency_monitor(start, end)
        >>> print(result)
        {'latencies': [{'timestamp': '2024-01-28T18:30:00Z', 'avg_latency': 0.05}, ...]}
        """
        path = f"/v1/model_prediction/monitor/latency"
        headers = {"Content-Type": "application/json"}
        body = {
            "granularity": granularity,
            "startDate": start_date,
            "endDate": end_date,
            "status": "AVG. LATENCY",
            "deploymentId": self.deployment_id,
        }
        resp = self.rpc.post(path=path, headers=headers, payload=body)

        return handle_response(
            resp,
            "Latency count monitored successfully",
            "An error occurred while monitoring the latency count.",
        )
    
    def create_dataset(
        self,
        dataset_name,
        is_unlabeled,
        source,
        source_url,
        is_public,
        dataset_description="",
        version_description="",
    ):
        """
        Create a dataset from deployment.  The deployment ID is required to create a dataset from deployment.
        Only zip files are supported for upload.

        Parameters
        ----------
        dataset_name : str
            The name of the new dataset.
        is_unlabeled : bool
            Indicates whether the dataset is unlabeled.
        source : str
            The source of the dataset.
        source_url : str
            The URL of the dataset to be created.
        is_public : bool
            Indicates whether the dataset is public.
        dataset_description : str, optional
            The description of the dataset (default is an empty string).
        version_description : str, optional
            The description of the dataset version (default is an empty string).

        Returns
        -------
        tuple
            A tuple containing three elements:
            - API response (dict): The raw response from the API.
            - error_message (str or None): Error message if an error occurred, None otherwise.
            - status_message (str): A status message indicating success or failure.

        Example
        -------
        >>> resp, err, msg = dataset.create_dataset_from_deployment(
                dataset_name="New Dataset", is_unlabeled=False, source="aws",
                source_url="https://example.com/dataset.zip", deployment_id="123",is_public=True,
                dataset_description = "Enter your dataset description",
                version_description = "Enter your version description"  )
        >>> if err:
        >>>     print(f"Error: {err}")
        >>> else:
        >>>     print(f"Dataset creation in progress: {resp}")
        """
        dataset_size, err, msg = self._get_dataset_size(source_url) #TODO: Implement get_dataset_size
        print(f"dataset size is = {dataset_size}")
        path = f"/v1/dataset/deployment?projectId={self.project_id}"
        headers = {"Content-Type": "application/json"}
        body = {
            "name": dataset_name,
            "isUnlabeled": is_unlabeled,  # false,
            "source": source,  # "lu",
            "sourceUrl": source_url,  # "https://s3.us-west-2.amazonaws.com/dev.dataset/test%2Fb34ea15a-1f52-48a3-9a70-d43688084441.zip",
            "_idDeployment": self.deployment_id,
            "cloudProvider": "AWS",
            "isCreateNew": True,
            "oldDatasetVersion": None,
            "newDatasetVersion": "v1.0",
            "datasetDescription": dataset_description,
            "newVersionDescription": version_description,
            "isPublic": is_public,  # false,
            "computeAlias": "",
            "targetCloudStorage": "GCP",
            "inputType": self.model_input,
            "copyData": False,
            "isPrivateStorage": False,
            "cloudStoragePath": "",
            "urlType": "",
            "datasetSize": 0,
            "deleteDeploymentDataset": False,
            "_idProject": self.project_id,
            "type": self.model_type,
        }
        resp = self.rpc.post(path=path, headers=headers, payload=body)

        print(resp)

        return handle_response(
            resp,
            "Dataset creation in progress",
            "An error occured while trying to create new dataset",
        )       

    def get_prediction(self, image_path , auth_key):
        """
        Fetches model predictions for a given image using a deployment.

        Parameters:
        -----------
        image_path : str
            The path to the image for prediction.
        auth_key : str
            The authentication key for authorizing the prediction request.
        deployment_id : str, optional
            The ID of the deployment for prediction.
        deployment_name : str, optional
            The name of the deployment for prediction.

        Returns:
        --------
        tuple:
            A tuple consisting of (result, error, message) with the prediction results.

        Example:
        --------
        >>> result, error, message = model.get_deployment_prediction("/path/to/image.jpg", auth_key="auth123", deployment_id="deploy123")
        >>> print(result)
        {'predictions': [{'class': 'cat', 'confidence': 0.95}, ...]}
        """
        if not auth_key:
            raise ValueError("auth_key is required for deployment predictions.")

        files = {"image": open(image_path, "rb")}

        if self.deployment_id:
            url = f"/v1/model_prediction/deployment/{self.deployment_id}/predict"
        elif self.deployment_name:
            url = f"/v1/model_prediction/deployment_name/{self.deployment_name}/predict"
        else:
            raise ValueError("Either deployment_id or deployment_name must be provided.")

        # Check if the server is running
        server_status, error, message = self._get_details(self.deployment_id or self.deployment_id)
        if error:
            print(f"Error checking server status: {error}")
            return None, error, message

        if server_status["status"] != "active":
            # Wake up the server if it's not running
            wakeup_resp, wakeup_error, wakeup_message = self.wakeup_deployment_server()
            if wakeup_error:
                print(f"Error waking up server: {wakeup_error}")
                return None, wakeup_error, wakeup_message

            # Wait for the server to be fully awake
            import time
            time.sleep(10)  # Adjust the sleep time as needed


        data = {"authKey": auth_key}
        headers = {"Authorization": f"Bearer {self.rpc.AUTH_TOKEN.bearer_token}"}

        resp = self.rpc.post(url, headers=headers, data=data, files=files)
        success_message = "Model prediction fetched successfully"
        error_message = "An error occurred while fetching the model prediction."

        return handle_response(resp, success_message, error_message)

    def _get_dataset_size(self, url):
        """
        Fetch the size of the dataset from the given URL.

        Parameters
        ----------
        url : str
            The URL of the dataset to fetch the size for.

        Returns
        -------
        tuple
            A tuple containing three elements:
            - API response (dict): The raw response from the API.
            - error_message (str or None): Error message if an error occurred, None otherwise.
            - status_message (str): A status message indicating success or failure.

        Example
        -------
        >>> size, err, msg = dataset.get_dataset_size(url="")
        >>> if err:
        >>>     print(f"Error: {err}")
        >>> else:
        >>>     print(f"Dataset size: {size} MB")
        """
        path = (
            f"/v1/dataset/get_dataset_size_in_mb_from_url?projectId={self.project_id}"
        )
        requested_payload = {"datasetUrl": url}
        headers = {"Content-Type": "application/json"}
        resp = self.rpc.post(path=path, headers=headers, payload=requested_payload)

        return handle_response(
            resp, f"Dataset size fetched successfully", "Could not fetch dataset size"
        )