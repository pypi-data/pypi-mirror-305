from enum import Enum


class AuthenticatedClient:
    def __init__(self, session, url):
        self.session = session
        self.url = url

    def has_given_consent(self, pid):  # has_given_consent
        """
        Retrieves patient data for a given patient ID (PID)
        by making an HTTP request to a configured URL.

        Parameters
        ----------
        pid : str
            The patient ID to fetch data for.

        Returns
        -------
        bool
            True if consent status is ACTIVE,
            False if consent status is REJECTED.
            False if pid is not recognized.

        Raises
        ------
        ValueError
            If PID is empty or consent status is not recognized.
        HTTPError
            If an HTTP error occurs during the request.
        """
        if not pid or not pid.strip():
            raise ValueError("PID is empty")

        url = self.url
        if not url:
            raise ValueError("URL is empty")

        params = {"patient": pid}

        response = self.session.get(url, params=params)
        response.raise_for_status()
        return self.parse_status(response.json())

    @staticmethod
    def parse_status(data):
        if not data.get("entry"):
            return False

        consent_status_str = data["entry"][0]["resource"]["status"]["code"].lower()

        try:
            consent_status = ConsentStatus(consent_status_str)
            if consent_status == ConsentStatus.ACTIVE:
                return True
            elif consent_status == ConsentStatus.REJECTED:
                return False
        except ValueError as err:
            raise ValueError("Consent status not recognized.") from err


class ConsentStatus(Enum):
    ACTIVE = "active"
    REJECTED = "rejected"
