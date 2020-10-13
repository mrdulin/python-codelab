import googleapiclient.discovery
import logging


class Service:
    def __init__(self, project, event):
        self.project_id = project
        self.compute = googleapiclient.discovery.build('compute', 'v1', cache_discovery=False)
        self.event = event
        self.zones = self._validate_event()

    def _validate_event(self):
        if "jsonPayload" not in self.event:
            zones = self.compute.zones().list(project=self.project_id).execute()['items']
        else:
            zones = self.compute.zones().get(project=self.project_id,
                                             zone=self.event["jsonPayload"]["resource"]["zone"]).execute()

        logging.debug(f"Identified Zones are {zones}")
        return [zone["name"] for zone in zones]
