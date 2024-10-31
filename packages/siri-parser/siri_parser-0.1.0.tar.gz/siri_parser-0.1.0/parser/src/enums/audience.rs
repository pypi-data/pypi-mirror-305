use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize, PartialEq, GoGenerate)]
#[serde(rename_all = "camelCase")]
pub enum Audience {
    Public,
    EmergencyService,
    Authorities,
    TransportOperators,
}
