use  serde::{Serialize, Deserialize};

use super::connection_monitoring_feeder_delivery::ConnectionMonitoringFeederDelivery;


#[derive(Debug, Serialize, Deserialize, PartialEq)]
#[serde(rename_all = "PascalCase")]
pub struct ServiceDelivery {
    pub connection_monitoring_feeder_delivery: Option<ConnectionMonitoringFeederDelivery>,
    pub connection_monitoring_distributor_delivery: Option<ConnectionMonitoringDistributorDelivery>,
}