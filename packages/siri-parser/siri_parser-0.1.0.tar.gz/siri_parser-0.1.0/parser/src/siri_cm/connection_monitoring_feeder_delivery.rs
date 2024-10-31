use serde::{Deserialize, Serialize};

#[derive(Debug, Default, Serialize, Deserialize, PartialEq, GoGenerate)]
#[serde(rename_all = "PascalCase")]
pub struct ConnectionMonitoringFeederDelivery {
    version: String,
    #[serde(flatten)]
    leader: XxxDelivery,
    monitored_feeder_arrival: MonitoredFeederArrival,
    monitored_deeder_arrival__cancellation: MonitoredFeederArrivalCancellation,
}
