use go_generation_derive::GoGenerate;
use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize, PartialEq, GoGenerate)]
pub enum MonitoringError {
    GPS,
    GPRS,
    Radio,
}
