"""
Class to handle alert related to microsleep
microsleep is detected with EV19 and behavior type 1
This is detected as event not alert
"""

import datetime
import os
import time

import pytz
import redis
from loguru import logger

from its_system_alerts.system.alerts.alertTracker import AlertTracker

MICROSLEEP_EVENT = "EV19"
MICROSLEEP_TYPE = "1"
TAKO_TYPE_ALERT = "1"


class MicrosleepAlert(AlertTracker):
    """
    Class to handle alert related to microsleep
    """

    def __init__(
        self, redis_client: redis.Redis, whatsapp_config: dict, time_window: int = 300, alert_threshold: int = 5
    ):
        """ """
        super().__init__(redis_client, whatsapp_config, time_window, alert_threshold)

    @staticmethod
    def _is_microsleep(alert: dict) -> bool:
        """
        Check if the alert is a microsleep
        """
        event_code = alert.get("codigoEvento")
        behaviour_type = alert.get("codigoComportamientoAnomalo")

        return str(event_code) == MICROSLEEP_EVENT and str(behaviour_type) == MICROSLEEP_TYPE

    def send_whatsapp_notification(self, message: str):
        raise NotImplementedError

    def send_email_notification(self, message: str):
        raise NotImplementedError

    def save_alert(self, data, alert_count):
        """
        Save alert into the system
        """
        company_id = data.get("company_id")
        vehicle_id = data.get("idVehiculo")
        timestamp = data.get("fechaHoraLecturaDato")

        latitud = data.get("localizacionVehiculo", {}).get("latitud")
        longitud = data.get("localizacionVehiculo", {}).get("longitud")

        dt = datetime.datetime.strptime(timestamp, "%d/%m/%Y %H:%M:%S.%f")
        formatted_timestamp = dt.strftime("%Y-%m-%d %H:%M:%S.%f")

        alert = {
            "vehicle": vehicle_id,
            "longitud": str(longitud),
            "latitud": str(latitud),
            "last_reported_time": formatted_timestamp,
            "total_events": alert_count,
            "id_alert_type": TAKO_TYPE_ALERT,
            "send_whatsapp": False,
            "send_email": False,
            "company_id": company_id,
        }

        url_post = os.getenv("URL_POST_ALERT", "")
        url_login = os.getenv("URL_LOGIN_TAKO", "")

        self.save_to_postgres(url=url_post, login_url=url_login, data=alert)

    def process_alert(self, data: dict):
        """
        Process the alert
        """
        company_id = data.get("company_id")
        vehicle_id = data.get("idVehiculo")
        alert_code = data.get("codigoEvento")
        behavior_type = data.get("codigoComportamientoAnomalo")
        timestamp = data.get("fechaHoraLecturaDato")

        if not all([company_id, vehicle_id, alert_code, timestamp, behavior_type]):
            return

        if not self._is_microsleep(data):
            return

        logger.debug(f"Microsleep alert detected: {data}")
        key = f"microsleep:{company_id}:{vehicle_id}:{alert_code}"
        current_time = time.time()

        if not timestamp:
            return

        local_tz = pytz.timezone("America/Bogota")
        dt = datetime.datetime.strptime(timestamp, "%d/%m/%Y %H:%M:%S.%f")
        dt_local = local_tz.localize(dt)
        dt_utc = dt_local.astimezone(pytz.utc)
        timestamp = dt_utc.timestamp()

        self.redis_client.zadd(key, {timestamp: timestamp})
        self.redis_client.expire(key, self.time_window * 5)  # TTL is double the time window
        self.redis_client.zremrangebyscore(key, 0, current_time - self.time_window)
        alert_count = self.redis_client.zcard(key)

        if alert_count >= self.alert_threshold:
            logger.info(f"Microsleep alert detected: {alert_count} alerts in the last {self.time_window} seconds")
            # Save the alert into the database
            self.save_alert(data=data, alert_count=alert_count)
            self.redis_client.delete(key)
