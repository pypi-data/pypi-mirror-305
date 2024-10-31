use crate::{
    models::service_delivery_info::ServiceDeliveryInfo,
    notifications::facility_monitoring_notification::FacilityMonitoringNotification,
};
use go_generation_derive::GoGenerate;
use serde::{Deserialize, Serialize};

#[derive(Debug, Deserialize, Serialize, PartialEq, Eq, GoGenerate)]
#[serde(rename_all = "PascalCase")]
pub struct NotifyFacilityMonitoring {
    pub service_delivery_info: ServiceDeliveryInfo,
    pub notification: FacilityMonitoringNotification,
}
