use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize, PartialEq, GoGenerate)]
#[serde(rename_all = "camelCase")]
enum QualityIndex {
    Certain,
    VeryReliable,
    Reliable,
    Unreliable,
    Unconfirmed,
}
