use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize, PartialEq, GoGenerate)]
#[serde(rename_all = "PascalCase")]
pub struct GeneralMessage {
    general_message_delivery: Option<GeneralMessageDelivery>,
}
