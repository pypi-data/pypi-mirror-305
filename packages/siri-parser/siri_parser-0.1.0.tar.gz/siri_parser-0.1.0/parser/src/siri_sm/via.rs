use go_generation_derive::GoGenerate;
use serde::{Deserialize, Serialize};

#[derive(Debug, Default, Serialize, Deserialize, PartialEq, GoGenerate)]
#[serde(rename_all = "PascalCase")]
pub struct Via {
    place_ref: Option<String>,  // JourneyPlaceCode for the via stop
    place_name: Option<String>, // Name of the via stop
}
