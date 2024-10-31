use crate::enums::end_time_precision::EndTimePrecision;
use go_generation_derive::GoGenerate;
use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize, PartialEq, Eq, GoGenerate)]
#[serde(rename_all = "PascalCase")]
pub struct ValidityPeriod {
    pub start_time: String,
    pub end_time: String,
    pub end_time_precision: Option<EndTimePrecision>,
}
