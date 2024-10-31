use go_generation_derive::GoGenerate;
use serde::{Deserialize, Serialize};

use crate::siri_et::estimated_call::EstimatedCall;

#[derive(Debug, Serialize, Deserialize, PartialEq, Eq, GoGenerate)]
pub struct EstimatedCalls {
    #[serde(alias = "EstimatedCall")]
    pub calls: Option<Vec<EstimatedCall>>,
}
