use crate::{
    models::service_delivery_info::ServiceDeliveryInfo,
    notifications::production_timetable_notification::ProductionTimetableNotification,
};
use go_generation_derive::GoGenerate;
use serde::{Deserialize, Serialize};

#[derive(Debug, Deserialize, Serialize, PartialEq, Eq, GoGenerate)]
#[serde(rename_all = "PascalCase")]
pub struct NotifyProductionTimetable {
    pub service_delivery_info: ServiceDeliveryInfo,
    pub notification: ProductionTimetableNotification,
}
