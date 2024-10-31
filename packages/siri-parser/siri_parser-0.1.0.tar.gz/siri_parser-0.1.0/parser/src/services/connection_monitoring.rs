use go_generation_derive::GoGenerate;
use serde::{Deserialize, Serialize};

use crate::{
    models::service_delivery_info::ServiceDeliveryInfo,
    notifications::connection_monitoring_notification::ConnectionMonitoringNotification,
};

#[derive(Debug, Deserialize, Serialize, PartialEq, Eq, GoGenerate)]
#[serde(rename_all = "PascalCase")]
pub struct NotifyConnectionMonitoring {
    pub service_delivery_info: ServiceDeliveryInfo,
    pub notification: ConnectionMonitoringNotification,
}
